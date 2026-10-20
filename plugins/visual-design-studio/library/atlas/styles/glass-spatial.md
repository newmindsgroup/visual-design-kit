---
id: style.glass-spatial
axis: style
name: Glass and Spatial UI
aliases: [glassmorphism, liquid glass, visionos glass, frosted glass, spatial ui, translucent ui, vibrancy, apple glass]
summary: Translucent, layered interfaces from glassmorphism to visionOS glass and Apple's 2025 Liquid Glass; blur, light and depth build hierarchy, but legibility rules decide whether it works.
tags: [glass, translucent, blur, liquid-glass, visionos, spatial, depth, apple, vibrancy, frosted]
pairs_with: [channel.native-app, industry.ai-products, industry.automotive-mobility, industry.digital-health-wellness, industry.media-entertainment-streaming, archetype.magician, tier.premium, channel.video-motion]
avoid_with: [audience.low-bandwidth-entry-devices, audience.older-adults, audience.disability-accessibility-first, industry.government-civic, channel.print-collateral, channel.email]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Glass and Spatial UI

## Essence

Make controls feel like physical, light-bending material floating above content. Three generations share the idea: Windows Aero and early "glassmorphism" (2020 web trend), visionOS (2023) where windows are real glass in the user's room, and Liquid Glass (announced at Apple's WWDC25, June 9, 2025) which brought a dynamic, refracting material to iOS 26, iPadOS 26, macOS Tahoe 26, watchOS, tvOS and visionOS. The material belongs to the control layer (navigation, toolbars, sheets, floating buttons), never to the content itself. Used there, it keeps context visible and feels premium; used everywhere, it destroys contrast.

## Visual signature

- A rich, moving or photographic background (wallpaper, album art, map, video) seen through translucent panels with blur 20-40px and a saturation lift of 1.4-1.8.
- Edges that catch light: a 1px inner border at 16-24% white, a brighter top edge, and a soft long shadow beneath.
- Large concentric corner radii and capsule shapes; inner radius equals outer radius minus padding.
- Floating chrome inset from the screen edges; content runs under bars and shows through them.
- Vibrant text: white (or near-black on light glass) in three emphasis levels, never colored text on glass.
- Controls that morph and merge as they move (Liquid Glass), and depth cues such as parallax, lift on hover, specular highlights.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | SF Pro Display / SF Pro Rounded (Apple platforms; license limits use to Apple-platform software, verify); web stand-ins: Instrument Sans (OFL), Albert Sans (OFL); commercial: Aeonik, Neue Montreal |
| Body font | SF Pro Text via `font-family: -apple-system, system-ui`; OFL stand-in: Instrument Sans at weight 500 |
| Mono | SF Mono (Apple platforms) or DM Mono (OFL) |
| Type scale ratio | Apple Dynamic Type steps (body 17pt, title 28pt, large title 34pt); on web 1.250 with body 16-17px |
| Body size / line-height | 17px / 1.4-1.5; glass body copy at weight 500 because thin type dissolves into the backdrop (visionOS also uses heavier weights) |
| Display letter-spacing | -0.02em at 28px+; default tracking below; line-height 1.1-1.2 |
| Caps / labels | Avoid all caps; use 13px weight 600 sentence case secondary labels |
| Weights | 500 body on glass, 600 labels and buttons, 700 large titles |
| Palette | Scene deep #17203A (oklch 0.25 0.051 268); Scene bloom #4B6BFB (oklch 0.59 0.217 269); Scene warm #F2A65A (oklch 0.78 0.129 64); Glass tint #11162A (oklch 0.21 0.041 272); Light-glass ink #101828 (oklch 0.21 0.034 263); System blue light #007AFF (oklch 0.60 0.218 257); System blue dark #0A84FF (oklch 0.62 0.206 255); White labels #FFFFFF |
| Dark glass recipe | `background: rgb(17 22 42 / 0.60); backdrop-filter: blur(24px) saturate(1.5); border: 1px solid rgb(255 255 255 / 0.18)`; white text |
| Light glass recipe | `background: rgb(255 255 255 / 0.72); backdrop-filter: blur(24px) saturate(1.6); border: 1px solid rgb(255 255 255 / 0.6)`; text #101828 |
| Radius | Cards and sheets 24-32px; controls 12-16px; buttons capsule (9999px); keep concentric: inner = outer - padding |
| Borders | 1px translucent white (16-24%) plus 1px top highlight `inset 0 1px 0 rgb(255 255 255 / 0.25)` |
| Shadow / elevation | `0 16px 48px rgb(0 0 0 / 0.25)` plus a contact shadow `0 2px 6px rgb(0 0 0 / 0.15)`; elevation = more blur, not more opacity |
| Spacing density | 8px base; panel padding 16-24px; touch targets 44pt on iOS, at least 60pt on visionOS (verify against the current HIG) |
| Grid | Content-first; floating bars inset 8-16px; sidebars 240-320px; do not build a visible grid |
| Motion | Springs: response 0.35-0.5s, damping ratio 0.8-0.9; web equivalent 280-420ms cubic-bezier(0.2, 0.8, 0.2, 1); shapes morph rather than cut |

## Composition and layout

- Put content on the base layer and glass only on the layer that controls it. Never place glass on glass; separate groups with spacing and a single shared container instead.
- Let content scroll under the toolbar and use a scroll-edge treatment: a soft blur fade for general screens and a harder edge where headers must stay legible. Apple names both effects in its Liquid Glass guidance.
- Establish hierarchy with layout, grouping and size, not with tinted glass backgrounds. Reserve color tint for the one primary action.
- On visionOS, keep windows glass (opaque windows feel heavy), place sidebars on a darker material than content, and avoid stacking light materials on light materials.
- Design the backdrop. Specify what can sit behind each glass element (image library, user wallpaper, map) and test the extremes: pure white, pure black, a saturated mid-tone, and a busy photo.

## Imagery and iconography

- Backgrounds: soft mesh or photographic scenes with controlled luminance; add a baked-in 20-35% dark gradient behind areas where white glass text sits.
- Icons: SF Symbols on Apple platforms (weights matched to text); on web use 1.75-2px outline icons at weight matching the label, white on dark glass.
- 3D/spatial: objects with soft contact shadows and depth, rendered with consistent light from above-left; keep text 2D, because 3D text is harder to read (visionOS guidance).
- Avoid emoji and multicolor icons on glass; they lose separation from the backdrop.

## Motion

Material that responds: glass lifts and brightens on press, merges with neighboring glass shapes when they approach, and settles with a damped spring (response 0.35-0.5s). On web, approximate with 280-420ms eased transitions on transform, opacity and backdrop saturation. Keep `backdrop-filter` animation to small areas (it is GPU-expensive) and never animate blur radius on full-screen layers. Under Reduce Motion, replace parallax and morphing with cross-fades. Apple's materials also respond to Reduce Transparency and Increase Contrast by becoming more opaque; implement the same.

## Fits and risks

- **Fits:** native iOS, iPadOS, macOS and visionOS apps that want to feel current with the platform, media and music players, maps, camera and photo tools, smart-home and car dashboards, premium wellness and AI assistants where ambient atmosphere matters (`tier.premium`, `archetype.magician`).
- **Risks:** legibility. Blur does not change average backdrop luminance, so contrast is decided by the brightest and darkest content that can sit behind the panel. Public criticism of Liquid Glass centered on notifications and text over busy backgrounds; Apple responded in iOS 26.1 with a Clear/Tinted setting under Settings > Display & Brightness > Liquid Glass (Tinted raises opacity and contrast).
- **Also costly:** `backdrop-filter` drains low-end GPUs and batteries; web recreation of refraction (SVG displacement filters inside `backdrop-filter`) is reported to work mainly in Chromium, with plain frosted fallbacks elsewhere (verify against caniuse before shipping).
- **Wrong for:** accessibility-first, older-adult, low-bandwidth, government and print/email contexts. Use `style.civic-plain` or `style.clinical-calm` instead.

## Do and don't

- Do use glass for navigation, toolbars, floating actions, sheets and media overlays; keep reading surfaces opaque or at 85%+ opacity.
- Do follow platform components first on Apple platforms (SwiftUI `glassEffect`, standard bars and sheets) and customize second; the system adapts to appearance and accessibility settings for you.
- Do tint sparingly: one tinted primary control per view.
- Do ship fallbacks: `@supports not (backdrop-filter: blur(1px))` gets a solid fill; `prefers-reduced-transparency: reduce` and `prefers-contrast: more` (check browser support) get opaque surfaces and stronger borders.
- Don't layer glass on glass, put long paragraphs on glass over photos, or blur whole pages.
- Don't use hairline-thin type or light gray labels on glass; use weight 500+ and white or near-black only.
- Don't copy Apple's artwork, wallpapers or SF Symbols into non-Apple products.

## Clichés and AI tells

- Lazy version: every card is `backdrop-filter: blur(10px)` with `rgba(255,255,255,0.1)` on a purple-pink gradient blob background, white 400-weight text, 16px radius, and a glow border. It is the 2021 "glassmorphism" template and fails on any bright region.
- Fix: choose the backdrop first, specify a minimum tint per panel (dark glass at 60% or more, light glass at 72% or more), set text at weight 500+, use concentric radii, add a solid fallback, limit glass to the control layer, and test the panel over white, black and the worst photo in the product.

## Accessibility notes

- White on scene-bloom blue #4B6BFB is 4.38:1, white on warm #F2A65A is 2.02:1 and white on pale #EAF0FA is 1.14:1: a clear white label on untinted glass fails on mid-tone and bright backdrops.
- Dark glass: #11162A at 60% over pure white composites to #70737F, giving white text 4.72:1. At 55% it is #7C7F8A and only 3.99:1. Use 60% or more wherever the backdrop can be white.
- A 35% black scrim over warm #F2A65A gives #9D6C3B, white text 4.52:1; 55% gives 7.81:1. This matches the common advice to dim bright media behind clear glass (Apple's exact dimming figure: verify in the current HIG).
- Light glass at 72% white over a black backdrop composites to #B8B8B8; ink #101828 on it is 8.95:1. System blue #007AFF is only 4.02:1 on white (large text and icons only); use a darker link blue on light glass.
- Support Reduce Transparency, Increase Contrast, Reduce Motion and Dynamic Type; keep targets at 44x44 CSS px (60pt on visionOS). Never encode state by tint alone.

## Reference anchors

- Apple Human Interface Guidelines: Materials, and the visionOS and Liquid Glass sections (developer.apple.com/design)
- WWDC25 session "Meet Liquid Glass" (session 219) and the September 2025 HIG materials update on semantic use, legibility and avoiding glass layers
- WWDC23 session "Design for spatial user interfaces" (visionOS glass, vibrancy levels, 60pt targets)
- Microsoft Fluent acrylic and Windows Aero as earlier translucent systems
- Michal Malewicz's 2020 glassmorphism articles as the web-trend origin
- Verified in this entry: WWDC25 announcement, regular and clear variants, accessibility adaptations, iOS 26.1 Clear/Tinted setting. Unverified: exact blur radii, tint opacities and system color values in iOS 26, which Apple does not publish.
