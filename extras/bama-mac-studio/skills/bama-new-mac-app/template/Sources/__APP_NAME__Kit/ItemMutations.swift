// Version-Timestamp: 2026-10-27 08:10:06 AST
// Derived from the MIT BAMA template. Preserve its accompanying LICENSE.
import Foundation

public enum MutationOrigin: Sendable { case interface, agent }

public enum MutationFailure: LocalizedError {
    case unsavedUserEdits
    public var errorDescription: String? {
        "The app has unsaved edits. Finish editing or save them in the app, then retry the agent command."
    }
}

/// Each synchronous operation begins from a clean context. Agent commands never
/// save or roll back someone else's pending interface edits. Interface actions
/// first save existing edits, and stop before mutation when that save fails.
@MainActor
public enum SavedMutation {
    public static func perform<Result>(
        origin: MutationOrigin,
        hasChanges: () -> Bool,
        save: () throws -> Void,
        rollback: () -> Void,
        mutation: () throws -> Result
    ) throws -> Result {
        if hasChanges() {
            guard origin == .interface else { throw MutationFailure.unsavedUserEdits }
            // Outside the mutation catch: a failed save must retain those edits.
            try save()
        }
        do {
            let result = try mutation()
            try save()
            return result
        } catch {
            // No unrelated unsaved changes existed when this operation began.
            rollback()
            throw error
        }
    }
}

/// Testable pending confirmation state. Returning an ID means an immediate
/// action was requested with confirmation disabled. Cancellation returns no ID.
public struct DeleteIntent<ID: Equatable> {
    public private(set) var pending: ID?
    public init() {}
    public mutating func request(_ id: ID, confirmationRequired: Bool) -> ID? {
        pending = confirmationRequired ? id : nil
        return confirmationRequired ? nil : id
    }
    public mutating func cancel() { pending = nil }
}
