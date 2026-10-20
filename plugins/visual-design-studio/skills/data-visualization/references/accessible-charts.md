# Accessible charts

Version-Timestamp: 2026-10-20 02:07:10 UTC

An accessible chart works without sight, without color, without a mouse and at 400% zoom. Build it in four layers: perceivable marks, a text alternative with the takeaway, the data as a table, and keyboard and screen-reader operation for interactive charts. W3C's [complex images tutorial](https://www.w3.org/WAI/tutorials/images/complex/) is the reference pattern; Frank Elavsky's Chartability heuristics are a good audit checklist.

## Layer 1: perceivable marks

- Marks at 3:1 against the background or outlined; text at 4.5:1 (see [data palettes](data-palettes.md) and the `color` skill's [contrast reference](../../color/references/contrast.md)).
- Meaning never by color alone (WCAG 2.2 SC 1.4.1): direct labels first, then shapes, dash patterns or fills.
- Labels 12px minimum and real text (SVG or HTML), not pixels baked into an image, so they scale, translate and can be read aloud.
- Charts reflow at 320px width and stay legible at 200% zoom; on phones simplify instead of shrinking.
- Interactive points get at least a 24x24px hit area (`--size-target-min`), using an invisible larger target around small dots.

## Layer 2: text alternatives

**Short alternative** (alt text or `aria-label`): chart type, subject and the takeaway in one or two sentences.

- Bar: "Bar chart of 2026 returns by category: footwear has the highest return rate at 24%, twice the average."
- Line: "Line chart of weekly active users, Jan to Jun 2026: steady at about 40,000, then rising to 58,000 after the April redesign."
- Pie: "Pie chart of traffic sources: search 52%, direct 27%, social 14%, email 7%."

**Long description** (visible text, `<figcaption>`, or a linked description) for complex charts:

1. Chart type and what it shows (title, subtitle, unit, period).
2. Axes and ranges ("x axis: months, Jan 2025 to Jun 2026; y axis: revenue in USD millions, 0 to 6").
3. The main pattern, then key values: highs, lows, crossings, outliers, annotated events.
4. Comparisons that matter for the takeaway.
5. Source and date.

Do not repeat every value in prose; that is what the table is for.

## Layer 3: the data table

Provide the underlying data as a real table next to the chart, collapsed if needed:

```html
<figure>
  <svg role="img" aria-labelledby="rev-title rev-desc" viewBox="0 0 640 360">
    <title id="rev-title">Online orders overtook store sales in March 2026</title>
    <desc id="rev-desc">Line chart of monthly revenue by channel, USD millions, January to June 2026. Online rose from 2.1 to 4.2; stores fell from 3.4 to 3.0; the lines cross in March.</desc>
    <!-- marks: decorative internals get aria-hidden="true" -->
  </svg>
  <figcaption>Source: company finance data, July 2026.</figcaption>
  <details>
    <summary>Show data table</summary>
    <table>
      <caption>Monthly revenue by channel, USD millions, 2026</caption>
      <thead><tr><th scope="col">Month</th><th scope="col">Online</th><th scope="col">Stores</th></tr></thead>
      <tbody><tr><th scope="row">January</th><td>2.1</td><td>3.4</td></tr><!-- ... --></tbody>
    </table>
  </details>
</figure>
```

(The values above are illustrative only.)

- Use `<caption>`, `<th scope="col">` and `<th scope="row">`; put units in headers, not in every cell.
- Right-align numbers with tabular figures; format them like the chart.
- Offer a CSV download for analysts.
- For canvas-rendered charts (many chart libraries), put the table adjacent to the canvas; canvas content is invisible to assistive technology.

## Layer 4: keyboard and screen reader operation

For interactive charts (tooltips, drill-down, filtering, brushing):

- **One tab stop for the chart,** then arrow keys move between points or bars (roving `tabindex`); Home and End jump to the first and last point; Enter or Space activates drill-down; Escape closes tooltips and exits.
- **Each focusable point has a label** that reads as data: "March 2026, Online, 3.5 million US dollars."
- **Focus is visible** on the mark (outline or enlarged marker, 3:1), and the tooltip opens on focus as well as hover (WCAG 2.2 SC 1.4.13: dismissible, hoverable, persistent).
- **Controls** (series toggles, range sliders, filters) are real buttons and inputs with labels and states (`aria-pressed`, `aria-expanded`).
- **Announce changes:** when filters update a chart, update its summary text and announce it in a polite live region ("Showing EMEA, last 30 days: revenue 1.2 million, up 4%").
- **Do not trap focus** inside the chart.
- Libraries with built-in support (keyboard navigation, screen-reader descriptions, sonification) save effort; Highcharts' accessibility module is one example. Verify with real assistive technology; library claims are not test results.

```html
<g role="list" aria-label="Online revenue by month">
  <circle role="listitem" tabindex="-1" aria-label="January 2026, Online, 2.1 million US dollars" cx="40" cy="250" r="4"></circle>
  <!-- roving tabindex: exactly one point has tabindex="0" -->
</g>
```

## Patterns, shapes and dashes

Use these in addition to color, especially for print, grayscale and forced-colors modes. Use restraint: direct labels are clearer than patterns, and heavy hatching adds noise.

| Mark | Variations |
| --- | --- |
| Lines | Solid; dashed `stroke-dasharray: 6 4`; dotted `2 3`; dash-dot `8 3 2 3` |
| Points | Circle, square, triangle, diamond, cross (one shape per series) |
| Areas and bars | Solid, diagonal hatch, dots, crosshatch |

```html
<svg width="0" height="0" aria-hidden="true">
  <defs>
    <pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <rect width="6" height="6" fill="#E69F00"></rect>
      <line x1="0" y1="0" x2="0" y2="6" stroke="#000" stroke-width="1.5"></line>
    </pattern>
  </defs>
</svg>
```

## Motion and forced colors

- Animated charts: respect `prefers-reduced-motion` (show the final state); anything that moves for more than 5 seconds needs pause (WCAG 2.2 SC 2.2.2); never flash more than 3 times per second.
- In Windows forced-colors mode, browsers replace SVG `fill` and `stroke` colors with system colors, so series that differ only by color become identical. Rely on labels, shapes and patterns, or set `forced-color-adjust: none` on the chart and verify its contrast against the system background.

## Testing

1. Keyboard only: reach, operate and leave every interactive chart; focus always visible.
2. Screen readers: VoiceOver (macOS, iOS), NVDA or JAWS (Windows), TalkBack (Android). Listen to the summary, the table and point navigation.
3. Zoom to 200% and 400% (320px reflow); check label overlap and clipping.
4. Grayscale and color-vision-deficiency emulation (Chrome DevTools Rendering panel).
5. Forced colors (Windows Contrast themes or DevTools emulation).
6. Automated checks (axe) catch missing names and contrast in text, not chart meaning; do the manual steps.

## Accessible chart checklist

- Marks 3:1 or outlined; labels 4.5:1; meaning carried by labels, shapes or patterns as well as color.
- Short alternative with the takeaway; long description for complex charts.
- Data table with caption and scoped headers, plus CSV where useful.
- Interactive charts: one tab stop, arrow-key navigation, labeled points, focus-visible marks, focusable tooltips, announced updates.
- Reduced motion and forced colors handled.
- Tested with a keyboard and at least one screen reader.
