"""Version-Timestamp: 2026-10-27 07:53:44 AST. Preference isolation contract."""
import json,os,shutil,subprocess,tempfile,unittest,uuid
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'skills/bama-new-mac-app/template/Sources/__APP_NAME__/TestState.swift'
class Preferences(unittest.TestCase):
 def test_isolated_domain_does_not_change_standard_preferences(self):
  self.assertTrue(SOURCE.exists(),'a central test-state adapter is required')
  with tempfile.TemporaryDirectory(prefix='bama-pref-compile-') as tmp:
   work=Path(tmp);probe=work/'Probe.swift';binary=work/'probe'
   probe.write_text(r'''import Foundation
@main @MainActor struct Probe {
 static func main() throws {
  let key=CommandLine.arguments[1]
  if TestIsolation.root != nil {
   let isolated=AppPreferences.shared !== UserDefaults.standard
   AppPreferences.shared.set("test-value",forKey:key)
   let standardUnchanged=UserDefaults.standard.object(forKey:key)==nil
   AppPreferences.clearTestDomain()
   let cleared=AppPreferences.shared.object(forKey:key)==nil
   print("{\"isolated\":\(isolated),\"standardUnchanged\":\(standardUnchanged),\"cleared\":\(cleared)}")
  } else { print("{\"normalUsesStandard\":\(AppPreferences.shared === UserDefaults.standard)}") }
 }
}''')
   subprocess.run(['xcrun','swiftc','-swift-version','6',str(SOURCE),str(probe),'-o',str(binary)],check=True,capture_output=True,text=True)
   normalenv={k:v for k,v in os.environ.items() if k not in ('APP_TEST_ROOT','APP_STORE')}
   normal=subprocess.run([str(binary),str(uuid.uuid4())],env=normalenv,capture_output=True,text=True,check=True)
   self.assertTrue(json.loads(normal.stdout)['normalUsesStandard'])
   isolated=Path(tempfile.mkdtemp(prefix='bama-test-')).resolve()
   try:
    (isolated/'.bama-test-root').write_text('owned fixture')
    result=subprocess.run([str(binary),str(uuid.uuid4())],env={**normalenv,'APP_TEST_ROOT':str(isolated),'APP_STORE':str(isolated/'test.store')},capture_output=True,text=True,check=True)
    self.assertEqual(json.loads(result.stdout),{'isolated':True,'standardUnchanged':True,'cleared':True})
   finally:shutil.rmtree(isolated)
if __name__=='__main__':unittest.main()
