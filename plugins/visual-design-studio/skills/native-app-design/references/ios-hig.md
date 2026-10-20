# iOS and iPadOS: Human Interface Guidelines in practice

Version-Timestamp: 2026-10-20 02:08:24 UTC

Checked against Apple's Human Interface Guidelines (developer.apple.com/design/human-interface-guidelines) on 2026-10-20: layout, typography, materials, color, tab bars, toolbars, sheets, accessibility, app icons, widgets, Live Activities and haptics. Items marked "verify" could not be confirmed from Apple's own pages. Apple revises the HIG several times a year; check the page's change log before production.

## Platform state (as of October 2026)

- **iOS 26 (2025)** introduced **Liquid Glass**: a translucent functional layer for controls and navigation (tab bars, toolbars, sidebars, sheets) that floats above content. Standard UIKit and SwiftUI components adopt it automatically when built with the iOS 26 SDK or later.
- **iOS 27 (2026)** keeps Liquid Glass and refines readability. Apple's WWDC26 UIKit session states that iPhone apps are now fully resizable (iPhone Mirroring on Mac, iPhone apps on iPad) and that `UIRequiresFullscreen` no longer opts an app out of resizing. Press coverage describes a user control for glass opacity; the HIG only says people can "choose a preferred look for Liquid Glass" in Settings (verify the exact options).
- **iPhone Duo**: Apple's developer site lists an iPhone with an outer and an inner display and asks apps to resize dynamically. See [large screens](large-screens.md).
- Xcode 26 offered a temporary compatibility opt-out from the new design (`UIDesignRequiresCompatibility`). Treat it as gone for new work; verify against current Xcode release notes.

## Layout, safe areas and margins

| Item | Default | Notes |
| --- | --- | --- |
| Design frame | 402x874pt (6.3 in: iPhone 17, 16 Pro, 17 Pro) or 393x852pt (6.1 in: iPhone 15, 16), and 440x956pt (Pro Max); check 375x667pt for small devices | Common starting points; Apple removed the device table from the HIG layout page in Sept 2026 and points to Device Hub in Xcode, so verify current sizes there |
| Safe area | Always lay out inside `safeAreaInsets`; read them, never hardcode | Typical portrait insets: top 47-62pt on Face ID iPhones (Dynamic Island models at the high end), bottom 34pt for the home indicator. Landscape adds leading/trailing insets |
| Side margins | 16pt on compact width; 20pt on wider iPhones and iPad regular width | Use the system layout margins (`layoutMargins`, SwiftUI default padding) rather than a fixed number |
| Readable width | Constrain long text to the readable content guide (about 60-75 characters) | Matters on iPad and in landscape |
| Backgrounds | Extend full-bleed backgrounds under tab bars, toolbars and sidebars | Use `backgroundExtensionEffect()` when a sidebar would cover key image content |
| Corners | Keep custom shapes concentric with the bar or container they sit in | Liquid Glass components use concentric radii; mismatched radii look broken |

Order content by importance from the top and leading edge, align to few axes, use indentation for hierarchy, and support right-to-left by using system components that mirror automatically.

## Size classes

Decide layout from size classes, never from device type or orientation. Every combination can occur because windows resize on iPad, in iPhone Mirroring and (from iOS 27) for iPhone apps on iPad.

| Context | Horizontal | Vertical |
| --- | --- | --- |
| iPhone portrait | Compact | Regular |
| iPhone landscape (most models) | Compact | Compact |
| iPhone landscape (largest models) | Regular | Compact |
| iPad full screen, either orientation | Regular | Regular |
| iPad narrow split or small window | Compact | Regular |

Keep functionality identical across size classes; only change how much is visible. Typical switch: tab bar on compact width, sidebar (or tab bar convertible to sidebar) on regular width.

## Touch targets and spacing

- Hit region at least **44x44pt** for every control; 28x28pt is Apple's stated minimum for dense secondary controls only.
- Spacing: about 12pt around controls that have a visible bezel, about 24pt around borderless controls (HIG accessibility guidance).
- Visual size can be smaller than the hit region: a 22pt symbol with a 44pt hit area is normal. Expand with `contentShape` or padding, not by enlarging the glyph.
- Always design a pressed state for custom buttons.

## Navigation

| Pattern | Use for | Rules |
| --- | --- | --- |
| Tab bar | 3-5 top-level sections on iPhone | Navigation only, never actions. Always visible except under modals. Single-word labels, filled SF Symbols. Do not hide or disable tabs; explain empty sections instead. Avoid the overflow More tab |
| Tab bar (iOS 26+) | Same | Floats over content on Liquid Glass. Can minimize on scroll with an accessory such as a mini player inline. A dedicated search tab can sit at the trailing end |
| Tab bar (iPadOS) | Same | Appears near the top; can convert to a sidebar (`sidebarAdaptable`). Default list of five or fewer if people can customize it |
| Navigation stack | Drill-down hierarchy | `NavigationStack`. Large title on the root screen collapsing to an inline title on scroll. Standard Back button using the system chevron; never block the left-edge swipe-back gesture |
| Sidebar / split view | Deep hierarchies on iPad and Mac | `NavigationSplitView` with 2 or 3 columns |
| Sheet | Focused subtask that returns to the parent | One sheet at a time. Cancel at leading edge, Done at trailing edge, never all of Cancel, Done and Back together |
| Full-screen cover | Immersive tasks (camera, media, onboarding) | Provide an obvious close control |

## Toolbars and navigation bars

- Toolbars hold the view title, navigation controls and actions. Aim for at most three groups: leading (back, sidebar toggle, title), center (common tools), trailing (primary action, search, More menu).
- Keep titles under about 15 characters. Do not title a view with the app name.
- Prefer borderless SF Symbols; the glass group supplies the container. Use text only where a symbol is ambiguous (Edit, Done).
- Give exactly one primary action the prominent (tinted) style, on the trailing side.
- Do not paint custom backgrounds or heavy tints on bars in iOS 26+. Let content inform the bar and use a scroll edge effect to separate bar from content.
- Avoid a text label reading "Back" or "Close"; use the standard symbols.

## Sheets and detents

- Detents: **large** (full height, always available) and **medium** (about half). Add medium for progressive disclosure (share sheet pattern); specify only medium to prevent full expansion. Custom heights are available in code.
- Show a grabber on resizable sheets; it is also how VoiceOver users resize.
- Support swipe-down to dismiss. If there are unsaved changes, confirm with an action sheet.
- In iOS 26+, partial-height sheets render as inset Liquid Glass panels that become edge-attached at full height (from WWDC25 sessions; verify the current behavior in the simulator).
- iPad: prefer page or form sheet styles centered over a dimmed background.

## Typography: Dynamic Type

Use the system text styles so text scales with Dynamic Type. The default ("Large") size, from the HIG typography specifications:

| Style | Weight | Size (pt) | Leading (pt) | Emphasized weight |
| --- | --- | --- | --- | --- |
| Large Title | Regular | 34 | 41 | Bold |
| Title 1 | Regular | 28 | 34 | Bold |
| Title 2 | Regular | 22 | 28 | Bold |
| Title 3 | Regular | 20 | 25 | Semibold |
| Headline | Semibold | 17 | 22 | Semibold |
| Body | Regular | 17 | 22 | Semibold |
| Callout | Regular | 16 | 21 | Semibold |
| Subhead | Regular | 15 | 20 | Semibold |
| Footnote | Regular | 13 | 18 | Semibold |
| Caption 1 | Regular | 12 | 16 | Semibold |
| Caption 2 | Regular | 11 | 13 | Semibold |

- Range: xSmall (Body 14pt) to xxxLarge, then accessibility sizes AX1 (Body 28pt) to AX5 (Body 53pt). Test at AX5.
- Default iOS text size 17pt; minimum 11pt. Avoid Ultralight, Thin and Light weights at small sizes.
- At accessibility sizes: stack horizontally adjacent items vertically, let rows grow, reduce columns, avoid truncation in scrolling content, and keep primary elements at the top. Not everything must scale: tab labels can stay put while content grows.
- Custom fonts must scale too: map each to a text style (`Font.custom(_:size:relativeTo:)`, `UIFontMetrics`) and support Bold Text. See [SwiftUI and Compose handoff](handoff-swiftui-compose.md).

## SF Pro, New York and SF Symbols

- **SF Pro** is the iOS system font; **SF Pro Rounded** for soft UI; **New York** is the companion serif; **SF Mono** for code. The variable system fonts use dynamic optical sizes, so do not pick Text vs Display cuts manually in code; mockups may need tracking adjustments (tracking tables are in the HIG).
- Never embed the system fonts in the app; access them through system APIs. Apple's font license limits SF fonts to Apple-platform interfaces, so do not use SF Pro on Android or the web.
- **SF Symbols** (version 7 as of 2025): 9 weights, 3 scales (small, medium, large), rendering modes monochrome, hierarchical, palette and multicolor, variable color, animations (including Draw in SF Symbols 7) and gradient rendering. Match symbol weight to adjacent text weight; symbols scale with Dynamic Type automatically.
- Custom icons: draw them as custom symbols from the SF Symbols template so they align, scale and animate like system symbols.

## Color: system, semantic and Liquid Glass color

- Use **semantic** colors defined by purpose: `label`, `secondaryLabel`, `tertiaryLabel`, `quaternaryLabel`; `systemBackground`, `secondarySystemBackground`, `tertiarySystemBackground`; grouped variants for grouped lists; `separator`; `tint`/accent. Do not repurpose them (separator is not a text color).
- **System colors** (red, orange, yellow, green, mint, teal, cyan, blue, indigo, purple, pink, brown, six grays) each have light, dark and increased-contrast values. Apple updated the values in June 2025, so never hardcode old hex values; read them from Apple's design resources or the API.
- Liquid Glass has no inherent color; it takes color from content beneath. Tint sparingly: color the background of the one prominent action (the system does this for Done), not symbols scattered across the bar. If content is colorful, keep bars monochrome.
- Brand color lives in the content layer (hero areas, cards, illustrations, the accent tint), not as an opaque bar color. Apple's WWDC26 session "Communicate your brand identity on iOS" makes the same recommendation.
- Contrast: 4.5:1 for text up to 17pt (Apple's table), 3:1 for larger text and UI. Check light, dark and Increase Contrast, and check text over the brightest content that can scroll beneath glass.

## Materials and Liquid Glass

| Use | Material | Rule |
| --- | --- | --- |
| Controls and navigation (bars, sidebars, floating buttons) | Liquid Glass, regular variant | Default for system components; use sparingly on custom controls |
| Controls over photos or video | Liquid Glass, clear variant | Add a dark dimming layer of about 35% opacity when content beneath is bright |
| Content layer surfaces (cards, backgrounds) | Standard materials: ultraThin, thin, regular (default), thick, or solid colors | Never put Liquid Glass in the content layer, except transient states of sliders and toggles |
| Text on materials | Vibrant label colors (`label` to `quaternaryLabel`) | Avoid quaternary on thin and ultraThin |

Accessibility settings (Reduce Transparency, Increase Contrast, the user's preferred glass look) change glass appearance; design so every state still meets contrast. The generic failure is "glass on everything": frosted cards, glass buttons in content, blur stacked on blur.

## Haptics

- Prefer standard controls (toggles, sliders, pickers) that play system haptics automatically.
- Feedback generators: **notification** (success, warning, error) for outcomes; **impact** (light, medium, heavy, soft, rigid) for physical metaphors such as snapping; **selection** while a value changes. SwiftUI: `.sensoryFeedback(_:trigger:)`.
- Use each pattern for its documented meaning, pair it with visual feedback, keep it short, and make haptics optional. Core Haptics for custom patterns, mainly games.

## App icon (iOS, iPadOS, macOS)

- **1024x1024px** square, layered: a background layer plus one or more foreground layers assembled in **Icon Composer** (ships with Xcode). The system applies Liquid Glass effects (specular highlights, refraction, translucency) and the rounded mask.
- Appearances: default, dark, clear light, clear dark, tinted light, tinted dark. The system generates any you do not supply; design at least default and dark yourself and keep the same core shapes across all.
- Provide unmasked square layers with crisp edges; vector (SVG or PDF) layers preferred, PNG for raster or mesh gradients. Color spaces sRGB, Display P3 or Gray Gamma 2.2.
- Do not draw your own highlights, bevels, drop shadows or glows; the system does it dynamically. Avoid text, photos, UI replicas and Apple hardware. Keep the main shape centered.
- Alternate icons need their own dark, clear and tinted variants. Store export specs: [app store assets](app-store-assets.md).

## Widgets and Live Activities (overview)

- **Widgets**: system small, medium, large (plus extra large on iPad); accessory circular, rectangular and inline on the Lock Screen. On a 393x852pt iPhone: small 158x158pt, medium 338x158pt, large 338x354pt. Margins 16pt standard, 11pt for tight groupings; text at least 11pt; use `ContainerRelativeShape` for concentric corners. Widgets render full-color, accented or vibrant, and people choose light, dark, clear or tinted on the Home Screen, so test monochrome legibility.
- **Live Activities**: presentations compact (leading and trailing around the camera), minimal (when several are active), expanded (on press), Lock Screen banner, and StandBy (Lock Screen layout scaled 2x). Use for events with a clear start and end, ideally no longer than 8 hours. Fit compact and minimal content inside a 28pt circle for limited-width contexts such as landscape. Never show sensitive data. iOS 27 adds a landscape Dynamic Island style (WWDC26 "Live Activities essentials").

## Accessibility checklist for iOS screens

- VoiceOver: every control has a label; group related elements; logical order; custom actions for swipe-only actions.
- Dynamic Type to AX5 without clipped essential text; Bold Text; Button Shapes; Smart Invert (exclude photos and video).
- Reduce Motion: replace slides and zooms with fades; Reduce Transparency: glass becomes more opaque, check it.
- Contrast in light, dark and Increase Contrast; no meaning by color alone.
- App Store Accessibility Nutrition Labels (2025) let you declare supported features; only claim what you have tested.
