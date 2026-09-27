#!/usr/bin/env python3
# Version-Timestamp: 2026-09-27 14:34:20 AST
"""Read-only, offline reference preflight, integrity checks, and citation search.

Preflight hashes the catalog and extractions and checks original-file metadata
without reading original bytes. It never establishes source consultation,
interprets source instructions, or executes a configured tool. Use verify for
every manifest entry and search for integrity-checked bounded source excerpts.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys


LOCAL_REFERENCE_CONFIG = Path('private/reference-library.local.json')
SHA256 = re.compile(r'[0-9a-fA-F]{64}\Z')


class LibraryError(ValueError):
    """A bounded error code safe for CLI output."""


def external_path(value):
    """Accept an explicit local path without following symlink components."""
    path = Path(value).expanduser().absolute()
    current = Path(path.anchor)
    for part in path.parts[1:]:
        current /= part
        if current.is_symlink():
            raise LibraryError('unsafe_symlink')
    return path


def within(root, relative):
    if (not isinstance(relative, str) or not relative or
            Path(relative).is_absolute() or '..' in Path(relative).parts):
        raise LibraryError('unsafe_relative_path')
    path = root / relative
    current = root
    for part in Path(relative).parts:
        current /= part
        if current.is_symlink():
            raise LibraryError('unsafe_symlink')
    resolved = path.resolve()
    if not resolved.is_relative_to(root) or resolved == root:
        raise LibraryError('unsafe_relative_path')
    return resolved


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def read_object(path):
    with path.open(encoding='utf-8') as stream:
        data = json.load(stream)
    if not isinstance(data, dict):
        raise LibraryError('invalid_object')
    return data


def objects(path):
    with path.open(encoding='utf-8') as stream:
        for line in stream:
            if not line.strip():
                continue
            row = json.loads(line)
            if not isinstance(row, dict):
                raise LibraryError('invalid_row')
            yield row


def manifest_files(root):
    manifest = read_object(within(root, 'manifests/files.json'))
    for key in ('schema', 'schema_version'):
        if key in manifest and (type(manifest[key]) not in (int, str) or
                                manifest[key] not in (1, '1')):
            raise LibraryError('unsupported_schema')
    files = manifest.get('files')
    if not isinstance(files, dict) or not files:
        raise LibraryError('invalid_manifest')
    return files


def validate_entry(entry):
    if (not isinstance(entry, dict) or not isinstance(entry.get('sha256'), str) or
            not SHA256.fullmatch(entry['sha256'])):
        raise LibraryError('invalid_manifest_entry')
    if 'bytes' in entry and (type(entry['bytes']) is not int or entry['bytes'] < 0):
        raise LibraryError('invalid_manifest_entry')


def checked_file(root, relative, files, check_digest=True):
    path = within(root, relative)
    if relative not in files:
        raise LibraryError('missing_manifest_coverage')
    entry = files[relative]
    validate_entry(entry)
    if not path.is_file():
        raise LibraryError('missing')
    if 'bytes' in entry and path.stat().st_size != entry['bytes']:
        raise LibraryError('mismatch')
    if check_digest and digest(path) != entry['sha256'].lower():
        raise LibraryError('mismatch')
    return path


def catalog_rows(path):
    for row in objects(path):
        if not isinstance(row.get('id'), str) or not row['id'].strip():
            raise LibraryError('invalid_catalog_row')
        if row.get('display_title') is not None and not isinstance(row['display_title'], str):
            raise LibraryError('invalid_catalog_row')
        for key in ('original', 'extraction'):
            if row.get(key) is not None and not isinstance(row[key], str):
                raise LibraryError('invalid_catalog_row')
        yield row


def extraction_units(path):
    for unit in objects(path):
        if not isinstance(unit.get('text'), str):
            raise LibraryError('invalid_extraction_unit')
        if 'page' in unit and unit['page'] is not None and type(unit['page']) not in (int, str):
            raise LibraryError('invalid_source_locator')
        for key in ('page_label', 'section'):
            if key in unit and unit[key] is not None and not isinstance(unit[key], str):
                raise LibraryError('invalid_source_locator')
        yield unit


def resolve_reference_config(config=None, project_root=None):
    """Resolve optional settings without importing or executing the optional tool.

    A tool path is checked as a local regular file only. Its presence does not
    attest publisher trust or authorize execution. The installed helper is used.
    """
    if config is None:
        base = Path(project_root) if project_root is not None else Path.cwd()
        config = base / LOCAL_REFERENCE_CONFIG
    try:
        config = external_path(config)
        if not config.exists():
            return None
        if not config.is_file():
            raise LibraryError('invalid_config')
        data = read_object(config)
        root = data.get('reference_library_root')
        if not isinstance(root, str) or not root.strip() or not Path(root).expanduser().is_absolute():
            raise LibraryError('invalid_config')
        tool = data.get('reference_library_tool')
        if 'reference_library_tool' in data:
            if not isinstance(tool, str) or not tool.strip() or not Path(tool).expanduser().is_absolute():
                raise LibraryError('invalid_config')
            tool = external_path(tool)
            if not tool.is_file():
                raise LibraryError('invalid_config')
        return {'reference_library_root': Path(root).expanduser(), 'reference_library_tool': tool}
    except (OSError, ValueError, TypeError, RuntimeError) as exc:
        raise LibraryError('invalid_config') from exc


def library_preflight(root, verify_originals=False):
    """Hash catalog/extractions; check originals as metadata unless requested.

    Status avoids reading original bytes. Search requests referenced original
    hashes too; full verify additionally hashes unreferenced manifest entries.
    """
    files = manifest_files(root)
    # Every declaration must be safe and well-formed, but unrelated file bytes are
    # deliberately left to full verify. No directories are scanned.
    for relative, entry in files.items():
        within(root, relative)
        validate_entry(entry)
    catalog = checked_file(root, 'catalog/items.jsonl', files)
    checked = set()
    extraction_content = {}
    searchable = False
    gaps = False
    for row in catalog_rows(catalog):
        for key in ('original', 'extraction'):
            relative = row.get(key)
            if not relative:
                gaps = True
                continue
            check_digest = key == 'extraction' or verify_originals
            check_key = (relative, check_digest)
            if check_key not in checked:
                checked_file(root, relative, files, check_digest=check_digest)
                checked.add(check_key)
        relative = row.get('extraction')
        if relative:
            if relative not in extraction_content:
                has_text = False
                for unit in extraction_units(within(root, relative)):
                    has_text = bool(unit['text'].strip()) or has_text
                extraction_content[relative] = has_text
            searchable = searchable or extraction_content[relative]
            gaps = gaps or not extraction_content[relative]
    if not searchable:
        return False, 'no_searchable_sources'
    return True, 'local_library_ready_with_gaps' if gaps else 'local_library_ready'


def reference_status(mode='auto', root=None, config=None, require_source=False):
    """Return bounded availability evidence. Available never means consulted."""
    result = {'requested_mode': mode, 'effective_mode': 'standalone',
              'available': False, 'reason': 'standalone_requested', 'consulted': False}
    if mode != 'standalone':
        try:
            if root is None:
                settings = resolve_reference_config(config)
                if settings is None:
                    raise LibraryError('not_configured')
                root = settings['reference_library_root']
            try:
                root = external_path(root).resolve(strict=True)
                if not root.is_dir():
                    raise LibraryError('invalid_root')
            except LibraryError:
                raise
            except (OSError, ValueError, TypeError, RuntimeError) as exc:
                raise LibraryError('invalid_root') from exc
            try:
                available, reason = library_preflight(root)
            except LibraryError:
                raise
            except (OSError, ValueError, TypeError, RuntimeError) as exc:
                raise LibraryError(error_code(exc)) from exc
            result.update(available=available, reason=reason)
            if available:
                result['effective_mode'] = 'local-library'
        except LibraryError as exc:
            result['reason'] = str(exc)
    held = require_source and not result['available']
    if held:
        result['hold'] = 'source_dependent_work'
    return result, 1 if held else 0


def error_code(exc):
    if isinstance(exc, LibraryError):
        return str(exc)
    if isinstance(exc, (json.JSONDecodeError, UnicodeError)):
        return 'invalid_json'
    if isinstance(exc, OSError):
        return 'unreadable_file'
    return 'invalid_library'


def verify(root):
    files = manifest_files(root)
    failures = []
    for relative in files:
        try:
            checked_file(root, relative, files)
        except (OSError, ValueError, KeyError, TypeError, RuntimeError) as exc:
            failures.append({'path': relative, 'status': error_code(exc)})
    print(json.dumps({'checked': len(files), 'failures': failures}))
    return 1 if failures else 0


def search(root, query, limit):
    if not query.strip():
        raise LibraryError('empty_query')
    # Search checks referenced original hashes before emitting any excerpts.
    available, _ = library_preflight(root, verify_originals=True)
    if not available:
        raise LibraryError('no_searchable_sources')
    seen = set()
    count = 0
    for row in catalog_rows(within(root, 'catalog/items.jsonl')):
        relative = row.get('extraction')
        if not relative or relative in seen:
            continue
        seen.add(relative)
        for unit in extraction_units(within(root, relative)):
            text = unit['text']
            pos = text.casefold().find(query.casefold())
            if pos < 0:
                continue
            hit = {'source_id': row['id'], 'title': row.get('display_title'),
                   'excerpt': text[max(0, pos-80):pos+len(query)+160],
                   'original': row.get('original')}
            for key in ('page', 'page_label', 'section'):
                if key in unit:
                    hit[key] = unit[key]
            print(json.dumps(hit, ensure_ascii=False))
            count += 1
            if count >= limit:
                return 0
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    location = parser.add_mutually_exclusive_group()
    location.add_argument('--root', type=Path)
    location.add_argument('--config', type=Path)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('verify', help='verify every manifest file')
    find = sub.add_parser('search', help='emit bounded excerpts with source locators')
    find.add_argument('query')
    find.add_argument('--limit', type=int, default=10, choices=range(1, 101), metavar='1..100')
    status = sub.add_parser('status', help='preflight references; never marks sources consulted')
    status.add_argument('--mode', choices=('auto', 'standalone', 'local-library'), default='auto')
    status.add_argument('--require-source', action='store_true', help='hold dependent work if no usable library')
    status_location = status.add_mutually_exclusive_group()
    status_location.add_argument('--root', type=Path, default=argparse.SUPPRESS)
    status_location.add_argument('--config', type=Path, default=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.root is not None and args.config is not None:
        parser.error('--root and --config are mutually exclusive')
    if args.command == 'status':
        result, code = reference_status(args.mode, args.root, args.config, args.require_source)
        print(json.dumps(result, sort_keys=True))
        return code
    try:
        root = args.root
        if root is None:
            settings = resolve_reference_config(args.config)
            if settings is None:
                raise LibraryError('not_configured')
            root = settings['reference_library_root']
        root = external_path(root).resolve(strict=True)
        if not root.is_dir():
            raise LibraryError('invalid_root')
        return verify(root) if args.command == 'verify' else search(root, args.query, args.limit)
    except (OSError, ValueError, KeyError, TypeError, RuntimeError) as exc:
        print(json.dumps({'error': error_code(exc)}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
