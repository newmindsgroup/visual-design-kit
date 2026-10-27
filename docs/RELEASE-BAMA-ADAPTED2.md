# BAMA 1.0.0-adapted.2 toolbar appearance repair

Version-Timestamp: 2026-10-27 17:02:30 AST

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 16:58:23 AST

The starter's native toolbar title could render white against a light window.
`ItemList` now reads the window's SwiftUI color scheme and passes it to
`.toolbarColorScheme(_:for:)` for `.windowToolbar`. This retains the native
navigation title, system colors and automatic theme changes. No custom title,
fixed foreground color, forced toolbar background or global appearance setting
is introduced. Both host packages use the same repaired template.

On the authoring Mac with Xcode 27.1, an active light window reproduced the issue:
the native title field used a dark appearance while its toolbar ancestors were
light. Application activation, key window and foreground process were confirmed
for the captured process/window pair. The same controlled test passed with the
scheme modifier in light and dark. Background visibility alone failed; forcing
the toolbar background was unnecessary.

## Regression and acceptance

Generate a fresh synthetic starter. Build it without installation, run its core
tests and isolated self-test, then capture both sidebar pages and both Settings
tabs in light and dark. For foreground visual acceptance, launch the owned bundle
normally, confirm its process and window identity, and record active/key/foreground
state with each capture. Test light to dark and dark to light, page changes and Command-N.
Inspect the native title as well as content. A key-window flag alone is insufficient.

A controller already authorized to capture can capture only the identified owned
window when the launched app cannot capture itself. Record this as separate visual
evidence. Do not relabel it as a passing template snapshot manifest or change OS
privacy permissions. Pixel measurements of the controlled title region are a
regression diagnostic, not a complete accessibility audit.

On macOS 26.6.2 with Xcode 27.1, the fresh production scaffold passed its build,
core test (four parameterized cases), nine self-test checks and eight native
snapshot contract checks. Separate foreground verification passed in both
transition directions across both sidebar pages and both Settings tabs. Command-N
created and selected a new item with its detail fields visible. All 17 foreground
captures recorded active/key/foreground state and the owned process/window pair.
Only the diagnostic copy's snapshot driver added gates and native-view inspection;
its application, model and theme code retained the production implementation.
The diagnostic driver was restored afterward. Its intentionally incomplete
in-app manifests are not the eight passing production snapshot contract checks.

The controlled All Items title region reproduced a failure before the fix and
passed afterward. Pixel ratios use dominant glyph/background pixels after
checking an opaque region and active capture preconditions:

| Controlled title | Before | Repaired, forward and reverse |
| --- | --- | --- |
| Light | 1.119:1 | 14.938:1 |
| Dark | 14.058:1 | 12.561:1 |

Repaired raw template ContentView SHA-256:
`24e583241d0d09bbc466661b532e45e08559b353b4a72f1a7eedbb50bd7b305e`.
Foreground evidence index SHA-256 is recorded in the packaged derivation record;
synthetic screenshots and detailed local receipts remain outside the plugin.

The earlier [0.9.1 limitation](RELEASE-091.md) is historical. This edition's current
acceptance record is here. Existing generated apps need the same focused source
change and their own build/visual checks; updating a plugin does not rewrite them.

## Scope

Only the BAMA companion advances to 1.0.0-adapted.2. Visual Design Studio 0.9.1 and
REA Toolkit 0.1.0 retain their payloads. Package pin and installed file inventories
are verified separately from application rendering. Native behavior on other OS
or SDK versions, signing, distribution and client acceptance remain project checks.

Apple reference: [toolbarColorScheme(_:for:)](https://developer.apple.com/documentation/swiftui/view/toolbarcolorscheme(_:for:)).
