"""Synthetic archive import checks. No private reference material is used."""
# Version-Timestamp: 2026-09-27 14:43:14 AST
import hashlib
import importlib.util
import json
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import warnings
import zipfile


CLI = Path(__file__).resolve().parents[1] / 'tools/import_reference_archive.py'
MANIFEST = 'manifests/files.json'


class ReferenceArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path.cwd())
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.destination = self.root / 'installed'
        self.contents = {
            'catalog/items.jsonl': b'{"id":"sample","original":"originals/sample","extraction":"extracted/sample.jsonl"}\n',
            'originals/sample': b'Synthetic reference bytes.\n',
            'extracted/sample.jsonl': b'{"page":1,"text":"Synthetic reference text."}\n',
        }
        self.manifest = {'files': {
            name: {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
            for name, data in self.contents.items()
        }}

    def members(self, manifest=None):
        return {**self.contents, MANIFEST: json.dumps(manifest or self.manifest).encode()}

    def archive(self, members=None, name='part.zip', prefix=''):
        path = self.root / name
        with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for relative, contents in (members or self.members()).items():
                archive.writestr(prefix + relative, contents)
        return path

    def invoke(self, archives, *args, destination=None):
        command = [sys.executable, str(CLI)]
        for archive in archives:
            command.extend(['--archive', str(archive)])
        command.extend(['--destination', str(destination or self.destination), *args])
        return subprocess.run(command, capture_output=True, text=True)

    def valid(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stderr, '')
        data = json.loads(result.stdout)
        self.assertTrue(data['valid'])
        self.assertTrue(data['integrity_valid'])
        return data

    def invalid(self, result, code=None):
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(result.stderr, '')
        data = json.loads(result.stdout)
        self.assertFalse(data['valid'])
        self.assertFalse(data['applied'])
        if code:
            self.assertIn(code, data['errors'])
        self.assertFalse(self.destination.exists())
        self.assertEqual(list(self.root.glob('.reference-import-*')), [])

    def test_default_dry_run_verifies_and_records_pins_without_writes(self):
        archive = self.archive()
        before = sorted(self.root.iterdir())
        data = self.valid(self.invoke([archive]))
        self.assertFalse(data['applied'])
        self.assertEqual(data['manifest_files'], 3)
        self.assertEqual(data['normalization_count'], 0)
        self.assertEqual(data['archives'], [{'index': 1, 'sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}])
        self.assertEqual(data['manifest_sha256'], hashlib.sha256(self.members()[MANIFEST]).hexdigest())
        self.assertEqual(sorted(self.root.iterdir()), before)

    def test_split_wrapper_archive_restores_unique_appended_extension(self):
        members = self.members()
        original = members.pop('originals/sample')
        first = self.archive(members, name='part1.zip', prefix='library-v1/')
        second = self.archive({'originals/sample.eml': original}, name='part2.zip', prefix='library-v1/')
        data = self.valid(self.invoke([first, second], '--apply'))
        self.assertTrue(data['applied'])
        self.assertEqual(data['normalizations'], [{'from': 'originals/sample.eml', 'to': 'originals/sample'}])
        installed = {p.relative_to(self.destination).as_posix(): p.read_bytes()
                     for p in self.destination.rglob('*') if p.is_file()}
        self.assertEqual(installed, self.members())
        self.assertEqual(list(self.root.glob('.reference-import-*')), [])

    def test_legacy_manifest_without_sizes_or_schema_is_accepted(self):
        for entry in self.manifest['files'].values():
            del entry['bytes']
        self.valid(self.invoke([self.archive()]))

    def test_normalization_is_not_a_fuzzy_name_match(self):
        for candidate in ('originals/sampleX', 'elsewhere/sample.eml', 'originals/sample.', 'originals/sample.eml.more'):
            with self.subTest(candidate=candidate):
                members = self.members()
                members[candidate] = members.pop('originals/sample')
                self.invalid(self.invoke([self.archive(members)]), 'missing_manifest_file')

    def test_ambiguous_appended_extensions_are_rejected_even_if_both_match(self):
        members = self.members()
        original = members.pop('originals/sample')
        members['originals/sample.eml'] = original
        members['originals/sample.bin'] = original
        self.invalid(self.invoke([self.archive(members)], '--apply'), 'ambiguous_normalization')

    def test_missing_part_changed_content_wrong_size_and_extra_files_fail(self):
        for mutation, code in ((lambda m: m.pop('originals/sample'), 'missing_manifest_file'),
                               (lambda m: m.update({'originals/sample': b'changed'}), 'integrity_mismatch'),
                               (lambda m: m.update({'unexpected.txt': b'extra'}), 'unexpected_archive_file')):
            with self.subTest(code=code):
                members = self.members()
                mutation(members)
                self.invalid(self.invoke([self.archive(members)], '--apply'), code)
        self.manifest['files']['originals/sample']['bytes'] += 1
        self.invalid(self.invoke([self.archive()], '--apply'), 'integrity_mismatch')

    def test_changed_appended_extension_bytes_are_rejected(self):
        members = self.members()
        members.pop('originals/sample')
        members['originals/sample.eml'] = b'wrong bytes'
        self.invalid(self.invoke([self.archive(members)], '--apply'), 'integrity_mismatch')

    def test_unsafe_archive_paths_are_rejected_before_writing(self):
        for relative in ('../outside', '/absolute', 'C:/drive', 'a\\b', './dot', 'a//b', 'a/../b', 'a/\x00b'):
            with self.subTest(relative=relative):
                members = self.members()
                members[relative] = b'untrusted'
                self.invalid(self.invoke([self.archive(members)], '--apply'))

    def test_nonregular_entries_are_rejected(self):
        for file_type in (stat.S_IFLNK, stat.S_IFIFO, stat.S_IFSOCK):
            with self.subTest(file_type=file_type):
                archive = self.archive()
                info = zipfile.ZipInfo('special')
                info.create_system = 3
                info.external_attr = (file_type | 0o600) << 16
                with zipfile.ZipFile(archive, 'a') as stream:
                    stream.writestr(info, b'outside')
                self.invalid(self.invoke([archive], '--apply'), 'nonregular_archive_entry')

    def test_duplicate_file_names_within_or_across_parts_are_rejected(self):
        archive = self.archive()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            with zipfile.ZipFile(archive, 'a') as stream:
                stream.writestr('originals/sample', self.contents['originals/sample'])
        self.invalid(self.invoke([archive]), 'duplicate_archive_file')
        first = self.archive(name='first.zip')
        second = self.archive({'originals/sample': self.contents['originals/sample']}, name='second.zip')
        self.invalid(self.invoke([first, second]), 'duplicate_archive_file')

    def test_duplicate_directory_headers_are_allowed_but_file_conflicts_are_not(self):
        archive = self.archive()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            with zipfile.ZipFile(archive, 'a') as stream:
                stream.writestr('originals/', b'')
                stream.writestr('originals/', b'')
        self.valid(self.invoke([archive]))
        with zipfile.ZipFile(archive, 'a') as stream:
            stream.writestr('originals', b'file blocks directory')
        self.invalid(self.invoke([archive]), 'archive_path_conflict')

    def test_case_and_unicode_collisions_are_rejected_portably(self):
        for names in (('Extra', 'extra'), ('caf\u00e9', 'cafe\u0301')):
            with self.subTest(names=names):
                members = self.members()
                members.update({name: b'bytes' for name in names})
                self.invalid(self.invoke([self.archive(members)]), 'archive_path_collision')

    def test_entry_uncompressed_and_manifest_bounds_are_enforced(self):
        archive = self.archive()
        for options, code in ((('--max-entries', '2'), 'entry_limit_exceeded'),
                              (('--max-total-bytes', '10'), 'uncompressed_limit_exceeded'),
                              (('--max-manifest-bytes', '10'), 'manifest_limit_exceeded')):
            with self.subTest(options=options):
                self.invalid(self.invoke([archive], *options), code)

    def test_manifest_requires_safe_paths_valid_hashes_and_catalog_coverage(self):
        invalid_manifests = [
            {'files': {}}, {'files': []}, {'schema': 2, 'files': self.manifest['files']},
            {'files': {'../escape': {'sha256': 'a' * 64}}},
            {'files': {'catalog/items.jsonl': {'sha256': 'bad'}}},
            {'files': {'catalog/items.jsonl': {'sha256': 'a' * 64, 'bytes': True}}},
            {'files': {'originals/sample': self.manifest['files']['originals/sample']}},
            {'files': {**self.manifest['files'], MANIFEST: {'sha256': 'a' * 64}}},
        ]
        for manifest in invalid_manifests:
            with self.subTest(manifest=manifest):
                self.invalid(self.invoke([self.archive(self.members(manifest))]))

    def test_duplicate_json_keys_are_rejected(self):
        members = self.members()
        members[MANIFEST] = b'{"files":{},"files":{}}'
        self.invalid(self.invoke([self.archive(members)]), 'duplicate_manifest_key')

    def test_manifest_output_file_directory_conflict_is_rejected_in_dry_run(self):
        self.contents['originals/sample/child'] = b'child'
        self.manifest['files']['originals/sample/child'] = {
            'sha256': hashlib.sha256(b'child').hexdigest()}
        members = self.members()
        members['originals/sample.eml'] = members.pop('originals/sample')
        self.invalid(self.invoke([self.archive(members)]), 'manifest_path_conflict')

    def test_multiple_or_mixed_wrapper_roots_are_rejected(self):
        first = self.archive(name='first.zip', prefix='first/')
        second = self.archive(name='second.zip', prefix='second/')
        self.invalid(self.invoke([first, second]), 'manifest_count_invalid')
        members = {f'first/{name}': data for name, data in self.members().items()}
        members['outside.txt'] = b'unexpected'
        self.invalid(self.invoke([self.archive(members)]), 'mixed_archive_roots')

    def test_existing_destination_is_never_overwritten(self):
        archive = self.archive()
        self.destination.mkdir()
        (self.destination / 'preserved').write_bytes(b'keep')
        result = self.invoke([archive], '--apply')
        self.assertEqual(result.returncode, 1)
        self.assertIn('destination_exists', json.loads(result.stdout)['errors'])
        self.assertEqual((self.destination / 'preserved').read_bytes(), b'keep')

    def test_destination_symlink_parent_is_rejected(self):
        (self.root / 'real').mkdir()
        (self.root / 'link').symlink_to(self.root / 'real', target_is_directory=True)
        result = self.invoke([self.archive()], '--apply', destination=self.root / 'link' / 'new')
        self.invalid(result, 'unsafe_destination_symlink')
        self.assertEqual(list((self.root / 'real').iterdir()), [])

    def test_missing_destination_parent_is_rejected_without_creation(self):
        result = self.invoke([self.archive()], '--apply', destination=self.root / 'missing' / 'new')
        self.invalid(result, 'destination_parent_missing')
        self.assertFalse((self.root / 'missing').exists())

    def test_crc_corruption_is_rejected_without_installation(self):
        path = self.root / 'corrupt.zip'
        with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_STORED) as archive:
            for name, data in self.members().items():
                archive.writestr(name, data)
        raw = path.read_bytes()
        raw = raw.replace(b'Synthetic reference bytes.', b'Corrupted reference bytes.', 1)
        path.write_bytes(raw)
        self.invalid(self.invoke([path], '--apply'), 'invalid_archive')

    def test_invalid_deflate_stream_has_a_bounded_error(self):
        path = self.archive()
        with zipfile.ZipFile(path) as archive:
            info = archive.getinfo('originals/sample')
            offset = info.header_offset + 30 + len(info.filename.encode()) + len(info.extra)
        raw = bytearray(path.read_bytes())
        raw[offset] = 7  # Invalid DEFLATE block type.
        path.write_bytes(raw)
        self.invalid(self.invoke([path], '--apply'), 'invalid_archive')

    def test_failure_during_copy_cleans_own_staging_directory(self):
        spec = importlib.util.spec_from_file_location('archive_import', CLI)
        subject = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(subject)
        archive = self.archive()
        with mock.patch.object(subject, 'copy_verified_file', side_effect=OSError('simulated write failure')):
            with self.assertRaises(OSError):
                subject.import_archives([archive], self.destination, apply=True)
        self.assertFalse(self.destination.exists())
        self.assertEqual(list(self.root.glob('.reference-import-*')), [])

    def test_concurrent_destination_creation_cannot_be_overwritten(self):
        spec = importlib.util.spec_from_file_location('archive_import', CLI)
        subject = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(subject)
        archive = self.archive()
        rename = subject.exclusive_rename

        def race(parent_fd, source, destination):
            self.destination.mkdir()
            return rename(parent_fd, source, destination)

        with mock.patch.object(subject, 'exclusive_rename', side_effect=race):
            with self.assertRaisesRegex(subject.ArchiveError, 'destination_exists'):
                subject.import_archives([archive], self.destination, apply=True)
        self.assertEqual(list(self.destination.iterdir()), [])
        self.assertEqual(list(self.root.glob('.reference-import-*')), [])

    def test_swapped_destination_parent_does_not_redirect_staged_writes(self):
        spec = importlib.util.spec_from_file_location('archive_import', CLI)
        subject = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(subject)
        archive = self.archive()
        parent = self.root / 'parent'
        parent.mkdir()
        moved = self.root / 'moved'
        outside = self.root / 'outside'
        outside.mkdir()
        self.destination = parent / 'new'
        copy_file = subject.copy_verified_file
        swapped = False

        def race(*args):
            nonlocal swapped
            if not swapped:
                parent.rename(moved)
                parent.symlink_to(outside, target_is_directory=True)
                swapped = True
            return copy_file(*args)

        with mock.patch.object(subject, 'copy_verified_file', side_effect=race):
            with self.assertRaises(subject.ArchiveError):
                subject.import_archives([archive], self.destination, apply=True)
        self.assertEqual(list(outside.iterdir()), [])
        self.assertEqual(list(moved.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
