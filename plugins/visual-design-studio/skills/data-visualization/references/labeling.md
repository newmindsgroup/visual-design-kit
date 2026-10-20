# Labeling, axes and number formatting

Version-Timestamp: 2026-10-20 02:07:10 UTC

Text does most of the work in a good chart. The title states the finding, labels sit on the data, axes are honest, and numbers are formatted for the reader's locale and precision needs.

## Title, subtitle, source

| Part | Rule | Example |
| --- | --- | --- |
| Title | The takeaway, 12 words or fewer, sentence case | "Online orders overtook store sales in March" |
| Subtitle | What is measured, unit, scope, period | "Monthly revenue by channel, USD millions, Jan 2025 to Jun 2026" |
| Source and notes | Source, date, definitions, exclusions, below the chart in `--font-size-xs` | "Source: company finance data, July 2026. Store sales exclude franchise locations." |

Exploratory dashboards can use descriptive titles ("Revenue by channel"); explanatory charts (reports, decks, articles, social) state the finding. Do not write a takeaway the data does not support.

## Direct labels

- **Lines:** label each line at its right end (left end in RTL layouts) in the series color, darkened to 4.5:1 for text (see [data palettes](data-palettes.md)). Nudge labels vertically to avoid collisions; add a thin leader line if a label moves far from its line.
- **Bars:** put values at the bar end, outside the bar, unless the bar is long enough to hold the label inside with 4.5:1 contrast. When every bar is labeled, remove the value axis and gridlines.
- **Pies and donuts:** label segments directly with name and percentage; no legend.
- **Scatterplots:** label only highlighted or extreme points.
- **Legends,** when unavoidable: above the chart, horizontal, in the same order as the data (top series first), with swatches shaped like the marks (lines for lines, squares for bars).

## Annotation

- Annotate 1-3 things: an event (launch, policy change), a threshold or target, an outlier or the peak.
- Reference lines (target, average) are dashed 1px in `--color-fg-muted`, labeled at their end ("Target 95%").
- Event markers: a thin vertical rule with a short label at the top.
- Annotation text is 12-14px, `--color-fg-muted`, set in sentence case close to the point it explains; connectors are 1px and do not cross data.
- Shaded ranges (recessions, campaign periods) use a very light neutral band behind the data.

## Axes and baselines

- **Bars and areas start at zero.** Length encodes value; a cut axis exaggerates differences. If differences are small relative to values, switch to a dot plot or show the change directly.
- **Lines may start above zero** when the range of change is the story (temperatures, stock prices, rates); make the axis start value clearly visible and never imply a zero that is not there.
- **No broken bar axes.** If one bar dwarfs the rest, use a log scale (labeled), a separate panel, or label the outlier and clip it with a clear break symbol.
- **Ticks:** 3-6 per axis on round values (intervals of 1, 2, 2.5 or 5 times a power of 10). Put the unit on the top tick only ("40%") or in the subtitle.
- **Time axes:** equal spacing for equal time; label sparingly (Jan, Apr, Jul, Oct; the year at boundaries). Show gaps for missing periods; do not interpolate across them silently.
- **Aspect ratio of line charts:** aim for an average slope near 45 degrees (Cleveland's "banking to 45"); a very wide chart flattens change, a very tall one exaggerates it.
- **No rotated labels.** If category labels do not fit horizontally, switch to a horizontal bar chart.
- **Dual axes:** avoid. Use two aligned charts or index both series to 100 at a shared start date.
- **Y-axis title:** place the unit horizontally above the axis rather than rotated 90 degrees.

## Units

- State the unit once, clearly: in the subtitle, the axis title, or the top tick.
- Distinguish percent from percentage points: a rate going from 4% to 6% is "+2 pp" or "+50%".
- Normalize where comparison demands it: per capita, per 1,000 users, inflation-adjusted, seasonally adjusted. Say so in the subtitle.
- Keep units and scales identical across small multiples, or label each clearly.

## Number formatting

| Situation | Format | Example |
| --- | --- | --- |
| Data labels and tiles | 2-3 significant digits, compact notation | 1.2M, 34.5K, 920 |
| Tables and tooltips | Full precision with separators | 1,234,567 |
| Currency | Symbol and code where ambiguous | $1.2M, US$1.2M, EUR 1.2M |
| Percent | Fixed decimals within a chart | 12.5%, 3.0%, 48.2% |
| Change | Signed, with a real minus (U+2212) | +3.2%, −1.4% |
| Accounting tables | Parentheses for negatives, if the audience expects them | (1,240) |
| Missing value | Em dash or "n/a", with a note; never 0 | — |
| Rounding | Note when parts do not sum to the total | "Percentages may not add to 100 because of rounding." |

Locale conventions differ; format with the platform's locale tools rather than by hand:

| Locale | One million and a quarter |
| --- | --- |
| en-US, en-GB | 1,250,000.00 |
| de-DE | 1.250.000,00 |
| fr-FR | 1 250 000,00 (narrow no-break spaces) |
| de-CH | 1'250'000.00 |
| en-IN, hi-IN | 12,50,000.00 (lakh grouping; 1 crore = 10,000,000) |

```js
const compact = new Intl.NumberFormat(locale, { notation: "compact", maximumSignificantDigits: 3 });
const pct = new Intl.NumberFormat(locale, { style: "percent", minimumFractionDigits: 1, maximumFractionDigits: 1 });
const money = new Intl.NumberFormat(locale, { style: "currency", currency: "EUR", notation: "compact" });
const signed = new Intl.NumberFormat(locale, { signDisplay: "exceptZero", maximumFractionDigits: 1 });
compact.format(1234567);   // "1.23M" in en-US
```

Dates: store ISO 8601 (2026-03-04); display in the locale's format, and avoid numeric-only dates (03/04/2026 means March 4 in the US and 3 April elsewhere). Use month names or abbreviations on axes.

## Tooltips

- Show series name, exact value with unit, and the date or category, formatted like the table.
- Tooltips are supplementary: anything essential is visible without them.
- They must open on keyboard focus as well as hover, stay open while the pointer moves onto them, and close with Escape (WCAG 2.2 SC 1.4.13 Content on Hover or Focus).
- On touch, open on tap and close on tap outside.

## Chart typography

- Use the product's body face with tabular lining figures: `font-variant-numeric: tabular-nums lining-nums;`.
- Sizes: tick and data labels 12px minimum (13-14px preferred), axis titles 12-14px, chart titles 16-20px, KPI numbers 28-48px. On slides and signage scale with the medium.
- Axis labels in `--color-fg-muted`; data labels in `--color-fg-default` or the darkened series color.
- Sentence case for all labels; avoid all caps except very short overlines.

## Labeling checklist

- Title states the takeaway; subtitle carries unit, scope and period; source and date present.
- Direct labels used; legend only where unavoidable, in data order.
- Bars start at zero; no dual axes; no rotated labels.
- Units clear; percent vs percentage points correct.
- Numbers formatted for the locale with consistent precision and real minus signs.
- Tooltips reachable by keyboard and never the only place for key values.
