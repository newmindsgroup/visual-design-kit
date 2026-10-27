# Version-Timestamp: 2026-10-27 09:01:10 AST
import unittest, subprocess, tempfile, os, json, shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
NEW=ROOT/'skills/bama-new-mac-app/scripts/new-app.sh'
class Guards(unittest.TestCase):
 def test_scaffold_never_commits(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp); bin=p/'bin'; bin.mkdir(); log=p/'git-calls'
   (bin/'git').write_text('#!/bin/sh\necho called >> "'+str(log)+'"\n'); (bin/'git').chmod(0o755)
   result=subprocess.run(["zsh",str(NEW),'Probe','com.example.probe',str(p)],env={**os.environ,'PATH':str(bin)+':'+os.environ['PATH']},capture_output=True,text=True)
   self.assertEqual(result.returncode,0,result.stderr)
   self.assertFalse(log.exists(),'scaffolding must not stage/commit')
 def test_scaffold_rejects_invalid_bundle(self):
  with tempfile.TemporaryDirectory() as tmp:
   result=subprocess.run(["zsh",str(NEW),'Probe','bad/bundle',tmp],capture_output=True,text=True)
   self.assertNotEqual(result.returncode,0)
   self.assertFalse((Path(tmp)/'Probe').exists(),'invalid bundle must be rejected before writing')
 def test_scaffold_refuses_existing_content(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'Probe'; p.mkdir(); f=p/'keep.md'; f.write_text('must keep __APP_NAME__')
   result=subprocess.run(["zsh",str(NEW),'Probe','com.example.probe',tmp],capture_output=True,text=True)
   self.assertNotEqual(result.returncode,0)
   self.assertEqual(f.read_text(),'must keep __APP_NAME__')
class IsolatedChecks(unittest.TestCase):
 def test_selftest_gets_an_owned_isolated_store(self):
  with tempfile.TemporaryDirectory() as tmp:
   executable=Path(tmp)/'fake-app'
   executable.write_text('#!/usr/bin/env python3\nimport os,json\nfrom pathlib import Path\np=Path(os.environ["APP_TEST_ROOT"])\nassert (p/".bama-test-root").is_file()\nassert Path(os.environ["APP_STORE"]).parent==p\nassert "APP_AGENT_WRITES" not in os.environ\nprint("isolated fixture passed")\n(Path(os.environ[\'APP_TEST_ROOT\'])/\'selftest-completion.json\').write_text(json.dumps({\'schema_version\': 1, \'started\': True, \'completed\': True, \'status\': \'passed\', \'check_count\': 1, \'required_check_count\': 1, \'required_check_ids\': [\'fixture-isolation\'], \'checks\': [{\'id\': \'fixture-isolation\', \'name\': \'Fixture isolation checks\', \'passed\': True, \'detail\': \'\'}], \'failures\': [], \'exit_code\': 0}))\n')
   executable.chmod(0o755)
   runner=ROOT/'skills/bama-new-mac-app/template/tools/run_checks.py'
   result=subprocess.run(['python3',str(runner),'selftest',str(executable)],capture_output=True,text=True)
   self.assertEqual(result.returncode,0,result.stderr)
   path=Path(next(line.split('=',1)[1] for line in result.stdout.splitlines() if line.startswith('BAMA_TEST_ROOT=')))
   self.assertTrue((path/'receipt.json').exists())
   shutil.rmtree(path)
 def test_failed_check_status_is_propagated(self):
  runner=ROOT/'skills/bama-new-mac-app/template/tools/run_checks.py'
  result=subprocess.run(['python3',str(runner),'selftest','/usr/bin/false'],capture_output=True,text=True)
  self.assertEqual(result.returncode,1)
  path=Path(next(line.split('=',1)[1] for line in result.stdout.splitlines() if line.startswith('BAMA_TEST_ROOT=')))
  shutil.rmtree(path)
 def test_snapshot_without_images_fails(self):
  runner=ROOT/'skills/bama-new-mac-app/template/tools/run_checks.py'
  result=subprocess.run(['python3',str(runner),'snapshot','/usr/bin/true'],capture_output=True,text=True)
  self.assertEqual(result.returncode,1)
  self.assertIn('no PNG',result.stderr)
  path=Path(next(line.split('=',1)[1] for line in result.stdout.splitlines() if line.startswith('BAMA_TEST_ROOT=')))
  shutil.rmtree(path)
if __name__=='__main__': unittest.main()
