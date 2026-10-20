# Type pairing

Version-Timestamp: 2026-10-20 02:07:10 UTC

A pairing is a division of labor: one face carries personality at large sizes, the other carries reading and interface at small sizes. Every family below is licensed under the SIL Open Font License 1.1 (OFL) and is available from the Google Fonts repository (`github.com/google/fonts/tree/main/ofl/<name>`) as of 2026. Confirm the license file of the exact version you ship.

## Principles

1. **Contrast one thing, match the rest.** Pair a serif with a sans, or a wide display with a normal text face, or a heavy grotesque with a light serif italic. Two similar sans-serifs (Manrope with Plus Jakarta Sans) look like a mistake.
2. **Match proportions.** Similar x-height and width make the pair feel related. When x-heights differ, adjust the size of one role, or use `size-adjust` in `@font-face`.
3. **Superfamilies are the safe default.** Source Serif 4 with Source Sans 3, Instrument Serif with Instrument Sans, IBM Plex Serif/Sans/Mono, DM Serif Display with DM Sans: shared skeletons, designed to work together.
4. **Keep era and construction coherent,** or clash on purpose. Geometric with geometric (Jost, League Spartan), humanist with humanist (Literata, Source Sans 3). A deliberate clash (Anton with Courier Prime) needs a reason from the brief.
5. **One family is often enough.** A variable family with weight, width and optical-size axes (Roboto Flex, Archivo, Bricolage Grotesque, Mona Sans) gives hierarchy without a second voice.
6. **Display faces stay large.** Check the display face at its smallest heading size (usually 24-32px). Cormorant, Bodoni Moda at high contrast, Shrikhand and Michroma fall apart below that.
7. **Two families plus a mono, maximum.** A third voice needs a job (code, data, a campaign headline).
8. **Test with the real copy:** the brand name, the longest headline, a price, a table, the hardest language.

## Inter, system sans and the generic default

Inter is excellent for dense product UI: large x-height, tabular figures, a slashed zero, very wide language coverage and an optical-size axis since version 4. It becomes the generic AI look when it is used for every brand, every headline and every tier without a reason. Use it when the brief is a data-heavy product and neutrality is the point. Otherwise pick a face with a point of view; neutral alternatives that still read clearly: Hanken Grotesk, Instrument Sans, Figtree, Public Sans, Geist, Onest, Schibsted Grotesk, Albert Sans.

## Thirty vetted OFL pairings

Heading face first, text and UI face second. Atlas IDs refer to `style.*` entries; read them with `python3 ../../../library/scripts/atlas.py show <id>`.

### Serif with sans

| # | Heading | Text / UI | Mood | Best for | Atlas styles |
| --- | --- | --- | --- | --- | --- |
| 1 | Newsreader (optical size 48-72 for heads) | Hanken Grotesk | Informed, contemporary newsroom | News, think tanks, content hubs, annual reports | `style.editorial-magazine` |
| 2 | Instrument Serif | Instrument Sans | Understated studio editorial | Agencies, architecture, portfolios, culture | `style.editorial-magazine`, `style.quiet-minimal` |
| 3 | Fraunces (SOFT 100, WONK 0) | Figtree | Warm, soft, hand-finished | DTC food, bakeries, wellness, children's publishing | `style.handcrafted-organic`, `style.eco-natural-sustainable` |
| 4 | Albert Sans (headings, UI) | Literata (reading) | Calm, Nordic, bookish | Reading apps, education, furniture, slow-living retail | `style.scandinavian-nordic`, `style.quiet-minimal` |
| 5 | Source Serif 4 | Source Sans 3 (+ Source Code Pro) | Neutral, institutional, multilingual | Government, NGOs, research, documentation | `style.civic-plain`, `style.corporate-modern` |
| 6 | Merriweather | Public Sans | Plain public service | Public services, forms, civic tech (the US Web Design System offers both) | `style.civic-plain` |
| 7 | Cormorant Garamond (28px+ only) | Jost | Airy, refined luxury | Hotels, jewelry, weddings, spas | `style.classic-luxury-serif` |
| 8 | Bodoni Moda (optical size high) | Work Sans | High-fashion contrast | Fashion, perfume, magazines | `style.fashion-editorial-didone` |
| 9 | Gloock | Onest | Bold editorial beauty | Cosmetics, boutique retail, salons | `style.fashion-editorial-didone`, `style.editorial-magazine` |
| 10 | EB Garamond | Libre Franklin | Literary, scholarly, heritage | Publishers, universities, law firms, wine | `style.classic-luxury-serif`, `style.vintage-heritage-americana` |
| 11 | Libre Caslon Display + Libre Caslon Text | Archivo (SemiCondensed for labels) | Americana heritage | Craft drinks, outdoor goods, heritage retail | `style.vintage-heritage-americana` |
| 12 | Young Serif | Karla | Retro-friendly mid-century | Restaurants, coffee, homeware | `style.mid-century-modern` |
| 13 | Lora | Nunito Sans | Gentle, caring, steady | Healthcare, therapy, family services | `style.clinical-calm` |
| 14 | IBM Plex Serif | IBM Plex Sans + IBM Plex Mono | Engineered, corporate | Enterprise software, technical docs | `style.corporate-modern` (Plex is IBM's corporate face; avoid for IBM competitors) |

### Sans with sans, and display with text

| # | Heading | Text / UI | Mood | Best for | Atlas styles |
| --- | --- | --- | --- | --- | --- |
| 15 | Schibsted Grotesk | Inter | Objective Swiss clarity | Finance, B2B, wayfinding, conferences | `style.swiss-international` |
| 16 | Inter (tabular figures, slashed zero) | JetBrains Mono | Utilitarian precision | Dashboards, admin, trading, analytics | `style.data-dense-utilitarian` |
| 17 | Geist | Geist Mono | Developer-native, crisp | Developer tools, infrastructure, AI products | `style.dark-tech-developer` |
| 18 | League Spartan | Work Sans | Constructivist, geometric, assertive | Cultural institutions, architecture, posters | `style.bauhaus-constructivist` |
| 19 | Marcellus (caps, +0.08em) | Jost | Art Deco glamour | Bars, theaters, events, premium spirits | `style.art-deco` |
| 20 | Big Shoulders Display | Barlow | Industrial sport energy | Sports, fitness, logistics, events | `style.bold-geometric-sport` |
| 21 | Archivo (Expanded, 800) | Archivo + Space Mono | Loud, honest, graphic | Challenger brands, Gen Z fintech, campaigns | `style.neo-brutalist` |
| 22 | Space Grotesk | Space Mono | Raw, nerdy, web-native | Indie tools, online zines, experimental sites | `style.web-brutalist` |
| 23 | Syne (700-800) | Manrope | Art-world, experimental | Galleries, festivals, creative studios | `style.kinetic-experimental-type`, `style.maximalist-eclectic` |
| 24 | Unbounded | Rubik | Wide, chrome-era futurism | Music, campaigns, crypto, youth brands | `style.y2k-cyber`, `style.memphis-postmodern` |
| 25 | Michroma (caps, 24px+) | Outfit | Space-age, synth retro | Events, gaming, audio gear | `style.retro-futurism-synthwave` |
| 26 | Shrikhand | DM Sans | Groovy, sunny, retro | Food trucks, festivals, merchandise | `style.seventies-psychedelic-groovy` |
| 27 | Anton | Courier Prime | Cut-and-paste urgency | Zines, activism, music, streetwear | `style.grunge-punk-zine`, `style.collage-mixed-media` |
| 28 | Fredoka | Nunito | Bubbly, kind, round | Kids, casual games, friendly consumer apps | `style.playful-bubbly`, `style.soft-ui-neumorphic` |
| 29 | Lexend | Atkinson Hyperlegible Next | Clear, low-effort reading | Education, public services, accessibility-first products | `style.clinical-calm`, `style.civic-plain` |
| 30 | Bricolage Grotesque (optical size) | IBM Plex Mono | Inky, characterful, printed | Riso-style posters, indie publishing, illustrated brands | `style.risograph-print-texture`, `style.illustrative-narrative` |

### Single-family systems

| Family | Axes or range | Fits | Atlas styles |
| --- | --- | --- | --- |
| Roboto Flex | Weight, width, optical size, grade and more | Material-based apps, dense-to-display range in one file | `style.flat-material` |
| Manrope | Weight 200-800 | Calm tech, glassy and gradient SaaS that wants a softer voice than Inter | `style.glass-spatial`, `style.vibrant-gradient-saas` |
| Mona Sans | Weight, width | Product brands that need condensed and expanded cuts | `style.neo-brutalist`, `style.bold-geometric-sport` |
| Recursive | Weight, slant, casual, mono | Developer brands that move between sans and mono | `style.dark-tech-developer`, `style.kinetic-experimental-type` |
| Hanken Grotesk | Weight 100-900 | Corporate and B2B with warmth | `style.corporate-modern` |

## Mono uses

| Job | Recommended | Notes |
| --- | --- | --- |
| Code blocks, terminals | JetBrains Mono, Geist Mono, Source Code Pro, Fira Code | Programming ligatures off by default in docs (`font-variant-ligatures: none`) so `!=` reads as typed |
| Data captions, metadata, timestamps | IBM Plex Mono, DM Mono, Red Hat Mono | Use sparingly as a texture; prefer tabular figures in the text face for tables |
| Display and brand texture | Space Mono, Martian Mono, Azeret Mono | Strong personality; not for long code |
| Screenplays and typewriter voice | Courier Prime | Designed as a screenplay Courier replacement |
| Accessibility-first code and forms | Atkinson Hyperlegible Mono | Distinct I, l, 1, O and 0 |

Mono text runs wide: set it 0.9-0.95x the size of adjacent sans text so it looks the same size.

## Commercial alternatives for premium tiers

When budget and licensing allow, these are common upgrades for the same moods (license per use; see [font sourcing](font-sourcing.md)):

- Editorial serif: Tiempos (Klim), GT Super (Grilli Type), Publico (Commercial Type).
- Neutral grotesque: Söhne (Klim), Suisse Int'l (Swiss Typefaces), Neue Haas Unica (Monotype).
- Luxury display: Canela (Commercial Type), Ogg (Sharp Type), Editorial New (Pangram Pangram).
- Geometric: Futura PT (ParaType), GT Walsheim (Grilli Type).
- Tech and mono: GT America Mono (Grilli Type), Berkeley Mono (US Graphics).

## Pairing check before presenting

- Headline, paragraph, button, label, price and table row rendered with real copy at real sizes.
- The pairing differs from the category's usual pair (run the category scan in the `design-director` skill).
- Both faces cover every required language and the symbols the content uses (currency, arrows, fractions).
- Weights in use: no more than 3 per family; no faux bold or italic.
- Contrast and size checked in dark mode, where thin strokes thin further.
