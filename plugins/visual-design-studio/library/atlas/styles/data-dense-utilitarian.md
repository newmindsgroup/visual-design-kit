---
id: style.data-dense-utilitarian
axis: style
name: Data-Dense / Utilitarian
aliases: [dense ui, terminal ui, trading ui, bloomberg style, ops dashboard, control room ui, information-dense, power-user interface]
summary: Maximum information per screen for expert users, with tabular figures, small type, tight rows, semantic color only, keyboard control and tiled panels, as in trading terminals and ops tools.
tags: [dense, data, utilitarian, trading, dashboard, tables, terminal, ops, expert, monospace]
pairs_with: [audience.expert-power-users, industry.fintech-banking, industry.logistics-supply-chain, industry.industrial-manufacturing-construction, industry.energy-climate, industry.saas-b2b, industry.crypto-web3, channel.web-app, archetype.sage, tier.mid-market]
avoid_with: [audience.children-under-13, audience.older-adults, audience.low-literacy-plain-language, tier.luxury, archetype.lover, channel.native-app]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Data-Dense / Utilitarian

## Essence

Treat the screen as an instrument panel. Experts working all day (traders, dispatchers, analysts, SREs, controllers) need many values visible at once, comparable at a glance, reachable by keyboard and trustworthy to the last digit. The Bloomberg Terminal (launched 1982; black ground, amber and green type, a command line and tiled panels) is the canonical example; modern equivalents include trading platforms, Grafana and Datadog-style observability, logistics control towers and process-control HMIs. Density here is respect, not clutter, provided hierarchy is rigorous.

## Visual signature

- Small, even type (11-13px) with tabular numerals; numbers right-aligned or decimal-aligned in columns.
- Tight rows (20-28px), 1px grid lines, almost no padding, no cards-within-cards.
- Tiled, resizable panels instead of a scrolling page; saved layouts and linked panels.
- Color is semantic only: up/down, severity, selection, freshness. Everything else is neutral.
- Charts as sparklines, small multiples and thin 1px lines with direct labels; heat cells in tables.
- Command line, hotkeys and context menus as primary control; the mouse is secondary.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Archivo (OFL, variable width: use SemiCondensed, wdth 75-90); IBM Plex Sans Condensed (OFL); commercial: Söhne Schmal, Berthold Akzidenz-Grotesk Condensed |
| Body font | Archivo at wdth 100 or IBM Plex Sans (OFL); commercial: Söhne, Akzidenz-Grotesk |
| Mono / numerals | Roboto Mono (OFL) or JetBrains Mono (OFL) for tickers and IDs; enable `font-variant-numeric: tabular-nums slashed-zero`; commercial: Akkurat Mono, Söhne Mono |
| Type scale ratio | 1.125 (major second): 11, 12, 13, 14, 16, 18, 22px; most of the UI is 12-13px |
| Body size / line-height | 12-13px / 1.3-1.4; table cells 12px / 20-24px row height; measure not applicable for tables, 70ch for help text |
| Display letter-spacing | 0 to -0.01em; titles are 14-16px weight 600, not display type |
| Caps / labels | 10-11px, uppercase, +0.04em to +0.06em, label gray, for column headers and panel titles |
| Weights | 400 data, 500 emphasis, 600 headers; avoid light weights because small type needs stem strength |
| Palette (dark) | Canvas #0D0D0D (oklch 0.16 0 0); Panel #171717 (oklch 0.20 0 0); Grid line #2E2E2E (oklch 0.30 0 0); Body text #E0E0E0 (oklch 0.91 0 0); Label gray #9A9A9A (oklch 0.69 0 0); Amber data #FFB000 (oklch 0.81 0.17 76); Up green #19C37D (oklch 0.72 0.164 158); Down red #FF5A4F (oklch 0.69 0.202 27) |
| Palette extras (dark) | Info cyan #4FC3F7 (oklch 0.77 0.127 231); Selection blue #1F4E8C (oklch 0.43 0.115 257) |
| Palette (light, ops) | Canvas #FFFFFF; Panel #F3F4F6 (oklch 0.97 0.003 265); Grid #D0D4D9 (oklch 0.87 0.008 254); Text #1C1F23 (oklch 0.24 0.009 256); Label #5B636D (oklch 0.50 0.019 254); Up #0E7A4B (oklch 0.51 0.117 157); Down #C62828 (oklch 0.54 0.194 27); Amber #8A5A00 (oklch 0.51 0.108 73) |
| Accent proportion | Color under 5% of pixels, only on changes, alerts and selection; amber as the single "primary data" hue on dark |
| Radius | 0-2px; panels are rectangles |
| Borders | 1px grid lines #2E2E2E (dark) or #D0D4D9 (light) between panels and rows; focus and selection use 1-2px colored outlines |
| Shadow / elevation | None; menus and popovers get a 1px border and `0 4px 12px rgb(0 0 0 / 0.4)` |
| Spacing density | 4px base; cell padding 4px vertical, 8px horizontal; panel padding 8px; panel gap 1-4px |
| Grid | Tiled panel layout (CSS grid with resizable splitters), 12-24 logical columns inside tables; support 1920x1080 through multi-monitor 5K |
| Motion | 0-100ms; value changes flash their cell background (green or red at 20% alpha) for 300-600ms, then fade; no easing on layout |

## Composition and layout

- Design the default workspace for the top three jobs: for example watchlist, chart and order ticket, or alert queue, topology and logs. Put the most time-critical panel top left.
- Make panels linkable: selecting an instrument, host or order in one panel updates others via a shared context (color-coded groups).
- Tables are the primary component: sticky headers, resizable and reorderable columns, sortable and filterable, column chooser, sticky first column, virtualized rows (10,000+), right-aligned numerals, units in headers.
- Add a command line (`/` or `⌘K`) with function codes or fuzzy search for every screen and action; show shortcuts in menus.
- Show data freshness: timestamps, "stale after 5s" indicators, connection state, last-updated per panel.
- Provide density settings (compact 20px, standard 24px, comfortable 32px rows) and persist them.

## Imagery and iconography

- No decorative imagery. Icons are 14-16px, single-color, used for status (alert, link, lock) and always paired with text or tooltips.
- Charts follow Tufte-style rules: maximize data-ink, 1px lines, light grid at 10-15% opacity, direct labels, small multiples with shared scales, sparklines in table cells.
- Use heat cells and bullet graphs instead of gauges and donuts.
- Status glyphs with shape (triangle up/down, circle, square), not color alone.

## Motion

Almost none. State changes are immediate (0-100ms). Value ticks flash the cell briefly so changes are noticed in peripheral vision, limited to cells that actually changed, and throttle updates to 4-10 per second per panel to avoid flicker. Panel resizing follows the pointer 1:1. Provide a pause-updates control for reading and a reduced-motion setting that replaces flashes with a static change marker (arrow or border).

## Fits and risks

- **Fits:** trading and market-data products, crypto exchanges, risk and treasury tools, observability, SOC/NOC and incident consoles, logistics and fleet control, industrial and energy monitoring, internal admin tools, analytics for expert users (`audience.expert-power-users`).
- **Risks:** onboarding cost; unreadable on phones; legibility fatigue if type is small and contrast low; designers over-polish into generic "dashboards" with big cards. Color-only gain/loss coding excludes color-blind users (about 8% of men have red-green deficiency).
- **Wrong for:** novices, older adults, low-literacy users, consumer mobile apps and luxury brands. A simplified summary view should front the dense workspace for occasional users.
- **Why these pair:** `industry.fintech-banking` and `industry.crypto-web3` trade on live markets; `industry.logistics-supply-chain`, `industry.industrial-manufacturing-construction` and `industry.energy-climate` run control rooms and monitoring; `industry.saas-b2b` has admin and analytics surfaces; `channel.web-app` has the screen area; `archetype.sage` values precision; `tier.mid-market` fits pragmatic tools.
- **Why these clash:** `audience.children-under-13`, `audience.older-adults` and `audience.low-literacy-plain-language` cannot use small, dense type; `tier.luxury` and `archetype.lover` promise indulgence, not instruments; `channel.native-app` phones cannot carry the density (use a summary companion).

## Do and don't

- Do tune for scanning: align decimals, align units, align headers with data, and keep consistent precision per column.
- Do offer both dark and light palettes; trading floors favor dark, control rooms and offices often prefer light.
- Do add redundancy to color: ▲/▼, +/- signs, severity words, shapes.
- Don't wrap the UI in 16px-radius cards, 24px padding and 40px KPI numbers; that is a marketing dashboard, not a tool.
- Don't animate charts on load or use 3D, donut or gauge charts for exact comparison.
- Don't hide critical actions behind hover-only menus; keep keyboard paths complete and documented.

## Clichés and AI tells

- Lazy version: a "Welcome back, Alex" dashboard with four large KPI cards showing green +12% pills, one gradient-filled area chart, a donut chart, a rounded sidebar with emoji, Inter, and a table with 48px rows.
- Fix: start from the analyst's task, show 30-100 values per screen, use tabular figures and right alignment, put the table first with sparklines and small multiples, apply semantic color sparingly, add a command line and density setting, and prototype with real, messy data (long names, nulls, negative values, 8-digit numbers).

## Accessibility notes

- Dark palette contrast: amber #FFB000 on canvas is 10.61:1; label gray #9A9A9A is 6.91:1 on canvas and 6.37:1 on panel; body text #E0E0E0 on panel is 13.58:1; up green is 7.81:1, down red 5.83:1 and info cyan 8.95:1 on panel. White on selection blue #1F4E8C is 8.31:1.
- Light palette: text #1C1F23 on white is 16.54:1; label #5B636D on panel is 5.53:1; up #0E7A4B is 5.38:1, down #C62828 is 5.62:1 and amber #8A5A00 is 5.93:1 on white.
- Grid lines (#2E2E2E at 1.43:1 on canvas, #D0D4D9 at 1.49:1 on white) are decorative. Row selection and focus need a 2px outline or fill that reaches 3:1 against neighboring rows.
- Minimum text size: allow 12px for dense numerals but offer zoom or a larger-type setting; 11px is for labels only, and target size for dense controls should still be 24x24 CSS px (WCAG 2.2 SC 2.5.8).
- Screen readers: real `<table>` markup with headers, `aria-sort`, live regions for alerts (polite, throttled); full keyboard navigation with roving tabindex in grids.

## Reference anchors

- Bloomberg Terminal (since 1982): keyboard-first, tiled, amber-and-green on black; study, do not copy
- Edward Tufte, *The Visual Display of Quantitative Information* (data-ink, sparklines, small multiples)
- Stephen Few, *Information Dashboard Design* and bullet graphs
- Grafana, Datadog and Interactive Brokers TWS as contemporary dense UIs
- ISA-101 (human-machine interfaces for process automation) and high-performance HMI practice: muted ground, color only for abnormal states
- IBM Carbon data table and AG Grid documentation for dense-table interaction patterns
