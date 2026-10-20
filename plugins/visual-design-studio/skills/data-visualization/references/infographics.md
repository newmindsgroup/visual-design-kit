# Infographics and data stories

Version-Timestamp: 2026-10-20 02:07:10 UTC

An infographic explains: it combines a few charts, numbers, diagrams and short text into one argument. Plan the story and the hierarchy before drawing anything, and keep every number traceable to a source. For client projects, the full process (evidence records, specification, handoff) is in the [design-infographics draft skill](../../../library/draft-skills/design-infographics/SKILL.md) and its [layout and style repertoire](../../../library/draft-skills/design-infographics/references/layouts.md).

## Story structure

| Beat | Job | Typical content |
| --- | --- | --- |
| Hook | Make the reader care in 3 seconds | Headline with the finding, one hero number with its denominator and period |
| Context | Why it matters, for whom | One or two sentences, a small comparison or map |
| Evidence | 2-4 points that support the finding | One chart or diagram per point, each with a takeaway subhead |
| Implication | What it means or what to do | A short conclusion, a call to action, or a forward look |
| Source and method | Trust | Sources, dates, definitions, sample sizes, author |

Interactive and long-form patterns (from Segel and Heer's 2010 study of narrative visualization):

- **Martini glass:** an author-driven story first, then open exploration at the end.
- **Interactive slideshow:** a sequence of steps the reader advances, each one chart and one point.
- **Drill-down story:** an overview the reader can open into details.
- **Scrollytelling:** a sticky chart that changes as text steps scroll past; keep steps short (25-60 words) and provide a static version for reduced motion and print.

## Information hierarchy

| Level | Element | Typical size (web or social) |
| --- | --- | --- |
| 1 | Headline and hero number | 40-120px; one per piece |
| 2 | Section takeaways | 24-32px |
| 3 | Charts, diagrams, labels | Labels 12-16px; marks sized for the format |
| 4 | Notes, sources, definitions | 12-13px, `--color-fg-muted` |

- Unequal importance gets unequal space. A modular grid where every module is the same size says every point matters equally.
- Keep explanations next to what they explain; avoid separate keys and footnote hunting.
- Reading path: top to bottom (or a clear Z) with numbered sections when order matters.

## Word budgets (rules of thumb)

| Format | Words |
| --- | --- |
| Single social panel (1080x1350) | 20-50 |
| Social carousel slide | 15-40 per slide, 5-10 slides |
| Poster or one-page print | 80-150 |
| Long-form web infographic | 40-80 per section, 4-8 sections |
| Slide | One sentence of takeaway plus labels |

If the content needs more words, it is an article with charts; design it as one (see the `typography` skill for long-form setting).

## Formats

| Format | Composition notes |
| --- | --- |
| Long-form web (scrolling) | Content column 640-960px wide with full-bleed charts where useful; responsive charts, not a scaled image |
| Single panel (social, poster) | One finding, one chart or hero number, source line; test at the size people will see it (a phone feed) |
| Carousel | Slide 1: hook and key number. Middle: one point per slide, consistent layout. Last: summary, source, call to action |
| Slide | One chart and one takeaway title per slide; build complex charts across several slides |
| Print spread or report page | Modular grid with a baseline; captions close to charts; print-safe colors (see the `color` skill) |
| Animated or video | One idea per scene, hold each number long enough to read twice, captions on, static fallback |

Format sizes and safe areas: the `layout` skill's formats reference and the `print-packaging-social` skill.

## Visual vocabulary

- One illustration and icon style throughout: same stroke weight, perspective, corner style and color logic (see the `imagery` skill).
- **Pictograms count, they do not scale.** Show quantities by repeating icons (each icon = a stated number), the Isotype method developed by Otto Neurath and Gerd Arntz. Never enlarge an icon to show a bigger number; area exaggerates.
- Diagrams (processes, cycles, hierarchies) must not imply quantities through size or width unless they encode data.
- Maps only for spatial questions; normalize rates (see [chart selection](chart-selection.md)).
- Color: 1-2 accents for emphasis plus neutrals; data colors per [data palettes](data-palettes.md).
- Avoid generic infographic decoration: 3D pie charts, gradient-filled icons, ribbon banners and clip-art people.

## Accuracy

- Every number has a source, date, unit and denominator in the working file. Recompute totals and percentages from the source before export.
- Do not invent statistics or round toward a better story. Unknown data stays unknown; fictional examples are labeled as fictional.
- Keep the visual honest: zero baselines on bars, equal time spacing, no area or 3D distortion, no causal language for correlations.
- Keep a data table and a short method note with the deliverable.

## Production

- Build charts from data, not by eye: Observable Plot, D3 or Vega-Lite in code; Datawrapper or Flourish for quick publishing; then refine art in Figma or Illustrator if needed, keeping values intact.
- Keep text live (HTML or SVG text) on the web; outline only in final print files where required.
- Export SVG for the web where possible, PNG at 2x for social, PDF/X for print.
- Provide accessible equivalents: alt text, a long description or the HTML text version, and the data table (see [accessible charts](accessible-charts.md)).
- A worked, buildable example lives in the kit's [infographic story](../../../library/examples/infographic-story/README.md); the [infographic specification template](../../../library/templates/infographic-spec.md) records elements, sources and alternatives for client work.

## Infographic checklist

- One finding in the headline; 2-4 evidence points; source and method present.
- Hierarchy visible in a blurred screenshot; unequal points get unequal space.
- Word budget respected for the format.
- Icons and illustrations in one style; pictograms repeat rather than scale.
- Numbers recomputed and traceable; visual encodings honest.
- Rendered at real size for each format; accessible equivalents delivered.
