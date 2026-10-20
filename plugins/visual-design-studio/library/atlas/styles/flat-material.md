---
id: style.flat-material
axis: style
name: Flat / Material
aliases: [flat design, material design, material 3, material you, material expressive, google material, android design language]
summary: Color-field, ornament-free flat design plus Google's Material system with tonal color, state layers, tiered elevation and spring motion; a predictable, highly implementable look for apps and tools.
tags: [flat, material, material-3, android, tonal, elevation, ui-kit, buttons, google, systematic]
pairs_with: [channel.native-app, channel.web-app, industry.saas-b2b, industry.marketplaces-platforms, audience.low-bandwidth-entry-devices, market.india-south-asia, market.southeast-asia, market.sub-saharan-africa, tier.value, archetype.everyperson]
avoid_with: [tier.ultra-luxury, tier.luxury, archetype.lover, industry.luxury-goods, industry.fashion-apparel]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Flat / Material

## Essence

Remove ornament, keep meaning. Flat design (Windows Phone Metro in 2010, Apple's iOS 7 in 2013) swapped textures and bevels for color fields, type and layout. Material Design (Google, 2014) added a physics model: surfaces, elevation, and motion that explains cause and effect. Material 3 (2021, "Material You") replaced fixed palettes with tonal color generated from a seed and adaptive layouts; Material 3 Expressive (announced 2025) pushes bolder shapes, color and spring-based motion. The value is predictability: engineers, users and tools all know how the parts behave.

## Visual signature

- Solid color fields; no gradients, textures or skeuomorphic shading. Depth comes from tone, not shadow (M3 uses tonal surface colors and sparing elevation).
- A tonal palette from one seed: primary, secondary, tertiary, neutral, neutral-variant and error, each with light and dark roles and "container" tints.
- Rounded rectangles from a defined shape scale; pill buttons and segmented controls.
- Large, clear type with a defined scale, and a variable icon set (Material Symbols).
- Floating action buttons, bottom navigation or navigation rails, top app bars that collapse on scroll, sheets, snackbars.
- Interaction states drawn as translucent "state layers" over components.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Roboto Flex (OFL, many axes); Google Sans Flex (OFL on Google Fonts, verify platform use); commercial: Circular, Graphik |
| Body font | Roboto (OFL) or Roboto Flex; Noto Sans / Noto Sans families for multiscript coverage |
| Mono | Roboto Mono (OFL) |
| Type scale ratio | M3 fixed scale in sp: Display 57/64, 45/52, 36/44; Headline 32/40, 28/36, 24/32; Title 22/28, 16/24, 14/20; Body 16/24, 14/20, 12/16; Label 14/20, 12/16, 11/16 |
| Body size / line-height | Body large 16sp / 24sp (tracking +0.5sp); body medium 14sp / 20sp; web 16px / 1.5; measure 60-75ch |
| Display letter-spacing | 0 at display sizes; M3 adds positive tracking only to small text (body 0.25-0.5sp, labels 0.1-0.5sp) |
| Caps / labels | Sentence case labels 11-14sp, weight 500, tracking +0.1sp; avoid all caps (older Material buttons used caps) |
| Weights | 400 body, 500 labels/titles/buttons, 700 only for emphasis |
| Palette | Primary #9B4500 (oklch 0.49 0.133 49); Primary container #FFDBC8 (oklch 0.92 0.048 50); Secondary #765848 (oklch 0.49 0.047 49); Tertiary #5F6219 (oklch 0.48 0.093 112); Surface #FFF8F5 (oklch 0.98 0.009 45); On-surface #201A17 (oklch 0.22 0.011 48); Outline #85736B (oklch 0.57 0.026 45); Error #BA1A1A (oklch 0.51 0.193 28) |
| Palette method | Pick a brand seed, generate tones with Material Color Utilities (HCT): primary at tone 40 light / 80 dark, container at 90 / 30, on-colors at 100 / 20 |
| Accent proportion | Primary 8-12% (filled buttons, FAB, active indicators); tertiary only for a contrasting accent; surfaces carry the rest |
| Radius | M3 shape scale: none 0, extra-small 4dp, small 8dp, medium 12dp, large 16dp, extra-large 28dp, full; buttons full, cards 12dp, sheets/dialogs 28dp |
| Borders | Outlined components use 1dp outline #85736B (4.29:1 on surface); dividers use outline-variant #D8C2B9, decorative only |
| Shadow / elevation | Levels 0-5 = 0, 1, 3, 6, 8, 12dp; prefer tonal elevation (surface tint steps) and use shadow for floating elements only |
| Spacing density | 4dp base; component padding 16dp; layout margins 16dp compact, 24dp medium and larger; touch target 48dp |
| Grid | Window size classes: compact under 600dp (4 columns), medium 600-839 (8), expanded 840-1199 (12), large 1200+ (12) with max content width about 1240dp; verify current breakpoints |
| Motion | M3 durations short 50-200ms, medium 250-400ms, long 450-600ms; easing standard cubic-bezier(0.2, 0, 0, 1), emphasized decelerate cubic-bezier(0.05, 0.7, 0.1, 1); Expressive adds spring specs (damping ratio and stiffness) |

## Composition and layout

- Pick the navigation pattern by window class: bottom navigation bar (compact), navigation rail (medium), permanent drawer or rail plus list-detail (expanded and larger). Move content, not just scale it.
- Use canonical layouts: list-detail, supporting pane, feed. They are the shortest path to adaptive behavior on foldables and tablets.
- Establish hierarchy with tone and size: a filled button for the one primary action, tonal for secondary, outlined for tertiary, text for low emphasis.
- Group with surface containers (tone steps) and 16-24dp whitespace instead of borders and shadows.
- On the web, apply the same system through tokens (CSS variables, Material Web or MUI); do not mimic Android chrome on desktop.

## Imagery and iconography

- Icons: Material Symbols (variable font, Apache 2.0) at 24dp with FILL, wght 400 and optical size axes; use filled for the active state and outlined for inactive.
- Illustration: flat geometric, limited to the tonal palette plus two accents; characters rendered with simple shapes and no outlines.
- Photography: full-bleed, cropped to the shape scale (12-28dp); apply a scrim of 30-40% black only behind overlaid text.
- Avoid skeuomorphic or gradient 3D icons; they break the system's tonal logic.

## Motion

Material motion explains hierarchy: container transforms connect a card to its detail view, shared axis transitions show sibling movement, fade-through marks unrelated destinations. Use 200-300ms for small elements, 300-450ms for full-screen changes, standard easing for most movement, and emphasized easing for hero moments. Material 3 Expressive introduces spring-based motion so elements settle naturally and shapes morph (for example a selected button changing corner radius); verify the exact spring parameters in the current Material 3 spec before implementing. With reduced motion, replace transforms with 100-150ms fades.

## Fits and risks

- **Fits:** Android and cross-platform apps, admin consoles, marketplaces, utilities, education, anything shipped quickly by many engineers. Strong in India, Southeast Asia and Africa where Android and entry-level devices dominate (`audience.low-bandwidth-entry-devices`), and for `tier.value` brands that need clarity over polish.
- **Risks:** it reads as "Google" and can look generic; default M3 baseline purple is the most common outcome. Flat design without signifiers makes buttons look like labels (a long-documented usability criticism). Expressive styling can feel childish in conservative sectors.
- **Wrong for:** luxury, fashion and romance-led brands, where ornament, serif type and texture carry the promise.

## Do and don't

- Do seed color from the brand, not the default purple, and keep neutrals slightly tinted toward the seed hue (here hue 45-50).
- Do make state visible: hover 8%, focus 10%, pressed 10%, dragged 16% state layers, plus a 3dp focus ring.
- Do keep one filled button per view and use button hierarchy rather than extra colors.
- Don't mix Material components with iOS-style controls on the same platform surface without reason.
- Don't remove outlines on inputs for the sake of flatness; boxed or underlined fields need visible boundaries.
- Don't use elevation and tonal tint together on large surfaces; choose one depth cue.

## Clichés and AI tells

- Lazy version: MUI or M3 defaults with the baseline purple (#6750A4-like), Roboto everywhere, 4dp-radius cards with shadows, centered "Get started" hero, a floating action button on a landing page, and rounded avatar circles in every list row.
- Fix: derive a custom seed palette (here burnt orange, olive tertiary), use tonal surface containers instead of shadows, use the shape scale intentionally (28dp sheets, full pills, 12dp cards), set a distinctive display face such as Roboto Flex with width or grade axes, and write interaction states into tokens before building components.

## Accessibility notes

- White on primary #9B4500 is 6.47:1; primary on its container #FFDBC8 is 5.00:1; on-surface #201A17 on #FFF8F5 is 16.37:1; secondary #765848 is 6.13:1, tertiary #5F6219 is 6.16:1 and error #BA1A1A is 6.15:1 on the surface.
- Outline #85736B is 4.29:1 against the surface, which clears the 3:1 boundary rule for fields; outline-variant #D8C2B9 is 1.62:1 and may only separate decoration.
- Tonal pairing helps: in HCT, a tone difference of about 50 targets 4.5:1 and about 40 targets 3:1 (verify by measuring, not by assuming).
- Targets: 48dp minimum with 8dp spacing; support system font scale to 200% without clipping by sizing text in sp (Android) or rem (web).
- Never rely on color alone for state; pair icons and labels, especially for error and success.

## Reference anchors

- Material Design 3 (m3.material.io) and Material Symbols
- Material 3 Expressive research and updates announced at Google I/O 2025
- Material Color Utilities and the HCT color space
- Microsoft Metro (Windows Phone 7, 2010) as an origin of flat design
- Apple iOS 7 (2013) redesign by Jony Ive's team
- Nielsen Norman Group on flat design and weak signifiers
