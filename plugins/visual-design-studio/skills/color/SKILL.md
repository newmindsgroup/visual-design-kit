---
name: color
description: >-
  Build color systems for brands, products and campaigns: palette roles and proportions, 11-13 step OKLCH ramps, semantic
  tokens, WCAG 2.2 contrast with APCA as an advisory check, dark and high-contrast modes, cultural meaning, and
  distinctive brand colors with Pantone, CMYK and RGB specs. Use when choosing or extending a palette, generating ramps
  or color tokens, checking contrast, designing dark mode, picking status or brand colors, or replacing a generic
  purple-gradient look with something ownable.
license: MIT
metadata:
  version-timestamp: "2026-10-20 02:07:10 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 02:07:10 UTC"
---

# Color

Excellent color work is mostly neutrals and restraint: a tuned neutral ramp does 80-90% of the job, one accent marks what matters, status colors are unambiguous, every text pair passes contrast, and the brand hue is chosen against the category rather than by default.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Palette structure | 1 neutral ramp (13 steps) + 1 accent ramp (11 steps) + 4 status ramps | Brand needs a secondary accent (max 2 more) or data visualization needs a categorical set |
| Proportion | 60-30-10 as a starting point: 60% neutral surfaces, 30% secondary surfaces and text, 10% accent | Product UI: accent under 10% of the surface; bold campaigns and neo-brutalist work flood with color |
| Authoring space | OKLCH; ship sRGB hex with optional Display P3 values behind `@media (color-gamut: p3)` | Print: author in the target CMYK profile or spot colors |
| Ramps | 11 steps (50-950), lightness linear from L 0.975 to 0.165, chroma peaking at 500; neutrals add 850 and 975 | Yellows and oranges need a hue shift so dark steps do not turn olive |
| Neutrals | Tinted toward the accent hue or a warm bias, chroma 0.01-0.02 | Pure gray for photography-led and Swiss work; warm neutrals for food, hospitality, luxury |
| Text contrast | 4.5:1 body, 3:1 large text (24px, or 18.66px bold), 7:1 in high-contrast mode | Never lower; logos and decorative text are the only exemptions |
| Non-text contrast | 3:1 for input borders, icons, focus rings, chart marks against adjacent colors | Decorative dividers may go lower (`--color-border-subtle`) |
| APCA (advisory) | Body Lc 75+, preferred Lc 90; Lc 60 for large or UI text; Lc 45 for headlines | Use it to tune dark mode and thin type; WCAG 2.2 stays the pass/fail baseline |
| Focus ring | 2px+ solid `--color-focus-ring`, 3:1 against the background and the component | High-contrast mode: thicker ring and system colors in forced-colors |
| Status hues | Success about 150, warning about 75, danger about 22-27, info about 255 (OKLCH hue); fg/bg/border from one ramp | Brand accent sits on a status hue: shift the status hue 15-25 degrees or change lightness |
| Dark mode | Canvas L 0.15-0.20, about +0.045 L per elevation level, text L 0.92-0.95, accent moved to a light step (300) with dark text on it | OLED-first media apps may use a true black canvas |
| Brand hue | Off the category default unless strategy says belong; avoid indigo/violet (hue 270-300) as an unexamined default | The brand already owns the hue; the brief rewards category fit |
| Gradients | 2-3 stops, neighboring hues, `in oklch` interpolation, never behind body text without a solid backing | Gradient is the brand's core asset (`style.vibrant-gradient-saas`) |
| Print specs | Pantone C and U, CMYK per named profile, RGB, hex | Digital-only brands may skip Pantone |

## Workflow

1. **Read locks and context.** Existing brand colors are fixed primitives; extend around them. Run `python3 ../../library/scripts/atlas.py query "<brief>"` for the style, industry and market entries and read their palette, category conventions and color symbolism.
2. **Define roles before hues** with [palette architecture](references/palette-architecture.md): canvas, surfaces, text levels, borders, accent states, status, focus, overlay, data.
3. **Choose the brand hue** with [brand color](references/brand-color.md): map competitors on a hue wheel, pick an ownable position, test it in a real composition.
4. **Generate ramps** with [OKLCH ramps](references/oklch-ramps.md): `python3 ../../library/scripts/color_tools.py ramp --hue <H> --chroma <C> --name <name>`. Match the brand color to its nearest step.
5. **Map ramps to tokens.** Fill the semantic set (`--color-bg-*`, `--color-fg-*`, `--color-border-*`, `--color-accent-*`, `--color-{success,warning,danger,info}-{fg,bg,border}`, `--color-focus-ring`, `--color-overlay-scrim`) for light, dark and high-contrast.
6. **Check contrast** for every pair that ships, per [contrast](references/contrast.md): `python3 ../../library/scripts/color_tools.py contrast <fg> <bg>`, then `apca` for advisory tuning. Fix failures by moving ramp steps, never by suppressing the check.
7. **Build dark mode** per [dark mode](references/dark-mode.md), not by inverting.
8. **Check meaning** per [meaning and culture](references/meaning-and-culture.md) for the target markets; make sure nothing relies on color alone.
9. **Render and inspect.** Real screens or layouts in light, dark and high-contrast; grayscale screenshot to test value hierarchy; color-vision-deficiency simulation (Chrome DevTools Rendering panel). Use the `design-critique` skill's render loop.

## Decisions that change the answer

- **Style:** each atlas style has a palette recipe (Swiss: ink, paper, one red; quiet minimal: warm neutrals and one muted accent; neo-brutalist: saturated flat fills with black outlines; classic luxury: near-black, ivory, a metallic accent used sparingly).
- **Industry:** sets category defaults to work with or against (finance blue and green, health blue and teal, food warm hues); see each industry entry's *Category conventions* and *Where to differentiate*.
- **Market:** color associations and regulated colors vary; read `market.*` *Color and symbolism*.
- **Audience:** older adults and low-vision users need higher contrast and no low-chroma pastel text; children's products tolerate more saturation; expert users need calm neutrals and strong status colors.
- **Tier:** luxury uses fewer, darker or quieter colors and more neutral space; value uses saturated, high-contrast promotional color.
- **Channel:** screens are sRGB or P3; print is CMYK or spot with dot gain; signage needs contrast at distance and under ambient light; email needs colors that survive client dark modes.

## Common failures

- **Default indigo or purple-to-pink gradient.** Fix: choose the hue from the category map in [brand color](references/brand-color.md).
- **Pure gray neutrals with a saturated accent.** Looks unfinished. Fix: tint neutrals 0.005-0.015 chroma toward the accent or a warm or cool bias.
- **Brand color used as text color everywhere.** Mid-lightness brand hues often fail 4.5:1. Fix: use a darker ramp step for text (`--color-accent-fg`) and the brand step for fills.
- **Light gray text.** `#999` on white is 2.85:1. Fix: `--color-fg-muted` (4.5:1+) for secondary text; `--color-fg-subtle` only for decorative, non-essential text (placeholders use `--color-fg-muted`).
- **Status by color alone.** Fix: icon plus text plus color.
- **Inverted dark mode.** Pure black canvas, pure white text, same saturated accents: glare and vibration. Fix: [dark mode](references/dark-mode.md).
- **Too many accents.** Five competing hues flatten hierarchy. Fix: one accent; others become neutrals or data colors.
- **Hex-to-CMYK by formula.** Fix: convert with the print profile, proof, and specify Pantone where the brand must match.

## References

- [Palette architecture](references/palette-architecture.md): roles and the kit token mapping, 11-13 step ramps, accent count, status colors, proportions, brand vs UI color.
- [OKLCH ramps](references/oklch-ramps.md): why OKLCH, the ramp algorithm, gamut mapping, and `../../library/scripts/color_tools.py` usage.
- [Contrast](references/contrast.md): WCAG 2.2 math and thresholds, APCA as advisory, non-text and focus, testing.
- [Dark mode](references/dark-mode.md): elevation by lightness, desaturation, off-black and off-white, borders, images.
- [Meaning and culture](references/meaning-and-culture.md): associations by context and market, never color alone.
- [Brand color](references/brand-color.md): category mapping, ownable hues, avoiding the generic default, Pantone, CMYK and RGB specs.
- Atlas: `python3 ../../library/scripts/atlas.py query "..."` and `python3 ../../library/scripts/atlas.py show <id>`; IDs in [the registry](../../library/atlas/registry.json).
- Sibling skills: `data-visualization` for chart palettes, `design-system` for token builds and theming, `typography` for text sizes that set the contrast threshold, `print-packaging-social` for prepress.
- Deep process for client projects: [design-color-system](../../library/draft-skills/design-color-system/SKILL.md) with [palette craft](../../library/draft-skills/design-color-system/references/palette-craft.md) and [proofing and maintenance](../../library/draft-skills/design-color-system/references/proofing-and-maintenance.md); record decisions in the [color decision template](../../library/templates/color-decision.md); worked reasoning in [color in use](../../library/knowledge/color-in-use.md).

Catalog IDs covered: color
