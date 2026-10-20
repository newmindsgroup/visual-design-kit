# Grids

Version-Timestamp: 2026-10-20 02:07:10 UTC

A grid is a set of decisions made once so every later placement is easy and consistent. Choose the grid type from the content, set columns, margins, gutters and a baseline, then let deliberate exceptions create tension.

## Grid types

| Type | Structure | Use for | Reference |
| --- | --- | --- | --- |
| Manuscript | One text block with margins | Books, long articles, legal documents, single-column apps | Classical book canons; Tschichold |
| Column | 4, 8 or 12 columns with gutters | Most websites, apps, reports | Universal default |
| Modular | Columns plus rows forming modules | Catalogs, galleries, dashboards, posters, product grids | Josef Müller-Brockmann, *Grid Systems in Graphic Design* |
| Hierarchical | Irregular zones sized by content importance | Homepages, editorial features, landing pages | Most news homepages |
| Compound | Two grids overlaid (for example 5 and 6 columns) | Editorial systems that need many layouts | Karl Gerstner's 58-unit grid for *Capital* magazine, which divides into 1-6 columns |
| Baseline | Horizontal lines at the body leading | Print text alignment across columns; UI vertical rhythm | Swiss print tradition |

## Column grids per breakpoint

| Viewport | Columns | Side margin | Gutter | Container |
| --- | --- | --- | --- | --- |
| Under 640px (phones) | 4 | 16px (20-24px for editorial) | 16px | Fluid |
| 640-767px (large phones, small tablets) | 8 | 24px | 16-24px | Fluid |
| 768-1023px (tablets) | 8 | 32px | 24px | Fluid |
| 1024-1279px (small laptops, tablet landscape) | 12 | 32-48px | 24px | Fluid |
| 1280-1535px (desktop) | 12 | Auto (centered) | 32px | `--container-xl` 1280px |
| 1536px+ (large desktop) | 12 | Auto | 32px | 1280-1440px content, full-bleed backgrounds and images |

- The token `--gutter` is `clamp(1rem, 4vw, 2rem)`: 16px on phones rising to 32px on desktop. Use it for column gaps and as the minimum side margin.
- Containers: `--container-sm` 640, `--container-md` 768, `--container-lg` 1024, `--container-xl` 1280px.
- Android reference: Material 3 window size classes are compact (under 600dp), medium (600-839dp), expanded (840-1199dp), large (1200-1599dp) and extra-large (1600dp+), with 16dp margins on compact and 24dp from medium up; confirm against current Material 3 guidance.
- iOS reference: system layout margins are 16-20pt on iPhone; use the readable content guide for text width on iPad.

## Spans that create tension

- Asymmetric splits on 12 columns: 5+7, 4+8, 3+9, 7+5 with an offset. Symmetric 6+6 is calm and static.
- Text blocks: 6-7 of 12 columns on desktop (about 60-75ch at 18px).
- Hero headlines: 7-10 of 12 columns at display size; let them run past the text column.
- One deliberate breakout per view (an image to the edge, a number crossing two columns) gives the grid life. Several breakouts become chaos.
- Product and card grids: 4 across on desktop, 2 on tablets, 1-2 on phones; never 5 identical cards in a row without a reason.

## CSS Grid patterns

Responsive column grid on the tokens:

```css
.grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  column-gap: var(--gutter);
  row-gap: var(--space-8);
  padding-inline: var(--gutter);
  max-inline-size: var(--container-xl);
  margin-inline: auto;
}
@media (min-width: 640px)  { .grid { grid-template-columns: repeat(8, minmax(0, 1fr)); } }
@media (min-width: 1024px) { .grid { grid-template-columns: repeat(12, minmax(0, 1fr)); } }
.hero-title { grid-column: 1 / -1; }
@media (min-width: 1024px) { .hero-title { grid-column: 1 / span 9; } .hero-aside { grid-column: 10 / -1; } }
```

Content, wide and full-bleed lanes with named lines (articles, marketing pages):

```css
.page {
  display: grid;
  grid-template-columns:
    [full-start] minmax(var(--gutter), 1fr)
    [wide-start] minmax(0, 10rem)
    [content-start] min(100% - 2 * var(--gutter), var(--measure-body))
    [content-end] minmax(0, 10rem)
    [wide-end] minmax(var(--gutter), 1fr) [full-end];
}
.page > * { grid-column: content; }
.page > .wide { grid-column: wide; }
.page > .full { grid-column: full; }
```

Intrinsic card grid that needs no media queries:

```css
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 18rem), 1fr)); gap: var(--space-6); }
```

Subgrid so card titles, bodies and actions align across a row (supported in all major browsers since 2023):

```css
.card { display: grid; grid-row: span 3; grid-template-rows: subgrid; gap: var(--space-3); }
```

Container queries so a component adapts to its slot, not the viewport:

```css
.card-slot { container-type: inline-size; }
@container (min-width: 32rem) {
  .card { grid-template-columns: 2fr 3fr; align-items: start; }
}
```

## Baseline grids

- **UI:** a 4px baseline. Every line-height in px and every vertical space is a multiple of 4 (16 x 1.5 = 24; 14 x 1.43 = 20; 20 x 1.4 = 28). Exact baseline alignment of text on the web is not practical; consistent multiples give the same rhythm.
- **Trimming leading:** `text-box: trim-both cap alphabetic;` removes the space above caps and below the baseline so headings align optically with images and boxes. It is a progressive enhancement (Chromium and Safari as of 2026; verify others).
- **Print:** set the baseline to the body leading (10/13pt text means a 13pt baseline). Body text snaps to it; headings use leading in multiples or half-multiples so columns stay aligned. Start the grid at the top margin.

## Print grids

| Item | Default | Notes |
| --- | --- | --- |
| Bleed | 3mm (ISO markets) or 0.125in (US) on every trimmed edge | Packaging and large formats can need more; follow the printer's template |
| Safe zone | 3-5mm (0.125-0.25in) inside trim for text and logos | Business cards: 3-4mm |
| Document margins (A4 or Letter report) | Top 15-20mm, outer 15-20mm, inner 20-25mm, bottom 20-25mm | Increase inner for thick bound documents |
| Perfect binding | Add 3-6mm to the inner margin; content near the spine is lost in the curve | Ask the printer for the spine allowance |
| Saddle stitch | Keep content 5mm+ from trim; inner pages creep outward on thick booklets | Printers compensate for creep; confirm |
| Wire or coil binding | Leave 10-12mm on the bound edge for holes | |
| Columns | Reports 2-3 columns; magazines 3-4 on a 12-column base; newspapers 5-6 | Gutter 4-6mm, at least one line of body leading |
| Classical book page | Margins in proportions such as 2:3:4:6 (inner:top:outer:bottom) | From Tschichold's analysis of medieval manuscripts; generous and calm |

- Design spreads, not single pages: facing pages mirror inner and outer margins, and images can cross the gutter only where the binding allows (never in perfect-bound spines with text).
- Posters: margins of at least 5% of the short side; a modular grid of 4x6 or 6x8 fields works for most compositions.
- Slides (1920x1080): 12 columns, 80-120px side margins, 64-96px top and bottom; keep 5% inside the edges for projectors that overscan.

## Choosing a grid quickly

| Content | Grid |
| --- | --- |
| Long reading (articles, docs, legal) | Manuscript or content lane at 66ch, with wide and full lanes for media |
| Marketing page with mixed sections | 12-column with asymmetric spans and full-bleed bands |
| Product listing, gallery, portfolio | Modular, intrinsic `auto-fill` cards with subgrid alignment |
| Dashboard | 12 or 24 columns, 16px gutters, cards spanning 3, 4, 6 or 12 |
| Editorial homepage | Hierarchical: lead story at 8 columns, secondary at 4, tertiary rows of 3 |
| Report or brochure | 12-column print grid with a baseline, 2-3 text columns |
| Poster or cover | Modular grid; one dominant axis; type and image locked to modules |

## Grid checklist

- Columns, margins, gutters and container defined per breakpoint and recorded as tokens or CSS.
- Text never wider than `--measure-body`.
- 2-4 vertical alignment axes per view; everything else aligns to them.
- At least one deliberate asymmetry or breakout per key view.
- Print: bleed, safe zone and binding allowance from the printer's spec.
