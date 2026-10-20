# Cross-platform apps: React Native and Expo, Flutter, Compose Multiplatform

Version-Timestamp: 2026-10-20 02:08:24 UTC

Choose the framework from the product's needs, then decide per element what must stay native. Framework facts below are as of October 2026 from vendor blogs and docs reachable from this environment; versions move quickly, so confirm against each project's current release notes before committing a client to a stack.

## Default recommendation

| Situation | Default | Why |
| --- | --- | --- |
| Product is the app, platform feel and newest OS features matter (widgets, Live Activities, Liquid Glass, M3 Expressive) | Native: SwiftUI + Jetpack Compose, shared logic optional via Kotlin Multiplatform | First access to platform components and behaviors |
| Startup or agency team with web/React skills, one codebase, platform-correct UI | React Native with Expo | Renders real native views; Expo UI exposes SwiftUI and Compose components |
| Brand-led UI that should look identical everywhere (games-adjacent, media, kids, kiosks), custom rendering | Flutter | Draws every pixel itself; consistent custom UI, strong animation |
| Android-first team that wants to share UI with iOS | Compose Multiplatform | One Kotlin UI codebase; iOS stable since 1.8.0 (May 2025) |
| Content-heavy, low-interaction, web team only | Responsive web app or PWA first | Ship faster; move to native when retention or device APIs justify it |

## Framework notes

### React Native and Expo

- The New Architecture (Fabric renderer, TurboModules) is the default in current React Native. Components map to real UIKit and Android views, so system text, accessibility and scrolling behave natively.
- **Expo UI** (`@expo/ui`) became stable in Expo SDK 56 (May 2026) per the Expo blog: platform packages `@expo/ui/swift-ui` and `@expo/ui/jetpack-compose` render actual SwiftUI and Compose components, and can be mixed inside one `Host`. Use them for pickers, menus, sliders, glass effects and Material components rather than JavaScript look-alikes.
- `expo-glass-effect` exposes Liquid Glass views on iOS 26+ (verify its API for your SDK). Expo Router with native stacks gives platform push transitions and the iOS edge-swipe back.
- Pitfalls: JS-drawn tab bars and headers that ignore Liquid Glass and predictive back; one shared style file with iOS shadows on Android; custom text inputs that break autofill.

### Flutter

- Flutter paints with its own engine (Impeller), so platform components are re-implementations. Material 3 is the default theme. Cupertino widgets approximate iOS.
- Flutter is moving Material and Cupertino out of the core SDK into standalone `material_ui` and `cupertino_ui` packages (opt-in in Flutter 3.47 per Flutter docs), and the Flutter blog says official Liquid Glass and Material 3 Expressive implementations are in progress. Until those ship, glass and Expressive effects are approximations; verify the current package status.
- Strengths: pixel-identical custom brand UI, complex animation, one rendering pipeline. Costs: the app can feel slightly "off" on both platforms if you use Material on iOS; platform views (maps, web views, native ads) add complexity.
- Use `Theme.of(context).platform` or adaptive constructors (`Switch.adaptive`, `showAdaptiveDialog`) for elements that must stay native.

### Compose Multiplatform and Kotlin Multiplatform

- **Kotlin Multiplatform (KMP)** shares business logic, networking and data while each platform keeps a native UI (SwiftUI and Compose). This is the lowest-risk way to share code without changing the UI.
- **Compose Multiplatform** shares the UI too. On iOS it renders Compose (Skia) inside a UIKit host, so Material components appear on iPhone unless you build iOS-style alternatives or embed SwiftUI/UIKit views through interop. Good for internal, B2B and Android-first products; weaker where iOS users expect platform polish.

## What must stay native (whatever the framework)

| Element | iOS behavior | Android behavior |
| --- | --- | --- |
| Back navigation | Back button with chevron at top-leading; left-edge swipe back | System back gesture or button with predictive back; no on-screen back required on root screens |
| Top-level navigation | Tab bar at the bottom (Liquid Glass, floating) | Navigation bar at the bottom on compact; rail on medium+ |
| Titles | Large title collapsing to inline | Top app bar, start-aligned or centered |
| Typography | SF Pro through text styles with Dynamic Type | Roboto or the brand font with sp and font scale. SF Pro is licensed for Apple platforms only |
| Icons | SF Symbols | Material Symbols |
| Alerts and choices | Alerts, action sheets, confirmation dialogs, context menus (long press) | Dialogs, bottom sheets, menus |
| Pickers and inputs | Wheel and inline date pickers, keyboard types, AutoFill and passkeys | Material date and time pickers, IME actions, Autofill and Credential Manager |
| System sheets | Share sheet, photo picker, document picker | Sharesheet, photo picker, system file picker |
| Permissions | System alert, optional single-button pre-alert screen | Runtime dialog with rationale; settings deep link after repeated denial |
| Feedback | Haptic generators (notification, impact, selection) | `HapticFeedbackConstants` / Compose haptic types |
| Surfaces outside the app | Widgets, Live Activities, App Intents, notifications with interruption levels | Widgets (Glance), notification channels, app shortcuts |
| Icons and store assets | Layered Icon Composer icon, App Store screenshots | Adaptive icon with monochrome layer, Play listing assets |
| Accessibility | VoiceOver, Dynamic Type, Reduce Motion and Transparency | TalkBack, font scale 200%, remove animations, high-contrast scheme |

Brand can and should be shared: color tokens, illustration, photography, content layout, custom content components (cards, charts, hero modules), voice and motion character. Platform chrome is not where brand differentiation pays off.

## Decision checklist

1. Which OS features are must-haves at launch (widgets, Live Activities, Wallet, HealthKit, CarPlay, Wear OS)? Each one tilts toward native or a framework with mature bridges.
2. What does the team already know, and who maintains the app after launch?
3. How custom is the UI? Mostly standard components favors native or React Native; heavily custom brand rendering favors Flutter.
4. Performance-critical areas (camera, AR, real-time audio, large lists)? Prototype them in the candidate stack before committing.
5. Accessibility parity: test VoiceOver and TalkBack on a prototype; drawn-pixel frameworks need explicit semantics work.
6. Share the design system through tokens, not shared component code: one DTCG source compiled to Swift, Kotlin, CSS and framework themes. See the `design-system` skill and [SwiftUI and Compose handoff](handoff-swiftui-compose.md).

## Common failures

- One design file with iOS chrome reused for Android: rebuild the chrome per platform, share content components.
- Custom JS or Flutter tab bars that ignore safe areas, glass and minimize-on-scroll: use native navigation containers.
- Shadows and blur tuned on iOS that render as muddy gray boxes on Android: use tonal elevation on Android.
- Gesture conflicts: horizontal carousels near the iOS left edge or Android back-gesture edges. Keep 16-24pt/dp from edges or offer arrows.
- Web-style hover states and tooltips as the only affordance on touch.
