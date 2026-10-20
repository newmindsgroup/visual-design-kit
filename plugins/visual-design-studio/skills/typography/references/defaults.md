# Typography defaults

Version-Timestamp: 2026-10-20 02:07:10 UTC

Start from these numbers, then move off them for a stated reason. Sizes are CSS px unless a medium uses points (print, iOS) or sp (Android).

## Modular scale by context

A scale is a base size multiplied by one ratio per step. Fewer, more distinct steps read as hierarchy; many close steps read as noise.

| Context | Ratio | Base | Steps from base 16 (px) |
| --- | --- | --- | --- |
| Dense UI, admin, trading, data tables | 1.125 (major second) to 1.2 (minor third) | 14-16 | 1.125: 14.2, 16, 18, 20.2, 22.8, 25.6 / 1.2: 13.3, 16, 19.2, 23, 27.6, 33.2 |
| Product UI, web apps, docs | 1.25 (major third) | 16 | 12.8, 16, 20, 25, 31.2, 39.1, 48.8 |
| Marketing sites, campaigns | 1.333 (perfect fourth) | 16-18 | 12, 16, 21.3, 28.4, 37.9, 50.5, 67.3, 89.8 |
| Editorial features, posters, covers | 1.5 (perfect fifth) to 1.618 (golden) | 16-20 | 1.5: 16, 24, 36, 54, 81, 121.5 / 1.618: 16, 25.9, 41.9, 67.8, 109.7 |

Rules:

- Use 6-8 steps in a system. A page rarely needs more than 5.
- Round UI sizes to whole pixels, and to multiples of 2 or 4 below 32px so line boxes land on a 4px grid.
- Display moments may skip 2-3 steps for drama (a 6:1 headline-to-body ratio is normal in Swiss and editorial work). Keep the skip deliberate and rare.
- Negative steps shrink fast at large ratios (1.5 gives 10.7px at step -1). Pin small roles to fixed sizes (12, 13, 14px) instead of following the ratio down.

### Mapping to the token contract

The contract's font sizes are a product-UI scale close to 1.2-1.25:

| Token | rem | px | Typical role |
| --- | --- | --- | --- |
| `--font-size-xs` | 0.75 | 12 | Captions, legal, table meta |
| `--font-size-sm` | 0.875 | 14 | Secondary UI text, labels |
| `--font-size-md` | 1 | 16 | Body, inputs, buttons |
| `--font-size-lg` | 1.25 | 20 | Lead paragraph, H4 |
| `--font-size-xl` | 1.5 | 24 | H3, card titles |
| `--font-size-2xl` | 1.875 | 30 | H2 |
| `--font-size-3xl` | 2.25 | 36 | H1 in product UI |
| `--font-size-4xl` | 3 | 48 | Marketing H1 |
| `--font-size-5xl` | 3.75 | 60 | Display |

Keep `xs` to `lg` fixed for UI predictability. For marketing or editorial ratios, override `--font-size-2xl` to `--font-size-5xl` in the project's own CSS layer with the fluid values below; do not invent new size names.

## Body size by medium

| Medium | Body | Secondary | Floor | Notes |
| --- | --- | --- | --- | --- |
| Marketing and content web | 16-18px | 14px | 12px | Long-form articles 18-20px |
| Web apps and dashboards | 14-16px | 12-13px | 12px | 13-14px only in dense tables with tabular figures |
| iOS | Body 17pt | Footnote 13pt, Caption 1 12pt | Caption 2 11pt | Use Dynamic Type text styles so text scales with user settings (Apple HIG) |
| Android | Body Large 16sp / 24 | Body Medium 14sp / 20 | Label Small 11sp | Use sp so font scaling applies (Material 3 type scale) |
| Books, reports | 10-12pt on 13-15pt leading | Notes 8-9pt | 7pt | Magazine body 8.5-10pt |
| Business cards, stationery | 7.5-9pt | 6.5-7pt | 6pt | Test print at 100%; hairline serifs vanish below 7pt |
| Packaging | Per regulation | | | EU food information (Regulation (EU) 1169/2011): mandatory text x-height at least 1.2mm, 0.9mm on small packs; verify current rules for the product and market |
| Slides | 18-28pt on a 960x540pt canvas (PowerPoint 16:9) | 14-16pt for sources | 14pt | Keynote's default 1920x1080 canvas doubles these numbers: 36-56pt body. Rule of thumb: body cap height at least 2% of slide height |
| Email | 16px | 14px | 13px | iOS Mail enlarges text below about 13px, which breaks layouts |
| Signage, wayfinding | 25mm (1in) cap height per 3m (10ft) of viewing distance for comfortable reading | | | US: ADA 2010 Standards section 703 sets minimum character heights by viewing distance and mounting height; confirm locally |
| Video supers at 1080p | 40-60px | 32px | 28px | Keep inside the title-safe area (about 90% of frame); hold on screen at least twice the time it takes to read aloud |

## Measure

- Body copy: 45-75 characters per line, 66 as the target. Tokens: `--measure-narrow` 45ch, `--measure-body` 66ch, `--measure-wide` 75ch.
- Apply measure to the text container, not the page: `max-inline-size: var(--measure-body);`.
- Phones at 16px give roughly 35-45ch, which is fine; do not shrink type to fit more.
- Justified text needs at least 50-60ch and hyphenation, or it opens rivers.
- CJK: 30-40 full-width characters per line. Arabic: similar to Latin in words per line, so 50-70ch equivalent.

## Line-height by role

Line-height falls as size rises, rises as measure widens, and rises with large x-heights and on dark backgrounds.

| Role | Size | Line-height | Token |
| --- | --- | --- | --- |
| Display | 64px+ | 0.95-1.05 | unitless value or `--line-height-tight` (1.1) |
| H1-H2 | 30-60px | 1.1-1.2 | `--line-height-tight` |
| H3-H4, card titles | 20-24px | 1.25-1.3 | `--line-height-snug` |
| UI body, inputs | 14-16px | 1.4-1.5 | `--line-height-normal` |
| Long-form body | 16-20px | 1.55-1.7 | `--line-height-relaxed` (1.65) |
| Captions, helper text | 12-14px | 1.35-1.45 | `--line-height-snug` to `--line-height-normal` |
| Buttons, tags (single line) | any | 1-1.25 | padding sets the height, not leading |
| Table cells | 13-14px | 1.25-1.4 | `--line-height-snug` |

Use unitless line-heights so they scale with font size. For a 4px baseline, check that size x line-height lands on a multiple of 4 (16 x 1.5 = 24, 20 x 1.4 = 28).

## Tracking by size

| Size or role | Letter-spacing | Token |
| --- | --- | --- |
| 64px+ display | -0.03 to -0.04em | `--letter-spacing-tight` plus a local -0.01 to -0.02em |
| 32-48px headings | -0.01 to -0.02em | `--letter-spacing-tight` |
| 14-24px text | 0 | `--letter-spacing-normal` |
| 11-13px small text | +0.01 to +0.02em | `--letter-spacing-wide` |
| All-caps labels, overlines | +0.05 to +0.12em | `--letter-spacing-caps` (0.06em) |

Fonts with an optical-size axis or separate Display cuts already tighten at large sizes; reduce the negative tracking by half when using them. Never track lowercase body text open for "elegance"; it slows reading.

## Weights

- Body 400. On dark backgrounds, light text looks heavier: drop 20-50 units on a variable font or use a grade axis if the font has one.
- UI emphasis 500-600 (`--font-weight-medium`, `--font-weight-semibold`). Headings 600-700 (`--font-weight-bold`).
- Rule of thumb: hierarchy needs at least 200 weight units between body and heading, or a 1.5x size difference, or both.
- Thin weights (100-300) only at 32px+ and only in high-contrast color.
- Load only the weights in use; 3-4 static files or one variable file.

## Fluid type with clamp()

Fluid type interpolates between a minimum size at a small viewport and a maximum at a large one.

Formula, with `vmin` and `vmax` the viewport widths in px:

```text
slope     = (max_px - min_px) / (vmax - vmin)
intercept = min_px - slope * vmin
font-size: clamp(min_px/16 rem, intercept/16 rem + slope*100 vw, max_px/16 rem)
```

Worked example: an H1 that is 32px at 360px wide and 64px at 1280px wide.

```text
slope     = (64 - 32) / (1280 - 360) = 0.03478   -> 3.4783vw
intercept = 32 - 0.03478 * 360 = 19.478px        -> 1.2174rem
font-size: clamp(2rem, 1.2174rem + 3.4783vw, 4rem);
```

Body from 16px to 18px over the same range: `clamp(1rem, 0.9511rem + 0.2174vw, 1.125rem)`.

A marketing scale that grows from ratio 1.2 on base 16 (at 360px) to ratio 1.333 on base 18 (at 1280px):

| Step | Role | Min px | Max px | CSS |
| --- | --- | --- | --- | --- |
| 0 | Body | 16 | 18 | `clamp(1rem, 0.9511rem + 0.2174vw, 1.125rem)` |
| 1 | Lead, H4 | 19.2 | 24 | `clamp(1.2rem, 1.083rem + 0.5207vw, 1.499rem)` |
| 2 | H3 | 23 | 32 | `clamp(1.44rem, 1.221rem + 0.9717vw, 1.999rem)` |
| 3 | H2 | 27.6 | 42.6 | `clamp(1.728rem, 1.362rem + 1.628vw, 2.664rem)` |
| 4 | H1 | 33.2 | 56.8 | `clamp(2.074rem, 1.495rem + 2.571vw, 3.552rem)` |
| 5 | Display | 39.8 | 75.8 | `clamp(2.488rem, 1.609rem + 3.908vw, 4.735rem)` |

Accessibility rules for fluid type:

- Always keep a rem term in the middle value; pure `vw` text does not grow with browser zoom (WCAG 2.2 SC 1.4.4 Resize Text).
- Keep the maximum at or below 2.5x the minimum; Maxwell Barvian's analysis (Smashing Magazine, 2023) shows that ratio still reaches 200% under zoom in modern browsers. Then test 200% zoom anyway.
- Keep steps below 0 fixed; they shrink as the ratio grows.
- Product UI text (`--font-size-xs` to `--font-size-lg`) stays fixed; only headings and display go fluid.

## Generating a scale with the kit script

The kit ships a standard-library scale generator. Check the exact flags first:

```sh
python3 ../../../library/scripts/type_scale.py --help
```

Typical runs (static, then fluid, then CSS ready to paste):

```sh
python3 ../../../library/scripts/type_scale.py --base 16 --ratio 1.25
python3 ../../../library/scripts/type_scale.py --fluid --min-base 16 --max-base 18 --min-ratio 1.2 --max-ratio 1.333 --min-vw 360 --max-vw 1280
python3 ../../../library/scripts/type_scale.py --fluid --min-base 16 --max-base 18 --min-ratio 1.2 --max-ratio 1.333 --min-vw 360 --max-vw 1280 --format css
python3 ../../../library/scripts/type_scale.py --list-ratios
```

The script's fluid default range is 360-1440px, so pass `--max-vw 1280` to match the token container. It names steps -2 to 6 as `--font-size-xs` to `--font-size-5xl` (change with `--down`, `--up` and `--prefix`). The fluid run above reproduces the marketing table in this file. For product UI keep the contract's fixed `xs` to `lg` values and take only the upper steps from the script. Without the script, apply the formula by hand; it is exact.

## Minimal CSS

```css
:root { font-size: 100%; }                      /* respect the user's default */
body {
  font-family: var(--font-family-body);
  font-size: var(--font-size-md);
  line-height: var(--line-height-normal);
  font-synthesis: none;
}
h1, h2, h3 {
  font-family: var(--font-family-display);
  line-height: var(--line-height-tight);
  letter-spacing: var(--letter-spacing-tight);
  text-wrap: balance;
}
p, li { max-inline-size: var(--measure-body); text-wrap: pretty; }
.overline { font-size: var(--font-size-xs); letter-spacing: var(--letter-spacing-caps); text-transform: uppercase; }
```
