---
id: style.swiss-international
axis: style
name: Swiss / International Typographic Style
aliases: [swiss style, international typographic style, international style, grid modernism, swiss design]
summary: Objective, grid-driven design with asymmetric layouts, grotesque sans-serif type, flat color and photography; clarity itself is the aesthetic.
tags: [grid, sans-serif, typographic, modernist, objective, asymmetric, flat, systematic]
pairs_with: [industry.fintech-banking, industry.saas-b2b, industry.legal-professional-services, industry.events-conferences, archetype.sage, archetype.ruler, channel.presentation, channel.environmental-wayfinding]
avoid_with: [audience.children-under-13, archetype.jester, style.maximalist-eclectic]
version_timestamp: 2026-10-20 01:42:00 UTC
---

# Swiss / International Typographic Style

## Essence

Information first, decoration never. A strict modular grid, a single grotesque sans-serif family, asymmetric balance and generous negative space make content feel objective and trustworthy. Developed in Switzerland in the 1950s (Basel and Zurich schools), it underpins most modern corporate identity, wayfinding and interface design.

## Visual signature

- One sans-serif family (two at most), set flush-left, ragged-right; hierarchy through size, weight and position rather than ornament.
- Visible or strongly implied modular grid; text and images snap to columns and a baseline.
- Asymmetric layouts with large deliberate white space; headlines often very large and tightly set.
- Flat color fields; red, black and white is the canonical palette, but any 1-2 saturated accents on neutrals works.
- Objective photography (cropped tight, high contrast, often black-and-white) instead of illustration.
- Numbers, rules (hairlines) and alignment do the decorative work.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Inter Display or Inter Tight (OFL); Schibsted Grotesk (OFL); commercial: Neue Haas Unica, Helvetica Now Display, Suisse Int'l |
| Body font | Inter (OFL); IBM Plex Sans (OFL); commercial: Neue Haas Grotesk Text, Suisse Int'l |
| Mono (data, captions) | IBM Plex Mono or JetBrains Mono (OFL) |
| Type scale ratio | 1.333 (perfect fourth) for marketing; 1.25 for product UI; display can jump 2-3 steps at once for drama |
| Body size / line-height | 16-18px / 1.45-1.55; measure 55-70ch |
| Display letter-spacing | -0.02em to -0.04em at 48px+; line-height 0.95-1.05 |
| Caps / labels | 11-13px, uppercase, +0.06em to +0.1em, medium weight |
| Weights | Regular 400 and Bold 700 (or Medium 500 / Bold 700); avoid more than 3 weights |
| Palette | Ink #111111 (oklch 0.18 0 0); Paper #F7F6F2 (oklch 0.97 0.005 95); Swiss red #E30613 (oklch 0.58 0.234 28); Mid gray #8A8A8A (oklch 0.63 0 0); Rule gray #D9D9D6 (oklch 0.88 0.004 106) |
| Accent proportion | Accent covers 5-15% of the surface; it marks the single most important element |
| Radius | 0-2px. Rounded corners read as a different style |
| Borders | 1px hairline rules in ink or rule gray to separate rows and columns |
| Shadow / elevation | None. Use space, rules and color fields for layering |
| Spacing density | Generous: 8px base with section spacing of 96-160px on desktop |
| Grid | 12 columns desktop (gutter 24px, margin 48-80px), 6 tablet, 4 mobile; baseline 4px or 8px |
| Motion | 160-240ms, cubic-bezier(0.2, 0, 0, 1); position and opacity only; no bounce |

## Composition and layout

- Start from the grid, not the content: decide columns, margins and baseline first, then place.
- Use asymmetry: anchor the headline to the left columns and let images or data span unequal widths (for example 5 + 7 or 3 + 9 of 12).
- Align everything to a small number of vertical axes (2-4 per spread or page). Every misaligned element is noticed.
- Put white space in big contiguous blocks rather than evenly sprinkling it.
- Let numbers and labels be structural: section numbers, index columns, captions in caps.
- Web: let the hero headline span 7-10 columns at 64-120px; keep body copy within 6-7 columns.

## Imagery and iconography

- Photography: objective, cropped hard, often grayscale or duotone with the accent. Avoid stock-smile lifestyle shots.
- Icons: geometric, 1.5-2px monoline on a 24px grid, square or butt caps, no fills or gradients. Use few icons; prefer text labels.
- Data visualization fits naturally: thin bars, direct labels, no chart junk.

## Motion

Precise and mechanical: elements slide along grid axes, text reveals line by line, 160-240ms with standard easing, stagger 30-40ms. No overshoot, bounce, parallax or blur. Respect `prefers-reduced-motion` by switching to opacity-only or no motion.

## Fits and risks

- **Fits:** finance, B2B software, consulting, architecture, museums, conferences, wayfinding, annual reports, public institutions, anything where trust and clarity beat warmth.
- **Risks:** can feel cold or generic when the grid has no tension; many brands already look like this, so differentiation must come from a distinctive accent, photography or typographic scale contrast.
- **Wrong for:** children, playful consumer brands, products whose value is warmth or indulgence (unless deliberately subverted).

## Do and don't

- Do commit to one family and let scale do the work; a 6:1 headline-to-body ratio is normal here.
- Do show the grid through alignment, rules and index numbers.
- Do keep the accent scarce so it guides attention.
- Don't center text blocks or use justified text without hyphenation control (rivers).
- Don't add drop shadows, gradients or rounded cards; they dilute the style into generic SaaS.
- Don't use Helvetica on its own as a substitute for an idea; the composition carries the identity.

## Clichés and AI tells

- Generic "Swiss" that is really just Inter on white with centered headings and three cards: lacks asymmetry and grid tension.
- Overused red/black/white posters with a giant "+" or circle: fine for homage, weak for a client identity.
- Default 16px radius cards and soft shadows creeping in from component libraries.
- Fix: introduce a real asymmetric grid, an extreme type-scale jump, a distinctive accent or crop, and remove every effect that is not structural.

## Accessibility notes

- Thin weights at large sizes look elegant but fail at small sizes; keep body at 400+ and 16px+.
- Gray text on off-white often fails 4.5:1; mid gray #8A8A8A on #F7F6F2 is about 3.2:1, so use it for large text or decoration, not body copy.
- Swiss red #E30613 is 4.9:1 on white but only 4.5:1 on the warm paper, right at the limit; brighter, more orange reds such as #FF3B30 drop to 3.6:1 on white. Compute the exact pair before using red for text.
- Ragged-right text supports readability for dyslexic readers; keep it.

## Reference anchors

- Josef Müller-Brockmann, *Grid Systems in Graphic Design* (1981)
- Emil Ruder, *Typographie* (1967)
- Armin Hofmann, Basel School of Design posters
- Massimo Vignelli and Bob Noorda, 1970 New York City Subway map and signage
- Swiss Federal Railways (SBB) identity and timetable design
- *Neue Grafik* magazine (1958-1965)
