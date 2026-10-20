---
id: style.soft-ui-neumorphic
axis: style
name: Soft UI / Neumorphism
aliases: [neumorphism, soft ui, new skeuomorphism, extruded ui, soft shadows ui, clay ui]
summary: Monochrome surfaces extruded or pressed with paired light and dark shadows; tactile and calm, but a frequent AI default with weak contrast and affordance unless engineered carefully.
tags: [neumorphism, soft-ui, shadows, monochrome, tactile, extruded, minimal, rounded, controls]
pairs_with: [industry.digital-health-wellness, industry.automotive-mobility, archetype.caregiver, archetype.innocent, channel.native-app, tier.mid-market]
avoid_with: [audience.older-adults, audience.disability-accessibility-first, audience.low-literacy-plain-language, industry.fintech-banking, industry.healthcare-provider, channel.web-app]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Soft UI / Neumorphism

## Essence

Interface elements appear molded from the same soft material as the page: raised buttons catch a light from the top left, pressed controls sink into the surface. It surfaced on Dribbble in late 2019 and was popularized as "neumorphism" around 2020. The result is serene and object-like, which suits physical-control metaphors (dials, toggles, sliders). It is also one of the most frequently generated AI looks and has well-documented problems: the same-color surfaces give little contrast between object and background, and raised versus pressed states are hard to tell apart. Treat it as a controlled accent for specific controls, not a whole-product default.

## Visual signature

- One mid-light base color for the page, cards and controls (a cool gray-blue is canonical).
- Paired shadows: a white highlight toward the light source and a darker tint of the base on the opposite side, both soft.
- Raised (convex) elements for actions; inset (concave) elements for wells, inputs and active toggles.
- Large radii: pills, circles and 16-28px cards; no hard edges, almost no borders.
- Sparse, quiet color: a single saturated accent for the one active state, often a glowing ring or fill.
- Big round dials, sliders and toggles with generous spacing; a physical "device panel" feel.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Lexend (OFL); Atkinson Hyperlegible Next (OFL); commercial: Gotham Rounded, Circular |
| Body font | Atkinson Hyperlegible Next (OFL) or Lexend; commercial: Circular Std |
| Mono | Not needed; if required, DM Mono (OFL) |
| Type scale ratio | 1.200 (minor third); keep few sizes because the surfaces are already busy |
| Body size / line-height | 16-17px / 1.5; labels never below 13px; measure 55-65ch |
| Display letter-spacing | 0 to -0.01em; line-height 1.15; avoid tight tracking on soft shapes |
| Caps / labels | Prefer sentence case 13-14px, weight 600; if caps, +0.04em |
| Weights | 500 body, 600-700 labels and numbers; avoid 300 because thin text on soft gray fails contrast fast |
| Palette | Base surface #E0E5EC (oklch 0.92 0.011 257); Highlight shadow #FFFFFF (oklch 1 0 0); Dark shadow #A3B1C6 (oklch 0.76 0.034 258); Ink #2B3340 (oklch 0.32 0.026 260); Muted ink #4D5868 (oklch 0.46 0.03 258); Accent teal-blue #0B5F8A (oklch 0.46 0.1 239); Edge line #6F7C90 (oklch 0.58 0.034 259) |
| Status colors | Success #17693D (oklch 0.46 0.105 155); Danger #B3261E (oklch 0.50 0.178 29); each with an icon and label |
| Accent proportion | Under 8%: the active toggle, the primary button fill or one ring; avoid the stock violet #6D5DFC (oklch 0.59 0.227 281) |
| Radius | 16-24px cards, 12-16px buttons, full circles for dials and icon buttons |
| Borders | Add a 1px #6F7C90 edge (3.34:1 on the base) to inputs and any control that must be found without shadows |
| Shadow / elevation | Raised: `6px 6px 12px rgb(163 177 198 / 0.9), -6px -6px 12px #fff`; inset: `inset 4px 4px 8px rgb(163 177 198 / 0.9), inset -4px -4px 8px #fff`; keep the light source top-left everywhere; blur 8-16px, not 30px |
| Spacing density | Generous: 8px base, 20-32px gaps between controls so shadows do not collide; touch targets 48px |
| Grid | Simple 4 or 6 column panels; align controls on a centerline like a hardware panel |
| Motion | 160-240ms, cubic-bezier(0.4, 0, 0.2, 1); press moves from raised to inset while the fill color also changes |

## Composition and layout

- Design the panel like a device: group related controls on one slab, leave generous gaps, and keep a clear focal control (a large dial, a play button).
- Limit raised elements to what can be pressed. If everything is extruded, nothing reads as clickable.
- Pair every shadow state with a second cue: color fill for the active state, a check or icon change, a border on focus.
- Use flat, high-contrast text outside the shadowed shapes; text sits on the surface, not inside deep wells.
- Keep one light direction. Mixed shadow angles are the fastest way to make the interface look broken.

## Imagery and iconography

- Icons: 2px rounded outline or simple filled glyphs in ink #2B3340, 24px, optically centered in 48px circles. Never use pale gray icons on the base color.
- Illustrations: soft 3D "clay" objects or none. Keep scenes monochrome with one accent.
- Data: thick rounded bars and ring gauges in accent plus ink labels; avoid thin, low-contrast chart lines on the same-gray base.
- Photography is rare; if used, crop to rounded shapes with inset frames.

## Motion

Physical but short. A button depresses in 120-160ms: shadow flips from raised to inset, fill shifts a step darker, and the icon scales to 0.96. Toggles slide a knob with 200ms ease and change the track color, not only the shadow. Sliders follow the pointer without lag. No bouncy overshoot, glow pulses or continuous float animations. Under reduced motion, snap states instantly (shadow and color change remain).

## Fits and risks

- **Fits:** device-like controls in smart-home, thermostat, audio and music apps, meditation and sleep timers (`industry.digital-health-wellness`), vehicle comfort controls (`industry.automotive-mobility`), calculators, kids' sensory toys, small marketing hero objects. Calm brands (`archetype.caregiver`, `archetype.innocent`) benefit from its gentleness.
- **Risks:** low contrast and weak affordance. The dark shadow #A3B1C6 against the base #E0E5EC is 1.72:1, the white highlight is 1.27:1, and the classic gray label #9BA7B8 is 1.93:1; none can carry meaning on their own. The popular violet accent #6D5DFC is 3.59:1 on the base, so it cannot be a text color. Focus rings, disabled states and error states are easy to omit.
- **Wrong for:** data-dense web apps, finance and healthcare forms, older adults, low vision and keyboard users, low-literacy users. Shadows also cost paint time on long lists.

## Do and don't

- Do use it on a small set of physical controls inside an otherwise flat, high-contrast interface.
- Do add a visible edge (#6F7C90) on inputs and a distinct fill on selected items.
- Do keep text at least 4.5:1: ink #2B3340 is 10.05:1 and muted ink #4D5868 is 5.70:1 on the base.
- Don't shadow every card, list row and chip; reserve raised for actionable items.
- Don't set labels in the shadow color or light gray; they are the signature failure of the style.
- Don't build long forms or tables from extruded fields; inset wells with 1px edges are the most you can justify.
- Do run a three-part gate before shipping: a squint test (blur the screenshot 50%: can you still find every button?), a grayscale test with 3:1 edges, and a keyboard-only pass. If any fails, add a border, a fill change or a label.

## Clichés and AI tells

- Lazy version: a banking or crypto dashboard with every card and button extruded in #E0E5EC, 30px blur shadows, a #6D5DFC violet accent, Poppins, pale gray labels, a circular progress ring and floating icon buttons.
- Fix: choose one object metaphor (a speaker, a thermostat, a stereo), build only those controls in soft UI, set all text at 4.5:1 or better, replace the violet with a darker brand accent (#0B5F8A is 5.50:1 on the base, white on it 6.96:1), add 1px edges and distinct active fills, and design keyboard focus and disabled states explicitly.

## Accessibility notes

- Non-text contrast: WCAG 2.2 asks 3:1 for the visual boundary of controls. Shadow-only controls usually fail it; the edge color #6F7C90 is 3.34:1 on the base, so use it on inputs, sliders and focused items.
- Text: ink #2B3340 is 10.05:1, muted ink #4D5868 is 5.70:1, accent #0B5F8A is 5.50:1, danger #B3261E is 5.16:1 and success #17693D is 5.31:1 on the base. The brighter green #1B7F4B is only 3.96:1, so it fails as small text.
- State by shape and label: a toggle needs an On/Off text or icon, not only an inset shadow. Selected cards need a check or border.
- Target size: 48px minimum for round controls; keep 12px or more between targets.
- Windows High Contrast / forced colors removes box-shadows entirely, so give every control a real `border` that appears under `@media (forced-colors: active)`.

## Reference anchors

- Alexander Plyuto's 2019 Dribbble "Skeuomorph Mobile Banking" concept, the origin of the trend
- 2019-2020 Dribbble and Medium write-ups that named and popularized "neumorphism" (origin details vary by source; verify before citing)
- Material Design 3 elevation guidance for how tonal color replaces shadow
- Dieter Rams / Braun and Teenage Engineering product panels as the physical references for dials and soft keys
- WCAG 2.2 Success Criterion 1.4.11 Non-text Contrast (w3.org/TR/WCAG22)
