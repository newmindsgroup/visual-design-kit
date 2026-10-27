"""A zero process exit must not substitute for completed self-test evidence.

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
RUNNER = ROOT/'skills/bama-new-mac-app/template/tools/run_checks.py'
FIXTURE = r'''#!/usr/bin/env python3
import json,os,sys
from pathlib import Path
case=os.environ['BAMA_SELFTEST_CASE'];root=Path(os.environ['APP_TEST_ROOT'])
if case in ['early_zero','missing_receipt']:
    if case=='missing_receipt': print('SELFTEST PASS 99 checks')
    sys.exit(0)
record={'schema_version':1,'started':True,'completed':True,'status':'passed','check_count':1,'required_check_count':1,'required_check_ids':['fixture-check'],'checks':[{'id':'fixture-check','name':'Fixture check','passed':True,'detail':''}],'failures':[],'exit_code':0}
code=0
if case=='incomplete':record.update(completed=False,status='running')
if case=='zero_checks':record.update(check_count=0,required_check_count=0,required_check_ids=[],checks=[])
if case=='failed_matching':
    code=7;record.update(status='failed',exit_code=7,failures=['Fixture check failed']);record['checks'][0]['passed']=False
if case=='return_mismatch':record.update(status='failed',exit_code=1,failures=['Fixture check failed']);record['checks'][0]['passed']=False
if case=='missing_required':record.update(required_check_count=2,required_check_ids=['fixture-check','not-executed'])
if case=='duplicate':record['checks']*=2;record['check_count']=2
if case=='oversized':record['padding']='x'*70000
if case=='bad_shape':record['checks']={}
(root/'selftest-completion.json').write_text(json.dumps(record));sys.exit(code)
'''

class SelfTestCompletion(unittest.TestCase):
    def run_fixture(self,case):
        with tempfile.TemporaryDirectory() as directory:
            app=Path(directory)/'selftest-fixture';app.write_text(FIXTURE);app.chmod(0o755)
            result=subprocess.run(['python3',str(RUNNER),'selftest',str(app)],env={**os.environ,'BAMA_SELFTEST_CASE':case},capture_output=True,text=True)
        paths=[line.split('=',1)[1] for line in result.stdout.splitlines() if line.startswith('BAMA_TEST_ROOT=')]
        self.assertTrue(paths,result.stderr)
        root=Path(paths[0]);self.addCleanup(shutil.rmtree,root)
        return result,json.loads((root/'receipt.json').read_text())

    def test_success_requires_a_completed_check_receipt(self):
        result,receipt=self.run_fixture('success')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertTrue(receipt.get('selftest',{}).get('passed'))
        self.assertTrue(receipt['selftest']['valid_completion'])

    def test_early_zero_exit_fails(self):
        result,receipt=self.run_fixture('early_zero')
        self.assertEqual(result.returncode,1)
        self.assertFalse(receipt['selftest']['passed'])

    def test_stdout_pass_claim_without_receipt_fails(self):
        result,_=self.run_fixture('missing_receipt')
        self.assertEqual(result.returncode,1)

    def test_incomplete_receipt_fails(self):
        result,_=self.run_fixture('incomplete')
        self.assertEqual(result.returncode,1)

    def test_zero_checks_fails(self):
        result,_=self.run_fixture('zero_checks')
        self.assertEqual(result.returncode,1)

    def test_valid_failed_completion_preserves_process_failure(self):
        result,receipt=self.run_fixture('failed_matching')
        self.assertEqual(result.returncode,7)
        self.assertTrue(receipt.get('selftest',{}).get('valid_completion'))
        self.assertFalse(receipt['selftest']['passed'])

    def test_return_code_must_match_receipt(self):
        result,_=self.run_fixture('return_mismatch')
        self.assertEqual(result.returncode,1)

    def test_all_required_checks_must_execute_before_success(self):
        result,_=self.run_fixture('missing_required')
        self.assertEqual(result.returncode,1)

    def test_duplicate_check_records_fail(self):
        result,_=self.run_fixture('duplicate')
        self.assertEqual(result.returncode,1)

    def test_receipt_is_bounded(self):
        result,_=self.run_fixture('oversized')
        self.assertEqual(result.returncode,1)

    def test_malformed_receipt_fails_without_traceback(self):
        result,_=self.run_fixture('bad_shape')
        self.assertEqual(result.returncode,1)
        self.assertNotIn('Traceback',result.stderr)


NATIVE_STUBS = r'''
import Foundation
import Darwin

struct FetchDescriptor<T> { init() {} }
enum FixtureError: Error { case fetch }
final class Item {
    let id: Int
    var title: String { didSet { context?.hasChanges = true } }
    var isStarred = false { didSet { context?.hasChanges = true } }
    weak var context: FixtureContext?
    init(id: Int, title: String) { self.id=id; self.title=title }
}
final class FixtureContext {
    var values: [Item] = []
    var hasChanges = false
    func fetch(_ descriptor: FetchDescriptor<Item>) throws -> [Item] {
        if ProcessInfo.processInfo.environment["BAMA_NATIVE_CASE"] == "fetch-fails" { throw FixtureError.fetch }
        return values
    }
    func save() throws { hasChanges=false }
    func rollback() { hasChanges=false }
}
final class FixtureContainer { let mainContext=FixtureContext() }
final class AppModel {
    let container=FixtureContainer()
    var selection: Int?
    var createCalls=0
    func addItem() { _ = try! createItem(title: "", origin: .interface) }
    @discardableResult func createItem(title: String,origin: MutationOrigin) throws -> Item {
        createCalls += 1
        let context=container.mainContext
        let item=Item(id:createCalls,title:ItemTitle.clean(title));item.context=context
        let result=try SavedMutation.perform(origin:origin,hasChanges:{context.hasChanges},save:{try context.save()},rollback:{context.rollback()},mutation:{context.values.append(item);context.hasChanges=true;return item})
        selection=ProcessInfo.processInfo.environment["BAMA_NATIVE_CASE"] == "selected-missing" ? 999 : item.id
        return result
    }
    func updateItem(_ item: Item,title: String?=nil,starred: Bool?=nil,origin:MutationOrigin) throws {
        let context=container.mainContext
        try SavedMutation.perform(origin:origin,hasChanges:{context.hasChanges},save:{try context.save()},rollback:{context.rollback()},mutation:{if let title {item.title=ItemTitle.clean(title)};if let starred {item.isStarred=starred}})
    }
    func deleteItem(_ item: Item,origin:MutationOrigin) throws {
        let context=container.mainContext
        try SavedMutation.perform(origin:origin,hasChanges:{context.hasChanges},save:{try context.save()},rollback:{context.rollback()},mutation:{context.values.removeAll{$0.id==item.id};context.hasChanges=true})
        if selection==item.id {selection=nil}
    }
}
final class FixtureWindow {
    var attachedSheet: FixtureWindow?
    func endSheet(_ sheet: FixtureWindow) { attachedSheet=nil }
}
final class FixtureApplication {
    var windows: [FixtureWindow]=[]
    var terminated=false
    var terminationCount=0
    func terminate(_ sender: Any?) { terminated=true;terminationCount+=1 }
}
let NSApp=FixtureApplication()
enum Store {
    static var isOverridden: Bool {
        guard let path=ProcessInfo.processInfo.environment["APP_STORE"] else {return false}
        return TestIsolation.contains(path)
    }
}

@main struct SelfTestFixtureDriver {
    static func main() async {
        func require(_ condition: Bool,_ message:String) {
            if !condition {print("HARNESS FAIL "+message);exit(2)}
        }
        require(SelfTest.requested,"selftest argument")
        require(SelfTest.exitCode != 0,"default must fail before checks run")
        if ProcessInfo.processInfo.environment["BAMA_NATIVE_CASE"] == "isolation-paths" {
            let rawRoot = ProcessInfo.processInfo.environment["APP_TEST_ROOT"]!
            let newStore = rawRoot + "/test.store"
            require(TestIsolation.contains(newStore),"brand-new store under Python canonical path")
            let existing = rawRoot + "/existing.store"
            _ = FileManager.default.createFile(atPath:existing,contents:Data())
            require(TestIsolation.contains(existing),"existing store under canonical path")
            if rawRoot.hasPrefix("/private/") {
                let alias = String(rawRoot.dropFirst(8))
                require(TestIsolation.contains(alias + "/test.store"),"canonical root aliases agree for new store")
                require(TestIsolation.contains(alias + "/existing.store"),"canonical root aliases agree for existing store")
            }
            require(!TestIsolation.contains(rawRoot),"root itself is not a child store")
            require(!TestIsolation.contains(rawRoot + "/new-nonexistent/../../outside.store"),"missing traversal is refused")
            require(!TestIsolation.contains("relative.store"),"relative path is refused")
            require(!TestIsolation.contains(rawRoot + "/bad\0path"),"NUL path is refused")
            let outside = ProcessInfo.processInfo.environment["BAMA_ISOLATION_OUTSIDE"]!
            let link = rawRoot + "/outside-link"
            try! FileManager.default.createSymbolicLink(atPath:link,withDestinationPath:outside)
            require(!TestIsolation.contains(link + "/new.store"),"symlink escape is refused")
            let dangling = rawRoot + "/dangling-link"
            try! FileManager.default.createSymbolicLink(atPath:dangling,withDestinationPath:outside + "/not-created")
            require(!TestIsolation.contains(dangling + "/new.store"),"dangling symlink escape is refused")
            print("HARNESS PASS isolation-paths")
            return
        }
        let model=AppModel()
        SelfTest.runIfRequested(model:model)
        SelfTest.runIfRequested(model:model)
        let root=TestIsolation.root!
        let receipt=root.appendingPathComponent("selftest-completion.json")
        let initial=(try! JSONSerialization.jsonObject(with:Data(contentsOf:receipt))) as! [String:Any]
        if initial["completed"] as? Bool != false { print("HARNESS INITIAL \(initial)") }
        require(initial["started"] as? Bool == true && initial["completed"] as? Bool == false,"initial receipt is incomplete")
        let deadline=Date().addingTimeInterval(5)
        while !NSApp.terminated && Date()<deadline {try? await Task.sleep(for:.milliseconds(20))}
        require(NSApp.terminated,"completion terminates")
        require(NSApp.terminationCount==1,"reentry schedules one run only")
        let result=(try! JSONSerialization.jsonObject(with:Data(contentsOf:receipt))) as! [String:Any]
        require(result["completed"] as? Bool == true,"completion receipt")
        let mode=ProcessInfo.processInfo.environment["BAMA_NATIVE_CASE"] ?? "normal"
        if mode=="normal" {
            require(SelfTest.exitCode==0 && result["status"] as? String == "passed","normal run passes")
            require(result["check_count"] as? Int == 9,"all nine required checks execute")
            require(model.createCalls==1,"reentry does not duplicate model changes")
        } else {
            require(SelfTest.exitCode != 0 && result["status"] as? String == "failed","invalid path fails")
            if mode=="selected-missing" {
                let checks=result["checks"] as! [[String:Any]]
                require(checks.contains{$0["id"] as? String == "selected-item-available" && $0["passed"] as? Bool == false},"missing selected item is explicit failure")
            }
        }
        print("HARNESS PASS "+mode)
    }
}
'''

@unittest.skipUnless(os.uname().sysname == 'Darwin' and shutil.which('xcrun'), 'requires the macOS Swift toolchain')
class NativeSelfTestState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory(prefix='bama-selftest-state-')
        cls.addClassCleanup(cls.temp.cleanup)
        cls.directory=Path(cls.temp.name).resolve()
        app=ROOT/'skills/bama-new-mac-app/template/Sources/__APP_NAME__'
        kit=ROOT/'skills/bama-new-mac-app/template/Sources/__APP_NAME__Kit'
        source=(app/'SelfTest.swift').read_text()
        source='\n'.join(line for line in source.splitlines() if line not in ['import AppKit','import SwiftData','import __APP_NAME__Kit'])
        (cls.directory/'SelfTest.swift').write_text('import Foundation\nimport Darwin\n'+source)
        (cls.directory/'Fixture.swift').write_text(NATIVE_STUBS)
        cls.binary=cls.directory/'selftest-state'
        command=['xcrun','swiftc','-swift-version','6','-default-isolation','MainActor','-warnings-as-errors','-module-cache-path',str(cls.directory/'module-cache'),str(cls.directory/'SelfTest.swift'),str(cls.directory/'Fixture.swift'),str(kit/'ItemTitle.swift'),str(kit/'ItemMutations.swift'),str(app/'TestState.swift'),'-o',str(cls.binary)]
        result=subprocess.run(command,capture_output=True,text=True)
        if result.returncode:raise AssertionError(result.stdout+result.stderr)

    def run_native(self,mode):
        root=Path(tempfile.mkdtemp(prefix='bama-test-')).resolve()
        self.addCleanup(shutil.rmtree,root)
        (root/'.bama-test-root').write_text('owned selftest harness\n')
        outside=Path(tempfile.mkdtemp(prefix='bama-selftest-outside-')).resolve()
        self.addCleanup(shutil.rmtree,outside)
        result=subprocess.run([str(self.binary),'--selftest'],env={**os.environ,'BAMA_NATIVE_CASE':mode,'APP_TEST_ROOT':str(root),'APP_STORE':str(root/'test.store'),'BAMA_ISOLATION_OUTSIDE':str(outside)},capture_output=True,text=True,timeout=10)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertIn('HARNESS PASS '+mode,result.stdout)

    def test_owned_isolation_paths_aliases_and_symlink_escape(self):self.run_native('isolation-paths')
    def test_default_failure_reentry_and_completed_success(self):self.run_native('normal')
    def test_missing_selected_item_is_explicit_failure(self):self.run_native('selected-missing')
    def test_fetch_error_cannot_become_empty_success(self):self.run_native('fetch-fails')

if __name__=='__main__':unittest.main()
