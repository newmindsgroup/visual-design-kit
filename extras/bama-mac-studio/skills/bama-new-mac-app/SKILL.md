---
name: bama-new-mac-app
description: Create a native macOS SwiftUI app from a working template (Swift package, SwiftData, build script, icon script, snapshot mode, git), with no Xcode GUI. Use when the user wants to start a new Mac app or scaffold a macOS project.
argument-hint: "<AppName> <bundle-id> [parent-folder]"
---

<!-- Version-Timestamp: 2026-10-27 07:36:32 AST -->

## Adapted execution contract

This is the pinned, MIT-attributed BAMA capability adapted for the owned design kit. Read `ADAPTATION.md` at the BAMA package root before executing helpers. Project instructions, approved DESIGN.md and canonical tokens take precedence. Use supported Codex or Claude Code tools. Resolve this skill's sibling files relative to its installed SKILL.md; `skill_dir` is a task-local shell variable that you set to that resolved directory before running the examples in either host. Invoke a named `bama-*` skill through the host's supported skill mechanism.

Stage local builds by default. Installation, signing identity selection, launch, CLI linking, MCP registration, system setting changes and capture access are separate explicit operations. Existing task authorization applies; ask only for an action not already authorized. Stage or commit only when the current task or repository workflow authorizes it. Stage explicit paths and include required attribution. The helpers do not commit. Preserve the feature, story and testing workflow below using the hardened helpers. Legacy installed-app paths in examples must be replaced by the staged binary returned by `build.sh`.

Before a new scaffold exists, keep planning evidence under the selected `<AppName>-planning/docs/` sibling or an existing approved planning folder. Treat docs paths below as relative to that planning folder until the fresh app is scaffolded, then copy the planning docs explicitly without replacing existing files. For an existing app, keep its current project layout.

The upstream acceptance statements describe checks to perform, never completed results. Screenshots, runtime behavior, permissions and cross-host acceptance require actual evidence. Use synthetic data and owned temporary test roots. Do not run a hosted session over real app data without project authorization.



# New Mac app

Build the unmodified template first to test the complete toolchain before feature work. A Swift version check or trivial View typecheck does not establish SwiftUI/SwiftData macro availability. A failed first build remains blocked until its actual prerequisite is fixed.

## What the template is

A Swift package with one executable target, plus a script that wraps the
binary in a real `.app` bundle. An agent can read and edit every file.

```text
<AppName>/
  Package.swift          macOS 26, Swift 6.2 tools, main-actor default isolation
  Info.plist.in          bundle id, name, icon, minimum macOS
  Icon/AppIcon.icon      the app icon: Icon Composer file, JSON plus SVG layers
  build.sh               swift build -> staged unsigned .app; explicit signing/install flags
  CLAUDE.md              build, check, and design rules for agents
  Sources/<AppName>/
    App.swift            window, menus, Settings, database location
    Models.swift         SwiftData models, sidebar pages, AppModel
    ContentView.swift    NavigationSplitView: sidebar, list, detail
    Snapshot.swift       APP_SNAPSHOT mode: PNG and layout file per page and Settings tab, light and dark
    UI/Theme.swift       accent colors, saved choice, accent tokens
    SettingsView.swift   Settings window: one tab per topic, sized to content
    UI/AppearanceSettings.swift  Settings: accent picker (mode follows the Mac)
    UI/WindowBehavior.swift  window focus and content sizing; verify keyboard access
    UI/Grid.swift        the 4 pt spacing scale, layout probes, grid overlay
  tools/
    grid-lint.sh         flags spacing numbers off the 4 pt grid
    check-layout.swift   checks the layout files from snapshot mode
    make_icon.sh         Icon/AppIcon.icon -> Resources/Assets.car + AppIcon.icns (actool)
    icon_review.sh       renders every icon look into one PNG (ictool)
    icon_sheet.swift     joins the renders for icon_review.sh
```

## Steps

1. Check the toolchain:

   ```bash
   swift --version            # Swift 6.2 or later
   sw_vers -productVersion    # 26.0 or later
   ```

   On macOS 15, set `.macOS(.v15)` in `Package.swift` and
   `LSMinimumSystemVersion` to 15 in `Info.plist.in`, and skip Liquid Glass APIs.

2. Pick the name (one UpperCamelCase word) and bundle id (reverse DNS). If
   `docs/BRIEF.md` exists, use its name.

3. Run the script with the parent folder. It copies the template, fills in
   the name and bundle id, creates only the fresh scaffold without Git actions. The destination must be fresh. Planning docs stay in the `<AppName>-planning` sibling or approved planning folder until the scaffold succeeds. Then copy its docs into the fresh app explicitly, preserving every existing file. Verify the copied brief/story hashes or content and switch to the app as working root.

   ```bash
   "${skill_dir}/scripts/new-app.sh" Tasks com.yourname.tasks ~/Developer
   ```

   In a Dropbox or iCloud Drive folder the script can take minutes: run it
   in the background.

4. Build the app and its icon, then open it:

   ```bash
   cd ~/Developer/Tasks && ./build.sh --open
   ```

5. Run the checks the template ships with, then look at the snapshots
   (`bama-build-and-verify` skill):

   ```bash
   swift test --scratch-path ~/Library/Developer/Tasks/test-build   # Kit unit tests
   tools/selftest.sh /explicit/staged/binary                       # fresh isolated store
   tools/snap.sh /explicit/staged/binary                           # fresh isolated light/dark captures
   ```

6. If `docs/BRIEF.md` exists, rename `Item` to the brief's main type and the
   sidebar pages to the brief's pages. Nothing else: features go through
   `bama-improve-loop`, one story at a time. Build, snapshot and review the scoped change. Commit under the project's existing authorization and attribution workflow.

## When to switch to an Xcode project

The Swift package covers most personal apps. Switch to an XcodeGen project
(`project.yml` -> generated `.xcodeproj`, built with `xcodebuild`) when the
app needs App Intents for Shortcuts and Spotlight, an asset catalog, app
extensions, or widgets. Keep `project.yml` in git and the `.xcodeproj` out
of it. Put build output outside Dropbox with `-derivedDataPath`.

## Signing

`build.sh` stages unsigned output by default. Choose `--sign-identity -` for an explicitly authorized ad hoc build, or the exact authorized identity for signing. No certificate enumeration or credential extraction occurs. Signing, installation and opening are distinct flags. Permissions remain tied to the resulting signature/path and require actual host testing; do not promise they persist across rebuilds.

## A CLI for agents

To let Claude Code, Codex, or scripts read and change the app's data, call
the host-supported skill mechanism for `bama-agent-cli`. The app binary becomes its own CLI and
sends each command to the running app, so the database keeps one writer
and the window updates live.

## When the build fails

- `cannot find 'X' in scope` after adding a file: SwiftPM cached the file
  list. Run `swift package clean --scratch-path ~/Library/Developer/<AppName>/build`.
- `binary is older than ...`: a file did not compile. Read the first errors.
- Concurrency errors: invoke the host-supported skill `bama-swift-swiftui`.

Done when the fresh scaffold exists, its build and applicable unit checks pass, the staged app opens when authorized, and isolated snapshots show every changed page in light and dark. Record missing toolchain or capture prerequisites separately. A commit or installed app is not required merely to create the scaffold.
