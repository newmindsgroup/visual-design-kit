# Large screens: iPad, foldables, resizable windows, pointer and keyboard

Version-Timestamp: 2026-10-20 02:08:24 UTC

Large screens are no longer optional. Android 16 (API 36, required on Google Play from 31 August 2026) ignores orientation and resizability locks on displays 600dp wide or more, iPadOS windows resize freely, and iOS 27 makes iPhone apps fully resizable on iPad and in iPhone Mirroring. Apple's developer site (October 2026) also lists iPhone Duo, an iPhone with outer and inner displays. Design every screen as a range of widths, not a phone layout stretched.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Layout trigger | Width size class (iOS) or window size class (Android), recomputed on every resize | Never use device model, orientation or "isTablet" |
| Panes | 1 pane under 600dp/compact; 2 panes at 840dp+ or iOS regular width; 3 panes from 1200dp+ only for deep hierarchies (mail, files, admin) | Medium width (600-839dp): one pane plus a rail, or two panes only if both fit at 360dp+ |
| List pane width | Fixed 320-400pt/dp; detail pane flexible | Dense data lists can go to 440dp |
| Navigation | iOS: tab bar convertible to sidebar; Android: rail at medium+, expanded rail at large+ | Single-task apps (camera, player) keep minimal chrome |
| Text measure | 60-75 characters for reading text; center or cap content width at about 680-840pt/dp | Dashboards and canvases use full width |
| State | Selection, scroll position and drafts survive resize, fold and unfold | Never reset a form when the window changes class |
| Input | Touch, pointer, keyboard and pencil all first-class | Kiosk or single-input hardware |

## Canonical layouts

| Layout | Compact | Expanded | Use for |
| --- | --- | --- | --- |
| List-detail | List, then push detail | List and detail side by side; selection stays highlighted | Mail, messages, settings, files, CRM records |
| Supporting pane | Supporting content in a sheet or below | Main content plus a 280-400 wide side pane | Docs with comments, video with chat, editor with inspector |
| Feed | 1 column | Adaptive grid of 2-4 columns, card min width 280-360 | News, shopping, social, media catalogs |

Compose: `ListDetailPaneScaffold`, `SupportingPaneScaffold`, `NavigationSuiteScaffold`, and lazy grids with `GridCells.Adaptive(minSize)`. SwiftUI: `NavigationSplitView` (two or three columns), `TabView` with `.sidebarAdaptable`, `inspector`, `LazyVGrid` with adaptive columns.

## iPad

- **Navigation**: the tab bar sits near the top and can convert to a sidebar; use `NavigationSplitView` when the app is hierarchy-first. Let people hide the sidebar for focus.
- **Windows and multitasking**: since iPadOS 26, windows resize freely and the iPad has a menu bar. Support multiple windows (scenes) for document and messaging apps; each window keeps its own state.
- **Menu bar and keyboard**: put every command in the menu bar with its shortcut. Standard shortcuts must work (Cmd-N, Cmd-F, Cmd-W, Cmd-Z/Shift-Cmd-Z, Cmd-comma for settings, arrow keys and Return in lists, Esc to dismiss). Holding Cmd shows the shortcut overlay.
- **Pointer**: hover effects on interactive elements (system controls do this automatically; add `.hoverEffect` to custom ones), right-click or two-finger click opens the same context menu as long press, drag-select multiple items, scroll and pinch on trackpads. Toolbars that minimize should reappear when the pointer hovers over them.
- **Apple Pencil**: Scribble works in standard text fields; drawing apps support pressure, tilt, hover, squeeze and barrel roll on supported models.
- **Drag and drop**: between your windows and other apps for text, images, files and records.
- **Popovers** anchor to their source on regular width and become sheets on compact width.

## iPhone resizing and iPhone Duo

- iOS 27: iPhone apps run fully resizable in iPhone Mirroring on Mac and on iPad. `UIRequiresFullscreen` now gives discrete resizing rather than opting out. Replace orientation checks with size-class checks.
- iPhone Duo (Apple developer site, October 2026): an outer display and an inner display. App Store screenshots for it are 1398x2034px (outer) and 2007x2853px (inner) portrait, required from April 2027 for apps built with the iOS 27.1 SDK or later. Treat the inner display as a regular-width canvas (list-detail, supporting pane) and keep task continuity when people open or close the device. Apple's HIG and WWDC26 sessions on iPhone Duo hold the detailed patterns; verify there before designing fold-specific behavior.

## Android foldables and tablets

- **Postures**: flat (treat as a tablet), **tabletop** (half-folded horizontally: content in the top half, controls in the bottom half), **book** (half-folded vertically: two pages or list-detail split at the fold). Detect with Jetpack WindowManager `FoldingFeature` (state, orientation, bounds, occlusion).
- **Hinge**: never place text, faces or buttons across a separating fold; split panes at the fold bounds.
- **Continuity**: unfolding moves the app from the cover screen to the inner screen; restore the same item and scroll position. Do not restart.
- **Taskbar and multi-window**: tablets show a taskbar; apps run side by side in split screen and in resizable windows on desktop-style environments. Test at one-third, half and two-thirds widths.
- **Keyboard and mouse**: Tab focus order, visible focus, Ctrl shortcuts (Ctrl-C/V/Z/F, Ctrl-Enter to send), right-click context menus, hover states, tooltips on icon buttons, and the keyboard shortcuts helper (Meta-/) listing your shortcuts. Stylus handwriting works in standard text fields.
- **Orientation**: do not lock it. At API 36 the system ignores the lock on large screens anyway, so a portrait-only layout fills the whole window (no pillarboxing) and looks stretched unless it adapts.

## Layout recipes by width

| Width | Phone-first app becomes |
| --- | --- |
| Under 600dp / compact | Single column, bottom navigation, sheets for secondary content |
| 600-839dp / iPad portrait split | Rail or sidebar; one wide column with max content width, or a 2-pane list-detail if the list fits at 320dp |
| 840-1199dp / iPad landscape | Rail or sidebar plus list-detail; dialogs instead of full-screen pages for short tasks |
| 1200dp and up / large windows | Sidebar plus list plus detail, or main plus inspector; multi-column grids for feeds |

## Common failures

- Phone layout stretched to 1200dp with 900dp-wide text lines and giant buttons: cap measure, add panes.
- Bottom navigation bar on a landscape tablet: switch to a rail or sidebar.
- Full-screen modal pages for every small edit on iPad: use popovers, sheets or inline editing.
- No hover or focus state, so pointer and keyboard users cannot see what is interactive.
- Selection lost when rotating, folding or resizing.
- Touch-only gestures with no menu, shortcut or button equivalent.

## Test matrix

Run at minimum: iPhone small and large, iPad full screen and smallest window, iPhone app resized on iPad (iOS 27), Android phone, Android foldable folded and unfolded (tabletop too), Android tablet in split screen at 50%, a keyboard-and-pointer pass on iPad and on an Android tablet or Chromebook, and largest text sizes on each.
