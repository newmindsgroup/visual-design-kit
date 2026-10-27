"""Bounded item receipts and pagination run against the actual Foundation helper.

Version-Timestamp: 2026-10-27 08:39:37 AST
"""
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HELPER=ROOT/'skills/bama-new-mac-app/template/Sources/__APP_NAME__Kit/AgentItemOutput.swift'
HARNESS=r'''
import Foundation
func size(_ value: [String: Any]) throws -> Int {
    try JSONSerialization.data(withJSONObject: value, options: [.sortedKeys, .withoutEscapingSlashes]).count
}
func record(_ id: String, notes: String, title: String = "Title") -> AgentItemOutput.Record {
    .init(id: id, title: title, notes: notes, starred: false, createdAt: "2026-10-27T00:00:00Z")
}
@main struct Check {
 static func main() throws {
    let huge = record("0123456789abcdef0123456789abcdef", notes: String(repeating: "界", count: 3_000_000), title: String(repeating: "\n", count: 50_000))
    for outcome in [AgentItemOutput.Outcome.created, .updated, .deleted] {
        let receipt = AgentItemOutput.receipt(huge, outcome: outcome)
        precondition(receipt["completed"] as? Bool == true)
        precondition(receipt["outcome"] as? String == outcome.rawValue)
        precondition(receipt["id"] as? String == huge.id)
        precondition(try! size(receipt) < 16_384, "saved mutation receipt exceeded its bounded contract")
        let item = receipt["item"] as! [String: Any]
        precondition(item["notesByteCount"] as? Int == huge.notes.utf8.count)
        precondition(item["truncated"] as? Bool == true)
        precondition(item["notes"] == nil, "receipt silently returned clipped notes as complete data")
    }
    let normal = record("normal", notes: "full small notes")
    let normalPage = try AgentItemOutput.page([normal], offset: 0, limit: 500, byteBudget: 32_768)
    let normalItem = (normalPage["items"] as! [[String: Any]])[0]
    precondition(normalItem["notes"] as? String == normal.notes)
    precondition(normalItem["recordTruncated"] == nil)

    let notes = String(repeating: "\\\n\"🌏", count: 400)
    let values = (0..<40).map { record("id\($0)", notes: notes) }
    var offset = 0
    var seen: [String] = []
    while offset < values.count {
        let page = try AgentItemOutput.page(values, offset: offset, limit: 500, byteBudget: 32_768)
        precondition(try! size(page) <= 32_768)
        let items = page["items"] as! [[String: Any]]
        precondition(!items.isEmpty, "page did not make progress")
        seen += items.map { $0["id"] as! String }
        if let next = page["nextOffset"] as? Int {
            precondition(next == offset + items.count, "pagination skipped unreturned rows")
            offset = next
        } else { offset = values.count }
    }
    precondition(seen == values.map(\.id), "byte pagination skipped or duplicated records")

    let over = try AgentItemOutput.page([huge, normal], offset: 0, limit: 1, byteBudget: 32_768)
    precondition(try! size(over) <= 32_768)
    let overItems = over["items"] as! [[String: Any]]
    precondition(overItems.first?["id"] as? String == huge.id)
    precondition(overItems.first?["recordTruncated"] as? Bool == true)
    precondition(overItems.first?["notesByteCount"] as? Int == huge.notes.utf8.count)
    precondition(over["nextOffset"] as? Int == 1, "oversized first row did not advance")
    let afterHuge = try AgentItemOutput.page([huge, normal], offset: 1, limit: 1, byteBudget: 32_768)
    precondition((afterHuge["items"] as! [[String: Any]])[0]["notes"] as? String == normal.notes)
    let many = (0..<600).map { record("short\($0)", notes: "x") }
    let capped = try AgentItemOutput.page(many, offset: 0, limit: 500)
    precondition((capped["items"] as! [[String: Any]]).count == 500)
    precondition(capped["nextOffset"] as? Int == 500)
    let show = AgentItemOutput.show(huge)
    precondition(show["recordTruncated"] as? Bool == true)
    precondition(try! size(show) < 16_384)
    print("PASS bounded mutation receipts, complete normal records, unicode byte pagination and oversize progress")
 }
}
'''
class ItemPayloads(unittest.TestCase):
 def test_receipts_and_byte_pagination(self):
  if not shutil.which('xcrun'):self.skipTest('Apple Swift compiler unavailable')
  with tempfile.TemporaryDirectory(prefix='bama-payload-tests-') as directory:
   directory=Path(directory); source=directory/'Check.swift'; source.write_text(HARNESS); binary=directory/'check'
   built=subprocess.run(['xcrun','swiftc','-swift-version','6','-parse-as-library',str(HELPER),str(source),'-o',str(binary)],capture_output=True,text=True)
   self.assertEqual(built.returncode,0,built.stderr)
   ran=subprocess.run([str(binary)],capture_output=True,text=True)
   self.assertEqual(ran.returncode,0,ran.stderr)
   self.assertIn('PASS bounded mutation receipts',ran.stdout)
 def test_agent_commands_wire_bounded_results(self):
  source=(ROOT/'skills/bama-agent-cli/template/Agent/AgentCommands.swift').read_text()
  self.assertIn('AgentItemOutput.page(',source)
  self.assertIn('AgentItemOutput.receipt(',source)
  self.assertIn('AgentItemOutput.show(',source)
  self.assertNotIn('return item.agentJSON',source)
if __name__=='__main__':unittest.main()
