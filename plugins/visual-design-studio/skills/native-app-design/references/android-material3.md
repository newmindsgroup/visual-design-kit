# Android: Material 3 and Material 3 Expressive in practice

Version-Timestamp: 2026-10-20 02:08:24 UTC

Checked on 2026-10-20 against developer.android.com (window size classes, Android 16 behavior changes, Play target API, adaptive icons, Play icon specs) and the Jetpack Compose Material 3 token sources (type scale, shape, elevation, motion, component sizes). The m3.material.io site could not be fetched from this environment; items marked "verify" come from Material's published guidance as last known. Compose Material 3 versions as of 2026-10-07: stable 1.4.0, beta 1.5.0-beta01 (most Expressive APIs are in 1.5 and annotated `@ExperimentalMaterial3ExpressiveApi`).

## Platform state (as of October 2026)

- **Material 3 Expressive** (announced May 2025) extends M3 with spring-based motion, a 35-shape library with shape morphing, bigger type and button sizes, and new components: button groups, split button, FAB menu, loading indicator, docked and floating toolbars, flexible navigation bar, expanded navigation rail.
- **Google Play target API**: from 31 August 2026, new apps and updates must target Android 16 (API 36). Consequences below are therefore defaults, not options.
- **Edge-to-edge** is enforced for apps targeting API 35; at API 36 the opt-out attribute is disabled.
- **Predictive back** system animations (back-to-home, cross-activity, cross-task) are on by default at API 36, and `onBackPressed` is no longer called.
- **Large screens**: at API 36, orientation, resizability and aspect-ratio restrictions are ignored on displays 600dp wide or more (games excepted). Design every screen to resize.

## Touch targets and density

- Touch target at least **48x48dp**, with at least 8dp between targets. Icons are 24dp inside that area. Compose enforces 48dp on interactive components through `minimumInteractiveComponentSize()`; do not disable it.
- Button heights (Expressive sizes): XS 32dp, S 40dp (the classic default), M 56dp, L 96dp, XL 136dp. Small visual sizes still get a 48dp target.
- Text scales to 200% (nonlinear scaling since Android 14). Size containers in sp-aware ways and test at the largest font size and display size.

## Window size classes (width drives layout)

| Class | Width | Typical devices | Navigation | Panes | Margin |
| --- | --- | --- | --- | --- | --- |
| Compact | under 600dp | Phones in portrait | Navigation bar | 1 | 16dp |
| Medium | 600-839dp | Tablets portrait, unfolded foldables portrait | Navigation rail | 1 (2 only with care) | 24dp |
| Expanded | 840-1199dp | Tablets landscape, foldables landscape | Rail (collapsed or expanded) | 2 | 24dp |
| Large | 1200-1599dp | Large tablets | Expanded rail or permanent drawer | 2-3 | 24dp |
| Extra-large | 1600dp and up | Desktop and connected displays | Expanded rail or permanent drawer | 3 | 24dp |

Height classes: compact under 480dp (phones in landscape), medium 480-899dp, expanded 900dp and up. A phone in landscape is medium width but compact height, so avoid two-pane layouts there. Breakpoints are from developer.android.com; margins are Material's layout guidance (verify). Compute with `currentWindowAdaptiveInfo()` (pass `supportLargeAndXLargeWidth = true` for the two largest classes). Never branch on "isTablet".

## Navigation components

| Component | Spec | Use |
| --- | --- | --- |
| Navigation bar | 3-5 destinations; 64dp tall in the Expressive flexible bar (80dp in the earlier baseline); icon plus label always | Compact width. On medium width the flexible bar can place label beside icon |
| Navigation rail | Collapsed 96dp wide (80dp narrow variant); expanded 220-360dp; optional FAB at top | Medium width and up. Expanded rail can be modal or standard |
| Navigation drawer | Modal on compact, permanent on large | Expressive guidance favors the expanded navigation rail instead of the drawer (verify current status) |
| `NavigationSuiteScaffold` | Switches bar, rail and drawer by window size | Default in Compose apps with 3-5 top-level destinations |
| Tabs | Primary (under the top app bar) or secondary | Peer views within one destination, not app-level navigation |

Material Symbols are the icon set: variable font with Fill, Weight (100-700), Grade and Optical size axes, in Outlined, Rounded and Sharp styles. Use filled icons for the selected navigation destination and outlined for unselected.

## Top app bars and toolbars

| Bar | Height | Behavior |
| --- | --- | --- |
| Small (title start-aligned or centered) | 64dp | Pinned or enter-always on scroll |
| Medium flexible | 112dp expanded | Collapses to small on scroll (exit-until-collapsed) |
| Large flexible | 152dp expanded | Collapses to small on scroll |
| Docked toolbar (Expressive) | Bottom, full width | Replaces the bottom app bar for screen actions |
| Floating toolbar (Expressive) | Floats above content, horizontal or vertical | Contextual actions; pair with a FAB |

Navigation icon at start, up to 2-3 action icons at end, overflow menu for the rest. Title is the screen name, not the app name.

## Floating action button

- Sizes: **FAB 56dp** (corner 16dp), **medium FAB 80dp** (corner 20dp, new in Expressive), **large FAB 96dp** (corner 28dp); extended FAB adds a label. Expressive de-emphasizes the 40dp small FAB (verify).
- One FAB per screen, for the single most common constructive action (compose, create, add). Never for destructive or minor actions.
- Placement: bottom-end, 16dp from edges on compact; in the rail on medium and larger.
- **FAB menu** replaces the speed dial: one FAB that opens 2-6 related actions.

## Type scale (Compose Material 3 tokens)

| Role | Size / line height (sp) | Weight | Tracking (sp) |
| --- | --- | --- | --- |
| Display Large | 57 / 64 | 400 | -0.2 |
| Display Medium | 45 / 52 | 400 | 0 |
| Display Small | 36 / 44 | 400 | 0 |
| Headline Large | 32 / 40 | 400 | 0 |
| Headline Medium | 28 / 36 | 400 | 0 |
| Headline Small | 24 / 32 | 400 | 0 |
| Title Large | 22 / 28 | 400 | 0 |
| Title Medium | 16 / 24 | 500 | 0.2 |
| Title Small | 14 / 20 | 500 | 0.1 |
| Body Large | 16 / 24 | 400 | 0.5 |
| Body Medium | 14 / 20 | 400 | 0.2 |
| Body Small | 12 / 16 | 400 | 0.4 |
| Label Large | 14 / 20 | 500 | 0.1 |
| Label Medium | 12 / 16 | 500 | 0.5 |
| Label Small | 11 / 16 | 500 | 0.5 |

- Default typeface is Roboto (the platform font on most devices); Roboto Flex (OFL) gives variable width, weight and optical size. A brand font replaces the families, not the roles. Expressive adds emphasized variants of each role (heavier weight).
- Use Body Large (16sp) for primary reading text; never below Label Small (11sp).

## Color: dynamic color and tonal palettes

- M3 derives a scheme from **key colors** (primary, secondary, tertiary, neutral, neutral variant, error) using the HCT color space. Each key color produces a **tonal palette** of tones 0-100 (0, 10, 20 ... 90, 95, 99, 100, plus extra surface tones).
- Roles, light and dark: `primary`, `onPrimary`, `primaryContainer`, `onPrimaryContainer`, the same for secondary, tertiary and error; `surface`, `onSurface`, `onSurfaceVariant`; surface containers `surfaceContainerLowest`, `Low`, `surfaceContainer`, `High`, `Highest`, plus `surfaceDim` and `surfaceBright`; `outline`, `outlineVariant`; `inverseSurface`, `inverseOnSurface`, `inversePrimary`; `scrim`; fixed roles (`primaryFixed`, `primaryFixedDim` and their "on" roles) that do not change between light and dark.
- Classic tone mapping: primary tone 40 (light) / 80 (dark); container 90 / 30; on-container 10 / 90. Newer color-spec versions adjust several tones for contrast, so generate the scheme (Material Theme Builder, Material Color Utilities) rather than hand-picking tones.
- **Dynamic color** (Android 12, API 31+) builds the scheme from the user's wallpaper. Default: support it for utility and productivity apps; keep a fixed brand scheme when brand recognition or regulated color meaning matters (banking, health status, sports teams), or offer it as a setting. Scheme variants include Tonal Spot (default), Neutral, Vibrant, Expressive, Fidelity, Content and Monochrome.
- Contrast levels: standard, medium and high schemes. Android 14+ exposes a user contrast setting; ship medium and high variants.
- Elevation is mostly tonal: higher surfaces use higher `surfaceContainer` roles instead of heavier shadows.

## Shape scale

| Token | Corner | Typical components |
| --- | --- | --- |
| None | 0dp | Full-bleed media, docked bars |
| Extra small | 4dp | Text field top corners, menus, snackbars |
| Small | 8dp | Chips |
| Medium | 12dp | Cards |
| Large | 16dp | FAB, navigation drawer, side sheets |
| Large increased | 20dp | Medium FAB (Expressive) |
| Extra large | 28dp | Dialogs, bottom sheet top corners, large FAB |
| Extra large increased | 32dp | Expressive containers |
| Extra extra large | 48dp | Expressive hero containers |
| Full | 50% | Buttons, search bar, badges |

Expressive adds `MaterialShapes`: 35 named shapes (Circle, Square, Pill, Cookie 4/6/7/9/12-sided, Clover 4/8-leaf, Sunny, Burst, Flower, Gem, Heart, Arch and others) that can morph. Use them for avatars, loading indicators, selection emphasis and illustrative moments, not for every container.

## Elevation

Levels 0-5 = 0, 1, 3, 6, 8, 12dp. Cards and app bars at rest sit at 0-1; menus and navigation drawers 1-3 (tonal); FAB at 3 resting; modal sheets and dialogs at 1-3 with a scrim. Prefer tonal containers to shadows; use shadow only when an element floats over varied content.

## Motion

| Scheme | Spatial spring (stiffness / damping) default, fast, slow | Effects spring default, fast, slow | Use |
| --- | --- | --- | --- |
| Standard | 700 / 0.9, 1400 / 0.9, 300 / 0.9 | 1600 / 1.0, 3800 / 1.0, 800 / 1.0 | Utilitarian, recurring interactions |
| Expressive | 380 / 0.8, 800 / 0.6, 200 / 0.8 | 1600 / 1.0, 3800 / 1.0, 800 / 1.0 | Hero moments, prominent components |

- Spatial specs move or resize things and may overshoot; effects specs animate color and opacity without overshoot.
- Easing-and-duration tokens remain for non-spring cases: standard `cubic-bezier(0.2, 0, 0, 1)`, emphasized decelerate `(0.05, 0.7, 0.1, 1)`, emphasized accelerate `(0.3, 0, 0.8, 0.15)`; durations short 50-200ms, medium 250-400ms, long 450-600ms. These match the kit's `--ease-*` tokens.
- Honor "Remove animations" (animator duration scale 0): replace motion with instant state changes or fades.

## Edge-to-edge and insets

- Call `enableEdgeToEdge()`; draw app backgrounds behind the status and navigation bars.
- Pad interactive content with `WindowInsets.safeDrawing` (or `systemBars`, `displayCutout`, `ime` as needed). Lists scroll under the navigation bar with bottom content padding equal to the inset.
- Gesture navigation bar is transparent; 3-button navigation gets a translucent scrim. Keep taps away from the bottom gesture area and the screen edges used for back.
- Status bar icons must contrast with whatever sits beneath them in light and dark themes.

## Predictive back

- Use `BackHandler`/`PredictiveBackHandler` (Compose) or `OnBackPressedCallback`; never intercept back with legacy key handling.
- Material components (bottom sheets, side sheets, navigation drawer, search) animate with the back gesture progress. Custom full-screen surfaces should scale down slightly and reveal the destination as the gesture progresses.
- Only intercept back to protect unsaved work; then confirm, do not trap.

## Other components to get right

- **Bottom sheets**: standard or modal, drag handle 32x4dp, top corners 28dp, max width about 640dp on large screens.
- **Dialogs**: basic dialogs with 1-2 actions, text buttons at the end; full-screen dialogs on compact widths for complex input.
- **Snackbars**: one at a time, one optional action, above the navigation bar and FAB.
- **Loading indicator** (Expressive): morphing shapes for waits under about 5 seconds and pull-to-refresh; linear progress for determinate work.

## Adaptive and themed icons

- Foreground and background layers at **108x108dp**; the inner **66x66dp** is the visible safe zone after masking; keep the logo between 48 and 66dp; the outer 18dp on each side is reserved for motion and masking effects.
- Add a **monochrome** layer (Android 13+) so the icon participates in themed icons; without it the launcher shows the full-color icon.
- Launchers mask to circles, squircles or rounded squares; never bake a shape or shadow into the layers.
- Play Store icon: see [app store assets](app-store-assets.md).

## Accessibility checklist for Android screens

- TalkBack: content descriptions on icon-only controls, merged semantics for list rows, meaningful traversal order, custom actions for swipe gestures.
- Font scale 200% and largest display size without clipped essential text.
- Contrast 4.5:1 text, 3:1 UI in standard and high-contrast schemes and with dynamic color from extreme wallpapers (test near-white and saturated wallpapers).
- Switch Access and keyboard: every action reachable with focus and Enter.
