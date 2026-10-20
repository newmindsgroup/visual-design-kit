---
id: channel.packaging
axis: channel
name: Packaging
aliases: [package design, pack design, labels, boxes, cartons, bottles, pouches, cpg packaging, unboxing]
summary: Three-dimensional, shelf-and-hand design where dielines, print process, barcodes, regulatory copy and material choice constrain a brand that must win in seconds.
tags: [packaging, dieline, label, carton, pouch, shelf, cpg, barcode, unboxing, regulatory]
pairs_with: [style.vintage-heritage-americana, style.handcrafted-organic, style.risograph-print-texture, style.bold-geometric-sport, style.illustrative-narrative, industry.food-beverage-cpg, industry.beauty-cosmetics, industry.ecommerce-dtc, industry.luxury-goods, tier.premium]
avoid_with: [style.glass-spatial, style.kinetic-experimental-type]
version_timestamp: 2026-10-20 02:01:01 UTC
---

# Packaging

## Formats and specs

The converter or printer supplies the dieline and print specification; use theirs, never a generic template. Regulations and GS1 rules are jurisdiction-specific; verify with the authority named.

| Item | Spec | Notes |
| --- | --- | --- |
| Dieline | Vector dieline from the converter on a locked, named spot-color layer (not printed, set to overprint); cut, crease, perforation and glue areas labelled | Design only after the structure is approved |
| Bleed | 3 mm (0.125 in) typical for cartons and rigid boxes; 1.5-3 mm for labels; 2-5 mm for flexible film (ask) | Extend art past cut and fold lines |
| Safe area | 3-5 mm inside cut and crease lines; keep text 6 mm from folds and glue flaps | Glue panels and tabs: keep clear of print or mark "no varnish" |
| Color | CMYK plus 1-3 Pantone spots for brand colors; check the printing process (offset, flexo, gravure, digital) for gamut and registration | Plan ink coverage for the substrate: kraft, uncoated board and clear film change color radically |
| Resolution | 300 ppi photos at final size; vector for logos, type and barcodes; flexo needs minimum line 0.5 pt and type 6 pt or larger (reverse 7 pt+) | Confirm minimums per process with the printer |
| Barcode (EAN-13 / UPC-A) | Nominal size about 37.29x25.93 mm at 100% magnification; allowed 80-200%; clear quiet zones left and right; dark bars on light background | Place on a flat panel away from folds and seams; check bar direction relative to print direction; GS1 allocates the numbers (verify the current specification) |
| File format | PDF/X-4 or native layered AI/PDF with dieline; fonts outlined; spot colors named; varnish and foil layers separate | Add a color bar and registration if the converter asks |
| Finishes | Matte or gloss varnish, soft-touch, foil, emboss, spot UV, window patching | Each finish raises MOQ and cost; test on stock |
| Mockup and proof | White dummy plus a printed prototype on actual board; hold in hand and view on shelf | Never approve from a flat PDF only |
| Legal copy (examples) | EU Regulation 1169/2011: mandatory food information with minimum x-height 1.2 mm (0.9 mm for small packs); US FDA Nutrition Facts format and net-quantity placement on the principal display panel; California Prop 65 warnings; pharma Braille in the EU | Verify per product category and market |

## Structure and hierarchy

- **Shelf hierarchy:** brand, product or variant, descriptor, then claims. Aim for the brand and variant to register at 2-3 meters in about 3 seconds ("billboard in an aisle"); secondary information waits for pick-up.
- **Panels:** front (principal display) carries 3 levels of information at most; side and back carry story, ingredients, nutrition, instructions, barcode, recycling, and legal. Design every panel; the pack is seen from 3-4 angles.
- **Variant systems:** hold structure constant (logo position, type, grid) and vary color, illustration or photo to signal flavor, scent or strength. Keep a distinct color per variant with sufficient hue separation in a row (deltaE visible side by side).
- **Blocking on shelf:** repeat facings should form a brand block; test a 3x3 and a 6x2 arrangement.
- **E-commerce:** the front panel must read at 150-300 px thumbnails; design a clean hero angle and an unboxing sequence (outer shipper, tissue, insert).
- **Shape and material:** structure carries brand as much as graphics: bottle shape, closure, carton form, texture. Consider opening experience, resealability and refill formats.

### Pack type notes

| Pack type | Common process and substrate | Design notes |
| --- | --- | --- |
| Folding carton | Offset, flexo or digital on SBS, FBB or kraft board | Dieline from the converter; spot UV, foil and emboss are common; keep glue flaps clear |
| Flexible pouch | Flexo or gravure on laminated film; digital for short runs | Keep text out of seal zones (commonly 10-15 mm at top and bottom; confirm); matte or gloss film changes color |
| Pressure-sensitive label | Flexo or digital on paper or film | Wrap-around labels need alignment to seams; 1.5-3 mm bleed; check curvature |
| Bottle or can | Direct print, shrink sleeve, or label; screen print on glass | Test on the curved form; allow for seams and caps |
| Tube | Offset or flexo on laminate, shoulder crimp area | Reserve the crimp end for code and batch marks |
| Rigid box | Printed wrap paper over board | Wrap folds, hinge and lid edges need tolerance; plan inserts and spine |

## Craft defaults

- Type: strong brand mark at minimum 8-10 mm cap height on small packs; ingredient and legal text at the legal minimum or larger (6 pt is the practical floor for many products, but check the rule); high contrast, 4.5:1 equivalent, flat color panels behind small text.
- Color: use brand color as a large field; limit palette to 2-4 inks for cost; verify contrast on the final substrate; consider the effect of varnish and light on a refrigerator case or shelf LED.
- Imagery: appetizing and honest; product photos must represent actual contents (serving suggestion disclaimers when needed); avoid decorating with unnecessary icons.
- Claims: only those you can substantiate ("organic", "recyclable", "sugar free" have legal definitions); keep claim icons consistent and few.
- Sustainability: reduce inks and finishes that block recycling, use mono-material where possible, add on-pack disposal guidance (How2Recycle in the US, Triman in France); avoid vague "eco" imagery.
- Accessibility: consider tactile cues (embossed indicators), large-print and QR links for accessible information; contrast for low-vision users; avoid reflective foil over key text.
- Motion: for digital and unboxing experiences, 300-600ms reveal animations that echo the pack's opening; keep them separate from the physical spec.

## Production and handoff

- Workflow: brief, structure selection (dieline library from converter), concept, flat art, 3D mockup (Adobe Dimension, Esko ArtiosCAD, Blender), regulatory review, prototype, proof, press check, production.
- Artwork management: version control with SKU, language and market variants; use a master template and layer-based variant system; change logs. The `print-packaging-social` skill holds the deeper prepress and packaging guide.
- Regulatory review: a qualified specialist reviews claims, nutrition, safety warnings, symbols and languages per market before print; label changes can take weeks.
- Supplier collaboration: ask for press-ready PDF proof, color-matched drawdowns for spot colors, and approvals signed by brand and regulatory owners.
- Cost levers: number of colors, finishes, board weight, print run, and structure complexity; show the client options with unit-cost estimates.

## QA checklist

- [ ] Dieline version matches the converter's current approved file; art is on the correct panels.
- [ ] Bleed, safe margins and glue areas respected; no text across creases unless intentional.
- [ ] Barcode scans (verify with a grader or scanner test), at 80% magnification or larger with quiet zones.
- [ ] Legal and nutrition copy checked by a regulatory reviewer for each market and language.
- [ ] Print proofs checked on actual stock; spot colors match drawdowns; no dark-on-dark small text.
- [ ] Variants distinguishable at 2-3 meters and side by side; front panel reads at thumbnail size.
- [ ] Recycling and sustainability marks accurate and positioned correctly.
- [ ] All SKUs and languages preflighted for fonts, links and spot-color names.

## Reference anchors

- GS1 General Specifications and barcode guidelines (gs1.org) for symbol size and placement
- Regulation (EU) No 1169/2011 on food information; US FDA labeling guidance for packaged foods
- Esko, Ghent PDF Workgroup and FTA (Flexographic Technical Association) technical guides
- Packaging of the World, The Dieline and Pentagram's packaging work as craft benchmarks
- Dyson, Aesop, Oatly, Heinz and Innocent as widely cited examples of structure and graphic working together
