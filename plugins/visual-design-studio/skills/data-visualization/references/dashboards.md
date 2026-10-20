# Dashboards

Version-Timestamp: 2026-10-20 02:07:10 UTC

A dashboard exists to support decisions. Start from who decides what, how often, and with what data; then show the fewest numbers and charts that answer those questions. Component behavior (filters, tables, tabs, states) follows the `ui-design` skill; this reference covers the data side.

## Kinds of dashboard

| Kind | User and rhythm | Shape |
| --- | --- | --- |
| Operational | Support leads, logistics, on-call engineers; glanced at constantly | Few big numbers, thresholds, alerts, live updates, fits one screen (often a 1920x1080 wall display) |
| Analytical | Analysts, product and marketing teams; explored weekly | Filters, comparisons, drill-down, tables, exports; scrolling is fine |
| Strategic | Executives, boards; read monthly or quarterly | 4-6 KPIs against targets, trends, short written commentary |
| Embedded customer analytics | End users of a SaaS product | Plain language, sensible defaults, few controls, explanations of each metric |

## KPI hierarchy

1. **Tier 1: headline KPIs** (top row, 3-6 tiles). The north-star metric and its direct drivers.
2. **Tier 2: explanation** (middle). Trend and breakdown charts that explain why the Tier 1 numbers moved.
3. **Tier 3: detail** (bottom or drill-down). Tables, segments, individual records.

Each KPI needs: a precise definition (shown in an info tooltip or help panel), a period, a comparison (previous period, same period last year, or target), and an owner. If nobody can say what decision a tile changes, remove it.

## KPI tile anatomy

| Element | Spec |
| --- | --- |
| Label | What and period: "Net revenue, last 30 days"; `--font-size-sm`, `--color-fg-muted` |
| Value | 28-48px, tabular figures, compact format ("$1.24M"); full value in a tooltip or on drill-down |
| Comparison | "▲ 8.2% vs previous 30 days": arrow, signed number, text, and color for good or bad |
| Good direction | Color by whether the change is good, not whether it is up: churn up is bad (danger), cost down is good (success) |
| Sparkline (optional) | 1.5px line, no axes, last point marked; never the only place a value appears |
| Status (optional) | On track, at risk, off track: icon plus text plus status color |
| Action | The whole tile links to the explanatory view |

Screen readers should hear the tile as a sentence: "Net revenue, last 30 days: 1.24 million US dollars, up 8.2% compared with the previous 30 days."

## Layout

- Use a 12-column grid with 16-24px gutters (see the `layout` skill). KPI tiles span 3 columns (4 across) or 2 (6 across); main charts span 6 or 12; tables span 12.
- Most important at top left (top right in RTL). Read order matches the KPI hierarchy.
- Keep card heights equal within a row; align chart plot areas so axes line up across cards.
- Operational wallboards: no scrolling, 3-6 elements, numbers readable from 3-5m (KPI values 64px+ at 1080p).
- Analytical views: 4-8 charts per view; move the rest to tabs or drill-downs instead of an endless scroll of equal-weight cards.
- Phones: KPI tiles 2 across, charts full-width and simplified (fewer series, fewer ticks), tables become lists or scroll with a sticky first column.

## Filters

- **Global filters** (date range, region, segment) sit in a sticky bar at the top, apply to everything, and show their current values in plain text.
- **Local filters** on a card affect only that card; mark them on the card.
- Show applied filters as removable chips and provide "Reset filters".
- Reflect the filter state in the chart subtitles ("EMEA, last 30 days") so screenshots and exports carry context.
- Persist filters in the URL so views can be shared and bookmarked.
- Cross-filtering (clicking a bar filters other charts) must be visible: highlight the selection, dim the rest, and offer a clear way out.
- Apply on change for fast queries; use an explicit Apply button when queries are slow, and show which filters are pending.

## Time ranges

- Presets: Today, Last 7 days, Last 30 days, Last 90 days, Last 12 months, Year to date, Custom. Default to the range that matches the decision rhythm (operational: today; analytical: 30 days; strategic: quarter or year).
- Comparison toggle: previous period or same period last year, drawn as a lighter or dashed line.
- Granularity follows the range: hourly for a day, daily up to about 90 days, weekly or monthly beyond. Aim for 30-100 points on a line.
- Mark incomplete periods (the current week or month) with a dashed segment or lighter bar and a note; otherwise every chart appears to collapse at the end.
- Show the time zone when it matters and a data freshness stamp: "Updated 5 minutes ago".

## Density

- Analysts accept compact density (32px table rows, 13-14px text); executives and customers need default density and more whitespace.
- Remove chart junk before shrinking: gridlines, borders, redundant legends, repeated axis titles.
- Use small multiples instead of one crowded chart.
- Provide a density toggle for heavy users (see the `layout` skill's spacing reference).

## States

| State | Show | Avoid |
| --- | --- | --- |
| Loading | Skeletons shaped like the chart and tile; keep layout stable; keep showing previous data with an "Updating" indicator on refresh | A spinner in every card; layout jumps when data arrives |
| Empty: no data for the filters | "No orders in EMEA for the last 7 days." plus actions: widen the range, clear filters | A blank chart frame or a zero line that implies a real zero |
| Empty: no data yet (first run) | What will appear, how to connect a source, optional sample data clearly labeled "Sample data" | Fake numbers that look real |
| Zero | A real zero is data: show 0 with its axis | Hiding the series |
| Partial or delayed data | Mark affected periods and say why | Silent gaps or interpolated lines |
| Error | Card-level error with what failed and a Retry button; the rest of the dashboard keeps working | Blanking the whole dashboard |
| Stale | "Data last updated 3 hours ago" in warning style when freshness matters | A current-looking dashboard with old data |
| No permission | Which data is restricted and who can grant access | Empty cards with no explanation |

## Live data and motion

- Update values in place without moving the layout; animate number changes and transitions in 200-300ms with `--ease-standard` and `--duration-moderate`.
- No constant motion: pulsing, ticking or auto-rotating cards draw attention from the data. Respect `prefers-reduced-motion` (the token contract sets durations to near zero).
- Alerts for thresholds: one clear visual state plus a notification, not flashing.

## Export and sharing

- CSV of the data behind each chart; PNG or PDF of the view with filters and timestamp printed on it.
- Shareable link with filters encoded.
- Printed or exported views include title, subtitle, source and freshness.

## Dashboard checklist

- Every tile and chart maps to a decision and an owner; definitions available.
- 3-6 headline KPIs with comparisons and good-direction coloring.
- Filters global, visible, persistent, and reflected in subtitles.
- Time ranges with presets, comparison, sensible granularity and incomplete-period marking.
- Loading, empty, zero, error, stale and permission states designed.
- Charts follow [chart selection](chart-selection.md), [labeling](labeling.md) and [data palettes](data-palettes.md); tiles and charts accessible per [accessible charts](accessible-charts.md).
- Table behavior follows the kit's [data table spec](../../../library/examples/component-specs/data-table.md).
