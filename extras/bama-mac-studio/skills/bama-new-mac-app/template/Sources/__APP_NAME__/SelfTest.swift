// Version-Timestamp: 2026-10-27 09:01:10 AST
// Adapted from MIT BAMA. Preserve its accompanying Dave Ebbelaar license notice.
import AppKit
import Darwin
import SwiftData
import __APP_NAME__Kit

/// Runs real model functions on an owned test store. Process exit alone is not
/// completion evidence: tools/run_checks.py also validates the atomic receipt.
@MainActor
enum SelfTest {
    static var requested: Bool { CommandLine.arguments.contains("--selftest") }
    /// Normal termination before completion must fail, including before Task starts.
    static private(set) var exitCode: Int32 = 1
    private static var started = false
    private static var completed = false
    private static var records: [[String: Any]] = []
    private static var runFailures: [String] = []
    private static let requiredIDs = [
        "create-count", "create-selection", "selected-item-available", "star",
        "agent-preserves-edits", "normalize-title", "delete-count",
        "delete-selection", "title-clean"
    ]

    static func runIfRequested(model: AppModel) {
        guard requested, !started else { return }
        // Reentry is refused before scheduling asynchronous work or touching state.
        started = true
        guard Store.isOverridden, TestIsolation.root != nil else {
            runFailures.append("Self-test requires an owned APP_TEST_ROOT and APP_STORE from tools/run_checks.py")
            finish()
            return
        }
        do { try writeReceipt(completed: false) }
        catch {
            runFailures.append("Could not write initial self-test receipt: \(error.localizedDescription)")
            finish()
            return
        }
        Task {
            do {
                try await Task.sleep(for: .seconds(0.5))
                let context = model.container.mainContext
                @MainActor func items() throws -> [Item] { try context.fetch(FetchDescriptor<Item>()) }
                let before = try items().count
                let created = try model.createItem(title: "", origin: .interface)
                check("create-count", "New Item adds one item", try items().count == before + 1)
                check("create-selection", "the new item is selected", model.selection == created.id)
                let selected = try items().first(where: { $0.id == model.selection })
                check("selected-item-available", "the selected item can be fetched", selected != nil)
                if let item = selected {
                    try model.updateItem(item, starred: true, origin: .interface)
                    check("star", "starring an item marks it starred", item.isStarred)
                    item.title = "Unsaved interface edit"
                    do {
                        try model.updateItem(item, title: "Agent replacement", origin: .agent)
                        check("agent-preserves-edits", "agent write refuses pending interface edits", false)
                    } catch MutationFailure.unsavedUserEdits {
                        check("agent-preserves-edits", "agent write preserves pending interface edits", item.title == "Unsaved interface edit" && context.hasChanges)
                    }
                    try context.save()
                    try model.updateItem(item, title: "  Clean   title  ", origin: .agent)
                    check("normalize-title", "UI and agent share title normalization", item.title == "Clean title")
                    try model.deleteItem(item, origin: .interface)
                    check("delete-count", "deleting the item removes it", try items().count == before)
                    check("delete-selection", "successful delete clears selection", model.selection == nil)
                } else {
                    runFailures.append("Selected item is unavailable; dependent model checks were not executed")
                }
            } catch {
                runFailures.append(String("Model self-test operation failed: \(error.localizedDescription)".prefix(512)))
            }
            check("title-clean", "titles are cleaned", ItemTitle.clean("  Buy   milk ") == "Buy milk")
            finish()
        }
    }

    private static func log(_ line: String) {
        print(line)
        // Flush line-oriented diagnostics without accessing the shared stdout variable.
        fflush(nil)
    }

    private static func check(_ id: String, _ name: String, _ ok: Bool, _ detail: String = "") {
        guard started, !completed else { return }
        guard records.count < 256, !records.contains(where: { $0["id"] as? String == id }) else {
            runFailures.append("Duplicate or excessive self-test check: \(id)")
            return
        }
        records.append(["id": id, "name": String(name.prefix(256)), "passed": ok, "detail": String(detail.prefix(512))])
        log(ok ? "PASS \(name)" : "FAIL \(name)\(detail.isEmpty ? "" : ": \(detail)")")
    }

    private static func failures(final: Bool) -> [String] {
        var result = runFailures.map { String($0.prefix(512)) }
        result += records.filter { $0["passed"] as? Bool == false }.map { "Failed check: \($0["id"] as? String ?? "unknown")" }
        if final {
            let executed = Set(records.compactMap { $0["id"] as? String })
            result += requiredIDs.filter { !executed.contains($0) }.map { "Required check not executed: \($0)" }
        }
        return result
    }

    private static func writeReceipt(completed isComplete: Bool) throws {
        guard let root = TestIsolation.root else { throw CocoaError(.fileWriteNoPermission) }
        let url = root.appendingPathComponent("selftest-completion.json")
        guard TestIsolation.contains(url.path), (try? url.resourceValues(forKeys: [.isSymbolicLinkKey]).isSymbolicLink) != true else {
            throw CocoaError(.fileWriteNoPermission)
        }
        let failureEvidence = failures(final: isComplete)
        let passed = isComplete && !records.isEmpty && failureEvidence.isEmpty
        let value: [String: Any] = [
            "Version-Timestamp": ISO8601DateFormatter().string(from: Date()),
            "schema_version": 1, "started": started, "completed": isComplete,
            "status": isComplete ? (passed ? "passed" : "failed") : "running",
            "check_count": records.count, "required_check_count": requiredIDs.count,
            "required_check_ids": requiredIDs, "checks": records,
            "failures": failureEvidence, "exit_code": passed ? 0 : 1
        ]
        let data = try JSONSerialization.data(withJSONObject: value, options: [.prettyPrinted, .sortedKeys])
        guard data.count <= 65536 else { throw CocoaError(.fileWriteOutOfSpace) }
        try data.write(to: url, options: .atomic)
    }

    /// Only final, fully recorded checks can produce success. Closing a window,
    /// an early normal termination or a failed receipt write leaves exitCode at 1.
    private static func finish() {
        guard started, !completed else { return }
        let successful = !records.isEmpty && failures(final: true).isEmpty
        do {
            try writeReceipt(completed: true)
            exitCode = successful ? 0 : 1
        } catch {
            exitCode = 1
            log("SELFTEST receipt write failed: \(error.localizedDescription)")
        }
        completed = true
        log(exitCode == 0 ? "SELFTEST PASS \(records.count) completed checks" : "SELFTEST FAIL; inspect the completion receipt and isolated logs")
        for window in NSApp.windows { if let sheet = window.attachedSheet { window.endSheet(sheet) } }
        NSApp.terminate(nil)
    }
}
