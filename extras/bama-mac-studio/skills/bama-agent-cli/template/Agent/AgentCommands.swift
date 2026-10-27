// Version-Timestamp: 2026-10-27 08:39:37 AST
import Foundation
import SwiftData
import __APP_NAME__Kit

/// Everything an agent can do in __CLI_NAME__. Add a command here and the CLI,
/// `help`, and the MCP tools all get it. Each `run` is on the main actor
/// with the app's model, like a button in the window.
enum AgentCommands {
    static let all: [AgentCommand] = [
        AgentCommand(name: "status", summary: "Show whether the app runs, the open page, and item counts.",
                     example: "__CLI_NAME__ status --json", readOnly: true) { _, model in
            let items = try model.container.mainContext.fetch(FetchDescriptor<Item>())
            return ["running": true, "page": model.sidebar?.rawValue ?? "none",
                    "items": items.count, "starred": items.filter(\.isStarred).count]
        },
        AgentCommand(name: "items list", summary: "List items, newest first.",
                     params: [.init(name: "starred", kind: .boolean, help: "only starred items"),
                              .init(name: "search", help: "only items whose title or notes contain this text"),
                              .init(name: "limit", kind: .integer, help: "at most this many (default 50)"),
                              .init(name: "offset", kind: .integer, help: "skip this many, for the next page")],
                     example: "__CLI_NAME__ items list --starred --limit 10 --json", readOnly: true) { args, model in
            var items = try model.container.mainContext.fetch(FetchDescriptor<Item>(sortBy: [SortDescriptor(\.createdAt, order: .reverse)]))
            if try args.bool("starred") == true { items = items.filter(\.isStarred) }
            if let text = args.string("search") {
                items = items.filter { $0.title.localizedStandardContains(text) || $0.notes.localizedStandardContains(text) }
            }
            let limit = try args.int("limit", default: 50)
            let offset = try args.int("offset", default: 0)
            guard (1...500).contains(limit), offset >= 0, offset <= 1_000_000 else { throw AgentError.usage("limit must be 1 to 500 and offset 0 to 1000000") }
            return try AgentItemOutput.page(items.map(\.agentRecord), offset: offset, limit: limit)
        },
        AgentCommand(name: "items show", summary: "Show one item.",
                     params: [.init(name: "id", required: true, positional: true, help: "the item's id (the first 8 characters are enough)")],
                     example: "__CLI_NAME__ items show 3f2a9c1e --json", readOnly: true) { args, model in
            AgentItemOutput.show(try find(try args.required("id"), in: model).agentRecord)
        },
        AgentCommand(name: "items add", summary: "Add an item and select it in the window.",
                     params: [.init(name: "title", required: true, help: "the title"),
                              .init(name: "notes", help: "notes under the title"),
                              .init(name: "starred", kind: .boolean, help: "star it")],
                     example: "__CLI_NAME__ items add --title \"Buy milk\" --starred --json") { args, model in
            let item = try model.createItem(title: try args.required("title"),
                notes: args.string("notes") ?? "", starred: try args.bool("starred"), origin: .agent)
            return AgentItemOutput.receipt(item.agentRecord, outcome: .created)
        },
        AgentCommand(name: "items update", summary: "Change an item. Only the options you give change.",
                     params: [.init(name: "id", required: true, positional: true, help: "the item's id"),
                              .init(name: "title", help: "new title"),
                              .init(name: "notes", help: "new notes"),
                              .init(name: "starred", kind: .boolean, help: "true or false")],
                     example: "__CLI_NAME__ items update 3f2a9c1e --starred false --json") { args, model in
            let item = try find(try args.required("id"), in: model)
            try model.updateItem(item, title: args.string("title"), notes: args.string("notes"),
                starred: try args.bool("starred"), origin: .agent)
            return AgentItemOutput.receipt(item.agentRecord, outcome: .updated)
        },
        AgentCommand(name: "items delete", summary: "Delete an item.",
                     params: [.init(name: "id", required: true, positional: true, help: "the item's id")],
                     example: "__CLI_NAME__ items delete 3f2a9c1e --yes --json", destructive: true) { args, model in
            let item = try find(try args.required("id"), in: model)
            // Capture bounded receipt data before deletion invalidates the model.
            let record = item.agentRecord
            guard args.confirmed else {
                return ["deleted": false, "wouldDelete": AgentItemOutput.show(record), "hint": "add --yes to delete it"]
            }
            try model.deleteItem(item, origin: .agent)
            return AgentItemOutput.receipt(record, outcome: .deleted)
        },
        AgentCommand(name: "open", summary: "Show a sidebar page in the window.",
                     params: [.init(name: "page", required: true, positional: true,
                                    help: SidebarItem.allCases.map(\.rawValue).joined(separator: ", "))],
                     example: "__CLI_NAME__ open starred") { args, model in
            let name = try args.required("page")
            guard let page = SidebarItem(rawValue: name) else {
                throw AgentError.usage("no page \"\(name)\". Pages: \(SidebarItem.allCases.map(\.rawValue).joined(separator: ", "))")
            }
            model.sidebar = page
            return ["page": page.rawValue]
        },
    ]

    /// An item by its id, or the start of it.
    static func find(_ id: String, in model: AppModel) throws -> Item {
        let items = try model.container.mainContext.fetch(FetchDescriptor<Item>())
        let matches = items.filter { $0.agentID.hasPrefix(id.lowercased()) }
        guard let item = matches.first else { throw AgentError.notFound("no item with id \(id). Run `__CLI_NAME__ items list`") }
        guard matches.count == 1 else { throw AgentError.usage("\(matches.count) items start with \(id). Give more characters") }
        return item
    }
}

extension Item {
    /// A stable id for agents: lowercase, without dashes.
    var agentID: String { uuid.uuidString.lowercased().replacingOccurrences(of: "-", with: "") }

    var agentRecord: AgentItemOutput.Record {
        .init(id: agentID, title: title, notes: notes, starred: isStarred, createdAt: JSON.date(createdAt))
    }
}
