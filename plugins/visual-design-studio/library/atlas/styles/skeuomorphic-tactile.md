---
id: style.skeuomorphic-tactile
axis: style
name: Skeuomorphic / Tactile
aliases: [skeuomorphism, skeuomorphic design, tactile ui, realistic ui, material realism, hardware ui, ios 6 style]
summary: Interfaces modeled on real materials and devices: leather, brass, felt, glass, knobs and switches, with consistent top lighting, bevels and texture so controls explain themselves by looking physical.
tags: [skeuomorphic, tactile, realistic, texture, leather, knobs, hardware, bevel, metaphor, audio]
pairs_with: [industry.media-entertainment-streaming, industry.gaming-esports, industry.food-beverage-cpg, audience.older-adults, audience.low-literacy-plain-language, archetype.creator, archetype.everyperson, channel.native-app, channel.packaging]
avoid_with: [industry.saas-b2b, industry.fintech-banking, audience.expert-power-users, audience.low-bandwidth-entry-devices, channel.email]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Skeuomorphic / Tactile

## Essence

Borrow the physics of real objects so people understand what to do without instructions: a knob turns, a switch flicks, a notepad has lines. Apple's iOS 6 and earlier (leather Calendar, felt Game Center, wooden iBooks shelf) made the style famous; iOS 7 (2013) flattened it. It never went away in audio plug-ins, camera and instrument apps, games, packaging and brands built on craft. Done with restraint it is the most self-explanatory interface style; done everywhere it is noisy and hard to maintain.

## Visual signature

- Real-material surfaces: leather, brushed metal, wood, felt, paper, enamel, glass, rubber. Each component class gets one material.
- A single top light source; highlights on top edges, shadows below, soft ambient occlusion in recesses.
- Bevels, inner shadows, stitching, screws, engraved or debossed labels, lens reflections.
- Controls that look like their real counterparts: rotary knobs with tick marks, toggle switches, faders, push buttons with a pressed depth.
- Warm, saturated, slightly muted palette that reads as dyed or machined material rather than screen color.
- Legible content sits on flat "plates" (paper, glass, LCD) inside the textured chrome.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Bitter (OFL slab); Special Elite (OFL typewriter) for labels and receipts; commercial: Clarendon, Trade Gothic Next Condensed |
| Body font | Libre Franklin (OFL); commercial: Helvetica Neue (the iOS 6 voice), Trade Gothic Next |
| Label / engraved font | Oswald (OFL) in caps for stamped metal plates; DSEG (OFL, 7-segment) for LCD readouts |
| Type scale ratio | 1.250 (major third); keep chrome labels at 12-14px and content at 16-18px |
| Body size / line-height | 16-17px / 1.5 on flat plates; measure 55-65ch |
| Display letter-spacing | 0 to +0.01em on slab; engraved caps +0.08em to +0.12em at 12-14px |
| Caps / labels | Condensed caps, 12-13px, +0.1em, with a 1px light text-shadow below to look debossed (`0 1px 0 rgb(255 255 255 / 0.35)`) |
| Weights | 400 body, 600-700 slab headings, 500 engraved labels |
| Palette | Leather #5B3A29 (oklch 0.38 0.054 48); Stitch cream #E8D8B0 (oklch 0.89 0.056 89); Brass #B8913F (oklch 0.68 0.11 83); Felt green #1F4D3A (oklch 0.38 0.061 164); Paper #F2E8D0 (oklch 0.93 0.034 88); Walnut #8A5A33 (oklch 0.51 0.083 58); Brushed steel #C9CDD2 (oklch 0.85 0.008 254); Ink #20150F (oklch 0.21 0.021 50) |
| Status color | Enamel red #A8261C (oklch 0.48 0.168 29) for record and alert lamps; add an icon |
| Accent proportion | Brass or red lamp under 10%: ring on a knob, toggle accent, record light |
| Radius | 6-10px on leather and metal panels; full circles on knobs and lamps; 2-4px on paper plates |
| Borders | Created by bevels, not outlines: `inset 0 1px 0 rgb(255 255 255 / 0.35), inset 0 -1px 0 rgb(0 0 0 / 0.35)`; stitching as a 1.5px dashed cream line inset 6px |
| Shadow / elevation | Layered and warm: `0 1px 1px rgb(43 26 16 / 0.4), 0 4px 8px rgb(43 26 16 / 0.3), 0 12px 24px rgb(43 26 16 / 0.2)`; pressed state swaps to inset |
| Spacing density | Cozy: 8px base, 16-24px panel padding, 56px minimum knob diameter, 48px minimum button height |
| Grid | Panel-based: 4 or 6 columns, controls aligned to a faceplate grid; screws and rails mark edges |
| Motion | 160-240ms presses; knob rotation 300-600ms with inertia; spring damping about 0.7 for switches; optional click sounds off by default |

## Composition and layout

- Compose like a physical product: a faceplate (leather, steel or wood), inset windows (LCD, paper, glass) and clustered controls with clear grouping by engraved rules.
- Put reading content on flat plates: 100% opaque paper (#F2E8D0) or LCD with a bezel. Never run paragraphs over leather or wood grain.
- Use real-world proportions: knobs 56-96px, sliders with a visible track and cap, toggles with 2:1 aspect ratio.
- One scene per screen: avoid mixing wood, leather, chrome and glass in the same viewport; pick a base material and one accent material.
- Align the light: shadows and highlights must agree on every surface, or the interface looks pasted together.

## Imagery and iconography

- Icons: embossed or debossed single-color glyphs, or small enamel-style badges; avoid glossy multicolor 3D icons.
- Textures: tileable textures of 256-512px at 4-10% overlay, optimized under 20-40KB each; generate with SVG `feTurbulence` or CSS gradients where possible to avoid heavy bitmaps.
- Photography and renders: product shots on matching materials; for packaging, real photographed or rendered textures at print resolution (300ppi).
- Avoid AI-rendered "photoreal" icon sets with inconsistent light; commission or build one coherent set.
- Build materials in CSS so they stay themeable: leather = `linear-gradient(180deg, rgb(255 255 255 / 0.08), rgb(0 0 0 / 0.14)), #5B3A29` plus a noise tile; brushed metal = `repeating-linear-gradient(90deg, rgb(255 255 255 / 0.10) 0 1px, transparent 1px 3px)` over #C9CDD2; felt = #1F4D3A with 6-8% noise.
- Dark variant: deepen the faceplate to walnut or black leather, lower highlights to about 15-20% white, and keep content plates paper-colored or LCD so reading contrast does not change.

## Motion

Mimic mass and friction. Knobs ease out over 300-600ms with slight inertia; switches flick in 160-200ms with a tiny overshoot (damping 0.7); buttons depress 1-2px and darken 6-10% in 80-120ms; pages can curl or slide with 400-700ms easing. Provide optional audio feedback with a visible mute. Keep animations purposeful: a spinning reel or tape counter should reflect real state. Under reduced motion, snap controls to their final position and keep the pressed visual state.

## Fits and risks

- **Fits:** audio, music and creative tools (`archetype.creator`), camera and film apps, games and casino/board metaphors, whisky, coffee, leather and craft packaging, calendar and notes products with a paper metaphor. Familiar object metaphors can help `audience.older-adults` and `audience.low-literacy-plain-language`, because the control explains itself; confirm with user testing.
- **Risks:** visual noise, asset weight, localization (engraved text in fixed-width plates), and dating quickly. Dense workflows (spreadsheets, admin tools) lose horizontal space to chrome. Texture layers behind text erode contrast.
- **Wrong for:** `industry.saas-b2b`, finance and compliance products, expert power users who want density, low-end devices and bandwidth, email.

## Do and don't

- Do pick one metaphor per product (a recorder, a notebook, a toolbox) and derive every control from it.
- Do keep content plates flat and high-contrast, and reserve texture for chrome.
- Do build materials with CSS gradients, layered shadows and small noise tiles so themes and dark variants stay possible.
- Don't mix light directions, overdo gloss, or add stitching to every surface.
- Don't fake physics you cannot support: a draggable knob that cannot be keyboard-operated is decoration.
- Don't revive iOS 6 as nostalgia without a concept; modern tactile design is quieter than 2011.

## Clichés and AI tells

- Lazy version: a "premium" app with a brown leather header, gold gradient buttons, a stitched border around every card, glossy 3D icons in four lighting directions, and a wooden background behind body text.
- Fix: choose one base material (for example felt green with brass accents), apply it to the faceplate only, set all copy on flat paper or LCD plates, use one coherent engraved icon set, define a single light angle in tokens, and test the chrome at 50% zoom to confirm the hierarchy still reads.

## Accessibility notes

- Plate pairs: ink #20150F on paper #F2E8D0 is 14.66:1; cream #E8D8B0 on leather #5B3A29 is 7.15:1; paper on felt #1F4D3A is 7.90:1; ink on brass #B8913F is 6.09:1; ink on steel #C9CDD2 is 11.18:1; paper on enamel red #A8261C is 5.82:1.
- Brass is decorative or large-only against dark material: brass on leather is 3.44:1, brass on paper is 2.41:1 (fails). Never use brass text on paper.
- Engraved text with a light shadow loses contrast when the base is mid-tone; keep engraved labels at 4.5:1 against their plate and 12px or larger.
- Every skeuomorphic control needs a native equivalent underneath (`role="switch"`, `<input type="range">`) with keyboard and screen-reader behavior, visible focus rings (2px cream or ink with offset), and 44px targets.
- Make sound and haptics optional and visible; honor `prefers-reduced-motion`; avoid flashing LCD or lamp effects above 3 flashes per second.

## Reference anchors

- iOS 6 and earlier Apple interfaces, and the 2013 flattening in iOS 7 (historical record, not for copying)
- Dieter Rams and Braun product design, which inspired many hardware-metaphor interfaces
- Teenage Engineering and Arturia / Native Instruments plug-in interfaces for contemporary tactile UI
- Don Norman, *The Design of Everyday Things* (affordances and signifiers)
- Nielsen Norman Group, "Flat Design: Its Origins, Its Problems, and Why Flat 2.0 Offers Better Usability" (nngroup.com) on signifiers lost when realism is removed
