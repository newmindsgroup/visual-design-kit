---
name: native-app-design
description: >-
  Design macOS, iOS, iPadOS and Android interfaces: native windows and surfaces, navigation, keyboard and pointer,
  accessibility, appearance modes, platform tokens, app icons and SwiftUI/Compose handoff. Use for native app
  screens, flows, store assets, Mac utilities or cross-platform choices. Mac implementation uses the optional
  BAMA workflow; preserve existing project OS targets and approved brand tokens.
license: MIT
metadata:
  version-timestamp: "2026-10-27 07:43:23 AST"
  agent-attribution: "computer=NMG-MBP-M5; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 07:43:23 AST"
---

# Native app design

Excellent app design feels like it belongs on the device: system navigation, type, gestures and accessibility behave exactly as people expect, and the brand shows up in content, color, imagery and motion rather than in re-skinned system chrome. Platform specs below were checked against Apple and Android sources on 2026-10-20; confirm against the current HIG and Material docs before production.

## Defaults

| Decision | iOS / iPadOS | Android | Change when |
| --- | --- | --- | --- |
| Touch target | 44x44pt hit region; 28x28pt only for dense secondary controls | 48x48dp, 8dp apart | Older adults, motor impairment, in-vehicle or gloved use: 56-64pt/dp |
| Body text | Body 17pt (Dynamic Type default); minimum 11pt | Body Large 16sp/24sp; minimum 11sp | Never fixed sizes; test AX5 and 200% font scale |
| Side margins | 16pt compact, 20pt wider and regular width (system margins) | 16dp compact, 24dp medium and up | Edge-to-edge media and maps |
| Primary navigation | Tab bar, 3-5 tabs, Liquid Glass; sidebar-adaptable on iPad | Navigation bar (compact), rail (medium+), expanded rail (large+) | Single-task apps (camera, player, scanner) need no tab bar |
| Layout switch | Size classes, never device or orientation | Window size classes: 600, 840, 1200, 1600dp | Never "isTablet" logic |
| Brand color | In the content layer and one accent tint; bars stay system glass | Fixed brand scheme generated from a seed; dynamic color optional | Utility apps: support dynamic color by default |
| Type family | SF Pro via text styles; custom fonts scaled with `relativeTo` | Roboto or brand font mapped to the 15 M3 roles | Editorial or luxury tiers: brand display face in content only |
| Icons | SF Symbols, weight matched to text | Material Symbols, 24dp, filled for selected state | Custom set drawn on the platform template |
| Modals | Sheets with medium and large detents, one at a time | Bottom sheets; full-screen dialog for complex input on compact | Destructive confirm: alert or dialog |
| Back | Back chevron plus left-edge swipe, never blocked | System back with predictive back (default at API 36) | Only intercept to protect unsaved work |
| Edges | Respect safe areas; extend backgrounds under bars | Edge-to-edge (mandatory at API 36); pad with insets | |
| Contrast | 4.5:1 text, 3:1 UI, checked over the worst content under glass | 4.5:1 and 3:1 in standard, medium and high-contrast schemes | High-contrast mode targets 7:1 body text |
| Motion | System transitions and springs; honor Reduce Motion | M3 springs (standard for utility, expressive for hero); honor remove animations | |

## Workflow

1. **Choose the platform route.** For macOS, read [macOS](references/macos.md) first and use desktop window, menu and keyboard conventions; the mobile defaults below do not apply. Preserve an existing minimum OS.
2. **Pin the targets.** OS versions (iOS 26+ and Android 16 / API 36 are the baselines in late 2026), devices (iPhone, iPad, iPhone Duo, Android phones, foldables, tablets), and stack. If cross-platform, choose with [cross-platform](references/cross-platform.md) first.
3. **Read the context.** Run `python3 ../../library/scripts/atlas.py query "native app <industry> <audience> <market>"` and read the `channel.native-app`, industry, audience and market entries it returns. Market decides the iOS/Android split and device classes; audience decides target and text sizes.
4. **Structure per platform.** Define 3-5 top-level destinations, stacks and modals for each platform with the `ux-design` skill's flows. Write the iOS and Android navigation maps separately even when the content is shared.
5. **Lay out compact first, then every width.** Phone portrait, phone landscape, iPad and foldable inner screen, split views. Use [large screens](references/large-screens.md) for panes and pointer/keyboard.
6. **Apply platform specifics.** [iOS HIG](references/ios-hig.md) for bars, sheets, Dynamic Type, materials, haptics; [Android Material 3](references/android-material3.md) for components, type roles, color roles, shape and motion.
7. **Map tokens.** Express every color, type, space and radius as a kit semantic token, then map to platform roles with [SwiftUI and Compose handoff](references/handoff-swiftui-compose.md). No raw hex in screen specs.
8. **Design the hard states.** Empty, loading, offline, error, permission denied, paywall, account deletion, first run. Use [app patterns](references/app-patterns.md).
9. **Render and inspect.** Build frames at real sizes (402x874pt and 440x956pt iPhone, 375x667pt small iPhone, 412x915dp and 360x800dp Android phones, 1024pt-wide iPad, foldable inner screen) in light, dark, high contrast, largest text, RTL and one translated locale. Screenshot and critique them with the `design-critique` skill before anyone sees them.
10. **Ship the store presence.** Icons and screenshots per [app store assets](references/app-store-assets.md).
11. **Hand off.** Specs name tokens, text roles, components and states per platform, with prototype links and the evidence of step 8.

## Decisions that change the answer

- **Market**: Android dominates devices in India, Brazil, Indonesia and much of Africa and Southeast Asia; iOS is strong in the US, Japan, UK and Australia. Check current share data for the specific market and design Android-first where it leads, including 360dp-wide budget phones.
- **Audience**: older adults and accessibility-first audiences need 56pt/dp targets, Body at xLarge as the design baseline and fewer tabs; expert power users get density, keyboard shortcuts and iPad multi-window; low-bandwidth audiences need offline-first states and small downloads.
- **Industry and regulation**: fintech and health need biometric re-auth, confirmation screens, privacy-safe notifications and widgets, and careful dynamic-color decisions where color carries meaning. Kids apps fall under COPPA (US) and the stores' kids programs: Apple's Kids Category bars links out, purchases and other distractions except behind a parental gate and restricts third-party analytics and ads (App Review 1.3); confirm with counsel.
- **Price tier and archetype**: premium and luxury apps show restraint in chrome and spend craft on content typography and imagery; playful archetypes can use M3 Expressive shapes and springs, but navigation stays standard.
- **Stack**: native gets new platform features first; React Native with Expo UI renders real native components; Flutter and Compose Multiplatform draw their own, so glass and Expressive effects may be approximations.

## Common failures

- iOS chrome shipped on Android (bottom tabs with iOS chevrons, SF Symbols, iOS switches): rebuild chrome with M3 components and Material Symbols; share only content components.
- Opaque brand-colored tab and navigation bars fighting Liquid Glass: let bars be system glass, move brand color into content, tint only the primary action.
- Glass in the content layer (frosted cards, glass buttons everywhere): use solid surfaces or standard materials.
- Text truncating at large sizes: stack horizontally adjacent items at accessibility sizes; allow multi-line labels.
- Hamburger menu as the primary navigation on phones: use a tab bar or navigation bar.
- Gesture-only actions, blocked edge swipe or intercepted Android back: add visible controls, use predictive back APIs.
- Permission prompts at launch: ask in context with a single-button pre-alert where justified.
- Hardcoded system color hex values (Apple changed them in 2025): use semantic colors.
- SF Pro used on Android or the web: license and platform mismatch; use Roboto or the brand font.
- Store screenshots that are posters with no UI, or iPhone frames on Google Play.

## References

- [macOS](references/macos.md): windows, inspectors, menus, pointer and keyboard, native state validation and toolchain prerequisites. Use the optional `bama-router` workflow for full native Mac implementation.
- [iOS HIG](references/ios-hig.md): safe areas, size classes, bars, sheets, Dynamic Type table, SF Symbols, color, Liquid Glass, haptics, app icon, widgets and Live Activities.
- [Android Material 3](references/android-material3.md): 48dp targets, window size classes, navigation, app bars, FAB, type scale, dynamic color, shape, elevation, motion, edge-to-edge, predictive back, adaptive icons.
- [Cross-platform](references/cross-platform.md): React Native and Expo, Flutter, Compose Multiplatform, and what must stay native.
- [Large screens](references/large-screens.md): iPad, foldables, iPhone Duo, list-detail, sidebars, pointer and keyboard.
- [App patterns](references/app-patterns.md): onboarding, permission priming, notifications, offline states, paywalls, account deletion, rating prompts, gestures.
- [SwiftUI and Compose handoff](references/handoff-swiftui-compose.md): token-to-theme mapping, Dynamic Type with custom fonts, dark and high contrast.
- [App store assets](references/app-store-assets.md): screenshot, preview, icon and listing specs as of 2026.
- Atlas: `python3 ../../library/scripts/atlas.py query "..."` when industry, market, audience or tier matters; `python3 ../../library/scripts/atlas.py show channel.native-app` for the channel entry.
- Tokens and theming: the [design-system skill](../design-system/SKILL.md).
- Deep process (client projects): [UI system](../../library/draft-skills/design-ui-system/SKILL.md) and its [system portability](../../library/draft-skills/design-ui-system/references/system-portability.md); [Figma production](../../library/draft-skills/design-production-interface/references/figma.md); the [dialog spec's native-sheet boundary](../../library/examples/component-specs/dialog.md); touch methods for [interaction patterns](../../library/draft-skills/design-touch-interaction-patterns/SKILL.md), [forms](../../library/draft-skills/design-touch-forms/SKILL.md), [offline](../../library/draft-skills/design-touch-offline/SKILL.md), [states and copy](../../library/draft-skills/design-touch-states-copy/SKILL.md), [device validation](../../library/draft-skills/design-touch-device-validation/SKILL.md) and [usability testing](../../library/draft-skills/design-touch-usability-testing/SKILL.md).

Catalog IDs covered: macos-app, ui, touch-interaction-patterns, touch-forms, touch-offline, touch-states-copy, touch-device-validation, touch-usability-testing
