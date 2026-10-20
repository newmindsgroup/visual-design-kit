---
name: typography
description: >-
  Choose, pair, size and set type for brand, web, app, print, slides, signage and motion: modular scales, fluid
  clamp() type, measure, leading, tracking, OpenType features, font licensing and web font loading, and multiscript
  setting for CJK, Arabic, Hebrew, Devanagari and Thai. Use when selecting or pairing fonts, building a type scale or
  type tokens, fixing weak hierarchy or bad line breaks, setting long-form text or numbers, loading web fonts, or
  localizing type for another market.
license: MIT
metadata:
  version-timestamp: "2026-10-20 02:07:10 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 02:07:10 UTC"
---

# Typography

Excellent typography makes the reading order obvious at a glance and makes long reading effortless: few sizes with real contrast between them, comfortable measure and leading, fonts chosen for this brief rather than by habit, and details (numerals, quotes, breaks) that nobody notices because they are right.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Scale ratio | 1.25 product UI; 1.125-1.2 dense UI and data; 1.333 marketing; 1.5-1.618 editorial and posters | Display moments may jump 2-3 steps; tiny screens compress the ratio (see fluid type) |
| Body size | Web 16-18px (`--font-size-md`); iOS 17pt; Android 16sp; print 9-11pt; slides 18pt+ on a 960x540pt canvas | Long-form reading 18-20px; older adults 18px+; dense tables 13-14px |
| Measure | 45-75ch, aim for 66ch (`--measure-body`) | Captions and sidebars 30-45ch (`--measure-narrow`); CJK 30-40 characters |
| Line-height | Body 1.5 (`--line-height-normal`); long-form 1.65 (`--line-height-relaxed`); headings 1.1-1.25 (`--line-height-tight`/`--line-height-snug`) | Dense UI 1.3-1.4; display 64px+ at 0.95-1.05; scripts with stacked marks 1.6-1.9 |
| Tracking | 0 for body; -0.02em at 32-48px (`--letter-spacing-tight`); -0.03 to -0.04em at 64px+; +0.06em for caps (`--letter-spacing-caps`) | Small text under 13px +0.01em (`--letter-spacing-wide`); never track Arabic or other connected scripts |
| Weights | 2-3 per family: 400 body, 500-600 UI emphasis, 700 headings (`--font-weight-*`) | Luxury display may go 300; sport and neo-brutalist 800-900; body never below 400 under 16px |
| Families | 1-2 families plus a mono if code or data needs one | One variable family with width or optical axes can do everything |
| Numerals | Tabular lining in tables, prices, timers, charts; proportional elsewhere; oldstyle in serif long-form | Brand uses a display numeral style deliberately |
| Minimum text | 12px for any UI text; 14px for secondary copy; iOS 11pt; print 6-7pt only for legal | Audience entries (older adults, low literacy) raise the floor |
| Fluid type | `clamp()` between 360 and 1280px viewports, rem term always present, max at most 2.5x min | Product UI: keep sizes fixed below `--font-size-xl` |
| Web loading | Self-hosted, subset woff2; `font-display: swap` with metric-matched fallback; preload 1-2 files | Performance-critical pages: `font-display: optional` |
| Line breaks | `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs; no single-word last lines in headings | Paginated output: set widows and orphans to 2 and inspect every page |

## Workflow

1. **Read the brief variables.** Style, market and script, audience, tier, channel, brand locks. If any of those are open, run `python3 ../../library/scripts/atlas.py query "<brief in plain words>"` and read the chosen style entry's *Token recipe* and the market entry's *Typography and layout*.
2. **Map content to roles.** Display, H1-H3, body, lead, UI label, caption, overline, data, code. Decide which roles carry personality and which carry reading. List every script and language the type must cover.
3. **Shortlist three candidates** from [pairing](references/pairing.md): one category-expected, one adjacent, one unexpected. Reject the default (Inter or system sans for everything) unless the brief is a dense product UI that benefits from it, and say why.
4. **Build the scale.** Pick the ratio from [defaults](references/defaults.md), generate it with `python3 ../../library/scripts/type_scale.py --help` (or the formula in that reference) and map steps to `--font-size-*` tokens. Set line-height, tracking and weight per role.
5. **Specimen with real copy.** Longest headline, a real paragraph, buttons and labels, a price and a table row, difficult strings (`Il1 O0`, accents, the brand name). Render at the actual target sizes, in light and dark.
6. **Set the details** with [setting](references/setting.md): quotes, dashes, numerals, small caps, hyphenation, wrapping, OpenType features.
7. **Source and load** per [font sourcing](references/font-sourcing.md): confirm the license for every use (web, app, PDF, logo, broadcast), self-host, subset, add fallback metrics.
8. **Localize** with [multiscript](references/multiscript.md) when any non-Latin script or RTL appears.
9. **Render and inspect.** Screenshot at 360, 768 and 1280px+, at 200% zoom, with web fonts blocked, and with the longest translation. Use the `design-critique` skill's render loop. Fix widows, collisions, layout shift and missing glyphs before handoff.

## Decisions that change the answer

- **Style:** each atlas style sets the family genre, ratio and tracking (Swiss: grotesque, 1.333, tight display; classic luxury: high-contrast serif, wide caps tracking; data-dense: 1.125-1.2, tabular everything).
- **Market and script:** CJK, Arabic, Devanagari and Thai change family, size, line-height and line breaking. Check `market.*` entries before choosing a Latin face.
- **Audience:** older adults (`audience.older-adults`) need 18px+ body and strong weight contrast; children need larger, rounder, simpler letterforms; low-literacy and dyslexic readers need short measure, generous spacing, ragged-right text and no all-caps paragraphs.
- **Tier:** luxury raises contrast between display and text, uses lighter display weights and more space; value tiers use bolder, tighter, larger type with fewer styles.
- **Channel:** native apps use platform text styles that scale with Dynamic Type and Android font scale; print works in points with real leading; signage sizes from viewing distance; email needs web-safe fallbacks; video needs title-safe placement and reading time.
- **Brand locks:** an approved typeface stays. Change setting (size, spacing, features) before proposing a replacement.

## Common failures

- **Inter or system sans for everything.** Fix: choose by brief from [pairing](references/pairing.md); keep Inter for dense UI where its tabular figures and wide language support earn it.
- **Too many sizes.** Eleven sizes that differ by 1-2px read as noise. Fix: 6-8 steps from one ratio.
- **Loose display type.** Default tracking and 1.5 leading at 72px look amateur. Fix: -0.03em and 1.0-1.05 leading.
- **Endless lines on wide screens.** Fix: `max-inline-size: var(--measure-body)` on text containers.
- **Thin or gray small text.** Light weights and `#999` captions fail contrast and legibility. Fix: 400+ weight and `--color-fg-muted`, which clears 4.5:1.
- **Faux bold and italic.** Fix: load the real styles and set `font-synthesis: none`.
- **Fluid type that does not zoom.** Pure `vw` sizes ignore browser zoom. Fix: always include a rem term; test 200%.
- **Layout shift when fonts load.** Fix: metric-matched fallback with `size-adjust` and the override descriptors.
- **Latin rules applied to other scripts.** Tracking Arabic breaks joining; italic CJK is synthetic. Fix: follow [multiscript](references/multiscript.md).

## References

- [Defaults](references/defaults.md): scale ratios, body sizes per medium, measure, line-height, tracking, weights, fluid type with a worked `clamp()` example and the scale script.
- [Pairing](references/pairing.md): pairing principles and 30 vetted OFL pairings with mood, use and atlas style IDs.
- [Setting](references/setting.md): micro-typography, wrapping, numerals, OpenType features, variable fonts.
- [Font sourcing](references/font-sourcing.md): licenses, foundries, self-hosting, subsetting, loading and fallback metrics.
- [Multiscript](references/multiscript.md): families and adjustments per script, RTL and mixed-script setting.
- Atlas: `python3 ../../library/scripts/atlas.py query "..."` for style and market type recipes; `python3 ../../library/scripts/atlas.py show <id>` to read one entry. IDs live in [the registry](../../library/atlas/registry.json).
- Sibling skills: `color` for text contrast, `layout` for grids and baselines, `design-system` for token builds, `motion` for kinetic type.
- Deep process for client projects: [design-typography](../../library/draft-skills/design-typography/SKILL.md) with its [type craft](../../library/draft-skills/design-typography/references/type-craft.md), [font discovery](../../library/draft-skills/design-typography/references/font-discovery.md), [editorial reading](../../library/draft-skills/design-typography/references/editorial-reading.md) and [advanced typesetting](../../library/draft-skills/design-typography/references/advanced-typesetting.md) methods; record decisions in the [typography decision template](../../library/templates/typography-decision.md); worked reasoning in [typography and composition](../../library/knowledge/typography-and-composition.md).

Catalog IDs covered: typography
