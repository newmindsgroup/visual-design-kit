// Version-Timestamp: 2026-10-27 08:10:06 AST
import Foundation
import SwiftData
import __APP_NAME__Kit

@Model
final class Item {
    var title: String
    var notes: String = ""
    var isStarred: Bool = false
    var createdAt: Date = Date.now
    /// A stable id for links, sync, and the agent CLI.
    var uuid: UUID = UUID()

    init(title: String) {
        self.title = title
    }
}

/// The sidebar pages. Snapshot mode walks through every case.
enum SidebarItem: String, CaseIterable, Identifiable {
    case all, starred

    var id: String { rawValue }

    var title: String {
        switch self {
        case .all: "All Items"
        case .starred: "Starred"
        }
    }

    var symbol: String {
        switch self {
        case .all: "tray"
        case .starred: "star"
        }
    }
}

/// App-wide state that menus, toolbars, and views share.
@Observable
final class AppModel {
    let container: ModelContainer
    var sidebar: SidebarItem? = .all
    var selection: PersistentIdentifier?
    /// Visible recovery feedback for menu and toolbar actions.
    var operationError: String?
    /// Settings reopens on the last tab. Test and snapshot runs leave it alone.
    var settingsTab: SettingsTab = SettingsTab(rawValue: AppPreferences.shared.string(forKey: "settings.tab") ?? "") ?? .general {
        didSet { if !Store.isOverridden { AppPreferences.shared.set(settingsTab.rawValue, forKey: "settings.tab") } }
    }

    init(container: ModelContainer) {
        self.container = container
    }

    /// Interface convenience used by the toolbar and Command-N.
    func addItem(title: String = "") {
        do {
            _ = try createItem(title: title, origin: .interface)
        } catch {
            operationError = "Could not add the item. Existing edits were retained. " + error.localizedDescription
        }
    }

    /// UI and agent mutations share validation, normalization and save handling.
    @discardableResult
    func createItem(title: String, notes: String = "", starred: Bool? = nil,
                    origin: MutationOrigin) throws -> Item {
        let item = try savedMutation(origin: origin) { context in
            let item = Item(title: ItemTitle.clean(title))
            item.notes = notes
            item.isStarred = starred ?? (sidebar == .starred)
            context.insert(item)
            return item
        }
        // A successful save assigns a permanent identifier before selection.
        selection = item.id
        return item
    }

    func updateItem(_ item: Item, title: String? = nil, notes: String? = nil,
                    starred: Bool? = nil, origin: MutationOrigin) throws {
        try savedMutation(origin: origin) { _ in
            if let title { item.title = ItemTitle.clean(title) }
            if let notes { item.notes = notes }
            if let starred { item.isStarred = starred }
        }
    }

    func deleteItem(_ item: Item, origin: MutationOrigin) throws {
        let deletedID = item.id
        try savedMutation(origin: origin) { context in context.delete(item) }
        // A failed save leaves the previous selection and item available to retry.
        if selection == deletedID { selection = nil }
    }

    private func savedMutation<Result>(origin: MutationOrigin,
                                       _ mutation: (ModelContext) throws -> Result) throws -> Result {
        let context = container.mainContext
        return try SavedMutation.perform(origin: origin,
            hasChanges: { context.hasChanges }, save: { try context.save() },
            rollback: { context.rollback() }, mutation: { try mutation(context) })
    }
}
