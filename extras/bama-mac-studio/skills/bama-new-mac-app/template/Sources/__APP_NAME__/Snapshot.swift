// Version-Timestamp: 2026-10-27 08:17:12 AST
// Adapted from MIT BAMA. Preserve the package's Dave Ebbelaar license notice.
import AppKit
import Darwin
import IOKit.pwr_mgt
import SwiftUI

/// Declares the actual capture matrix and records each window and capture method.
/// Run through tools/run_checks.py so an independent expected matrix is checked.
/// Cached-view previews are retained as degraded evidence and never pass native acceptance.
@MainActor
enum Snapshot {
    static var requested: Bool {
        !(ProcessInfo.processInfo.environment["APP_SNAPSHOT"] ?? "").isEmpty
    }
    /// AppDelegate uses this after normal termination, alongside SelfTest.exitCode.
    static private(set) var exitCode: Int32 = 1
    private static var running = false

    private struct WindowIdentity: Encodable {
        let number: Int
        let title: String
        let identifier: String?

        @MainActor init(_ window: NSWindow) {
            number = window.windowNumber
            title = window.title
            identifier = window.identifier?.rawValue
        }
    }

    private struct Capture: Encodable {
        let id: String
        let filename: String
        let window_role: String
        let window: WindowIdentity?
        let method: String
        let status: String
        let pixel_width: Int?
        let pixel_height: Int?
        let errors: [String]
        let attempts: [String]
    }

    private struct Manifest: Encodable {
        let schema_version = 1
        let requested: [String]
        var completed = false
        var native_complete = false
        var windows: [String: WindowIdentity] = [:]
        var captures: [Capture] = []
        var failures: [String] = []
    }

    static func runIfRequested(model: AppModel, openSettings: OpenSettingsAction) {
        let env = ProcessInfo.processInfo.environment
        guard let dir = env["APP_SNAPSHOT"], !dir.isEmpty, !running else { return }
        running = true
        guard Store.isOverridden, TestIsolation.root != nil, TestIsolation.contains(dir) else {
            print("SNAPSHOT refused: use an owned APP_TEST_ROOT and APP_STORE from tools/run_checks.py")
            NSApp.terminate(nil)
            return
        }
        let selected = env["APP_SNAPSHOT_PAGES"].map { Set($0.split(separator: ",").map(String.init)) }
        let selectedTabs = env["APP_SNAPSHOT_SETTINGS_TABS"].map { Set($0.split(separator: ",").map(String.init)) }
        let appearances = env["APP_SNAPSHOT_APPEARANCES"]?.split(separator: ",").map(String.init) ?? ["light", "dark"]
        let pages = SidebarItem.allCases.filter { selected?.contains($0.rawValue) ?? true }
        let tabs = SettingsTab.allCases.filter { selectedTabs?.contains($0.rawValue) ?? true }
        let includeSettings = selected?.contains("settings") ?? true
        let ids = appearances.flatMap { mode in
            pages.map { "\($0.rawValue)-\(mode)" } + (includeSettings ? tabs.map { "settings-\($0.rawValue)-\(mode)" } : [])
        }
        var manifest = Manifest(requested: ids)
        let allowedPages = Set(SidebarItem.allCases.map(\.rawValue) + ["settings"])
        let allowedTabs = Set(SettingsTab.allCases.map(\.rawValue))
        if let selected, !selected.subtracting(allowedPages).isEmpty {
            manifest.failures.append("Requested page filter contains unknown pages")
        }
        if let selectedTabs, !selectedTabs.subtracting(allowedTabs).isEmpty {
            manifest.failures.append("Requested Settings filter contains unknown tabs")
        }
        if appearances.isEmpty || Set(appearances).count != appearances.count || appearances.contains(where: { !["light", "dark"].contains($0) }) {
            manifest.failures.append("Requested appearances must be light and/or dark without duplicates")
        }
        if let raw = env["APP_SNAPSHOT_EXPECTED"] {
            if let data = raw.data(using: .utf8), let expected = try? JSONDecoder().decode([String].self, from: data), Set(expected) == Set(ids), expected.count == ids.count {
                // The app's actual pages and the runner's declaration agree.
            } else {
                manifest.failures.append("App page/appearance matrix differs from the runner's declared matrix")
            }
        }
        Task {
            do {
                try FileManager.default.createDirectory(atPath: dir, withIntermediateDirectories: true)
                try write(manifest, to: dir)
            } catch {
                print("SNAPSHOT manifest could not be created: \(error)")
                NSApp.terminate(nil)
                return
            }
            if !manifest.failures.isEmpty {
                manifest.completed = true
                try? write(manifest, to: dir)
                finish(manifest)
                return
            }
            var activity: IOPMAssertionID = 0
            IOPMAssertionDeclareUserActivity("Snapshots" as CFString, kIOPMUserActiveLocal, &activity)
            var awake: IOPMAssertionID = 0
            IOPMAssertionCreateWithName(kIOPMAssertionTypePreventUserIdleDisplaySleep as CFString,
                                      IOPMAssertionLevel(kIOPMAssertionLevelOn), "Snapshots" as CFString, &awake)
            try? await Task.sleep(for: .seconds(1.5))
            // Bind the initial main window once. Never let capture fall back to an arbitrary window.
            let mainCandidates = NSApp.windows.filter { $0.isVisible && $0.canBecomeMain && !$0.isSheet }
            let main = mainCandidates.count == 1 ? mainCandidates.first : nil
            if let main { manifest.windows["main"] = WindowIdentity(main) }
            else { manifest.failures.append("Main window missing or ambiguous") }
            for mode in appearances {
                NSApp.appearance = NSAppearance(named: mode == "light" ? .aqua : .darkAqua)
                for page in pages {
                    model.sidebar = page
                    try? await Task.sleep(for: .seconds(0.8))
                    manifest.captures.append(capture(id: "\(page.rawValue)-\(mode)", role: "main", folder: dir, window: main))
                    persist(&manifest, to: dir)
                }
            }
            if includeSettings {
                let before = Set(NSApp.windows.filter(\.isVisible).map(\.windowNumber))
                openSettings()
                try? await Task.sleep(for: .seconds(1))
                // A newly opened, unique visible window is the Settings target.
                // A missing/ambiguous result is a failure, never a relabelled main capture.
                let candidates = NSApp.windows.filter { $0.isVisible && !$0.isSheet && !before.contains($0.windowNumber) && $0 !== main }
                let settings = candidates.count == 1 ? candidates.first : nil
                if let settings { manifest.windows["settings"] = WindowIdentity(settings) }
                else { manifest.failures.append("Settings window missing or ambiguous after openSettings") }
                for mode in appearances {
                    NSApp.appearance = NSAppearance(named: mode == "light" ? .aqua : .darkAqua)
                    for tab in tabs {
                        model.settingsTab = tab
                        try? await Task.sleep(for: .seconds(0.8))
                        manifest.captures.append(capture(id: "settings-\(tab.rawValue)-\(mode)", role: "settings", folder: dir, window: settings))
                        persist(&manifest, to: dir)
                    }
                }
            }
            if activity != 0 { IOPMAssertionRelease(activity) }
            if awake != 0 { IOPMAssertionRelease(awake) }
            manifest.completed = true
            manifest.native_complete = manifest.failures.isEmpty && manifest.captures.count == ids.count && manifest.captures.allSatisfy { $0.status == "native" && $0.method == "screencapture" }
            persist(&manifest, to: dir)
            finish(manifest)
        }
    }

    private static func write(_ manifest: Manifest, to folder: String) throws {
        let encoder = JSONEncoder()
        encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
        try encoder.encode(manifest).write(to: URL(fileURLWithPath: folder).appendingPathComponent("capture-manifest.json"), options: .atomic)
    }

    private static func persist(_ manifest: inout Manifest, to folder: String) {
        do { try write(manifest, to: folder) }
        catch {
            manifest.native_complete = false
            manifest.failures.append("Capture manifest write failed: \(error)")
            print("SNAPSHOT manifest write failed: \(error)")
        }
    }

    private static func finish(_ manifest: Manifest) {
        exitCode = manifest.completed && manifest.native_complete && manifest.failures.isEmpty ? 0 : 1
        print(exitCode == 0 ? "SNAPSHOT native matrix complete" : "SNAPSHOT incomplete or degraded; inspect capture-manifest.json")
        for window in NSApp.windows { if let sheet = window.attachedSheet { window.endSheet(sheet) } }
        NSApp.terminate(nil)
    }

    private static func dimensions(at path: String) -> (Int, Int)? {
        guard let data = FileManager.default.contents(atPath: path), let image = NSBitmapImageRep(data: data), image.pixelsWide > 0, image.pixelsHigh > 0 else { return nil }
        return (image.pixelsWide, image.pixelsHigh)
    }

    private static func capture(id: String, role: String, folder: String, window: NSWindow?) -> Capture {
        let filename = id + ".png"
        let path = URL(fileURLWithPath: folder).appendingPathComponent(filename).path
        guard let window, window.isVisible, window.windowNumber > 0 else {
            return Capture(id: id, filename: filename, window_role: role, window: nil, method: "none", status: "failed", pixel_width: nil, pixel_height: nil, errors: ["Requested \(role) window is unavailable"], attempts: [])
        }
        if NSApp.isHidden { NSApp.unhideWithoutActivation() }
        NSApp.activate()
        window.makeKeyAndOrderFront(nil)
        let identity = WindowIdentity(window)
        let size = window.contentView?.bounds.size ?? .zero
        GridProbes.shared.write(to: path.replacingOccurrences(of: ".png", with: "-layout.json"), window: size)
        var attempts: [String] = []
        for attempt in 1...3 {
            try? FileManager.default.removeItem(atPath: path)
            let shot = Process()
            shot.executableURL = URL(fileURLWithPath: "/usr/sbin/screencapture")
            shot.arguments = ["-x", "-o", "-l", String(window.windowNumber), path]
            do {
                try shot.run()
                let deadline = Date().addingTimeInterval(5)
                while shot.isRunning && Date() < deadline { Thread.sleep(forTimeInterval: 0.05) }
                if shot.isRunning {
                    shot.terminate()
                    let stopDeadline = Date().addingTimeInterval(1)
                    while shot.isRunning && Date() < stopDeadline { Thread.sleep(forTimeInterval: 0.05) }
                    if shot.isRunning { kill(shot.processIdentifier, SIGKILL) }
                    shot.waitUntilExit()
                    attempts.append("Native capture attempt \(attempt) timed out")
                } else if shot.terminationStatus == 0, let pixels = dimensions(at: path) {
                    print("SNAPSHOT native \(id) window=\(identity.number)")
                    return Capture(id: id, filename: filename, window_role: role, window: identity, method: "screencapture", status: "native", pixel_width: pixels.0, pixel_height: pixels.1, errors: [], attempts: attempts)
                } else {
                    attempts.append("Native capture attempt \(attempt) did not produce a valid PNG (status \(shot.terminationStatus))")
                }
            } catch { attempts.append("Native capture attempt \(attempt) could not start: \(error)") }
            Thread.sleep(forTimeInterval: 0.5)
        }
        try? FileManager.default.removeItem(atPath: path)
        if let view = window.contentView?.superview ?? window.contentView, let rep = view.bitmapImageRepForCachingDisplay(in: view.bounds) {
            view.cacheDisplay(in: view.bounds, to: rep)
            if let data = rep.representation(using: .png, properties: [:]) {
                do {
                    try data.write(to: URL(fileURLWithPath: path), options: .atomic)
                    if let pixels = dimensions(at: path) {
                        let reason = "Native capture failed; cached view preview may omit materials or sidebars"
                        print("SNAPSHOT degraded \(id): \(reason)")
                        return Capture(id: id, filename: filename, window_role: role, window: identity, method: "view_cache", status: "degraded", pixel_width: pixels.0, pixel_height: pixels.1, errors: [reason], attempts: attempts)
                    }
                } catch { attempts.append("Cached view preview could not be written: \(error)") }
            }
        }
        return Capture(id: id, filename: filename, window_role: role, window: identity, method: "none", status: "failed", pixel_width: nil, pixel_height: nil, errors: ["Native capture and degraded preview both failed"], attempts: attempts)
    }
}
