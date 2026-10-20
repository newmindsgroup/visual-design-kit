---
id: channel.native-app
axis: channel
name: Native Mobile App
aliases: [mobile app, ios app, android app, iphone app, app store app, tablet app, cross-platform app]
summary: iOS and Android apps designed to platform conventions, thumb reach, safe areas, gestures and store requirements; judged by speed, clarity and how native they feel.
tags: [ios, android, mobile, app store, hig, material 3, gestures, safe area, swiftui, compose]
pairs_with: [style.flat-material, style.glass-spatial, style.soft-ui-neumorphic, industry.fintech-banking, industry.digital-health-wellness, industry.sports-fitness, industry.marketplaces-platforms, audience.teens-gen-z, audience.older-adults, archetype.everyperson]
avoid_with: [style.web-brutalist, audience.low-bandwidth-entry-devices]
version_timestamp: 2026-10-20 02:01:01 UTC
---

# Native Mobile App

## Formats and specs

Platform specs change with each OS and device cycle. Values below are as of 2026; confirm against Apple's Human Interface Guidelines and App Store Connect Help ("Screenshot specifications"), and Android's Material Design 3 and Google Play Console Help before production.

| Item | iOS | Android |
| --- | --- | --- |
| Layout unit | Points (pt); @2x and @3x | Density-independent pixels (dp) |
| Common screen sizes | iPhone 15 and 16 393x852 pt; iPhone 16 Pro, 17 and 17 Pro 402x874 pt; Pro Max models 440x956 pt; iPhone Air about 420x912 pt (verify per model); older small phones 375x667 pt | Compact under 600dp wide, medium 600-839dp, expanded 840dp and up (window size classes) |
| Safe areas | Respect system insets: Dynamic Island / status bar about 54-62pt top, home indicator 34pt bottom (read from the system, never hard-code) | Edge-to-edge is the default for recent targets; use window insets for status, navigation and cutouts |
| Touch target | 44x44pt minimum | 48x48dp minimum, 8dp spacing between targets |
| Bars | Navigation bar 44pt (large title about 96pt); tab bar 49pt plus safe area; 3-5 tabs | Top app bar 64dp; navigation bar 80dp in the M3 baseline and 64dp for the M3 Expressive flexible navigation bar (3-5 destinations); navigation rail for medium and expanded widths |
| Type | SF Pro, Dynamic Type from xSmall to AX5; body 17pt default; avoid under 11pt | Roboto or Roboto Flex; Material 3 type scale, body 14-16sp; scale with font size setting |
| App icon | 1024x1024 PNG, sRGB or Display P3, no transparency, square corners (the system applies the mask); iOS 26 icons can be layered (Icon Composer) with default, dark, clear and tinted appearances | Adaptive icon: 108x108dp canvas, keep the mark inside the 66dp-diameter center; separate foreground and background layers; optional monochrome layer for themed icons; Play listing icon 512x512 PNG, 1 MB or less |
| Store screenshots (as of 2026) | Recommended master 6.9 inch iPhone: 1320x2868 (also accepted 1290x2796 and 1260x2736); sources conflict on whether the required set is now the 6.9 inch or the 6.3 inch display (1206x2622 or 1179x2556), so check App Store Connect; 6.5 inch: 1284x2778 or 1242x2688; iPhone Duo outer 1398x2034 and inner 2007x2853 (verify); iPad 13 inch: 2064x2752 or 2048x2732; PNG or JPEG, 1-10 per localization | Phone: JPEG or 24-bit PNG without alpha, 320-3840 px per side, longer side no more than 2x the shorter, 2-8 per device type; feature graphic 1024x500 |
| Preview video | App Preview up to 30s, device-resolution capture | Promo video via YouTube link |
| Color | Display P3 on supported devices (asset catalog), sRGB fallback | sRGB baseline; dynamic color (Material You) from the wallpaper on Android 12+ |

## Structure and hierarchy

- **Navigation:** tab bar or navigation bar for 3-5 top-level destinations; push navigation for drill-down; sheets for focused tasks; avoid hamburger menus for primary destinations. Back is a swipe on iOS and system back on Android; never block it.
- **Thumb zone:** put frequent actions in the lower half; keep destructive actions away from the thumb arc; use bottom sheets and large primary buttons (48-56pt high, full width with 16-20pt margins).
- **First-run:** show value before asking for permissions. Ask for notifications, location, camera or tracking in context, after a pre-prompt explaining why. Account creation after the first success when possible.
- **Screen anatomy:** title, primary content, one primary action; lists use 56-72pt rows with leading icon or image, two text lines and trailing affordance.
- **Tablets and foldables:** adapt with split views, sidebars and multi-column layouts instead of stretched phone UI; support rotation and window resizing.
- **State coverage:** offline, slow network, permission denied, empty, error, loading skeletons, and interrupted flows (calls, backgrounding).

### Pattern equivalents

| Pattern | iOS | Android |
| --- | --- | --- |
| Primary navigation | Tab bar (3-5 items), labels always visible | Navigation bar (3-5), rail on wider windows |
| Back | Edge swipe and back button in the navigation bar | System back and predictive back gesture |
| Focused task | Sheet with medium and large detents | Modal bottom sheet or full-screen dialog |
| Refresh | Pull to refresh on scrollable lists | Pull to refresh (Material indicator) |
| Search | Search field in the navigation bar or Search tab | Search bar with suggestions |
| Sharing | Share sheet | Sharesheet |
| Dates and pickers | Wheel, compact or inline date picker | Material date and time pickers |
| Destructive confirm | Action sheet with red destructive action | Dialog with explicit verb labels |
| Settings | Grouped inset lists; deep link to system Settings for permissions | Preference screens; link to system settings |

## Craft defaults

- Use platform controls and patterns first (UIKit/SwiftUI, Jetpack Compose with Material 3). Custom components must still honor Dynamic Type, VoiceOver and TalkBack, haptics and dark mode.
- iOS 26 introduced the Liquid Glass design language, and Material 3 Expressive updates Android's components (both as of 2025-2026); confirm the current guidance and decide deliberately how much to adopt. Do not apply glass blur to every surface.
- Brand through color, typography, iconography, illustration, copy and motion inside the platform frame; do not clone iOS on Android or the reverse.
- Motion: 200-350ms transitions; use platform springs and easing (`cubic-bezier(0.2, 0, 0, 1)` as the web analogue); shared-element transitions for continuity; respect Reduce Motion and Remove animations settings.
- Haptics: light impact for selection, success and error patterns; never as the only feedback.
- Icons: SF Symbols on iOS; Material Symbols on Android; a custom set must match stroke weight (1.5-2pt) and optical sizes.

## Production and handoff

- Deliver Figma with iOS and Android frames, token variables, component states, safe areas annotated, and Dynamic Type at default and a larger size. The `native-app-design` skill holds the deeper platform guide, gestures, and SwiftUI/Compose handoff.
- Assets: vector PDF or SVG for icons (asset catalogs on iOS, vector drawables on Android); raster @2x/@3x or WebP; Lottie or Rive for animation.
- Store assets: localized screenshots with captions, icon, preview video, short description (Play: 80 chars), subtitle (App Store: 30 chars). Do not show UI that the app lacks.
- Policy: privacy nutrition labels (App Store) and Data safety form (Google Play); Sign in with Apple is required when offering third-party social login on iOS apps with exceptions (verify Guideline 4.8); in-app purchase rules apply to digital goods. Confirm review guidelines before launch.
- Children's apps: COPPA (US), GDPR-K and platform "Kids" and "Families" programs restrict tracking and ads. Confirm requirements with counsel.

## QA checklist

- [ ] Tested on a small phone (375pt), a large phone (440pt), a tablet and an Android compact device.
- [ ] Dynamic Type at largest accessibility size and Android font scale 200% without clipping.
- [ ] VoiceOver and TalkBack: labels, order, traits, custom actions for gestures.
- [ ] Safe areas, keyboard avoidance, landscape, split-screen, notches and cutouts.
- [ ] Dark mode, increased contrast, Reduce Motion, Reduce Transparency.
- [ ] Offline, airplane mode, permission-denied and low-battery paths.
- [ ] Touch targets 44pt / 48dp; no gesture is the only path to an action.
- [ ] Store screenshots match current build and device-size requirements.

## Reference anchors

- Apple Human Interface Guidelines (developer.apple.com/design/human-interface-guidelines)
- Material Design 3 (m3.material.io) and the Android design guidance on adaptive layouts
- Apple "Designing for iOS" WWDC sessions and Android Developers "Compose adaptive layouts" documentation
- Things 3 and Airbnb as widely cited craft benchmarks for interaction polish
- *Designing Interfaces* (Jenifer Tidwell) and *Mobile First* (Luke Wroblewski)
