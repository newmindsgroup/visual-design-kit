# Data palettes

Version-Timestamp: 2026-10-20 02:07:10 UTC

Data color encodes something: a category, an order, or a direction from a center. Choose the palette type from the data, keep UI status colors out of data, and test every palette in light, dark, grayscale and simulated color-vision deficiency. All ratios below are WCAG 2.2, computed; the dark background is the kit's Meridian dark canvas `#0B0F12` (`--color-bg-canvas` in dark mode; see the `color` skill's dark mode reference).

## Which palette

| Data | Palette | Steps |
| --- | --- | --- |
| Unordered categories (regions, products) | Categorical | Up to 6, 8 at most |
| One category matters, others are context | Highlight plus gray | 1 accent plus 1 gray |
| Ordered values from low to high (density, revenue) | Sequential, single hue | 5-9 classes, or continuous |
| Values above and below a meaningful center (zero, target, average, neutral answer) | Diverging, two hues | 5-11 classes, odd number with a neutral middle |
| Two variables at once | Bivariate (3x3) | Expert audiences only; include a legend grid |

## Categorical: the Okabe-Ito set

Masataka Okabe and Kei Ito's Color Universal Design palette stays distinguishable for the common forms of color-vision deficiency because it varies lightness as well as hue. Recommended series order: blue, orange, bluish green, vermillion, sky blue, reddish purple, yellow, black.

| # | Name | Hex | OKLCH | On white | On dark canvas | Label text on white (4.5:1) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Blue | #0072B2 | 0.53 0.131 244 | 5.19 | 3.71 | #0072B2 |
| 2 | Orange | #E69F00 | 0.75 0.158 77 | 2.25 | 8.54 | #9F6D01 |
| 3 | Bluish green | #009E73 | 0.62 0.130 165 | 3.42 | 5.62 | #068661 |
| 4 | Vermillion | #D55E00 | 0.62 0.170 48 | 3.87 | 4.98 | #C25603 |
| 5 | Sky blue | #56B4E9 | 0.73 0.117 236 | 2.31 | 8.34 | #0E7DB0 |
| 6 | Reddish purple | #CC79A7 | 0.68 0.118 346 | 3.06 | 6.29 | #AB5B88 |
| 7 | Yellow | #F0E442 | 0.90 0.172 105 | 1.32 | 14.55 | #807804 |
| 8 | Black | #000000 | 0 0 0 | 21.00 | 1.09 | #000000 |

How to use it:

- **On white,** orange, sky blue and yellow fall below 3:1. Give those marks a 1px outline in a darker shade, place them where they sit next to a direct label, or use them only for areas that are also labeled. Do not darken the fills to force 3:1: darkening all colors to the same lightness collapses the lightness differences that make the set colorblind-safe.
- **On dark,** every color except black clears 3:1 on the canvas (blue drops to 3.02:1 on the raised surface `#1E2429`, so keep charts on the canvas or surface); replace black with the light neutral `--color-fg-default` (`#E2E9EF`, 15.70:1).
- **Direct labels in series color** use the darker "label text" variants so text passes 4.5:1 on white; on dark, the original hues already pass for large labels, and all but blue pass 4.5:1 for small ones (blue is 3.71:1, so use the light neutral for its label text).
- **More than 8 categories:** group the tail into "Other", use small multiples, or label directly and drop color.

## Highlight plus gray

The strongest default for explanatory charts: one series in an accent, everything else in a context gray.

| Role | Hex | On white | On dark canvas |
| --- | --- | --- | --- |
| Context gray (works in both modes): neutral 500 | #6F7982 | 4.44 | 4.34 |
| Highlight: Okabe-Ito vermillion | #D55E00 | 3.87 | 4.98 |
| Highlight: brand accent (Meridian) | `--color-accent-default`: #006C6C light, #4FC2C2 dark | 6.25 | 9.01 |

Make the highlight 3px and the context lines 1.5px so the difference survives grayscale and color-vision deficiency.

## Sequential (OKLCH, single hue)

Lightness carries the order; hue may drift slightly so the dark end does not go muddy. This teal-to-blue ramp starts near the kit's Meridian hue:

| Class | OKLCH | Hex | On white |
| --- | --- | --- | --- |
| 1 (lowest) | 0.96 0.025 190 | #E0F8F5 | 1.11 |
| 2 | 0.89 0.055 193 | #B1E7E5 | 1.36 |
| 3 | 0.80 0.085 197 | #77CFD0 | 1.81 |
| 4 | 0.70 0.105 203 | #37B1BB | 2.57 |
| 5 | 0.60 0.110 212 | #0390A4 | 3.80 |
| 6 | 0.50 0.105 225 | #076E8B | 5.81 |
| 7 | 0.40 0.090 240 | #034D73 | 9.08 |
| 8 (highest) | 0.31 0.075 255 | #133155 | 13.14 |

Rules:

- Even L steps (here about 0.08-0.10) read as even value steps. Use 5-7 classes for maps and heatmaps; continuous scales for smooth fields.
- Light classes are under 3:1 on white. In heatmaps and choropleths this is acceptable when every value is also available through labels, a table or tooltips, and when adjacent cells are separated by a 1px white or canvas-colored border.
- **Dark mode:** map high values to light classes (they stand out against a dark canvas) and drop classes that vanish; on `#0B0F12` classes 1-6 clear 3:1 (17.33 down to 3.31) and classes 7-8 do not.
- Never use a rainbow (jet, hsv) for ordered data: it has false boundaries and is not lightness-ordered. Perceptually uniform options such as viridis (from #440154 to #FDE725) are a well-tested alternative.

## Diverging (OKLCH, two hues)

Two hues of similar chroma with matched lightness steps on each side of a light neutral center. Vermillion-to-blue is safe for red-green color-vision deficiency.

| Class | OKLCH | Hex | On white |
| --- | --- | --- | --- |
| -4 | 0.42 0.14 35 | #892408 | 9.05 |
| -3 | 0.53 0.16 38 | #B54016 | 5.66 |
| -2 | 0.65 0.13 45 | #CF7347 | 3.39 |
| -1 | 0.78 0.075 55 | #DEAB8A | 2.04 |
| 0 (center) | 0.95 0.008 90 | #F0EEE9 | 1.16 |
| +1 | 0.80 0.06 245 | #9EC3E2 | 1.85 |
| +2 | 0.68 0.10 248 | #649DD3 | 2.87 |
| +3 | 0.55 0.13 252 | #2F74BB | 4.84 |
| +4 | 0.43 0.13 258 | #1B4D95 | 8.26 |

Rules:

- Center on a value that means something (zero change, target, 50%, neutral survey answer) and say what it is in the legend.
- Keep both sides symmetric in lightness so neither side looks more extreme.
- Avoid red-green diverging scales; if the brief demands red and green (finance), add signs, arrows and labels, and check the market's convention.
- For Likert survey bars, gray the neutral answer and put it in the middle or set it apart.

## Building a brand-tuned categorical palette

1. Start from the brand accent as series 1.
2. Add hues at least 60 degrees apart, alternating lightness (for example L 0.50, 0.70, 0.58, 0.45, 0.78) so the set separates in grayscale.
3. Keep chroma similar (within about 0.04) so no color shouts unless it should.
4. Exclude the status hues used in the UI, or move them 20+ degrees away, so a series never reads as an error.
5. Test: grayscale screenshot, Chrome DevTools vision-deficiency emulation (protanopia, deuteranopia, tritanopia), light and dark backgrounds, thin lines and small points. If two series merge in any test, change lightness first, hue second.
6. Compute contrast for each mark and label with `python3 ../../../library/scripts/color_tools.py contrast '<mark>' '<background>'`.

## Mark contrast rules (WCAG 2.2 SC 1.4.11)

- Bars, lines, points and pie segments that are needed to understand the chart need 3:1 against the background, or a 3:1 outline.
- Adjacent segments (stacked bars, pie slices) need a visible separator: a 1-2px gap in the background color works for any palette.
- Gridlines and axis lines are context; they may be lighter (`--color-border-subtle`) as long as data labels or ticks carry the values.
- Text inside or beside marks needs 4.5:1 (3:1 at 24px+ or 18.66px+ bold). White text on a light orange bar fails; put the label outside the bar.

## Palette checklist

- Palette type matches the data (categorical, sequential, diverging).
- No more than 6-8 categorical colors; tail grouped or small multiples used.
- Marks at 3:1 or outlined; labels at 4.5:1.
- Dark-mode variant defined, not inverted.
- Passes grayscale and CVD emulation; meaning also carried by labels, shapes or patterns (see [accessible charts](accessible-charts.md)).
- Status colors not reused as series colors.
