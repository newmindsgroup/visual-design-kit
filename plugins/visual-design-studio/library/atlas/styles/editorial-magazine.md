---
id: style.editorial-magazine
axis: style
name: Editorial / Magazine
aliases: [editorial design, magazine layout, print editorial, longform editorial, publication design, magazine style]
summary: Publication-grade hierarchy: high-contrast serif display, readable text serif, multi-column grids, pull quotes, strong crops and one spot color; design that makes reading feel curated.
tags: [editorial, serif, magazine, typographic, longform, columns, publication, grid]
pairs_with: [industry.media-entertainment-streaming, industry.fashion-apparel, industry.creative-agencies-studios, industry.nonprofit-ngo, archetype.sage, archetype.creator, tier.premium, channel.print-collateral, channel.email, channel.marketing-website]
avoid_with: [channel.web-app, audience.low-bandwidth-entry-devices, industry.logistics-supply-chain]
version_timestamp: 2026-10-20 01:51:22 UTC
---

# Editorial / Magazine

## Essence

Design as editing. A magazine decides what matters, then makes the order of reading unmistakable: kicker, headline, deck, byline, lead, body, pull quote, caption. The tradition runs from Alexey Brodovitch at *Harper's Bazaar* (art director 1934-1958) and Alexander Liberman at *Vogue* to Herb Lubalin's *Avant Garde* (1968-1971), Neville Brody's *The Face* (1981-1986), David Carson's *Ray Gun* (1992-1995) and Bloomberg Businessweek's 2010s redesign. Use it when content is the product and the brand wants authority, taste and voice.

## Visual signature

- High-contrast serif display (Didone or transitional) beside a readable text serif and a small sans for labels and metadata.
- A visible information hierarchy in repeatable parts: kicker, headline, deck, byline, drop cap, pull quote, caption, folio.
- Multi-column text (2-4 columns in print, 1-2 on web), strong gutters and thin rules; images that bleed, crop tight or span columns.
- Dramatic scale contrast: a single 120-240px headline word or number against 9-10pt body copy.
- Generous margins and white space on openers; dense, tidy pages inside the story.
- One spot color for kickers, links and rules; photography carries the emotion.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Playfair Display (OFL, high-contrast); Bodoni Moda (OFL, optical-size axis); Instrument Serif (OFL, condensed display); commercial: Canela (Commercial Type), GT Sectra (Grilli Type), Tiempos Headline (Klim) |
| Body font | Newsreader (OFL, opsz axis, built for screen reading) 400-500 at 18-20px; Source Serif 4 (OFL); commercial: Tiempos Text, Publico Text |
| Sans (labels, bylines, UI) | Instrument Sans (OFL) 500-600, or Archivo (OFL) |
| Type scale ratio | 1.333 for article hierarchy; 1.5-1.618 for opener headlines; allow one oversized jump (6-10x body) |
| Body size / line-height | 18-20px / 1.55-1.65; measure 60-70ch; print 9-10pt on 12-13pt |
| Display letter-spacing | -0.02em to -0.035em at 56px+; line-height 0.95-1.05 |
| Caps / labels | 11-13px, uppercase, +0.08em to +0.14em, weight 600 |
| Weights | Display 400-700 (contrast beats weight); body 400; italic for decks and captions |
| Palette | Ink #111111 (oklch 0.18 0 0); Newsprint #FAF7F0 (oklch 0.98 0.010 87); Sunk panel #EFE9DC (oklch 0.94 0.018 86); Gray #6B6B6B (oklch 0.53 0 0); Rule #D8D3C8 (oklch 0.87 0.016 86); Spot red #D3311C (oklch 0.57 0.201 31); Highlight marigold #F2A900 (oklch 0.78 0.164 78) |
| Verified pairs | Ink on Newsprint 17.65:1; Gray on Newsprint 4.98:1; Spot red on Newsprint 4.64:1; white on Spot red 4.97:1; Ink on Marigold 9.40:1; Gray on Sunk only 4.41:1 (use Ink there); Rule on Newsprint 1.39:1 is decorative |
| Accent proportion | Spot color under 5% of the area: kickers, one rule, link underline, pull-quote mark |
| Radius | 0-2px; round only avatars |
| Borders | 1px ink or rule hairlines; 3-4px ink bar above section openers |
| Shadow / elevation | None; hierarchy by rules, scale and white space |
| Spacing density | 8px base; 24px gutters; 64-120px between stories; dense inside text, open around openers |
| Grid | 12 columns desktop (margin 48-80px), 6 tablet, 4 mobile; article body 5-6 columns centered or offset, pull quotes and images span wider |
| Motion | 400-700ms, cubic-bezier(0.16, 1, 0.3, 1); headline fade-up 16-24px, image clip-path reveal; scroll parallax under 8% |

## Composition and layout

- Open each story with a "front door": large image or giant type, kicker, headline, deck and byline in a deliberate arrangement. Reuse 4-6 opener templates across an issue or site.
- Break the text column every 400-600 words with a pull quote, full-width image or sidebar so the page keeps a rhythm.
- Align image edges to the column grid and cap-heights to baselines; allow one deliberate break per spread.
- Use rules (0.5-1pt) to separate sections and sort information into clear zones; use drop caps (3 lines) for the first paragraph only.
- On the web, keep the reading column at 640-720px, sticky small-sans headers, footnote-like sidenotes at 1200px+, and keep ads or modules out of the first screen.
- Email newsletters: single column 600px, ink on newsprint, a lead story with image, then 3-5 list items with kicker, headline and one-line deck.

## Imagery and iconography

- Photography: chosen and cropped with intent (portrait close-ups, environmental scenes, still lifes); full bleed on openers, captioned with credit.
- Illustration: commissioned, with a recognizable hand per publication; avoid generic vector spot art.
- Icons: minimal; use text labels, arrows and rules. Share, save and listen controls in 20px monoline.
- Data graphics: restrained, labelled directly, in ink and one accent (see `data-visualization` skill).

## Motion

Quiet and tactile, like turning a page. Headlines fade up 16-24px over 500ms, images reveal with a clip-path inset wipe over 600ms, and parallax stays under 8% of the viewport. Use cubic-bezier(0.16, 1, 0.3, 1). Avoid scrolljacking, auto-playing video and animated ads; the reader's attention is the product. `prefers-reduced-motion`: opacity only.

## Fits and risks

- **Fits:** publishers, studios and magazines (`industry.media-entertainment-streaming`), fashion and lifestyle brand journals (`industry.fashion-apparel`), agency and portfolio sites (`industry.creative-agencies-studios`), NGO impact reports and longform (`industry.nonprofit-ngo`), newsletters (`channel.email`), annual reports and print (`channel.print-collateral`), content-led marketing sites (`channel.marketing-website`). `archetype.sage` and `archetype.creator` express authority and taste; `tier.premium` justifies the editing effort.
- **Risks:** requires real content, photography and editing; templated "editorial" with lorem ipsum falls apart. Heavy image and font payloads hurt performance; always set text face first.
- **Wrong for:** transactional or data-dense apps (`channel.web-app`), `industry.logistics-supply-chain` workflows where speed beats voice, and `audience.low-bandwidth-entry-devices` (large imagery and multiple webfonts).

## Do and don't

- Do design for a hierarchy of at least five distinct text roles and keep their styles fixed across pages.
- Do write real kickers, decks and captions; they are 30% of the design.
- Do let one element per page be uncomfortably large.
- Don't center-align body copy or full-justify without hyphenation (rivers at narrow columns).
- Don't place text over busy photographs without a scrim or reserved quiet area.
- Don't use more than one decorative display face; contrast comes from scale and weight, not from font collecting.

## Clichés and AI tells

- The lazy version: a Playfair Display headline over a stock photo, three-column "latest articles" cards with rounded corners and drop shadows, and an uppercase "FEATURED" tag.
- Generated editorial layouts with mock text, overlapping captions and fake bylines.
- Fix: write the real hierarchy first (kicker, headline, deck, byline), choose a distinct display face with a proper text partner (for example Instrument Serif or Bodoni Moda with Newsreader), commit to one spot color, and test the layout with three real stories of different length.

## Accessibility notes

- The spot red #D3311C passes at 4.64:1 on Newsprint, but the common brighter vermilion #E4432D falls to 3.82:1; compute the exact pair before using red for small kickers or links.
- Gray #6B6B6B reaches 4.98:1 on Newsprint but 4.41:1 on the Sunk panel; set secondary text in Ink on tinted panels.
- Keep text 18px+ with line-height 1.55+ and measure under 75ch; avoid justified text without `hyphens: auto`.
- Provide alt text for editorial images and keep captions as real text; drop caps must not split the first word for screen readers (use `::first-letter` instead of a separate element).
- Pull quotes duplicate content: mark them `aria-hidden` or use `<aside>` so they are not read twice.

## Reference anchors

- Alexey Brodovitch, *Harper's Bazaar* (1934-1958) and his *Design Laboratory*; *Ballet* (1945) photobook
- Alexander Liberman, *Vogue* art direction (from 1943)
- Herb Lubalin and Ralph Ginzburg, *Avant Garde* (1968-1971); Fred Woodward, *Rolling Stone* (1987-2002) and *GQ*
- Neville Brody, *The Face* (1981-1986) and *Arena*; David Carson, *Ray Gun* (1992-1995)
- Bloomberg Businessweek (2010s redesign), *The New Yorker*, Monocle, Kinfolk and Cereal for contemporary editorial craft
- Robert Bringhurst, *The Elements of Typographic Style*
