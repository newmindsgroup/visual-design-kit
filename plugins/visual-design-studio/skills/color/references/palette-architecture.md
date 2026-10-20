# Palette architecture

Version-Timestamp: 2026-10-20 02:07:10 UTC

Design the roles first, then fill them with ramp steps. A palette is a set of jobs (background, text, border, action, status, focus, data), not a row of swatches.

## Roles, tokens and the kit's mapping

The kit's ramps use steps 50-950 (see [OKLCH ramps](oklch-ramps.md)); neutrals add 850 and 975 for dark surfaces. This is how the shipped semantic tokens map to them (`library/tokens/src/semantic.*.tokens.json`):

| Role | Token | Light | Dark | High contrast | Rule |
| --- | --- | --- | --- | --- | --- |
| Page background | `--color-bg-canvas` | neutral 50 | neutral 950 | white | Largest area; sets the temperature of the product |
| Cards, panels | `--color-bg-surface` | white | neutral 900 | white | Differs from canvas by lightness or a border |
| Popovers, menus | `--color-bg-surface-raised` | white + shadow | neutral 850 | white | In dark mode, lighter than surface |
| Wells, stripes, code | `--color-bg-sunken` | neutral 100 | neutral 975 | neutral 50 | Recessed areas |
| Inverse panels, tooltips | `--color-bg-inverse` | neutral 900 | neutral 100 | neutral 975 | Pairs with `--color-fg-inverse` |
| Primary text | `--color-fg-default` | neutral 900 | neutral 100 | neutral 975 | 12:1 or more on canvas is typical |
| Secondary text | `--color-fg-muted` | neutral 600 | neutral 300 | neutral 700 | At least 4.5:1 on every surface |
| Placeholder, non-essential | `--color-fg-subtle` | neutral 500 | neutral 400 | neutral 600 | At least 3:1; never for information the user needs |
| Text on accent fills | `--color-fg-on-accent` | white | neutral 950 | white | 4.5:1 on accent default, hover, active |
| Decorative dividers | `--color-border-subtle` | neutral 100 | neutral 800 | neutral 500 | Visual grouping only |
| Card and table borders | `--color-border-default` | neutral 200 | neutral 700 | neutral 700 | Structure; not enough for input outlines |
| Input outlines, controls | `--color-border-strong` | neutral 500 | neutral 500 | neutral 975 | 3:1 against the background (WCAG 2.2 SC 1.4.11) |
| Primary action fill | `--color-accent-default` | accent 600 | accent 300 | accent 800 | The brand-carrying step |
| Hover, pressed | `--color-accent-hover`, `--color-accent-active` | accent 700, 800 | accent 200, 100 | accent 900, 950 | Darker in light mode, lighter in dark |
| Selected rows, tints | `--color-accent-subtle` | accent 100 | accent 900 | accent 50 | Background only |
| Accent text, links | `--color-accent-fg` | accent 700 | accent 300 | accent 800 | 4.5:1 on canvas and on accent subtle |
| Status | `--color-{success,warning,danger,info}-{fg,bg,border}` | 700 / 100 / 300 | 300 / 900 / 700 | 800 / 50 / 700 | fg on bg 4.5:1 |
| Focus ring | `--color-focus-ring` | accent 600 | accent 300 | accent 800 | 3:1 against canvas and the focused component |
| Modal backdrop | `--color-overlay-scrim` | black 48% | black 64% | black 64% | Content behind is visibly suppressed |

## Ramp steps and their jobs

| Steps | Light-mode job | Dark-mode job |
| --- | --- | --- |
| 50-100 | Canvas, sunken areas, subtle tints | Text and the lightest accents |
| 200-300 | Borders, decorative fills | Secondary text, accent fills and links |
| 400-500 | Strong borders, placeholder text, icons | Strong borders, subtle text |
| 600-700 | Accent fills, secondary text, accent text | Default borders |
| 800-950 | Primary text, inverse surfaces | Surfaces: 950 canvas, 900 surface, 850 raised, 975 sunken |

Twelve-step scales with named jobs per step (the convention popularized by Radix Colors) work equally well. Whatever the numbering, keep the role mapping explicit and lint the pairs.

### Worked example: Meridian (the kit's default brand)

Meridian maps neutral to the `slate` ramp (cool, hue about 245, chroma 0.009-0.018) and accent to `teal` (hue 195, peak chroma 0.113). Values from `library/tokens/src/primitives.tokens.json`; ratios are WCAG 2.2, computed.

| Step | Slate | OKLCH | vs white | Teal | OKLCH | vs white |
| --- | --- | --- | --- | --- | --- | --- |
| 50 | #F2F7FC | 0.974 0.009 248 | 1.08 | #ECFAFA | 0.975 0.015 197 | 1.07 |
| 100 | #E2E9EF | 0.930 0.011 244 | 1.23 | #C3F3F2 | 0.931 0.049 195 | 1.21 |
| 200 | #C3CCD3 | 0.840 0.014 241 | 1.63 | #88DCDB | 0.841 0.082 195 | 1.58 |
| 300 | #A6AFB8 | 0.750 0.016 248 | 2.22 | #4FC2C2 | 0.749 0.103 195 | 2.14 |
| 400 | #8A949D | 0.661 0.018 245 | 3.09 | #00A7A7 | 0.659 0.113 195 | 2.96 |
| 500 | #6F7982 | 0.571 0.018 245 | 4.44 | #008989 | 0.570 0.097 195 | 4.25 |
| 600 | #565F67 | 0.481 0.017 245 | 6.50 | #006C6C | 0.481 0.082 195 | 6.25 |
| 700 | #3E464D | 0.390 0.016 245 | 9.60 | #005050 | 0.390 0.067 195 | 9.28 |
| 800 | #282F35 | 0.301 0.015 244 | 13.56 | #003636 | 0.301 0.051 195 | 13.28 |
| 850 | #1E2429 | 0.256 0.013 243 | 15.68 | | | |
| 900 | #14191D | 0.210 0.011 242 | 17.70 | #001D1D | 0.209 0.036 195 | 17.60 |
| 950 | #0B0F12 | 0.165 0.009 241 | 19.24 | #071010 | 0.164 0.014 196 | 19.25 |
| 975 | #070A0D | 0.143 0.009 246 | 19.84 | | | |

Light-mode pairs this mapping produces: fg-default on canvas 16.42:1; fg-muted on canvas 6.04:1 and on white 6.50:1; fg-subtle on canvas 4.12:1; white on accent 600, 700, 800 at 6.25, 9.28, 13.28:1; accent-fg on accent-subtle 7.70:1; border-strong and focus ring on canvas 4.12:1 and 5.80:1. Border-default on canvas is 1.51:1: fine for card edges, not for input outlines.

## How many colors

- **Accent:** one. A second accent needs a distinct job (a marketing highlight, a product line). A third almost always competes.
- **Neutrals:** one ramp, tinted. Two neutral ramps only when the brand deliberately mixes warm paper with cool UI chrome.
- **Status:** four hues (success, warning, danger, info), each a ramp so fg, bg and border come from the same hue.
- **Data:** a separate categorical set; do not reuse status colors for categories (see the `data-visualization` skill).
- **Brand extended palette** (illustration, campaign, packaging): 4-8 colors outside the UI tokens that never carry state.

## Status colors

The kit's status ramps (green hue 150, amber about 75, red 22, blue 255) give these light-mode pairs:

| Status | fg (700) | bg (100) | fg on bg | Dark fg (300) on bg (900) |
| --- | --- | --- | --- | --- |
| Success | #005423 | #CCF4D3 | 7.61:1 | #6DC582 on #001F09, 8.30:1 |
| Warning | #633A00 | #FDE5B8 | 8.00:1 | #DEA137 on #281200, 7.87:1 |
| Danger | #85001A | #FFDFDD | 8.37:1 | #FF8382 on #350206, 7.59:1 |
| Info | #004387 | #D9EAFF | 7.97:1 | #73B1FF on #021835, 7.99:1 |

Rules:

- Status `border` tokens (`--color-danger-border` and siblings) use ramp step 500 in light and dark modes, so they clear 3:1 on canvas and surface (3.6-4.6:1, enforced by `tokens.py lint`) and are valid as the boundary of an invalid text field (WCAG 1.4.11). Still pair the border with an icon and message: color alone never marks a state.
- Pair every status color with an icon and a text label. Never rely on color alone (WCAG 2.2 SC 1.4.1).
- Warning text is dark amber or brown; bright yellow text never passes on white.
- If the brand accent sits on a status hue (a red brand, a green fintech), move the status hue 15-25 degrees away or separate by lightness, and keep the danger color out of primary buttons.

## Proportion heuristics

- **60-30-10** is a starting point, not a law: 60% dominant (neutral surfaces), 30% secondary (text, secondary surfaces, imagery), 10% accent.
- **Product UI:** accent under 10% of the pixels. If everything is teal, nothing is.
- **Marketing:** a full-bleed accent section every 2-4 sections can carry the brand; keep text on it at 4.5:1.
- **Luxury and quiet styles:** 80-90% neutral, accent under 5%, often in a single detail.
- **Bold and neo-brutalist styles:** large flat fields of 2-3 saturated colors with black type; hierarchy comes from size and outline instead of scarcity.
- **Value check:** convert a screenshot to grayscale. The hierarchy should survive; if the primary button disappears, its lightness is too close to its surroundings.

## Brand color vs UI color

- Brand primitives are fixed identity values (logo color, Pantone). UI tokens are functional and must pass contrast.
- A mid-lightness brand color (L 0.60-0.75) is usually too light for white text and too dark for black text. Keep it for large fills, illustration and the logo; derive UI steps from its ramp (600 for fills, 700 for text in light mode).
- Document both: "Brand teal (logo, packaging): teal 400 #00A7A7; UI accent: `--color-accent-default` teal 600 #006C6C."
- Never silently change an approved brand color to pass contrast. Propose a functional variant and record it.
- Brand overrides live in `library/tokens/src/brands/<brand>.tokens.json` and remap only the brandable primitives (accent, neutral, fonts); the `design-system` skill covers the build.

## Checklist

- Every role has a token in light, dark and high contrast.
- Neutrals tinted; one accent; status ramps with icons and text.
- Input outlines and focus ring at 3:1; all text pairs at 4.5:1 (7:1 for body in high contrast).
- Grayscale screenshot keeps the hierarchy.
- Brand primitives and UI tokens documented separately.
