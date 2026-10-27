# macOS interface and visual design

Version-Timestamp: 2026-10-27 11:36:23 UTC

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 11:36:23 UTC

## Select a desktop structure

Design for resizable windows, pointer, keyboard, menus and persistent work. Do not scale an iPhone screen into a desktop window.
Pin the minimum macOS version and actual SwiftUI/AppKit capabilities before specifying newer materials or window APIs.
Accepted project DESIGN.md, tokens, approved UI and accessibility requirements override the starting dimensions here.
For a reconstruction preserve observed screen and command behavior, then label platform adaptations explicitly.

| Product shape | Starting structure | Use when |
| --- | --- | --- |
| Content library | Sidebar, list and optional detail or inspector | People move between collections and inspect selections |
| Document tool | Document window, toolbar and inspector | Independent files need multiple windows |
| Menu bar utility | Menu bar entry, focused panel and Settings | The primary task is quick and peripheral |
| Capture tool | Small task panel with one clear completion | People return immediately to another app |
| Long-running utility | Main status window and background progress | Work needs monitoring, cancel and recovery |

Choose entry points deliberately: app launch, menu command, toolbar, global shortcut, drag/drop or a declared URL scheme.
A global shortcut or background permission is an implementation capability to verify, not an automatic design prerequisite.
Write a command map before adding toolbar buttons. Reuse system command meanings where applicable.

## Start from measured desktop defaults

Use a 4pt spacing scale for custom content: 4, 8, 12, 16, 20, 24 and 32.
Start custom window content with 20pt margins, related controls 8pt apart and section spacing 24pt to 32pt.
Keep native forms, sidebars and toolbars on their platform metrics; a raw-number lint should not reject system-owned geometry.
Use system macOS text roles, with body near 13pt as a starting point rather than the iOS 17pt default.
Keep small metadata readable and raise sizes for audience needs; do not force a 10pt minimum into an accessibility-sensitive product.
Let native control size determine desktop control height. Do not impose a 44pt mobile control height on every Mac toolbar.
Use `NavigationSplitView`, `Form`, `Grid`, `LabeledContent` and baseline-aligned stacks before local offsets.
Start sheet-content widths around 360, 480 or 640pt according to the task, then test long text, localization and short screens.
Define minimum and preferred window sizes from content. Resize to the minimum and a wide case before accepting a layout.

## Place actions where their scope is clear

A toolbar item belongs above the pane it affects: collection actions over the list, selection actions over detail and inspector controls near the inspector.
Use few toolbar groups and at most one prominent completing action in the current task region.
Keep frequent commands in menus with conventional shortcuts; toolbar-only controls make keyboard use and discovery weaker.
Keep unavailable commands visible and disabled when their location teaches the command structure.
Provide context menus for relevant object actions without making them the only route to a required task.
Give icon-only actions a native label and help text. A drawing name does not communicate the action.
Use Command-comma for Settings, Command-W for closing a window, and preserve standard edit shortcuts.
Return and Escape follow the selected task's confirm/cancel contract; they must not trigger unrelated destructive work.
Use the shared [surface placement method](../../ux-design/references/surface-placement.md) for inline, popover, sheet, panel and window decisions.

## Preserve system behavior when customizing

Prefer native controls themed through tokens. Use ButtonStyle or ToggleStyle rather than a shape with a gesture.
A custom sidebar still needs arrow navigation, selection semantics, focus, inactive-window appearance and context commands.
Custom chrome must retain window dragging, traffic-light access, resizing, full screen and standard window commands.
Do not prescribe removing initial focus universally. Focus the primary typing task when expected and keep keyboard entry possible from every opening state.
Restore the caller's focus when a sheet or popover closes; specify the fallback if its original item no longer exists.
Keep scroll indicators consistent with system settings.
Use an inspector for ongoing selection detail and a separate window for independent parallel work.
Ask before discarding actual unsaved edits; do not add confirmation to harmless navigation.

## Apply materials and color

Use system semantic foregrounds and backgrounds for native chrome; keep approved brand character in content and scoped accents.
Use newer glass materials in navigation or control layers when the chosen OS and toolkit support them.
Avoid glass-on-glass and translucent content cards without a functional reason.
Treat desktop tint and active/inactive state as rendering conditions in visual evidence.
Support light, dark, Increase Contrast, Reduce Transparency and Reduce Motion using actual system behavior.
Use semantic on-accent text rather than fixed white; validate each allowed user accent against its background.
Do not automatically add a theme picker, accent picker or motion preference to an existing product. Extend settings only when the project requires the choice.
Keep status meaning in wording or shape as well as color.

## Specify interaction and recovery

Represent empty, loading, partial, offline, denied permission, failed save and success states for each affected flow.
Use cached content during refresh when safe and show freshness or an error without discarding useful data.
Optimistic changes need a rollback or recoverable failure state; closing a capture panel is not proof a background save succeeded.
Give long jobs progress, safe cancel and a clear result location.
Use Undo for reversible destructive operations where the product contract supports it; a confirmation dialog does not replace recoverability.
Request OS permissions at the feature that needs them and design denial, later revocation and unavailable-capability states.
Do not silently enable screen capture, global accessibility, clipboard monitoring or background startup to make a design demonstration work.

## Verify layout with three complementary checks

1. Inspect token usage and explicit geometry exceptions in changed source.
2. Measure actual rendered frames for shared edges, insets, bounds, spacing and overlap at the tested window sizes.
3. Inspect screenshots with optional grid and frame overlays to diagnose discrepancies.

A 4pt design scale does not prove every rendered coordinate must be a multiple of four; text baselines and system components have their own metrics.
For custom nested surfaces start with inner radius equal to outer radius minus inset, clamped at zero; adjust optical exceptions visibly.
Do not use local offsets to conceal a wrong container alignment.
Keep probes and forced gallery states in debug or test paths rather than changing production behavior.

## Capture a native review set

Capture every changed window, page, panel, menu, sheet and Settings tab in light and dark at documented logical size and scale.
Include focused, inactive, selected, empty, error and loading states relevant to the change.
Use synthetic fixtures in a newly created isolated store; never point snapshot cleanup at a real user store.
Verify keyboard-only operation and accessible names with actual native tools. Report screen-reader checks as pending unless executed.
A Swift typecheck, browser mockup or static SwiftUI preview does not prove a running Mac app's window or permission behavior.
Record screenshots, frame measurements, test results and remaining native limitations separately.

## Application icons

Use the [icon design method](../../icon-design/SKILL.md) for original concepts, geometry, optical review and asset licensing.
The layered macOS route requires `actool` plus Icon Composer's own `ictool`, with exact paths verified on the receiving Mac.
Compile and render to a new staging directory, inspect supported appearances and small Dock/Finder sizes, and verify actual outputs.
Missing full icon tooling leaves vector design possible and compiled/native icon acceptance pending.
Do not install the app, clear extended attributes, replace an existing bundle or restart Dock as part of asset design.

## Sources

- [BAMA mac-design](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310/skills/design/mac-design), [layout-grid](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310/skills/design/layout-grid) and [design-system](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310/skills/design/design-system): pinned method sources, selectively generalized here.
- [Apple designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos): verify current platform behavior before implementation.
