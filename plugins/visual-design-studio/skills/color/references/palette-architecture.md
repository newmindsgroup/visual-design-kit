# Palette architecture

Version-Timestamp: 2026-10-20 02:07:10 UTC

Design the roles first, then fill them with ramp steps. A palette is a set of jobs (background, text, border, action, status, focus, data), not a row of swatches.

## Roles and tokens

| Role | Token (contract name) | Light mode source | Rule |
| --- | --- | --- | --- |
| Page background | `--color-bg-canvas` | Neutral step 1 or white | Largest area; sets the temperature of the whole product |
| Cards, panels | `--color-bg-surface` | White or neutral 1 | Must differ from canvas by a border or lightness step |
| Popovers, menus, raised cards | `--color-bg-surface-raised` | White plus `--shadow-md` | In dark mode, lighter than surface |
| Wells, table stripes, code | `--color-bg-sunken` | Neutral step 2-3 | Recessed areas |
| Inverse panels, tooltips | `--color-bg-inverse` | Neutral step 12 | Pairs with `--color-fg-inverse` |
| Primary text | `--color-fg-default` | Neutral 12 | 12:1 or more on canvas is typical |
| Secondary text | `--color-fg-muted` | Neutral 9-10 | At least 4.5:1 on every surface |
| Placeholder, disabled, non-essential | `--color-fg-subtle` | Neutral 8 | At least 3:1; never for information the user needs |
| Text on dark | `--color-fg-inverse` | Neutral 1 | |
| Text on accent fills | `--color-fg-on-accent` | White or neutral 12 | 4.5:1 on accent default, hover and active |
| Decorative dividers | `--color-border-subtle` | Neutral 5-6 | No contrast requirement; purely visual grouping |
| Card and table borders | `--color-border-default` | Neutral 7 | Visual structure |
| Input borders, controls, focus-adjacent | `--color-border-strong` | Neutral 8 | 3:1 against the background (WCAG 2.2 SC 1.4.11) |
| Primary action fill | `--color-accent-default` | Accent 9 | The brand-carrying step |
| Hover, pressed | `--color-accent-hover`, `--color-accent-active` | Accent 10, 11 | Darken in light mode, lighten in dark mode |
| Selected rows, accent tint | `--color-accent-subtle` | Accent 3 | Background only |
| Accent text, links | `--color-accent-fg` | Accent 11 | 4.5:1 on canvas and on accent subtle |
| Status | `--color-{success,warning,danger,info}-{fg,bg,border}` | Status ramps 11 / 2-3 / 8 | fg on bg 4.5:1 |
| Focus ring | `--color-focus-ring` | Accent 8 or a dedicated blue | 3:1 against canvas and the focused component |
| Modal backdrop | `--color-overlay-scrim` | Neutral 12 at 50-60% opacity | Content behind must be visibly suppressed |

## The 12-step ramp

Twelve steps give every role a home with room for hover and active states. Eleven steps (50-950, as in Tailwind) also work; keep the role mapping explicit either way. The step semantics below follow the convention popularized by Radix Colors.

| Step | Job |
| --- | --- |
| 1 | App background |
| 2 | Subtle background (sunken areas, stripes) |
| 3 | Component background (tints, subtle accent) |
| 4 | Component hover |
| 5 | Component active or selected |
| 6 | Subtle border, separators |
| 7 | Border, default |
| 8 | Strong border, focus ring, input outline |
| 9 | Solid fill (the purest brand step) |
| 10 | Solid hover |
| 11 | Low-contrast text, accent text |
| 12 | High-contrast text |

### Worked example: Meridian-style teal and its neutral

OKLCH hue 195 (the token contract's default reference brand is a deep teal near this hue). Generated with the algorithm in [OKLCH ramps](oklch-ramps.md); contrast is WCAG 2.2.

| Step | Teal | OKLCH | vs white | Neutral (tinted 195) | OKLCH | vs white |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | #F0FDFD | 0.985 0.014 195 | 1.04 | #F9FAFA | 0.985 0.001 195 | 1.05 |
| 2 | #E0F9F9 | 0.965 0.026 195 | 1.10 | #F1F4F4 | 0.965 0.003 195 | 1.11 |
| 3 | #C7F4F3 | 0.935 0.046 195 | 1.19 | #E6EAEA | 0.935 0.005 195 | 1.21 |
| 4 | #A9EBEA | 0.895 0.066 195 | 1.33 | #D8DEDE | 0.895 0.007 195 | 1.36 |
| 5 | #84DEDE | 0.845 0.086 195 | 1.56 | #C6CECE | 0.845 0.009 195 | 1.60 |
| 6 | #56CCCC | 0.78 0.106 195 | 1.93 | #B0BAB9 | 0.78 0.011 195 | 1.99 |
| 7 | #06B1B2 | 0.69 0.117 195 | 2.65 | #939E9D | 0.69 0.012 195 | 2.76 |
| 8 | #029393 | 0.60 0.102 195 | 3.75 | #788382 | 0.60 0.012 195 | 3.91 |
| 9 | #047879 | 0.52 0.088 195 | 5.29 | #626B6B | 0.52 0.011 195 | 5.48 |
| 10 | #036262 | 0.45 0.076 195 | 7.17 | #4F5757 | 0.45 0.010 195 | 7.41 |
| 11 | #024D4D | 0.38 0.064 195 | 9.67 | #3E4444 | 0.38 0.008 195 | 9.93 |
| 12 | #002D2D | 0.27 0.046 195 | 14.86 | #232727 | 0.27 0.006 195 | 15.10 |

Pairs this mapping produces (all computed): white on accent 9 is 5.29:1, on accent 10 is 7.17:1, on accent 11 is 9.67:1; accent 11 text on accent 3 is 8.13:1; accent 8 focus ring on neutral 1 is 3.59:1; neutral 8 subtle text on neutral 1 is 3.74:1; neutral 9 muted text on neutral 2 is 4.95:1; neutral 12 on neutral 2 is 13.65:1. Neutral 7 on neutral 1 is only 2.64:1, which is why input borders use step 8.

## How many colors

- **Accent:** one. A second accent needs a distinct job (a marketing highlight, a secondary product line). A third almost always competes.
- **Neutrals:** one ramp, tinted. Two neutral ramps (warm and cool) only when the brand deliberately mixes them, for example warm paper backgrounds with cool UI chrome.
- **Status:** four hues (success, warning, danger, info), each a small ramp or at least fg, bg, border.
- **Data:** a separate categorical set; do not reuse status colors for categories (see the `data-visualization` skill).
- **Brand extended palette** (illustration, campaign, packaging): 4-8 colors that live outside the UI tokens and never carry state.

## Status colors

| Status | Hue | fg (text, icons) | bg | border | fg on bg |
| --- | --- | --- | --- | --- | --- |
| Success | 150 | #197037 (0.48 0.12 150) | #E8F9EB (0.965 0.025 150) | #4A9A5E (0.62 0.12 150) | 5.62:1 |
| Warning | 70 | #8A5601 (0.50 0.11 70) | #FFF1E2 (0.965 0.025 70) | #B47825 (0.62 0.12 70) | 5.55:1 |
| Danger | 27 | #B02B27 (0.50 0.17 27) | #FFEFED (0.965 0.025 27) | #C4675E (0.62 0.12 27) | 5.84:1 |
| Info | 250 | #0460A5 (0.48 0.14 250) | #EBF5FF (0.965 0.025 250) | #488ACB (0.62 0.12 250) | 5.91:1 |

The borders above clear 3:1 on white (3.46-3.85:1). Rules:

- Pair every status color with an icon and a text label. Never rely on color alone (WCAG 2.2 SC 1.4.1).
- Warning text must be dark amber or brown; bright yellow text never passes on white.
- If the brand accent sits on a status hue (a red brand, a green fintech), move the status hue 15-25 degrees away or separate them by lightness, and keep the danger color out of primary buttons.
- Dark-mode status values are in [dark mode](dark-mode.md).

## Proportion heuristics

- **60-30-10** is a starting point, not a law: 60% dominant (neutral surfaces), 30% secondary (text, secondary surfaces, imagery), 10% accent.
- **Product UI:** accent under 10% of the pixels. If everything is teal, nothing is.
- **Marketing:** a full-bleed accent section every 2-4 sections can carry the brand; keep text on it at 4.5:1.
- **Luxury and quiet styles:** 80-90% neutral, accent under 5%, often in a single detail.
- **Bold and neo-brutalist styles:** large flat fields of 2-3 saturated colors with black type; hierarchy comes from size and outline instead of scarcity.
- **Value check:** convert a screenshot to grayscale. The hierarchy should survive; if the primary button disappears, its lightness is too close to its surroundings.

## Brand color vs UI color

- Brand primitives are fixed identity values (logo color, Pantone). UI tokens are functional and must pass contrast.
- A mid-lightness brand color (L 0.60-0.75) is usually too light for white text and too dark for black text. Keep it for large fills, illustration and the logo; derive UI steps from its ramp (step 9 for fills, step 11 for text).
- Document both: "Brand Teal (logo, packaging): #029393 / PMS ... ; UI accent: `--color-accent-default` #047879."
- Never silently change an approved brand color to pass contrast. Propose a functional variant and record it.

## Checklist

- Every role in the table has a token in light, dark and high-contrast.
- Neutrals tinted; one accent; status triplets with icons and text.
- Input borders and focus ring at 3:1; all text pairs at 4.5:1 (7:1 in high contrast).
- Grayscale screenshot keeps the hierarchy.
- Brand primitives and UI tokens documented separately.
