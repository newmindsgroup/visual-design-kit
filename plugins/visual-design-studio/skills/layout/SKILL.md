---
name: layout
description: >-
  Set grids, spacing and composition for screens, print and environments: column grids per breakpoint, baseline and
  modular grids, print grids with bleed and binding margins, a 4/8px spacing scale mapped to tokens, hierarchy, focal
  point and asymmetric balance, responsive recomposition with fluid space, and format sizes for screens, print and
  social. Use when laying out a page, screen, poster, deck or publication, choosing breakpoints or a grid, fixing
  cramped, flat or unbalanced composition, or adapting one design across formats.
license: MIT
metadata:
  version-timestamp: "2026-10-20 02:07:10 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 02:07:10 UTC"
---

# Layout

Excellent layout makes the order of reading inevitable: one clear entry point, related things grouped by space, a grid that holds everything without showing off, and whitespace placed in deliberate blocks. It recomposes for each format instead of shrinking.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Columns | 4 below 640px, 8 from 640px, 12 from 1024px | Editorial and marketing may use 6 or 5+7 asymmetric splits; dashboards use 12 or 24 |
| Margins | 16px phones, 24-32px tablets, 32-80px desktop, content centered in `--container-xl` (1280px) | Full-bleed imagery; luxury and editorial use wider margins |
| Gutters | `--gutter` = clamp(1rem, 4vw, 2rem): 16px phones to 32px desktop | Dense data UI: 16px fixed |
| Text width | `--measure-body` (66ch) inside any column | Captions and sidebars `--measure-narrow` |
| Spacing base | 4px scale, 8px rhythm for layout (`--space-2`, `--space-4`, `--space-6`, `--space-8`...) | Never off-scale values except optical corrections |
| Proximity | Space between groups at least 2x the space inside them | Dense tables use rules or fills instead of space |
| Component padding | Buttons 8-12px by 16-24px; cards 16-24px mobile, 24-32px desktop | Compact density mode: one step down |
| Section spacing | 48-80px mobile, 80-160px desktop | Product UI: 24-48px between regions |
| Baseline | 4px for UI; body leading for print (for example 13pt for 10/13 text) | Editorial web with a strong rhythm: 8px |
| Breakpoints | Content-out; token breakpoints sm 640, md 768, lg 1024, xl 1280, 2xl 1536 | Add a breakpoint where content breaks, not where a device is |
| Targets | 44x44px recommended (`--size-target-comfortable`), 24x24px minimum (`--size-target-min`) | Dense desktop tools may use 32px rows with 24px targets |
| Alignment | 2-4 vertical alignment axes per view | Posters and covers may use one strong axis |
| Print | 3mm (0.125in) bleed, 3-5mm safe zone inside trim, inner margin wider for binding | Follow the printer's spec sheet exactly |

## Workflow

1. **Read the content and the format.** List content in reading order: entry point, explanation, evidence, action, qualification. Note format, viewing distance and interaction (scroll, tap, glance, print). For style, industry or channel conventions run `python3 ../../library/scripts/atlas.py query "<brief>"` and read the style entry's *Composition and layout* and the channel entry's *Formats and specs*.
2. **Choose the grid type** ([grids](references/grids.md)): column grid for most screens, modular for repeated units, hierarchical for editorial web, manuscript for long reading, print grids for documents.
3. **Set the spacing scale** ([spacing](references/spacing.md)) and density mode; map every gap to a `--space-*` token.
4. **Compose** ([composition](references/composition.md)): pick one focal point per view, build hierarchy with scale contrast, place whitespace in blocks, align to few axes.
5. **Make it responsive** ([responsive](references/responsive.md)): find the content's break points, recompose (reorder, stack, reveal, crop) rather than shrink; use fluid space with `clamp()`.
6. **Adapt to formats** ([formats](references/formats.md)): each print, social or screen size is its own composition with its own safe areas.
7. **Render and inspect** at 360, 768, 1024, 1280 and 1536px+, at 200% zoom, with long content and empty states; for print, at 100% on paper or a 1:1 PDF. Use the `design-critique` skill's render loop; check the squint test (blur the screenshot: the focal point must still win).

## Decisions that change the answer

- **Style:** Swiss and editorial use asymmetric grids and big type jumps; quiet minimal uses wide margins and few elements; neo-brutalist exposes the grid with thick rules; data-dense uses tight 12- or 24-column grids with 16px gutters; maximalist layers and breaks the grid on purpose.
- **Tier:** luxury and premium raise margins and section spacing and show fewer items per view; value tiers pack more products, prices and calls to action.
- **Audience:** older adults and low-vision users need larger targets, simpler single-column flows and more space between interactive items; expert users want density and compact modes.
- **Channel:** web scrolls, slides do not; social is cropped by the platform UI; print has trim, bleed and binding; signage is read at distance in seconds.
- **Market and script:** RTL mirrors the grid's reading direction; CJK and Thai need more line spacing and often denser information layouts (see the `typography` skill's multiscript reference and `market.*` entries).
- **Content volume:** a layout must survive the shortest and longest real content, including translations.

## Common failures

- **Centered hero plus three icon cards.** The generic template. Fix: an asymmetric composition with a real focal point (a product image, a number, a strong headline at 7-10 columns).
- **Equal spacing everywhere.** Groups dissolve. Fix: inside spacing at half the between spacing or less.
- **Everything the same size.** No entry point. Fix: one element 2-4x larger than the next level.
- **Off-scale values** (13px, 22px, 37px). Fix: snap to `--space-*` tokens; allow only documented optical corrections.
- **Full-width text on desktop.** Fix: `--measure-body` on text containers.
- **Desktop layout shrunk onto phones.** Fix: recompose: reorder, stack, crop and cut secondary content to a disclosure.
- **Grid with no tension.** Every block the same width reads as a spreadsheet. Fix: unequal spans (5+7, 3+9, 4+8) and one element that breaks out.
- **Ignoring safe areas.** Text under the notch, the social platform UI or the binding. Fix: the safe areas in [formats](references/formats.md) and [responsive](references/responsive.md).

## References

- [Grids](references/grids.md): column grids per breakpoint, baseline, modular, hierarchical and manuscript grids, print grids with binding, CSS Grid, subgrid and container queries.
- [Spacing](references/spacing.md): the 4/8 scale mapped to `--space-*`, proximity, internal vs external spacing, section ranges, density modes.
- [Composition](references/composition.md): hierarchy, focal point, visual weight, asymmetric balance, scale contrast, whitespace, alignment, reading patterns, gestalt, optical adjustments.
- [Responsive](references/responsive.md): content-out breakpoints, recomposition patterns, fluid space, aspect ratios, art direction, safe areas.
- [Formats](references/formats.md): common sizes and aspect ratios for screens, print and social, with atlas channel IDs.
- Atlas: `python3 ../../library/scripts/atlas.py query "..."` and `python3 ../../library/scripts/atlas.py show channel.<slug>`; IDs in [the registry](../../library/atlas/registry.json).
- Sibling skills: `typography` for measure and baseline, `web-design` and `native-app-design` for platform layout, `print-packaging-social` for prepress, `ui-design` for component layout.
- Deep process for client projects: [design-foundations](../../library/draft-skills/design-foundations/SKILL.md) with [composition across formats](../../library/draft-skills/design-foundations/references/adaptive-composition.md), [art direction](../../library/draft-skills/design-foundations/references/art-direction.md) and [critique calibration](../../library/draft-skills/design-foundations/references/critique-calibration.md); [responsive website art direction](../../library/draft-skills/design-web-responsive/SKILL.md); [extreme-format composition](../../library/draft-skills/design-screen-formats/SKILL.md); worked reasoning in [typography and composition](../../library/knowledge/typography-and-composition.md).

Catalog IDs covered: foundations, web-responsive, screen-formats
