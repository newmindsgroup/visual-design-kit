# Version-Timestamp: 2026-09-14T19:02:27.477726-04:00
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

CLI = Path(__file__).resolve().parents[1] / 'tools/reference_library.py'

class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for d in ('catalog', 'extracted', 'manifests'):
            (self.root/d).mkdir()
        (self.root/'extracted/u.jsonl').write_text(json.dumps({'page':7,'text':'Typography improves hierarchy.\u2028Balance matters.'})+'\n')
        (self.root/'catalog/items.jsonl').write_text(json.dumps({'id':'book-1','display_title':'Example','extraction':'extracted/u.jsonl'})+'\n')
        self.files = {p.relative_to(self.root).as_posix(): {'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in self.root.rglob('*.jsonl')}
        self.manifest()
    def manifest(self):
        (self.root/'manifests/files.json').write_text(json.dumps({'files':self.files}))
    def run_cli(self,*args):
        return subprocess.run([sys.executable,str(CLI),'--root',str(self.root),*args],capture_output=True,text=True)
    def test_verify(self):
        r=self.run_cli('verify');self.assertEqual(r.returncode,0,r.stderr)
    def test_changed_file(self):
        (self.root/'extracted/u.jsonl').write_text('changed')
        r=self.run_cli('verify');self.assertNotEqual(r.returncode,0);self.assertIn('mismatch',r.stdout)
    def test_missing_file(self):
        (self.root/'extracted/u.jsonl').unlink()
        r=self.run_cli('verify');self.assertNotEqual(r.returncode,0);self.assertIn('missing',r.stdout)
    def test_unsafe_manifest(self):
        self.files['../outside']={'sha256':'0'*64};self.manifest()
        r=self.run_cli('verify');self.assertNotEqual(r.returncode,0);self.assertIn('unsafe',r.stdout)
    def test_search_citation(self):
        r=self.run_cli('search','typography');self.assertEqual(r.returncode,0,r.stderr)
        hit=json.loads(r.stdout);self.assertEqual(hit['source_id'],'book-1');self.assertEqual(hit['page'],7)
    def test_search_rejects_escape(self):
        (self.root/'catalog/items.jsonl').write_text(json.dumps({'id':'bad','extraction':'../outside'})+'\n')
        r=self.run_cli('search','anything');self.assertNotEqual(r.returncode,0)

if __name__ == '__main__': unittest.main()
