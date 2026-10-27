"""Foundation mutation-boundary tests plus non-runtime template wiring checks.

Version-Timestamp: 2026-10-27 08:10:06 AST
"""
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TEMPLATE=ROOT/'skills/bama-new-mac-app/template/Sources'
HARNESS=r'''
import Foundation

enum SaveFailure: Error { case failed }
@MainActor
final class MemoryContext {
    var saved: [String: String] = ["user": "before"]
    var pending: [String: String] = [:]
    var saveCalls = 0
    var rollbacks = 0
    var failAt: Int?
    var hasChanges: Bool { !pending.isEmpty }
    func save() throws {
        saveCalls += 1
        if saveCalls == failAt { throw SaveFailure.failed }
        saved.merge(pending) { _, new in new }
        pending.removeAll()
    }
    func rollback() { pending.removeAll(); rollbacks += 1 }
    func mutate(origin: MutationOrigin, _ block: () throws -> Void) throws {
        try SavedMutation.perform(origin: origin, hasChanges: { self.hasChanges },
            save: { try self.save() }, rollback: { self.rollback() }, mutation: block)
    }
}

@main
struct Check {
 @MainActor static func main() throws {
    let pending = MemoryContext()
    pending.pending["user"] = "unsaved edit"
    var invoked = false
    do {
        try pending.mutate(origin: .agent) { invoked = true; pending.pending["new"] = "agent" }
        fatalError("agent accepted unsaved user edits")
    } catch MutationFailure.unsavedUserEdits {}
    precondition(!invoked && pending.pending["user"] == "unsaved edit")
    precondition(pending.saveCalls == 0 && pending.rollbacks == 0)

    let uiSaveFailure = MemoryContext()
    uiSaveFailure.pending["user"] = "unsaved edit"
    uiSaveFailure.failAt = 1
    invoked = false
    do {
        try uiSaveFailure.mutate(origin: .interface) { invoked = true }
        fatalError("failed pending save accepted")
    } catch SaveFailure.failed {}
    precondition(!invoked && uiSaveFailure.pending["user"] == "unsaved edit")
    precondition(uiSaveFailure.rollbacks == 0)

    let ownFailure = MemoryContext()
    ownFailure.pending["user"] = "accepted UI edit"
    ownFailure.failAt = 2
    do {
        try ownFailure.mutate(origin: .interface) { ownFailure.pending["new"] = "must not leak" }
        fatalError("failed mutation accepted")
    } catch SaveFailure.failed {}
    precondition(ownFailure.saved["user"] == "accepted UI edit")
    precondition(ownFailure.pending.isEmpty && ownFailure.saved["new"] == nil)
    try ownFailure.save()
    precondition(ownFailure.saved["new"] == nil, "later save leaked failed mutation")

    let good = MemoryContext()
    try good.mutate(origin: .agent) { good.pending["new"] = ItemTitle.clean("  Buy   milk\n") }
    precondition(good.saved["new"] == "Buy milk")
    precondition(good.rollbacks == 0)
    precondition(ItemTitle.clean(" \n") == "New Item")

    var deletion = DeleteIntent<String>()
    precondition(deletion.request("A", confirmationRequired: true) == nil)
    precondition(deletion.pending == "A")
    deletion.cancel()
    precondition(deletion.pending == nil, "cancel retained destructive intent")
    precondition(deletion.request("B", confirmationRequired: false) == "B")
    precondition(deletion.pending == nil)
    print("PASS mutation isolation, failure recovery, normalization and deletion intent")
 }
}
'''
class ModelMutations(unittest.TestCase):
 def test_foundation_mutation_boundary(self):
  if not shutil.which('xcrun'):self.skipTest('Apple Swift compiler unavailable')
  with tempfile.TemporaryDirectory(prefix='bama-model-tests-') as folder:
   folder=Path(folder); harness=folder/'Check.swift'; harness.write_text(HARNESS)
   helper=TEMPLATE/'__APP_NAME__Kit/ItemMutations.swift'
   title=TEMPLATE/'__APP_NAME__Kit/ItemTitle.swift'
   binary=folder/'check'
   built=subprocess.run(['xcrun','swiftc','-swift-version','6','-parse-as-library',str(helper),str(title),str(harness),'-o',str(binary)],capture_output=True,text=True)
   self.assertEqual(built.returncode,0,built.stderr)
   ran=subprocess.run([str(binary)],capture_output=True,text=True)
   self.assertEqual(ran.returncode,0,ran.stderr)
   self.assertIn('PASS mutation isolation',ran.stdout)
 def test_template_uses_shared_saved_operations(self):
  model=(TEMPLATE/'__APP_NAME__/Models.swift').read_text()
  ui=(TEMPLATE/'__APP_NAME__/ContentView.swift').read_text()
  agent=(ROOT/'skills/bama-agent-cli/template/Agent/AgentCommands.swift').read_text()
  self.assertIn('SavedMutation.perform(',model)
  self.assertIn('ItemTitle.clean(',model)
  for method in ('createItem(', 'updateItem(', 'deleteItem('):self.assertIn('model.'+method,agent)
  self.assertNotIn('mainContext.save()',agent)
  self.assertNotIn('mainContext.delete(',agent)
  self.assertIn('@AppStorage("confirmDelete")',ui)
  self.assertIn('.confirmationDialog(',ui)
  self.assertIn('model.deleteItem(',ui)
  self.assertNotIn('context.delete(item)',ui)
  self.assertIn('.gridArea("detail"',ui)
  self.assertIn('.gridProbe("detail.content"',ui)
if __name__=='__main__':unittest.main()
