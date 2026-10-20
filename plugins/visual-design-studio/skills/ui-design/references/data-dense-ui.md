# Data-dense UI: tables and dashboards

Version-Timestamp: 2026-10-20 02:04:32 UTC

Dense interfaces succeed through alignment, hierarchy and restraint, not through removing data. Expert users want more on screen, faster paths and predictable layouts. The deep table spec with full state logic is the kit's [data table example](../../../library/examples/component-specs/data-table.md). Chart choice and data palettes belong to the `data-visualization` skill.

## Table defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Text columns | Left-aligned, header left-aligned | RTL locales: mirror |
| Numeric columns | Right-aligned, header right-aligned, `font-variant-numeric: tabular-nums` | Identifiers that are not quantities (order 10423): left |
| Decimals | Same number of decimals per column; units in the header ("Revenue (USD)") | |
| Negative values | Minus sign (U+2212) plus `--color-danger-fg` or parentheses in accounting contexts | Never color alone |
| Dates | One format per column, sortable; relative ("2 h ago") only with the absolute date on hover or focus | |
| Row height | Compact 32px, default 40px, comfortable 48px | IBM Carbon offers 24-64px row sizes; pick one default and let users switch |
| Cell padding | 12-16px horizontal (`--space-3`/`--space-4`) | Compact: `--space-2` |
| Header | Sticky, `--font-weight-semibold`, `--color-fg-muted`, bottom border `--color-border-default` | |
| Row separators | 1px `--color-border-subtle`; zebra stripes optional for wide tables (6+ columns) | |
| Row hover | `--color-bg-sunken` | Touch: no hover; use selection state |
| Truncation | Ellipsis after 1 line (2 for descriptions), full value on hover and focus, expandable | Key identifiers never truncate |

## Sticky headers and columns

- `position: sticky; top: 0; z-index: var(--z-sticky)` on header cells inside the scroll container.
- Pin the identifier column on wide tables; show a subtle shadow when content scrolls under it.
- Set `scroll-padding-top` equal to the header height so keyboard focus is never hidden (WCAG 2.4.11).
- For page-level scrolling with a sticky app header, offset the table header by the app header's height.

## Sorting

- Sortable headers are buttons inside `th`; the sorted column carries `aria-sort="ascending"` or `"descending"`.
- Show an arrow on the sorted column and a faint affordance on hover or focus of sortable ones.
- Default sort is meaningful (most recent first, highest priority first) and stated.
- First click sorts in the most useful direction for that data (dates descending, names ascending).
- Multi-column sort (Shift+click) only for expert tools, with the sort order shown.
- Persist sort per user and put it in the URL.

## Filtering and search

- Filter bar above the table: a search field, the 2-4 most used filters as dropdown buttons, and "More filters" for the rest.
- Applied filters appear as removable chips with "Clear all", and the result count updates ("128 of 4,210 orders").
- Desktop: apply filters instantly. Mobile: filters in a sheet with an "Show 128 results" button.
- Saved views (filters + sort + columns) for recurring tasks; share by URL.
- Zero results: show the active filters and a one-click way to remove the most restrictive one.

## Pagination, load more and virtualization

| Pattern | Use when | Notes |
| --- | --- | --- |
| Pagination (25, 50, 100 per page) | People need position, references or a footer | Show "1-50 of 4,210"; keep page in URL |
| Load more | Browsing lists with a footer | Keep focus on the first new item |
| Infinite scroll | Feeds without a destination | Breaks footers, Back and "where was I"; avoid for task-based tables |
| Virtualization | Hundreds of complex rows, or thousands of simple ones, rendered at once | Use `aria-rowcount` and `aria-rowindex`; browser find-in-page and some screen readers only see rendered rows, so add a search |

Server-side sort, filter and pagination once data exceeds what the client can load in under 1 second.

## Selection and bulk actions

- Checkbox column 40-48px wide; header checkbox is tri-state (none, some, all on page).
- Selecting rows shows a bulk action bar in place of the filter bar: "3 selected", the actions, and "Clear selection".
- After selecting all on a page, offer "Select all 4,210 orders" across pages, and state it clearly.
- Destructive bulk actions confirm with the count and the object ("Delete 12 invoices?"); offer Undo where possible.
- Shift+click selects a range; keyboard: Space toggles the focused row.

## Row actions and detail

- Up to 2 frequent actions inline; the rest in an overflow menu at row end with a specific label ("Actions for invoice 1042").
- Actions revealed on hover must also appear on focus and on touch devices.
- Row click opens the detail (side panel 360-480px for quick review, full page for deep work); links inside the row remain separately focusable.
- Inline editing: Enter or double-click to edit a cell, Enter saves, Esc cancels, with visible saving and error states per cell.

## Column management

- Resize by dragging the header edge, with a keyboard alternative (WCAG 2.5.7).
- Show, hide and reorder columns from a "Columns" menu; pin columns left.
- Density switcher (compact, default, comfortable) in the same menu.
- Export to CSV of the current filtered view.

## Table states

| State | Show |
| --- | --- |
| Loading first time | Header plus 5-10 skeleton rows matching column widths |
| Refreshing | Existing data stays; a thin progress bar at the top; `aria-busy="true"` |
| Empty, no data yet | Explanation and the primary create or import action |
| Empty, no results | Active filters and how to broaden them |
| Error | Message with Retry; if stale data exists, keep it with a "Last updated 10:42" banner |
| Partial | Rows that loaded, plus an inline notice for what failed |
| No permission | What is restricted and who can grant access |

## Semantics and responsive behavior

- Use a real `table` with `caption`, `th scope="col"` and `scope="row"`. Use the ARIA grid pattern only when cells need arrow-key navigation (spreadsheets, editable grids).
- Narrow screens: keep the table in a horizontally scrolling region (`tabindex="0"`, labeled, with a visible scroll shadow) and a sticky first column; or, under 640px, switch to a card list showing the 3-5 most important fields with a link to the full record. Never drop data without a path to it.

## Dashboards

**Decide the job first.** Operational dashboards monitor live status and need alerts and freshness; analytical dashboards support exploration and need filters and drill-down; strategic dashboards report a few KPIs over long periods. Stephen Few's rule from *Information Dashboard Design*: the essentials fit on one screen.

**Layout:**

- 12-column grid with `--space-4` to `--space-6` gaps.
- Top row: 3-6 KPI cards. Then trends over time. Then breakdowns. Then detail tables.
- Most important information top-left for left-to-right readers.
- 5-9 visualizations per view is a practical ceiling; split by role or task beyond that.

**KPI card anatomy:**

| Part | Rule |
| --- | --- |
| Label | Plain name with a definition on hover or focus ("Active customers: paid accounts with a login in the last 30 days") |
| Value | `--font-size-2xl` to `--font-size-4xl`, `tabular-nums`, abbreviated sensibly (1.24M) with the exact value on hover |
| Comparison | Change versus the previous period with sign, arrow and text ("+4.2% vs last month"); color is a third cue, not the only one |
| Context | Target, threshold or sparkline |
| Freshness | "Updated 5 min ago" at card or dashboard level |

**Controls:** global date range and segment filters at the top, applied to every widget, with the current state always visible. Widgets that ignore a global filter say so.

**Drill-down:** clicking a chart segment or KPI opens the underlying table already filtered.

**States per widget:** skeleton while loading, inline error with Retry that does not break the rest of the dashboard, explicit "No data for this period", partial-data notices.

**Performance:** load the first row first, lazy-load widgets below the fold, cache expensive queries, and show the data's timestamp rather than pretending to be real-time.

**Personalization:** let people reorder and hide widgets only when several roles share one dashboard; otherwise design separate role-based views.

## Density principles

- Remove chrome before data: lighter borders (`--color-border-subtle`), fewer boxes, alignment and whitespace for grouping.
- Hierarchy through weight and color tone (`--color-fg-default`, `--color-fg-muted`), not size jumps.
- Consistent alignment axes across tables, forms and cards on the same screen.
- Keyboard paths for every frequent action; show shortcuts in tooltips.
- Query `audience.expert-power-users` and `style.data-dense-utilitarian` in the atlas for defaults that differ from general products.
