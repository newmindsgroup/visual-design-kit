import Foundation
import Darwin

// Version-Timestamp: 2026-10-27 09:01:10 AST
// A fresh marked temporary root is mandatory for model-store test modes.
enum TestIsolation {
    static var root: URL? {
        let env = ProcessInfo.processInfo.environment
        guard let raw = env["APP_TEST_ROOT"], !raw.isEmpty else { return nil }
        let root = URL(fileURLWithPath: raw).resolvingSymlinksInPath().standardizedFileURL
        let temporary = URL(fileURLWithPath: NSTemporaryDirectory()).resolvingSymlinksInPath().standardizedFileURL
        let marker = root.appending(path: ".bama-test-root")
        guard root.deletingLastPathComponent() == temporary,
              root.lastPathComponent.hasPrefix("bama-test-"),
              let attributes = try? FileManager.default.attributesOfItem(atPath: marker.path),
              attributes[.type] as? FileAttributeType == .typeRegular,
              (attributes[.ownerAccountID] as? NSNumber)?.uint32Value == getuid() else { return nil }
        return root
    }

    /// Resolve only existing ancestors, then append missing names as strings.
    /// Foundation can spell an existing /private/var root as /var while leaving
    /// a nonexistent child at /private/var. POSIX realpath gives both one base.
    private static func canonicalChildPath(_ path: String) -> String? {
        guard path.hasPrefix("/"), !path.utf8.contains(0) else { return nil }
        let components = (path as NSString).pathComponents
        guard !components.contains(".."), !components.contains(".") else { return nil }
        var ancestor = path
        var missing: [String] = []
        while true {
            if let pointer = realpath(ancestor, nil) {
                let existing = String(cString: pointer)
                free(pointer)
                return missing.isEmpty ? existing : existing + "/" + missing.reversed().joined(separator: "/")
            }
            // A dangling link must not become a trusted nonexistent component.
            if let attributes = try? FileManager.default.attributesOfItem(atPath: ancestor),
               attributes[.type] as? FileAttributeType == .typeSymbolicLink { return nil }
            let component = (ancestor as NSString).lastPathComponent
            let parent = (ancestor as NSString).deletingLastPathComponent
            guard !component.isEmpty, !parent.isEmpty, parent != ancestor else { return nil }
            missing.append(component)
            ancestor = parent
        }
    }

    static func contains(_ path: String) -> Bool {
        guard let root, let base = canonicalChildPath(root.path),
              let candidate = canonicalChildPath(path) else { return false }
        return candidate.hasPrefix(base + "/")
    }
}

// Production keeps its normal preferences. A marked test invocation uses a fresh
// unique domain shared by AppStorage and explicit UserDefaults access, then
// removes only that domain when its owned process terminates normally.
@MainActor
enum AppPreferences {
    private static let testDomain: String? = TestIsolation.root == nil ? nil : "com.bama.test.\(UUID().uuidString)"
    static let shared: UserDefaults = {
        guard let testDomain else { return .standard }
        guard let suite = UserDefaults(suiteName: testDomain) else { fatalError("Could not create isolated preferences") }
        return suite
    }()

    static func clearTestDomain() {
        if let testDomain { shared.removePersistentDomain(forName: testDomain) }
    }
}
