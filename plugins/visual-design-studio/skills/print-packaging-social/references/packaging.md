# Packaging

Version-Timestamp: 2026-10-20 02:07:10 UTC

Packaging is a structure, a shelf advertisement, a legal document and a piece of waste, in that order of design difficulty. Start from the converter's dieline, win the first two seconds at shelf distance with a clear hierarchy, leave the regulatory panel to the people accountable for it, and prove everything on a physical prototype. For the channel overview see the atlas entry [packaging](../../../library/atlas/channels/packaging.md); for print basics (profiles, ink limits, preflight) see [print production](print-production.md).

## Dieline workflow

1. **Get the structural dieline** from the converter or packaging engineer as vector (PDF or AI, or from ArtiosCAD or similar). Never draw a production dieline from a template found online.
2. **Lock it on its own layer**, as a named spot color ("Die" or "Cutter") set to overprint and marked non-printing. Use separate line styles for cut (solid), crease or fold (dashed), perforation (dotted) and glue areas (hatched).
3. **Build layers:** Die, Bleed guide, Safe guide, Art, Text, Varnish, Foil, White ink (for clear or metallic substrates), Technical notes (non-printing).
4. **Bleed** 3mm on cartons (or the converter's figure; flexible film often 2-5mm), extended past every cut. **Safe zone** 3-5mm inside cut and crease lines; 6mm from folds and glue flaps.
5. **Glue areas:** knock out ink and varnish where the converter specifies, or the glue will not hold.
6. **Panel map:** label each panel (front or principal display panel, back, left, right, top, bottom, inside flaps) and its reading orientation when the pack stands on shelf. Rotate text so it reads correctly once folded.
7. **White mockup** early: print the dieline at 100%, cut, fold and check panel order, orientation and flap overlaps.
8. **Printed prototype** on the actual board or film before artwork approval; hold it, put it on a shelf, photograph it.

## Structures and process implications

| Structure | Typical substrate | Print process | Design notes |
| --- | --- | --- | --- |
| Folding carton (tuck end, sleeve, tray, auto-lock bottom) | SBS, FBB or recycled board (CRB) | Offset litho, digital for short runs | Fine detail possible; check board shade (recycled board is gray-backed) |
| Corrugated shipper or e-commerce box | E, B or C flute | Flexo (post-print) or litho-laminated | Flexo: fewer colors, bolder type, coarser detail; litho-lam for retail-ready display |
| Rigid set-up box | Chipboard wrapped in printed or specialty paper | Offset on the wrap | Luxury; wrap paper bleeds around edges; foils and embossing common |
| Flexible (pouch, flow wrap, sachet) | Film laminates, paper-film, mono-PE or mono-PP | Gravure, flexo or digital | Needs white ink under color on clear or metallized film; seals and gussets eat space |
| Labels (pressure-sensitive, wrap, sleeve) | Paper, film | Flexo, digital, offset | Curved containers distort art; shrink sleeves need distortion artwork from the converter |
| Cans and bottles | Aluminum, glass, PET | Dry offset (cans), screen print, labels | Limited colors on direct print; check seam and curvature zones |

Flexo minimums (confirm with the converter): positive type about 6pt and reversed about 7-8pt in a sturdy sans, lines 0.2mm or more, avoid tiny highlight dots and long vignettes that break into steps.

## Panel hierarchy

The **principal display panel (PDP)** is the panel most likely to be seen at retail (a defined term in US FDA labeling rules). Design it for 2-3m and a few seconds:

1. **Brand block:** the brand's distinctive assets (logo, color, shape) in a consistent position across the range.
2. **Product identity:** what it is, in plain words (in US food law, the "statement of identity").
3. **Variant:** flavor, scent, strength, size; usually coded by color, and that code must survive color-blind viewing (add icons or words).
4. **Key benefit or reason to choose:** one, maybe two.
5. **Required PDP elements** for the market (for example net quantity in the US).

Everything else (story, secondary claims, usage, cross-sell) goes to side and back panels. A PDP with five claims has none.

Range architecture: keep the brand block, layout grid and type fixed; vary color and imagery by variant. Shoppers find their variant by color, then confirm by word.

## Regulatory panel elements

These vary by product category and jurisdiction and change over time. The client's regulatory team or counsel owns the content; the designer owns legibility and placement. Verify every item for the specific product and market.

Examples of what typically affects design:

- **US food (FDA):** statement of identity and net quantity on the PDP (net quantity in the bottom 30% of the PDP, in both US customary and metric units, with minimum type heights set by PDP area); Nutrition Facts panel in the prescribed format; ingredient list in descending order by weight; major food allergen declaration (nine allergens since sesame was added in 2023); name and place of business of the manufacturer, packer or distributor.
- **EU food (Regulation 1169/2011):** mandatory particulars with a minimum x-height of 1.2mm (0.9mm if the largest surface is under 80cm²); allergens emphasized within the ingredients list (for example in bold); nutrition declaration; net quantity; date marking; food business operator's name and address; origin where required.
- **EU cosmetics (Regulation 1223/2009):** responsible person, INCI ingredient list, period-after-opening symbol or date of minimum durability, batch number, function and precautions; translated per member state.
- **US cosmetics:** ingredient declaration and warnings under FDA rules, with additional requirements under MoCRA (2022), such as a domestic contact for adverse events.
- **Languages:** Canada requires English and French on most consumer packaging; Quebec's French-language rules tightened in 2025. Multi-country EU packs often carry several languages; plan panel space before design.
- **Recycling and environmental marks:** France requires the Triman logo with sorting information on many products; resin codes are not recyclability claims; the EU Packaging and Packaging Waste Regulation (Regulation (EU) 2025/40) is phasing in harmonized rules; EU Directive 2024/825 bans generic environmental claims ("eco-friendly", "green") without recognized proof from 27 September 2026; in the US, the FTC Green Guides govern environmental claims.
- **Warnings:** California Proposition 65 warnings; alcohol, tobacco, cannabis and pharmaceuticals have their own regimes (EU medicines also need Braille). Use specialist counsel for these categories.

Design rules for the regulatory panel: build a grid with fixed zones for nutrition or ingredient tables, legal copy at the required minimum size (never shrink to fit), high contrast, no text over imagery, and no line breaks that change meaning.

## Barcodes

For EAN-13 and UPC-A in general retail point of sale (per GS1 General Specifications; verify the current release and your GS1 member organization's guidance):

| Item | Value |
| --- | --- |
| Nominal size (100% magnification) | X-dimension 0.330mm; EAN-13 about 37.29mm wide including quiet zones, bars 22.85mm tall (about 25.93mm with the human-readable digits) |
| Allowed range | 80% to 200% magnification (X-dimension 0.264-0.660mm) |
| Quiet zones | EAN-13: 11X left, 7X right (3.63mm and 2.31mm at 100%); UPC-A: 9X both sides (2.97mm at 100%) |
| Height | Do not truncate bar height; it reduces scan tolerance |
| Colors | Dark bars (black, dark blue, dark green, dark brown) on a light background (white, yellow, orange, or red, because scanners use red light). Red, orange or yellow bars do not scan |
| Placement | Flat panel, away from folds, seams, edges and curves; usually lower right of the back panel |
| Curved surfaces | On small-diameter cylinders, rotate to ladder orientation (bars horizontal); check GS1 curvature guidance |
| Production | Generate from verified barcode software as vector; never redraw or stretch; account for the converter's bar width reduction on flexo |
| Verification | Test printed samples with an ISO/IEC 15416 verifier; GS1 sets a minimum grade for retail symbols |

GS1 numbers are allocated by GS1 member organizations to the brand owner; never invent or reuse numbers. Retailers are moving toward 2D barcodes (GS1 Digital Link QR codes) under GS1's "Sunrise 2027" program; plan for a QR plus the linear barcode during the transition.

## Shelf-impact tests

- **Shelf mockup:** photograph the real shelf (or build one) and place the new pack at true scale among 8-12 competitors. View at 2-3m and at a glance.
- **Find-the-pack:** ask 5-10 people to find the product on the shelf photo; note time and errors. Repeat with the variant.
- **Blur and grayscale:** blur the shelf photo; the brand block should still stand out by shape and contrast, not only by hue.
- **Billboard effect:** test one facing and a block of three to five facings; strong patterns and edge-to-edge color often work better in blocks.
- **E-commerce thumbnail:** view the pack at 100-200px wide, as on a mobile search results page. The "mobile ready hero image" approach (from Cambridge's Inclusive Design Group with Unilever, adopted by GS1 UK) shows brand, format, variant and size clearly in the thumbnail.
- **Color-vision check:** simulate deuteranopia and protanopia on the variant range.
- **Hand test:** hold the prototype; check grip, opening, readable panels at 40cm, and how it looks when the lid is open.

## Sustainability

- Prefer mono-material structures (all-paper, mono-PE, mono-PP) that local systems can recycle; avoid PVC and mixed laminates where possible.
- Paper is not automatically better than plastic; compare total impact and the recycling stream.
- Avoid full plastic lamination and metallized films on paper packs; use aqueous coatings or recyclable alternatives where performance allows. Soft-touch lamination and heavy foil can hinder recycling.
- Right-size boxes to reduce void space; the EU is introducing maximum empty-space ratios for some packaging.
- Use FSC- or PEFC-certified board and paper; print certification marks only with a valid license.
- Make environmental claims specific, substantiated and qualified ("Box made from 90% recycled fiber"), never generic.
- Design for the disposal step: on-pack sorting instructions in the market's system (Triman in France, How2Recycle in the US and Canada as a voluntary label).

## Mockups and presentation

- Present structural options as white or kraft prototypes before graphics.
- Render with a mockup made from the real dieline folded in 3D (packaging CAD, Blender, or a licensed mockup template), on the actual substrate color (kraft, gray-back board, clear film).
- Show context: on shelf with competitors, in hand, in an e-commerce grid, open and closed.
- Never show finishes the budget or the converter cannot produce.
- Final approval is on a printed prototype or press proof, never on a flat PDF alone.

## Production handoff

- Final artwork PDF with dieline, separations listed (CMYK and each spot with Pantone and CMYK fallback), finish layers named, barcode as vector with its number, fonts outlined, and a technical notes panel (substrate, process, finishes, color targets).
- Legal copy signed off in writing by the client's regulatory owner.
- Color approval on the actual stock; record the proof reference.
- Version and date on the non-printing slug.

## Common failures

- Designing on a generic template → converter's dieline first.
- Five claims on the PDP → one benefit; move the rest.
- Variants coded by color alone → add words and icons.
- Legal copy shrunk to fit the design → layout reserves its space at the required size.
- Barcode in brand red, on a curve, or truncated → dark on light, flat, full height, 80-200%.
- Approving from screen renders → printed prototype on the real board.
