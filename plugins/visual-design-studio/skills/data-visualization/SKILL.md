---
name: data-visualization
description: >-
  Load before answering any chart, graph, dashboard, infographic or chart-color question, even a quick one: it holds
  the kit's tested defaults. Covers chart choice by task, colorblind-safe categorical palettes (Okabe-Ito, limits past
  8 series), OKLCH sequential and diverging scales for light and dark mode, 3:1 mark contrast, direct labels, number
  formats, KPI tiles, dashboards with filters and empty states, and accessible charts with text alternatives and data
  tables.
license: MIT
metadata:
  version-timestamp: "2026-10-20 11:40:00 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 02:07:10 UTC"
---

# Data visualization

Excellent data visualization answers one question per chart, truthfully and fast: the right chart for the task, a title that states the finding, direct labels instead of legend hunting, color that encodes something, honest axes, and an equivalent that works without sight or color.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Chart by task | Compare: bar. Change over time: line. Relationship: scatter. Distribution: histogram or box/strip plot. Part of whole: stacked or 100% bar. Exact lookup: table | See [chart selection](references/chart-selection.md) for the full table and failure modes |
| Pie and donut | Only for 2-4 parts of a real whole, labeled directly | More parts, or comparisons between pies: use bars |
| Categorical color | Up to 6 series (8 at most) from the Okabe-Ito set; or one highlight hue with the rest neutral gray | More than 8 categories: group into "Other", use small multiples, or label directly without color |
| Sequential and diverging | OKLCH single-hue ramp, L 0.96 to 0.31, 5-9 steps; diverging around a neutral midpoint near L 0.95 | Diverging only when the data has a meaningful center (zero, target, average) |
| Mark contrast | 3:1 against the background for bars, lines, points and segment boundaries (WCAG 2.2 SC 1.4.11) | Light marks get a darker outline or a direct label |
| Title | States the takeaway in 12 words or fewer ("Returns fell 18% after the size guide launched") | Exploratory tools: a neutral descriptive title plus a dynamic summary |
| Labels | Direct labels at line ends and on bars; legend only when direct labels collide | Dense scatterplots: label only the highlighted points |
| Axes | Bars start at zero; lines may start elsewhere with the break made obvious; units in the axis title or tick suffix | Log scales only for multiplicative data, labeled "log scale" |
| Gridlines | Horizontal, light (`--color-border-subtle`), 3-6 of them | None when every bar is directly labeled |
| Numbers | Tabular figures, locale separators, 2-3 significant digits on labels, real minus sign (U+2212) | Finance tables show full precision |
| Type sizes | Tick and data labels 12px minimum, axis titles 12-14px, chart titles 16-20px | Slides and signage: scale with the medium (see the `typography` skill) |
| Marks | Lines 2px (highlight 3px), points 6-8px, bar gaps 20-40% of bar width | Sparklines: 1.5px, no axes |
| Dashboards | 3-6 KPI tiles in the top row, 4-8 charts per view, filters at the top and persistent | Operational wallboards: fewer, larger numbers |
| Accessibility | Text summary plus a data table, non-color cues, keyboard access for interactive charts | Never skip; see [accessible charts](references/accessible-charts.md) |
| Motion | 200-400ms transitions between states, `--ease-standard`; none under reduced motion | Data stories can sequence reveals, still with a static equivalent |

## Workflow

1. **Write the question** the reader needs answered ("Which region grew fastest this year?") and the takeaway, if known. One primary question per chart.
2. **Check the data:** units, denominators, time span, missing values (missing is not zero), estimates vs measurements, source and date. Never invent or round away inconvenient values.
3. **Choose the chart** from [chart selection](references/chart-selection.md). Sketch two options and pick the one that needs less decoding.
4. **Encode color** with [data palettes](references/data-palettes.md): categorical, sequential or diverging as the data demands, in light and dark variants, with 3:1 marks.
5. **Label** with [labeling](references/labeling.md): takeaway title, direct labels, honest axes, formatted numbers, source line.
6. **Annotate** the one or two points that matter (a launch date, a threshold, an outlier).
7. **Compose** dashboards with [dashboards](references/dashboards.md) and data stories or infographics with [infographics](references/infographics.md).
8. **Make it accessible** with [accessible charts](references/accessible-charts.md): summary, table, non-color cues, keyboard and screen reader support.
9. **Render and inspect** at the real size, in light and dark, in grayscale, with color-vision-deficiency emulation (Chrome DevTools Rendering panel), with the longest labels and with empty, loading and error data. Recompute every number shown against the source. Use the `design-critique` skill's render loop.

## Decisions that change the answer

- **Audience:** executives need the takeaway and one number; analysts need exploration, exact values and export; the public needs plain language, a takeaway title and fewer series; `audience.low-literacy-plain-language` favors simple bars and icons with numbers.
- **Medium:** interactive web charts can hide detail in tooltips (with accessible equivalents); print, slides and social cannot; signage needs huge numbers and one chart.
- **Style:** `style.data-dense-utilitarian` favors small multiples, tight spacing and mono figures; `style.editorial-magazine` favors annotated, story-driven charts; `style.swiss-international` favors thin bars, hairline rules and direct labels; playful styles may use pictograms (still with exact values).
- **Market:** number and date formats, RTL axis direction, and the meaning of red and green for financial change differ by market (see the `color` skill's meaning reference and `market.*` entries).
- **Brand:** chart palettes derive from the brand but must be tested for distinguishability; a brand ramp is rarely a good categorical palette.

## Common failures

- **Rainbow palettes and 12-color legends.** Fix: highlight plus gray, or small multiples.
- **Truncated bar axes.** A bar from 95 to 100 exaggerates a 5% difference. Fix: start at zero or switch to a dot plot.
- **Dual y-axes.** Readers infer false correlations. Fix: two aligned charts, or index both series to 100.
- **3D, shadows and gradients on marks.** They distort size. Fix: flat marks.
- **Legend hunting.** Fix: direct labels in the series color (text darkened to 4.5:1).
- **Pie charts for comparisons.** Fix: sorted bars.
- **Unformatted numbers** (1234567.891). Fix: "1.23M" in labels, full values in tooltips and tables.
- **Tooltip-only information.** Hover is invisible to touch, keyboard and print. Fix: show key values; make tooltips focusable.
- **Color-only meaning.** Fix: shapes, patterns, labels.
- **Decorative dashboards.** Twenty tiles, no decision. Fix: a KPI hierarchy tied to the decisions users make.

## References

- [Chart selection](references/chart-selection.md): task-to-chart table with failure modes.
- [Data palettes](references/data-palettes.md): Okabe-Ito in hex, OKLCH sequential and diverging ramps, mark contrast, dark-mode variants.
- [Labeling](references/labeling.md): titles, direct labels, annotation, axes, baselines, units and number formatting.
- [Dashboards](references/dashboards.md): KPI hierarchy, layout, filters, time ranges, density, empty and loading states.
- [Infographics](references/infographics.md): story structure, information hierarchy, production.
- [Accessible charts](references/accessible-charts.md): text alternatives, data tables, patterns and shapes, keyboard and screen readers.
- Atlas: `python3 ../../library/scripts/atlas.py query "..."` for style and audience defaults; IDs in [the registry](../../library/atlas/registry.json).
- Sibling skills: `color` for ramps and contrast math ([contrast](../color/references/contrast.md)), `typography` for numerals ([setting](../typography/references/setting.md)), `ui-design` for dashboard components, filters and states, `layout` for dashboard grids.
- Deep process for client projects: [design-infographics](../../library/draft-skills/design-infographics/SKILL.md) with [information design](../../library/draft-skills/design-infographics/references/information-design.md) and [layouts](../../library/draft-skills/design-infographics/references/layouts.md); the [infographic specification template](../../library/templates/infographic-spec.md); [data-driven screen content](../../library/draft-skills/design-screen-data-content/SKILL.md); worked reasoning in [information and infographics](../../library/knowledge/information-and-infographics.md); a built example in [infographic story](../../library/examples/infographic-story/README.md).

Catalog IDs covered: infographics, screen-data-content
