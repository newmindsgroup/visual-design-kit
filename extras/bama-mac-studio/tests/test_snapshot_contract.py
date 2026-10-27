"""Snapshot evidence requires the complete declared native matrix.

Version-Timestamp: 2026-10-27 09:01:10 AST
"""
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / 'skills/bama-new-mac-app/template/tools/run_checks.py'

FIXTURE = r'''#!/usr/bin/env python3
import json, os, struct, zlib
from pathlib import Path
root = Path(os.environ['APP_SNAPSHOT']); root.mkdir()
case = os.environ['BAMA_SNAPSHOT_CASE']
ids = json.loads(os.environ.get('APP_SNAPSHOT_EXPECTED', '["all-light","all-dark","starred-light","starred-dark","settings-general-light","settings-general-dark","settings-appearance-light","settings-appearance-dark"]'))
def chunk(kind, data):
    return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data)&0xffffffff)
png = b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',1,1,8,6,0,0,0))+chunk(b'IDAT',zlib.compress(b'\x00\x00\x00\x00\xff'))+chunk(b'IEND',b'')
windows = {'main': {'number': 100, 'title': 'Fixture', 'identifier': 'main'}, 'settings': {'number': 200, 'title': 'Settings', 'identifier': 'settings'}}
records = []
for i, capture_id in enumerate(ids):
    if case == 'missing_capture' and i == 0: continue
    role = 'settings' if capture_id.startswith('settings-') else 'main'
    window = dict(windows[role])
    if case == 'settings_is_main' and role == 'settings': window = dict(windows['main'])
    filename = capture_id+'.png'
    (root/filename).write_bytes(b'not png' if case == 'invalid_png' and i == 0 else png)
    record = {'id': capture_id, 'filename': filename, 'window_role': role, 'window': window, 'method': 'screencapture', 'status': 'native', 'pixel_width': 1, 'pixel_height': 1, 'errors': []}
    if case == 'degraded' and i == 0: record.update(method='view_cache', status='degraded', errors=['native capture unavailable'])
    if case == 'duplicate' and i == 1: record['id'] = ids[0]
    if case == 'boolean_dimensions' and i == 0: record.update(pixel_width=True, pixel_height=True)
    if case == 'path_traversal' and i == 0: record['filename'] = '../outside.png'
    records.append(record)
manifest = {'schema_version': 1, 'requested': ids, 'completed': True, 'native_complete': True, 'windows': windows, 'captures': records, 'failures': []}
if case == 'bad_shape': manifest['captures'] = {}
if case != 'missing_manifest': (root/'capture-manifest.json').write_text(json.dumps(manifest))
if case == 'linked_directory':
    actual = root.parent/'actual-shots';root.rename(actual);root.symlink_to(actual,target_is_directory=True)
'''

class SnapshotContract(unittest.TestCase):
    def run_fixture(self, case, *options):
        with tempfile.TemporaryDirectory() as directory:
            app = Path(directory)/'snapshot-fixture'
            app.write_text(FIXTURE);app.chmod(0o755)
            result = subprocess.run(['python3',str(RUNNER),'snapshot',str(app),*options],env={**os.environ,'BAMA_SNAPSHOT_CASE':case},capture_output=True,text=True)
        line = next(line for line in result.stdout.splitlines() if line.startswith('BAMA_TEST_ROOT='))
        root = Path(line.split('=',1)[1])
        self.addCleanup(shutil.rmtree,root)
        receipt = json.loads((root/'receipt.json').read_text())
        return result,receipt

    def test_complete_native_matrix_passes(self):
        result,receipt = self.run_fixture('valid')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertTrue(receipt.get('snapshot',{}).get('native_accepted'))
        self.assertEqual(len(receipt['snapshot']['verified']),8)

    def test_any_png_does_not_prove_complete_coverage(self):
        result,receipt = self.run_fixture('missing_capture')
        self.assertEqual(result.returncode,1)
        self.assertFalse(receipt['snapshot']['native_accepted'])
        self.assertIn('all-light',' '.join(receipt['snapshot']['errors']))

    def test_missing_manifest_fails(self):
        result,_ = self.run_fixture('missing_manifest')
        self.assertEqual(result.returncode,1)
        self.assertIn('manifest',result.stderr)

    def test_degraded_preview_does_not_pass_native_acceptance(self):
        result,receipt = self.run_fixture('degraded')
        self.assertEqual(result.returncode,1)
        self.assertFalse(receipt['snapshot']['native_accepted'])
        self.assertIn('degraded',' '.join(receipt['snapshot']['errors']))

    def test_settings_cannot_be_relabelled_main_window(self):
        result,receipt = self.run_fixture('settings_is_main')
        self.assertEqual(result.returncode,1)
        self.assertIn('window',' '.join(receipt['snapshot']['errors']))

    def test_invalid_png_is_not_evidence(self):
        result,receipt = self.run_fixture('invalid_png')
        self.assertEqual(result.returncode,1)
        self.assertIn('PNG',' '.join(receipt['snapshot']['errors']))

    def test_duplicate_capture_is_rejected(self):
        result,receipt = self.run_fixture('duplicate')
        self.assertEqual(result.returncode,1)
        self.assertIn('duplicate',' '.join(receipt['snapshot']['errors']))

    def test_malformed_manifest_fails_without_traceback(self):
        result,_ = self.run_fixture('bad_shape')
        self.assertEqual(result.returncode,1)
        self.assertNotIn('Traceback',result.stderr)

    def test_boolean_dimensions_are_not_integers(self):
        result,receipt = self.run_fixture('boolean_dimensions')
        self.assertEqual(result.returncode,1)
        self.assertIn('dimensions',' '.join(receipt['snapshot']['errors']))

    def test_capture_filename_cannot_traverse(self):
        result,receipt = self.run_fixture('path_traversal')
        self.assertEqual(result.returncode,1)
        self.assertIn('filename',' '.join(receipt['snapshot']['errors']))

    def test_linked_output_directory_is_rejected(self):
        result,receipt = self.run_fixture('linked_directory')
        self.assertEqual(result.returncode,1)
        self.assertIn('directory',' '.join(receipt['snapshot']['errors']))

    def test_selftest_clears_inherited_snapshot_seed_and_agent_modes(self):
        with tempfile.TemporaryDirectory() as directory:
            app = Path(directory)/'selftest-fixture'
            names = ['APP_SNAPSHOT', 'APP_SNAPSHOT_PAGES', 'APP_SNAPSHOT_SETTINGS_TABS', 'APP_SNAPSHOT_APPEARANCES', 'APP_SNAPSHOT_EXPECTED', 'APP_SEED', 'APP_AGENT_ENABLED', 'APP_AGENT_WRITES']
            app.write_text('#!/usr/bin/env python3\nimport os,json\nfrom pathlib import Path\nassert all(key not in os.environ for key in '+repr(names)+")\n(Path(os.environ['APP_TEST_ROOT'])/'selftest-completion.json').write_text(json.dumps({'schema_version': 1, 'started': True, 'completed': True, 'status': 'passed', 'check_count': 1, 'required_check_count': 1, 'required_check_ids': ['fixture-isolation'], 'checks': [{'id': 'fixture-isolation', 'name': 'Fixture isolation checks', 'passed': True, 'detail': ''}], 'failures': [], 'exit_code': 0}))\n")
            app.chmod(0o755)
            result = subprocess.run(['python3',str(RUNNER),'selftest',str(app)],env={**os.environ,**{key:'foreign' for key in names}},capture_output=True,text=True)
        root = Path(next(line.split('=',1)[1] for line in result.stdout.splitlines() if line.startswith('BAMA_TEST_ROOT=')))
        self.addCleanup(shutil.rmtree,root)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(json.loads((root/'receipt.json').read_text())['mode'],'selftest')

    def test_explicit_subset_has_its_own_complete_matrix(self):
        result,receipt = self.run_fixture('valid','--pages','starred')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(set(receipt['snapshot']['verified']),{'starred-light','starred-dark'})

if __name__ == '__main__': unittest.main()
