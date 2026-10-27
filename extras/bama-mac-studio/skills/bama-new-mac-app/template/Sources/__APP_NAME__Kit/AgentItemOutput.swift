// Version-Timestamp: 2026-10-27 08:39:37 AST
// Original guarded output helper for the MIT-attributed BAMA derivative.
import Foundation

/// Item output is built from value snapshots. IDs are the app-generated complete
/// UUID string, never a caller-supplied unbounded field. This module has no store
/// access and cannot change an item while constructing a response.
public enum AgentItemOutput {
    public static let maximumPayloadBytes = 4 * 1024 * 1024
    public enum Outcome: String, Sendable { case created, updated, deleted }
    public enum Failure: LocalizedError {
        case invalidPage, metadataExceedsBudget
        public var errorDescription: String? {
            switch self {
            case .invalidPage: "Use limit 1 to 500, a nonnegative offset, and a byte budget from 16384 to 4194304."
            case .metadataExceedsBudget: "The record metadata exceeds the page budget. Inspect the item in the app."
            }
        }
    }

    public struct Record {
        public let id: String
        public let title: String
        public let notes: String
        public let starred: Bool
        public let createdAt: String
        public init(id: String, title: String, notes: String, starred: Bool, createdAt: String) {
            self.id = id; self.title = title; self.notes = notes
            self.starred = starred; self.createdAt = createdAt
        }
        var full: [String: Any] {
            ["id": id, "title": title, "notes": notes, "starred": starred, "createdAt": createdAt]
        }
        var minimumEncodedBytes: Int {
            id.utf8.count + title.utf8.count + notes.utf8.count + createdAt.utf8.count
        }
    }

    /// Never serialize arbitrary notes after a successful save. The receipt says
    /// what completed and how to inspect it, rather than turning completion into
    /// a transport-size error. Full state is a separate bounded read operation.
    public static func receipt(_ item: Record, outcome: Outcome) -> [String: Any] {
        var readback: [String: Any] = ["command": "items show", "id": item.id]
        if outcome == .deleted { readback["expected"] = "not_found" }
        var value: [String: Any] = ["completed": true, "outcome": outcome.rawValue,
            "id": item.id, "item": summary(item, reason: "mutation_receipt"), "readback": readback]
        if outcome == .deleted { value["deleted"] = true }
        return value
    }

    /// Normal small reads retain complete title/notes. An oversized individual
    /// record explicitly returns identity, byte counts and previews, not an error
    /// that could be confused with the result of a preceding mutation.
    public static func show(_ item: Record) -> [String: Any] {
        if item.minimumEncodedBytes <= maximumPayloadBytes,
           let bytes = encodedSize(item.full), bytes <= maximumPayloadBytes {
            return item.full
        }
        return summary(item, reason: "record_exceeds_response_budget")
    }

    /// Serialize each candidate once, then account for the array commas and the
    /// exact metadata envelope. A byte-limited page advances by returned rows,
    /// never by the originally requested prefix count. An oversized first row is
    /// represented by explicit metadata so callers can always make progress.
    public static func page(_ records: [Record], offset: Int, limit: Int,
                            byteBudget: Int = maximumPayloadBytes) throws -> [String: Any] {
        guard offset >= 0, (1...500).contains(limit),
              (16_384...maximumPayloadBytes).contains(byteBudget) else { throw Failure.invalidPage }
        var entries: [[String: Any]] = []
        var encodedEntries = 0
        var cursor = min(offset, records.count)
        let end = min(records.count, cursor + limit)
        while cursor < end {
            let item = records[cursor]
            guard let overhead = encodedSize(envelope([], total: records.count, returned: entries.count + 1, next: cursor + 1)) else {
                throw Failure.invalidPage
            }
            let remaining = byteBudget - overhead - encodedEntries - entries.count
            var value: [String: Any]?
            var bytes: Int?
            // Avoid allocating JSON for an already-too-large original record.
            if item.minimumEncodedBytes <= remaining {
                let candidate = item.full
                if let size = encodedSize(candidate), size <= remaining { value = candidate; bytes = size }
            }
            if value == nil {
                if !entries.isEmpty { break }
                let candidate = summary(item, reason: "record_exceeds_page_budget")
                guard let size = encodedSize(candidate), size <= remaining else { throw Failure.metadataExceedsBudget }
                value = candidate; bytes = size
            }
            guard let value, let bytes else { throw Failure.metadataExceedsBudget }
            entries.append(value)
            encodedEntries += bytes
            cursor += 1
        }
        return envelope(entries, total: records.count, returned: entries.count, next: cursor)
    }

    private static func envelope(_ entries: [[String: Any]], total: Int, returned: Int, next: Int) -> [String: Any] {
        var result: [String: Any] = ["items": entries, "total": total, "returned": returned]
        if next < total { result["nextOffset"] = next }
        return result
    }

    private static func summary(_ item: Record, reason: String) -> [String: Any] {
        let title = prefix(item.title, utf8Limit: 512)
        let notes = prefix(item.notes, utf8Limit: 1024)
        return ["id": item.id, "title": title, "notesPreview": notes,
            "titleByteCount": item.title.utf8.count, "notesByteCount": item.notes.utf8.count,
            "truncated": title.utf8.count < item.title.utf8.count || notes.utf8.count < item.notes.utf8.count,
            "recordTruncated": true, "notesOmitted": true, "reason": reason,
            "starred": item.starred, "createdAt": prefix(item.createdAt, utf8Limit: 128),
            "readback": ["command": "items show", "id": item.id],
            "details": "Full fields are omitted from this response. Inspect the item in the app for complete text."]
    }

    private static func prefix(_ text: String, utf8Limit: Int) -> String {
        var result = String.UnicodeScalarView()
        var used = 0
        for scalar in text.unicodeScalars {
            let count = String(scalar).utf8.count
            if used + count > utf8Limit { break }
            result.append(scalar); used += count
        }
        return String(result)
    }

    private static func encodedSize(_ object: [String: Any]) -> Int? {
        (try? JSONSerialization.data(withJSONObject: object, options: [.sortedKeys, .withoutEscapingSlashes]))?.count
    }
}
