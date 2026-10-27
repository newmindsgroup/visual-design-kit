# __APP_NAME__

A native macOS app in SwiftUI. It runs on this Mac only, with a local
SwiftData database and no server.

## Layout

- `Sources/__APP_NAME__/` the app. `App.swift` has the window, menus, and the database location.
- `Sources/__APP_NAME__Kit/` rules and data logic with no SwiftUI. Tests in `Tests/__APP_NAME__KitTests/`.
- `Package.swift` a Swift package. There is no Xcode project.
- `build.sh` stages a local unsigned app. Explicit --sign-identity, --install and --open select separately authorized operations. The helper prints the actual staged paths.
- `Icon/AppIcon.icon` the app icon, an Icon Composer file (JSON plus SVG layers). `build.sh` compiles it with `tools/make_icon.sh`; `tools/icon_review.sh` renders every look into one PNG.
- `docs/` the brief, the screen index, and the user stories, when they exist.

## Build and check

- Build: `./build.sh` with icon tooling, or `./build.sh --no-icon` for code-only staging. Review warnings and preserve failure status. Explicit --open opens this output without quitting another app.
- Unit tests: `swift test --scratch-path ~/Library/Developer/__APP_NAME__/test-build`.
- Self-test (the app's real functions on a /tmp store): `tools/selftest.sh`. Exit 0 when every check passes. Add a check for every story with logic in `SelfTest.swift`.
- After every UI change, take snapshots with sample data and look at them: `tools/snap.sh`.
  It writes `/tmp/__APP_NAME__-shots/<page>-light.png` and `-dark.png` for every sidebar page, and `settings-<tab>-light.png` and `-dark.png` for every Settings tab, then quits. `APP_SNAPSHOT_PAGES=all,settings tools/snap.sh` limits the pages.
  For a panel, sheet, or popover, add a capture to `Snapshot.swift` like the Settings loop.
- Snapshots, seed data and self-test require the owned marked APP_TEST_ROOT created by tools/run_checks.py. Never use a real store for test modes.
- Never test against the real database in `~/Library/Application Support/__APP_NAME__/`.
- Then check the grid: `tools/grid-lint.sh` and `swift tools/check-layout.swift /tmp/__APP_NAME__-shots/*-layout.json`. Both print PASS.
- A change is done when the build has no errors, the grid checks pass, and you looked at the light and dark snapshots.

## Design rules

- Use Apple's controls and system styles. Only the accent color is custom: `UI/Theme.swift` (`ThemeStore.defaultID`). People change it, and light or dark mode, in Settings > Appearance.
- Views use `.tint`, `Palette.accent`, `Palette.accentText` (accent-colored text), and `Palette.onAccent` (text on an accent fill). Never hard-code colors, radii, or durations in views.
- Compare accents: add `APP_ACCENT=<id>` to the snapshot command.
- Spacing comes from `Space` in `UI/Grid.swift`, on a 4 pt grid. Mark custom pages and cards with `.gridArea` and `.gridProbe`.
- Windows open calm: `.noInitialFocus()` on every window and sheet (no focus ring or selected text on open), `.fitsContent()` on sheets and Settings tabs (no scroll bar with nothing to scroll). System scroll bars. Both in `UI/WindowBehavior.swift`.
- Settings: one tab per topic in `SettingsView.swift`, one grouped Form per tab. Add a case to `SettingsTab` for a new tab.
- Window chrome (title bar, toolbar, sidebar, menus, sheets) stays system. Buttons use system styles, like `.borderedProminent`.
- Colors: `.primary`, `.secondary`, `.tint`, and system colors. Never fixed grays or white for text.
- Every action has a menu bar item and a keyboard shortcut.
- `Label` for icon and text pairs. SF Symbols for icons.
- `ContentUnavailableView` for empty states.
- Liquid Glass belongs to floating controls only, never to content.

## Skills

The bama plugin has a skill for each step: `bama-mac-design` (design rules),
`bama-design-system` (accent and tokens), `bama-layout-grid`, `bama-ux-design`,
`bama-swift-swiftui`, `bama-os-integrations`, `bama-performance`, `bama-build-and-verify`,
`bama-test-mac-app`, `bama-app-icon`, `bama-user-stories`, and `bama-improve-loop`. Use them.

## Git

- Commit after each working change, with a message that says what the user can now do.
