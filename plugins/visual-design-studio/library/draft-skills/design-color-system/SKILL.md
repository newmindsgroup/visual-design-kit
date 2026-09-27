---
name: design-color-system
description: Research, choose and apply brand-specific color systems, including palette relationships, semantic states, cultural context, accessibility and screen/print color handling.
---

# Color strategy and systems

Version-Timestamp: 2026-09-10 20:21:06 AST

Status: authored instructions; palette quality and accessibility require actual combination tests.

Read [ownership](../../DESIGN-CRAFT.md) and the existing brand/reference decision. First distinguish preserving an approved palette, extending functional roles and exploring a new palette. Preserve exact approved values. If a supplied color fails a required use, propose an accessible pairing, separate functional variant or escalation; do not silently change the brand swatch.

## Research meaning and context

Record audience/geography, language/culture, category conventions, competitors, desired positioning, physical setting, product colors and existing brand recognition. Distinguish observed category patterns, research findings and proposed associations. Avoid deterministic claims such as a hue guarantees trust, appetite or conversion. Color-emotion studies do not prove commercial outcomes for a specific brand. Use the [color decision](../../templates/color-decision.md) to record each meaning hypothesis, its scope/source, uncertainty and what would change the decision.

An industry association is one input, not a palette assignment. For a new brand, explore meaningful alternatives around recognition, differentiation and readability. For an established brand, work within the allowed range. Consider cultural and safety-signage conflicts in the target context. Do not invent regulated color rules; verify applicable jurisdiction/medium requirements when relevant.

## Build relationships and roles

Explore hue, lightness/value and chroma/saturation independently. Monochromatic, analogous, complementary, split-complementary and triadic arrangements are starting relationships, not finished systems. Evaluate actual compositions with realistic imagery and copy, not swatches alone. Decide the relative prominence of neutral, primary, secondary and accent colors from the brand and content; no universal accent percentage applies to every client.

Separate brand primitives from semantic roles: canvas/surface, primary/secondary text, border, action, link, focus, selected, hover/pressed, success, warning, error, information and disabled as needed. Specify light/dark or high-contrast variants only when in scope; dark mode is not simple inversion. For charts, distinguish categorical, sequential and diverging scales and supply non-color cues. Never use a decorative brand sequence as an untested data scale.

The approved project token file is the value authority. The decision sheet references token IDs and stores combination-check evidence rather than a second palette. Check color relationships over actual surfaces, transparency, images and gradients. Gamut mapping can change an intended color; use an sRGB-compatible fallback where needed and test richer-gamut alternatives on supporting hardware. Specify RGB/ICC profile or print process, stock, proof and output profile as appropriate; a hex value is not a universal CMYK or spot-color match.

## Accessibility and verification

For web WCAG 2.2 AA, text contrast is normally at least 4.5:1, or 3:1 for large text (18 pt regular or 14 pt bold, equivalent to 24 CSS px regular or approximately 18.67 CSS px bold at the rendered size). Required non-text visual information uses at least 3:1 against adjacent colors under criterion 1.4.11. Apply documented exceptions narrowly; brand body text is not a logo exception. Do not communicate status or chart categories by color alone. References and applicability are in the research map (optional provenance in the pinned source version; not bundled). APCA, if used, is supplementary and does not replace WCAG 2.2 contrast-ratio evaluation.

Record foreground/background token IDs, actual composited values, type role/size/weight or graphic role, state/theme, measured ratio, target, result and evidence. For gradients/video backgrounds test relevant worst-case areas/frames or add a stable backing. A color-vision simulation helps inspection but is not proof of universal accessibility. Also inspect forced colors, focus visibility and state distinctions in the actual interface when relevant.

Use WCAG as applicable web criteria, not as proof of print/display legibility. For physical output inspect proof, ambient light, viewing distance, substrate/display behavior and actual text size. A monitor preview cannot certify manufacturing or an installed retail display.

## Output

Deliver rationale and rejected alternatives, project token references, role usage/misuse rules, measured combination matrix, image/data guidance, output-profile requirements and explicit pending checks. Typography owns type sizes and fonts; changes there invalidate dependent contrast results. Identity approves brand rules; production and delivery own final native/export artifacts. No isolated palette is called universally accessible or suitable for an entire industry.

Read the existing identity record and its approved typeface/palette selection before proposing a change. If no identity record exists, record the provisional choice in the existing work record with its design owner and approval status; do not create a fictional approval or force a full identity project.


Version-Timestamp: 2026-09-11T23:21:42-04:00

## Deeper craft methods

Version-Timestamp: 2026-09-11T19:32:14-04:00

- [palette craft ](references/palette-craft.md)
- [proofing and maintenance ](references/proofing-and-maintenance.md)

Use the [craft laboratory](../../CRAFT-LAB.md) for specimens and bounded checks.

## Screen-content extension

Version-Timestamp: 2026-09-11T19:51:13-04:00

Preserve approved product color and compare on intended hardware; assumed profiles do not establish accurate reproduction. Use the [specialist workflow](../../SCREEN-CONTENT-SKILLS.md) for the relevant detailed methods.

## Applied decision method

Version-Timestamp: 2026-09-27 14:25:39 AST

Read [Color in use](../../knowledge/color-in-use.md) when choosing relationships and semantic roles from realistic compositions. The card adds original worked reasoning; reuse this capability's existing prerequisites, records and acceptance checks. Load only the selected card. Its fictional example is teaching material, not tested project evidence.
