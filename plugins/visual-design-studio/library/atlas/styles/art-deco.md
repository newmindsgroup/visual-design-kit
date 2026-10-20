---
id: style.art-deco
axis: style
name: Art Deco
aliases: [deco, 1920s glamour, gatsby style, jazz age, streamline moderne, art moderne]
summary: Symmetrical geometric glamour - gold on black, sunbursts, chevrons and stepped forms, tall display capitals and lacquered, machine-age luxury from the Jazz Age.
tags: [geometric, gold, symmetrical, glamour, jazz-age, ornamental, luxury, 1920s]
pairs_with: [industry.hotels-travel, industry.restaurants-hospitality, industry.luxury-goods, industry.events-conferences, tier.luxury, archetype.ruler, archetype.lover, archetype.magician, channel.packaging, channel.print-collateral]
avoid_with: [industry.developer-tools, tier.value, audience.low-bandwidth-entry-devices, industry.government-civic]
version_timestamp: 2026-10-20 01:51:22 UTC
---

# Art Deco

## Essence

Machine-age opulence: rich materials and strict geometry, repeated until it feels ceremonial. The style takes its name from the 1925 Exposition internationale des arts décoratifs et industriels modernes in Paris (the label was popularized later, notably by Bevis Hillier's 1968 book). It ran through the 1930s in the Chrysler Building (William Van Alen, 1930), the Empire State Building (1931), Radio City Music Hall (1932) and the Miami Beach hotels. Where Art Nouveau imitates plants, Deco abstracts them into fans, zigzags and steps.

## Visual signature

- Bilateral symmetry on a strong central axis; stepped (ziggurat) silhouettes, fans, sunbursts, chevrons, scallops and concentric arcs.
- Gold or brass linework on near-black, deep green or navy; ivory and lacquer red as supporting colors.
- Tall, high-contrast or geometric display capitals with a small number of decorative letterforms (Cassandre's Bifur and Peignot, Broadway, Parisian).
- Double rules, inset frames, corner chamfers and borders built from repeating motifs.
- Streamlined figures and speed lines (the "Moderne" branch: Cassandre's Normandie poster, 1935); stylized animals, skyscrapers, ocean liners, women and dancers.
- Material cues: lacquer, marble, brass, inlay; on screen, flat gold fills and fine lines rather than photographic gold.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Poiret One (OFL, hairline; 36px+ only); Limelight (OFL, high-contrast Deco capitals); Marcellus (OFL, flared roman for readable subheads); commercial: Peignot or Acier (Cassandre revivals from Production Type), Broadway (Monotype) |
| Body font | Josefin Sans (OFL, 1920s geometric flavor) at 17-18px; Jost is a clean fallback; commercial: Gill Sans Nova |
| Type scale ratio | 1.333 (perfect fourth); tall caps in display, centered |
| Body size / line-height | 17-18px / 1.6 (Josefin has a small x-height, so size up); measure 50-60ch |
| Display letter-spacing | +0.04em to +0.12em for caps headlines; line-height 1.1 |
| Caps / labels | 12-14px, uppercase, +0.18em to +0.25em, weight 500 |
| Weights | 400 and 600 for body; display single weight |
| Palette | Noir #0E0E12 (oklch 0.17 0.008 285); Ivory #F3E9D2 (oklch 0.94 0.032 87); Gold #C6A15B (oklch 0.73 0.099 82); Emerald #0E4D41 (oklch 0.38 0.064 177); Navy #14233F (oklch 0.26 0.057 262); Lacquer #9E1B2B (oklch 0.46 0.165 21); Brass #7A5F2A (oklch 0.50 0.079 82) |
| Verified pairs | Gold on Noir 7.93:1; Ivory on Noir 15.96:1; Ivory on Emerald 8.07:1; Gold on Navy 6.45:1; Lacquer on Ivory 6.58:1; Brass on Ivory 4.97:1; Gold on Emerald 4.01:1 (large only); Gold on Ivory 2.01:1 fails |
| Accent proportion | Gold 5-12% as linework and ornaments; ground colors 80%+ |
| Radius | 0; use 8-16px chamfered corners (clip-path polygon) and full arches on feature panels |
| Borders | 1px gold, or a double rule (1px, 3px gap, 1px); stepped corner brackets |
| Shadow / elevation | None; depth through inset frames and layered rules |
| Spacing density | Generous: 8px base, 80-128px sections, wide margins around centered blocks |
| Grid | Symmetrical 12 columns on a central axis; centered 960-1120px container; 4 columns on mobile |
| Motion | 480-720ms, cubic-bezier(0.65, 0, 0.35, 1); curtain, iris and sunburst reveals; stagger 80-120ms |

## Composition and layout

- Center the main composition and mirror secondary elements; place a sunburst, fan or arch behind the focal point.
- Frame content with a thin inset border and corner ornaments; leave a clear margin of at least 24px inside the frame.
- Stack hierarchy vertically in tiers: small spaced-caps kicker, large display name, ornamental divider, short body, call to action.
- Build ornaments from vector primitives (repeating chevrons, concentric arcs, radiating lines) and reuse them as dividers, section headers and loading states.
- Menus, invitations, hotel and cocktail-bar sites: one hero panel, a stepped section divider, then centered text columns of 50-60ch.
- Keep UI plain beneath the ornament: forms and tables sit on flat noir or ivory panels with a single gold hairline.

## Imagery and iconography

- Photography: low-key, high-contrast interiors, architecture and portraits with warm highlights; black-and-white with a gold duotone also works.
- Illustration: flat, geometric, streamlined figures; stylized skylines, liners, peacocks, fans.
- Icons: 1.5px monoline in gold on a 24px grid with chamfered terminals; or filled glyphs inside a diamond or circle.
- Patterns: repeating chevron, scallop (fish-scale) and sunburst tiles at 5-10% opacity behind panels.

## Motion

Ceremonial and symmetrical: curtains parting from the center, sunburst rays growing outward with `clip-path: circle()`, panels rising like elevator doors. Use 480-720ms with cubic-bezier(0.65, 0, 0.35, 1) and 80-120ms stagger; gold lines draw along their length (stroke-dashoffset, 600ms). No bounce. With `prefers-reduced-motion`, swap reveals for a 150ms fade.

## Fits and risks

- **Fits:** hotels and resorts (`industry.hotels-travel`), cocktail bars and supper-club restaurants (`industry.restaurants-hospitality`), fragrance, jewelry and spirits (`industry.luxury-goods`, `channel.packaging`), galas and festivals (`industry.events-conferences`), invitations and programs (`channel.print-collateral`). Pairs with `tier.luxury` and the `archetype.ruler`, `archetype.lover` and `archetype.magician` brands that sell theatre and status.
- **Risks:** it can slide into costume (Gatsby party kitsch) and ornament-heavy pages load slowly; one distinctive motif used with discipline beats a full pattern kit.
- **Wrong for:** `industry.developer-tools` and `industry.government-civic` (ornament undermines utility and neutrality), `tier.value` (gold and symmetry promise a price point), and `audience.low-bandwidth-entry-devices` (heavy SVG ornament and webfonts).

## Do and don't

- Do commit to symmetry and one repeating motif (fan, chevron or step) used at three scales.
- Do keep gold to hairlines, ornaments and key numerals; let noir and emerald carry mass.
- Do design a plain ink-on-ivory variant for print so gold foil or metallic ink is an upgrade, not the only legibility device.
- Don't set long text in Poiret One or any hairline display face; use Marcellus or Josefin Sans.
- Don't apply gold gradients or bevels; flat gold reads classier and prints better.
- Don't mix in rounded UI cards with soft shadows; chamfers and rules keep the language intact.

## Clichés and AI tells

- The lazy version: black background, gold gradient "GATSBY" lettering, champagne-glass clipart, glitter, and a Poiret One body paragraph in gold on black.
- Generated "Art Deco" images with garbled metal lettering, asymmetric fans and mushy gold highlights.
- Fix: draw the motif as clean vectors, set copy in a real text face with checked contrast, restrict gold to 5-12% of the area, anchor the layout to a true central axis, and give the brand one specific element (the building, the liner, the product silhouette) as its sunburst focal point.

## Accessibility notes

- Gold #C6A15B has 7.93:1 on Noir but only 2.01:1 on Ivory; on light grounds use Brass #7A5F2A (4.97:1) for text and keep gold for decoration.
- Gold on Emerald is 4.01:1: large text and icons only; body copy on Emerald should be Ivory (8.07:1).
- Hairline display faces fail at small sizes; set 36px+ only and keep a plain fallback.
- Widely tracked caps slow reading; limit to labels and headlines under 8 words.
- Decorative sunbursts and patterns must be `aria-hidden` and sit behind a solid or 90%+ opaque panel when text overlays them.

## Reference anchors

- 1925 Exposition internationale des arts décoratifs et industriels modernes, Paris
- A.M. Cassandre, *Dubonnet* (1932) and *Normandie* (1935) posters; Bifur (1929) and Peignot (1937) typefaces
- William Van Alen, Chrysler Building (1930); Shreve, Lamb & Harmon, Empire State Building (1931); Donald Deskey, Radio City Music Hall interiors (1932)
- Tamara de Lempicka paintings; Erté illustrations for *Harper's Bazar*; René Lalique glass
- Bevis Hillier, *Art Deco of the 20s and 30s* (1968)
- Miami Beach Art Deco District (1930s hotels) and the Cartier Tank watch (1917-1919) as a restrained Deco object
- https://en.wikipedia.org/wiki/Art_Deco
