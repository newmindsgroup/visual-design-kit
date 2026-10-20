# Chart selection

Version-Timestamp: 2026-10-20 02:07:10 UTC

Choose the chart from the reader's task, not from the data's shape or the tool's gallery. Position along a common scale is read most accurately, then length, then angle and area, then color intensity (the ranking from Cleveland and McGill's graphical perception studies, 1984). Prefer encodings near the top of that list for the comparison that matters most.

## Pick in three steps

1. Finish the sentence "The reader needs to see..." with one relationship: a comparison, a change over time, a distribution, a relationship between variables, a part of a whole, a ranking, a deviation from a reference, a flow, a location, or an exact value.
2. Find that row below and take the first option unless its failure mode applies.
3. Sketch the runner-up. Keep whichever needs less explanation.

## Task to chart

### Comparison between categories

| Chart | Use when | Failure modes |
| --- | --- | --- |
| Bar (horizontal for long labels) | Default for comparing values across categories | Truncated axis; unsorted bars when order has no meaning; too many bars (over 15-20: show top N plus Other) |
| Grouped bar | 2-3 series per category | Four or more series become a color puzzle; use small multiples |
| Dot plot | Values far from zero, or small differences between categories | Readers may expect bars; label the axis clearly |
| Lollipop | Many categories where bars feel heavy | Same rules as bars, including a zero baseline |
| Bullet chart | Actual against target and ranges | Too many qualitative bands; keep 2-3 |
| Table | Readers need exact values or many attributes | A wall of numbers with no highlighting; add a heat column or bold key cells |

### Change over time

| Chart | Use when | Failure modes |
| --- | --- | --- |
| Line | Continuous series, trends, many time points | More than 4-5 lines becomes spaghetti: highlight one, gray the rest, or use small multiples; uneven time intervals drawn as even |
| Column | Few discrete periods (months, quarters), counts per period | Many periods: switch to a line |
| Area (single series) | Volume or cumulative amount over time | Stacked areas over 3-4 layers: the middle layers are unreadable |
| Step line | Values that change at specific moments (prices, rates, plan tiers) | Smoothing a step series implies values that never existed |
| Slope chart | Two points in time, ranking changes | More than about 10 lines tangle |
| Sparkline | Trend context beside a number in a tile or table | No axis, so never the only place a value appears |
| Candlestick or OHLC | Finance price movement | Up and down colors differ by market (see the `color` skill's meaning reference) |

### Distribution

| Chart | Use when | Failure modes |
| --- | --- | --- |
| Histogram | Shape of one variable | Bin width changes the story; test 2-3 widths and state the one used |
| Box plot with points | Comparing distributions across groups | General audiences do not read box plots; add points or a strip plot, or explain |
| Strip, beeswarm, jitter | Small to medium data sets where individual points matter | Overplotting with large n; use transparency or a density plot |
| Violin or density | Large data, shape comparison | Smoothing invents data at the tails; show the sample size |
| Cumulative distribution | Percentiles ("80% of orders ship within 2 days") | Unfamiliar to many readers; annotate the key percentile |

### Relationship between variables

| Chart | Use when | Failure modes |
| --- | --- | --- |
| Scatter | Two numeric variables | Implying causation; overplotting; missing axis zero is fine but label it |
| Bubble | A third variable as size | Area misread as diameter; scale by area, include a size legend, cap the count |
| Connected scatter | Two variables over time | Hard for general audiences; annotate direction |
| Heatmap | Two categorical dimensions with a value (weekday by hour) | Sequential color only; include the scale; avoid rainbow |

### Part of a whole

| Chart | Use when | Failure modes |
| --- | --- | --- |
| Stacked bar | Composition plus total | Only the bottom segment shares a baseline; keep 2-4 segments |
| 100% stacked bar | Composition comparison across groups | Hides the totals; state them |
| Pie or donut | 2-4 parts of a real whole, one moment | Non-exclusive categories; more than 4-5 slices; comparing two pies |
| Waffle (10x10) | Percentages for general audiences | Over 3-4 categories |
| Treemap | Many parts in a hierarchy | Precise comparison is hard; label the largest cells only |

### Ranking

| Chart | Use when | Failure modes |
| --- | --- | --- |
| Sorted bar | Ranking at one time | Unsorted bars |
| Bump chart | Rank changes over several periods | Hides the size of the differences between ranks |

### Deviation from a reference

| Chart | Use when | Failure modes |
| --- | --- | --- |
| Diverging bar | Positive and negative values around zero, survey agreement scales | Sequential colors on diverging data; neutral midpoint missing |
| Variance bar | Actual minus target or budget | Readers confusing the variance with the value; label both |

### Flow and process

| Chart | Use when | Failure modes |
| --- | --- | --- |
| Sankey | Measured flows that reconcile from stage to stage | Widths not matching data; more than 4-5 stages |
| Funnel as horizontal bars | Stage conversion | Decorative funnel shapes distort the drop-off; use bars with percentages |
| Flow diagram | Non-quantitative process | Widths or sizes implying quantities that do not exist |

### Geography

| Chart | Use when | Failure modes |
| --- | --- | --- |
| Choropleth | Rates or normalized values by region | Raw counts (maps population, not the phenomenon); large empty regions dominate |
| Proportional symbol | Counts by location | Overlapping symbols; scale by area |
| Tile or hex grid map | Equal weight per region (states, countries) | Readers need a moment to orient; label tiles |
| Dot density | Distribution of individuals | Dots read as exact locations; state what one dot represents |

### Uncertainty

| Technique | Use when | Failure modes |
| --- | --- | --- |
| Error bars, intervals | Estimates with confidence intervals | Not stating what the interval is (95% CI, standard error, range) |
| Confidence band | Forecasts and model estimates over time | A crisp forecast line that hides the band |
| Fan chart | Forecast ranges widening over time | Too many bands; 2-3 levels |

### Single values

| Pattern | Use when | Failure modes |
| --- | --- | --- |
| KPI tile: value, comparison, sparkline | The number is the message | A number with no comparison (vs last period, vs target) means little |
| Big number with sentence | Editorial and social | Missing denominator or period |

## Small multiples

When one chart holds too many series, repeat a small chart per category on shared axes. Keep scales identical (or label clearly when they are not), sort panels meaningfully, and label each panel directly. Small multiples beat legends with 6+ entries.

## Chart or table?

Use a table when readers look up exact values, compare many attributes per row, or need to copy data. Use a chart when the pattern (trend, ranking, outlier) is the message. Dashboards often need both: the chart for the pattern, the table for the detail.

## Charts to avoid by default

- 3D bars, pies and areas: perspective distorts values.
- Dual-axis charts: two scales let you draw any correlation; use two aligned charts or index both to 100.
- Radar charts: area exaggerates differences and axis order changes the shape; use bars or a dot plot.
- Gauges: a lot of space for one number; use a bullet chart or a KPI tile with a target.
- Word clouds: size is not comparable and long words look more important; use a sorted bar of term counts.
