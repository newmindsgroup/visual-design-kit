#!/usr/bin/env python3
# Version-Timestamp: 2026-09-27 14:43:14 AST
"""Validate owner-supplied reference ZIPs locally, then optionally install them.

Dry run is the default. Integrity is measured against the included manifest,
not an independent proof of origin or permission to use the reference material.
Installation requires a new destination under an existing nonsymlink directory.
Linux and macOS support atomic, exclusive installation; other platforms fail
closed on apply. Source content is never executed, uploaded, or interpreted.
"""
import argparse
from contextlib import ExitStack
import ctypes
import errno
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import secrets
import stat
import sys
import unicodedata
import zipfile
import zlib


MANIFEST = 'manifests/files.json'
CATALOG = 'catalog/items.jsonl'
MAX_TOTAL_BYTES = 8 * 1024 ** 3
MAX_ENTRIES = 100_000
MAX_MANIFEST_BYTES = 16 * 1024 ** 2
CHUNK = 1024 ** 2
SHA256 = re.compile(r'[0-9a-fA-F]{64}\Z')
APPENDED_EXTENSION = re.compile(r'\.[A-Za-z0-9]{1,16}\Z')


class ArchiveError(ValueError):
    """A bounded diagnostic that does not expose source content or host paths."""


def safe_relative(value, directory=False):
    if not isinstance(value, str) or not value or len(value) > 4096:
        raise ArchiveError('unsafe_archive_path')
    if any(ord(char) < 32 or ord(char) == 127 for char in value):
        raise ArchiveError('unsafe_archive_path')
    name = value[:-1] if directory and value.endswith('/') else value
    parts = name.split('/')
    if ('\\' in name or ':' in name or not name or
            any(part in ('', '.', '..') or len(part.encode('utf-8')) > 255
                for part in parts)):
        raise ArchiveError('unsafe_archive_path')
    return name


def collision_key(name):
    return unicodedata.normalize('NFC', name).casefold()


def register_path(name, aliases):
    """Reject portable filesystem collisions, including implicit directories."""
    parts = name.split('/')
    for end in range(1, len(parts) + 1):
        relative = '/'.join(parts[:end])
        key = collision_key(relative)
        if key in aliases and aliases[key] != relative:
            raise ArchiveError('archive_path_collision')
        aliases[key] = relative


def stream_digest(stream):
    digest = hashlib.sha256()
    for block in iter(lambda: stream.read(CHUNK), b''):
        digest.update(block)
    return digest.hexdigest()


def hash_archive(stream):
    stream.seek(0)
    value = stream_digest(stream)
    stream.seek(0)
    return value


def read_headers(archives, max_entries, max_total_bytes):
    files, directories, aliases = {}, set(), {}
    total_bytes, count = 0, 0
    for archive in archives:
        for info in archive.infolist():
            count += 1
            if count > max_entries:
                raise ArchiveError('entry_limit_exceeded')
            directory = info.is_dir()
            name = safe_relative(info.orig_filename, directory=directory)
            mode = stat.S_IFMT(info.external_attr >> 16)
            if (mode not in (0, stat.S_IFREG, stat.S_IFDIR) or
                    (directory and mode == stat.S_IFREG) or
                    (not directory and mode == stat.S_IFDIR) or
                    (directory and info.file_size != 0)):
                raise ArchiveError('nonregular_archive_entry')
            if info.flag_bits & 1:
                raise ArchiveError('encrypted_archive_entry')
            if info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED):
                raise ArchiveError('unsupported_zip_compression')
            total_bytes += info.file_size
            if total_bytes > max_total_bytes:
                raise ArchiveError('uncompressed_limit_exceeded')
            register_path(name, aliases)
            if directory:
                directories.add(name)
            else:
                if name in files:
                    raise ArchiveError('duplicate_archive_file')
                files[name] = (archive, info)
    for name in list(files) + list(directories):
        if name in files and name in directories:
            raise ArchiveError('archive_path_conflict')
        if any(str(parent) in files for parent in PurePosixPath(name).parents
               if str(parent) != '.'):
            raise ArchiveError('archive_path_conflict')
    return files, directories, total_bytes, count


def remove_wrapper(files, directories):
    manifests = [name for name in files
                 if name == MANIFEST or (name.endswith('/' + MANIFEST) and len(name.split('/')) == 3)]
    if len(manifests) != 1:
        raise ArchiveError('manifest_count_invalid')
    prefix = manifests[0][:-len(MANIFEST)]
    if prefix:
        if (any(not name.startswith(prefix) for name in files) or
                any(name != prefix[:-1] and not name.startswith(prefix) for name in directories)):
            raise ArchiveError('mixed_archive_roots')
    return {name[len(prefix):]: entry for name, entry in files.items()}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ArchiveError('duplicate_manifest_key')
        result[key] = value
    return result


def read_manifest(files, max_manifest_bytes, max_entries):
    archive, info = files[MANIFEST]
    if info.file_size > max_manifest_bytes:
        raise ArchiveError('manifest_limit_exceeded')
    with archive.open(info) as stream:
        raw = stream.read(max_manifest_bytes + 1)
    if len(raw) > max_manifest_bytes:
        raise ArchiveError('manifest_limit_exceeded')
    try:
        manifest = json.loads(raw, object_pairs_hook=unique_object)
    except (UnicodeError, json.JSONDecodeError, RecursionError) as exc:
        raise ArchiveError('invalid_manifest') from exc
    if not isinstance(manifest, dict):
        raise ArchiveError('invalid_manifest')
    for key in ('schema', 'schema_version'):
        if key in manifest and (type(manifest[key]) not in (int, str) or manifest[key] not in (1, '1')):
            raise ArchiveError('unsupported_manifest_schema')
    entries = manifest.get('files')
    if not isinstance(entries, dict) or not entries or len(entries) > max_entries:
        raise ArchiveError('invalid_manifest')
    aliases = {}
    for name, entry in entries.items():
        safe_relative(name)
        register_path(name, aliases)
        if (not isinstance(entry, dict) or not isinstance(entry.get('sha256'), str) or
                not SHA256.fullmatch(entry['sha256']) or
                ('bytes' in entry and (type(entry['bytes']) is not int or entry['bytes'] < 0))):
            raise ArchiveError('invalid_manifest_entry')
        if name == MANIFEST:
            raise ArchiveError('manifest_self_reference')
    output_names = set(entries) | {MANIFEST}
    for name in output_names:
        if any(str(parent) in output_names for parent in PurePosixPath(name).parents
               if str(parent) != '.'):
            raise ArchiveError('manifest_path_conflict')
    if CATALOG not in entries:
        raise ArchiveError('missing_catalog_coverage')
    return entries, raw


def map_files(entries, files):
    mapping, used, normalizations = {}, {MANIFEST}, []
    for name in sorted(entries):
        source = name
        if name not in files:
            parent = PurePosixPath(name).parent
            candidates = [candidate for candidate in files
                          if PurePosixPath(candidate).parent == parent and candidate.startswith(name)
                          and APPENDED_EXTENSION.fullmatch(candidate[len(name):])]
            if len(candidates) > 1:
                raise ArchiveError('ambiguous_normalization')
            if not candidates:
                raise ArchiveError('missing_manifest_file')
            source = candidates[0]
            normalizations.append({'from': source, 'to': name})
        if source in used:
            raise ArchiveError('ambiguous_normalization')
        used.add(source)
        mapping[name] = files[source]
    if set(files) != used:
        raise ArchiveError('unexpected_archive_file')
    return mapping, normalizations


def verify_member(member, entry, output=None):
    archive, info = member
    if 'bytes' in entry and info.file_size != entry['bytes']:
        raise ArchiveError('integrity_mismatch')
    digest, count = hashlib.sha256(), 0
    with archive.open(info) as stream:
        for block in iter(lambda: stream.read(CHUNK), b''):
            count += len(block)
            if count > info.file_size:
                raise ArchiveError('integrity_mismatch')
            digest.update(block)
            if output is not None:
                output.write(block)
    if count != info.file_size or digest.hexdigest() != entry['sha256'].lower():
        raise ArchiveError('integrity_mismatch')


def checked_destination(value):
    path = Path(os.path.abspath(Path(value).expanduser()))
    current = Path(path.anchor)
    for part in path.parts[1:]:
        current /= part
        if current.is_symlink():
            raise ArchiveError('unsafe_destination_symlink')
    if path.exists():
        raise ArchiveError('destination_exists')
    if not path.parent.is_dir():
        raise ArchiveError('destination_parent_missing')
    return path


DIRECTORY_FLAGS = os.O_RDONLY | getattr(os, 'O_DIRECTORY', 0) | getattr(os, 'O_NOFOLLOW', 0)


def open_directory(path):
    """Anchor each component without following any symlink, even during races."""
    descriptor = os.open(path.anchor, DIRECTORY_FLAGS)
    try:
        for part in path.parts[1:]:
            child = os.open(part, DIRECTORY_FLAGS, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def staged_file(root_fd, relative, writing=False):
    parent_fd = os.dup(root_fd)
    try:
        parts = relative.split('/')
        for part in parts[:-1]:
            if writing:
                try:
                    os.mkdir(part, mode=0o700, dir_fd=parent_fd)
                except FileExistsError:
                    pass
            child = os.open(part, DIRECTORY_FLAGS, dir_fd=parent_fd)
            os.close(parent_fd)
            parent_fd = child
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL if writing else os.O_RDONLY
        descriptor = os.open(parts[-1], flags | os.O_NOFOLLOW, mode=0o600, dir_fd=parent_fd)
        return os.fdopen(descriptor, 'wb' if writing else 'rb')
    finally:
        os.close(parent_fd)


def copy_verified_file(member, entry, staging_fd, name):
    with staged_file(staging_fd, name, writing=True) as output:
        verify_member(member, entry, output)


def clear_staging(descriptor):
    """Delete only children of our held staging directory, without symlinks."""
    for name in os.listdir(descriptor):
        if stat.S_ISDIR(os.stat(name, dir_fd=descriptor, follow_symlinks=False).st_mode):
            child = os.open(name, DIRECTORY_FLAGS, dir_fd=descriptor)
            try:
                clear_staging(child)
            finally:
                os.close(child)
            os.rmdir(name, dir_fd=descriptor)
        else:
            os.unlink(name, dir_fd=descriptor)


def exclusive_rename(parent_fd, source, destination):
    """Use the platform no-replace primitive; never fall back to overwriting."""
    libc = ctypes.CDLL(None, use_errno=True)
    if sys.platform == 'darwin':
        function = getattr(libc, 'renameatx_np', None)
        flags = 4  # RENAME_EXCL
    elif sys.platform.startswith('linux'):
        function = getattr(libc, 'renameat2', None)
        flags = 1  # RENAME_NOREPLACE
    else:
        function = None
        flags = 0
    if function is None:
        raise ArchiveError('atomic_install_unsupported')
    function.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
    function.restype = ctypes.c_int
    if function(parent_fd, os.fsencode(source), parent_fd, os.fsencode(destination), flags) != 0:
        error = ctypes.get_errno()
        if error in (errno.EEXIST, errno.ENOTEMPTY):
            raise ArchiveError('destination_exists')
        if error in (errno.ENOSYS, errno.ENOTSUP, errno.EINVAL):
            raise ArchiveError('atomic_install_unsupported')
        raise OSError(error, 'atomic installation failed')


def install(destination, mapping, entries, manifest_bytes):
    destination = checked_destination(destination)
    if sys.platform != 'darwin' and not sys.platform.startswith('linux'):
        raise ArchiveError('atomic_install_unsupported')
    parent_fd = open_directory(destination.parent)
    staging_name, staging_fd = None, None
    installed = False
    try:
        parent_identity = os.fstat(parent_fd)
        checked_destination(destination)
        if not os.path.samestat(parent_identity, destination.parent.stat()):
            raise ArchiveError('destination_parent_changed')
        staging_name = '.reference-import-' + secrets.token_hex(16)
        os.mkdir(staging_name, mode=0o700, dir_fd=parent_fd)
        staging_fd = os.open(staging_name, DIRECTORY_FLAGS, dir_fd=parent_fd)
        for name, member in mapping.items():
            copy_verified_file(member, entries[name], staging_fd, name)
        with staged_file(staging_fd, MANIFEST, writing=True) as stream:
            stream.write(manifest_bytes)
        for name, entry in entries.items():
            with staged_file(staging_fd, name) as stream:
                if stream_digest(stream) != entry['sha256'].lower():
                    raise ArchiveError('staging_integrity_mismatch')
        with staged_file(staging_fd, MANIFEST) as stream:
            if stream.read() != manifest_bytes:
                raise ArchiveError('staging_integrity_mismatch')
        checked_destination(destination)
        if not os.path.samestat(parent_identity, destination.parent.stat()):
            raise ArchiveError('destination_parent_changed')
        if not os.path.samestat(os.fstat(staging_fd), os.stat(staging_name, dir_fd=parent_fd, follow_symlinks=False)):
            raise ArchiveError('staging_directory_changed')
        exclusive_rename(parent_fd, staging_name, destination.name)
        installed = True
    finally:
        try:
            if staging_fd is not None and not installed:
                clear_staging(staging_fd)
                if os.path.samestat(os.fstat(staging_fd), os.stat(staging_name, dir_fd=parent_fd, follow_symlinks=False)):
                    os.rmdir(staging_name, dir_fd=parent_fd)
        finally:
            if staging_fd is not None:
                os.close(staging_fd)
            os.close(parent_fd)


def import_archives(paths, destination, apply=False, max_total_bytes=MAX_TOTAL_BYTES,
                    max_entries=MAX_ENTRIES, max_manifest_bytes=MAX_MANIFEST_BYTES):
    if not paths or len(paths) > 128:
        raise ArchiveError('archive_count_invalid')
    if any(type(limit) is not int or limit < 1 for limit in (max_total_bytes, max_entries, max_manifest_bytes)):
        raise ArchiveError('invalid_limit')
    destination = checked_destination(destination)
    with ExitStack() as stack:
        streams, archives, pins = [], [], []
        for index, path in enumerate(paths, start=1):
            descriptor = os.open(path, os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0) | getattr(os, 'O_NONBLOCK', 0))
            stream = stack.enter_context(os.fdopen(descriptor, 'rb'))
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise ArchiveError('nonregular_archive')
            streams.append(stream)
            pins.append({'index': index, 'sha256': hash_archive(stream)})
            archives.append(stack.enter_context(zipfile.ZipFile(stream)))
        files, directories, total_bytes, entry_count = read_headers(archives, max_entries, max_total_bytes)
        files = remove_wrapper(files, directories)
        entries, manifest_bytes = read_manifest(files, max_manifest_bytes, max_entries)
        mapping, normalizations = map_files(entries, files)
        for name, member in mapping.items():
            verify_member(member, entries[name])
        for stream, pin in zip(streams, pins):
            if hash_archive(stream) != pin['sha256']:
                raise ArchiveError('archive_changed')
        if apply:
            install(destination, mapping, entries, manifest_bytes)
    return {'valid': True, 'integrity_valid': True, 'applied': apply,
            'manifest_files': len(entries), 'archive_count': len(paths),
            'archive_entries': entry_count, 'uncompressed_bytes': total_bytes,
            'archives': pins, 'manifest_sha256': hashlib.sha256(manifest_bytes).hexdigest(),
            'normalization_count': len(normalizations), 'normalizations': normalizations[:100],
            'normalizations_truncated': len(normalizations) > 100}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', action='append', required=True, type=Path)
    parser.add_argument('--destination', required=True, type=Path)
    parser.add_argument('--apply', action='store_true', help='Install into a new directory after validation. Default: dry run.')
    parser.add_argument('--max-total-bytes', type=int, default=MAX_TOTAL_BYTES)
    parser.add_argument('--max-entries', type=int, default=MAX_ENTRIES)
    parser.add_argument('--max-manifest-bytes', type=int, default=MAX_MANIFEST_BYTES)
    args = parser.parse_args(argv)
    try:
        result = import_archives(args.archive, args.destination, args.apply, args.max_total_bytes,
                                 args.max_entries, args.max_manifest_bytes)
    except ArchiveError as exc:
        result = {'valid': False, 'integrity_valid': False, 'applied': False, 'errors': [str(exc)]}
    except (zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error, EOFError, NotImplementedError, RuntimeError, UnicodeError):
        result = {'valid': False, 'integrity_valid': False, 'applied': False, 'errors': ['invalid_archive']}
    except OSError:
        result = {'valid': False, 'integrity_valid': False, 'applied': False, 'errors': ['filesystem_error']}
    print(json.dumps(result, sort_keys=True))
    return 0 if result['valid'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
