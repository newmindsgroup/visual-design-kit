// Version-Timestamp: 2026-10-27T16:57:27.179246-04:00
import SwiftData
import SwiftUI
import __APP_NAME__Kit

struct ContentView: View {
    @Environment(AppModel.self) private var model
    @Environment(\.openSettings) private var openSettings

    var body: some View {
        NavigationSplitView {
            sidebar
        } content: {
            ItemList(page: model.sidebar ?? .all)
                .navigationSplitViewColumnWidth(min: 260, ideal: 320)
        } detail: {
            ItemDetail()
        }
        .alert("Could not complete action", isPresented: Binding(
            get: { model.operationError != nil },
            set: { if !$0 { model.operationError = nil } }
        )) {
            Button("Dismiss", role: .cancel) { model.operationError = nil }
        } message: {
            Text(model.operationError ?? "The action did not complete. Retry when the problem is resolved.")
        }
        .task {
            SeedData.insertIfRequested(into: model)
            SelfTest.runIfRequested(model: model)
            Snapshot.runIfRequested(model: model, openSettings: openSettings)
        }
    }

    private var sidebar: some View {
        @Bindable var model = model
        return List(SidebarItem.allCases, selection: $model.sidebar) { page in
            Label(page.title, systemImage: page.symbol)
                .tag(page)
        }
        .navigationSplitViewColumnWidth(min: 180, ideal: 212)
    }
}

struct ItemList: View {
    @Environment(\.colorScheme) private var toolbarScheme
    @Environment(AppModel.self) private var model
    @Query(sort: \Item.createdAt, order: .reverse) private var items: [Item]
    @AppStorage("confirmDelete") private var confirmDelete = true
    @State private var deletion = DeleteIntent<PersistentIdentifier>()
    let page: SidebarItem

    private var visible: [Item] {
        page == .starred ? items.filter(\.isStarred) : items
    }

    var body: some View {
        @Bindable var model = model
        List(visible, selection: $model.selection) { item in
            Label(item.title, systemImage: item.isStarred ? "star.fill" : "circle")
                .tag(item.id)
                .contextMenu {
                    Button("Delete", role: .destructive) {
                        if let id = deletion.request(item.id, confirmationRequired: confirmDelete) { delete(id) }
                    }
                }
        }
        .overlay {
            if visible.isEmpty {
                ContentUnavailableView(
                    "No Items",
                    systemImage: page.symbol,
                    description: Text("Press Command-N to add one.")
                )
            }
        }
        .confirmationDialog("Delete this item?", isPresented: Binding(
            get: { deletion.pending != nil },
            set: { if !$0 { deletion.cancel() } }
        ), titleVisibility: .visible, presenting: deletion.pending) { id in
            Button("Delete Item", role: .destructive) { deletion.cancel(); delete(id) }
            Button("Cancel", role: .cancel) { deletion.cancel() }
        } message: { _ in
            Text("This permanently removes the item. Cancel keeps it unchanged.")
        }
        .navigationTitle(page.title)
        // Keep the native title appearance aligned with this window.
        .toolbarColorScheme(toolbarScheme, for: .windowToolbar)
        .toolbar {
            ToolbarItem {
                Button("New Item", systemImage: "plus") { model.addItem() }
                    .help("Add an item (Command-N)")
            }
        }
    }

    private func delete(_ id: PersistentIdentifier) {
        guard let item = items.first(where: { $0.id == id }) else {
            model.operationError = "The item is no longer available. Refresh the selection and retry."
            return
        }
        do {
            try model.deleteItem(item, origin: .interface)
        } catch {
            model.operationError = "Could not delete the item. It remains available to retry. " + error.localizedDescription
        }
    }
}

struct ItemDetail: View {
    @Environment(AppModel.self) private var model
    @Query private var items: [Item]

    var body: some View {
        VStack(spacing: 0) {
            Group {
                if let item = items.first(where: { $0.id == model.selection }) {
                    @Bindable var item = item
                    Form {
                        TextField("Title", text: $item.title)
                        Toggle("Starred", isOn: $item.isStarred)
                        TextField("Notes", text: $item.notes, axis: .vertical)
                            .lineLimit(4...)
                    }
                    .formStyle(.grouped)
                } else {
                    ContentUnavailableView("No Selection", systemImage: "sidebar.right")
                }
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            // Measure the custom container, not the system Form's internal metrics.
            .gridProbe("detail.content", area: "detail", edge: nil)
        }
        .padding(Space.margin)
        .gridArea("detail", inset: Space.margin)
    }
}
