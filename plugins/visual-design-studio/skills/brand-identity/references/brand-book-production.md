# Brand book production

Version-Timestamp: 2026-10-23 20:10:44 UTC

Produce the guidelines book as finished files: a print-ready PDF master rendered by the kit, a screen PDF, and an editable twin in Canva for the team that will maintain it. [Guidelines](guidelines.md) says what the book must contain and how to write the rules; this file says how to lay it out page by page, where every value comes from, and who signs it off.

## Editions and defaults

| Edition | Format | Default spec | Change when |
| --- | --- | --- | --- |
| Screen PDF (primary) | Landscape 16:9, 1920x1080 px pages, RGB, fonts embedded, tagged, bookmarks per section | 24-40 pages for a startup, 40-60 mid-market, 60-100 enterprise | Portal-first clients: the screen PDF becomes a 10-15 page summary that links to the portal |
| Print master | A4 landscape 297x210 mm (US: Letter landscape 11x8.5 in), 3 mm (0.125 in) bleed, crop marks, PDF/X-4, CMYK for the printer's condition, spot colors kept as spot | Only when the book will be printed or the client asks for it | Bound hardcover or coffee-table edition: ask the printer for page count rules (multiples of 4 or 16) and spine width |
| Editable twin | Canva design built from the same tokens and copy | Pages the client team will edit: cover, contacts, templates section, changelog | Client works in Figma or InDesign instead: the twin lives there |
| Quick reference | 1-2 pages, same grid, PDF and PNG | Always | |

Layout defaults for both PDF editions: 12-column grid, 15 mm outer margins (print) or 96 px (screen), 5 mm (24 px) gutters, running footer with section name, page number, version and date. Body text 10-11 pt print, 20-24 px screen; one display size per page. Left half for the rule, right half for the visual is the default spread; full-bleed image pages for imagery and applications.

## Page-by-page contents (mid-market default, about 48 pages)

| Pages | Section | Contents and concrete defaults |
| --- | --- | --- |
| 1 | Cover | Logo, "Brand guidelines", version (v1.0) and date. No tagline unless it is part of the lockup |
| 2 | Contents | Section list with page numbers; PDF bookmarks match it |
| 3 | Start here | Purpose of the book, owner and contact, where to download files, version and date, status legend (approved, provisional, deprecated) |
| 4-6 | Brand foundation | Purpose, positioning statement, 3-5 attributes as "X, not Y", archetype, proof points. One idea per page |
| 7-9 | Voice | 3-4 voice principles with a do and don't line each, tone by context table, vocabulary and banned words, mechanics (capitalization, numbers, dates) |
| 10 | Logo overview | Primary lockup large, all approved versions small, one sentence on the idea |
| 11 | Logo construction | Base unit (the main stroke weight), the grid or geometry that drove decisions, optical corrections stated as numbers. Show only construction that was used |
| 12 | Clear space | Clear space = 1x the named element (cap height or symbol width) on all sides, drawn with the element itself as the measuring unit. Exception: 0.5x for tight UI headers, labeled |
| 13 | Minimum sizes | Table in px and mm: wordmark 80 px / 20 mm, horizontal lockup 100-120 px / 25-30 mm, symbol 16 px / 6 mm, tagline dropped below 150 px / 35 mm. Replace with the values from your render and print tests |
| 14 | Lockups | Horizontal, stacked, symbol only, with tagline, co-brand lockup. Name each one as its file name says |
| 15 | Color versions | Full color, 1-color black, 1-color white (reversed), on brand color, on photography. Approved backgrounds shown |
| 16-17 | Logo misuse | 8-12 drawn misuses with a text label each (stretched, recolored, rotated, outlined, effects, rearranged, crowded, low contrast, busy photo, tagline too small) |
| 18 | Co-branding | Partner lockup spacing (2x clear space between marks, divider rule optional), equal optical size, who leads |
| 19 | Color palette | Swatches at their usage proportion (for example 60% neutral, 25% primary, 10% secondary, 5% accent), names and roles |
| 20 | Color specifications | One row per color: HEX, RGB, CMYK coated, CMYK uncoated, Pantone C, Pantone U, RAL or NCS for signage. Source of truth per column (see below) |
| 21 | Tints and dark mode | Tint steps, dark-mode values from the token file's dark mode |
| 22 | Accessible pairs | Approved text and background pairs with computed contrast ratios, AA or AAA marked, pairs never to use |
| 23-24 | Typography | Families and weights, where to license, web, app and Office rights, fallbacks (Arial for sans, Georgia for serif) for Office and email |
| 25 | Type scale | Display to caption with size, line height, tracking, case. Screen values from tokens; print values in pt |
| 26 | Non-Latin scripts | Matched families per script, or "not yet defined" marked provisional |
| 27-28 | Graphic device | Construction, scale, crop and color rules; 3 correct and 3 incorrect uses |
| 29-32 | Imagery | Photography principles with 6-12 do and don't images (licensed or commissioned only), illustration style, AI imagery policy and labeling |
| 33 | Iconography | One icon family (see the [asset licenses](../../../library/knowledge/ASSETS-LICENSES.md) defaults), 24 px grid, 1.5-2 px stroke at 24 px, corner treatment, color rules, when to draw custom icons |
| 34 | Motion and sound | Logo animation (duration 1.5-3 s), easing from tokens, reduced-motion version, sonic logo if any |
| 35-42 | Applications | Business card, letterhead, email signature, presentation, social posts, website, signage, packaging or merchandise. Real layouts, not mockup-only scenes |
| 43 | Accessibility | Contrast rules, minimum text sizes (print body 9 pt minimum, screen 16 px), alt text and captions policy |
| 44-45 | Files and naming | Folder tree, file naming convention, "which file for which use" table. See [identity deliverables](identity-deliverables.md) |
| 46 | Governance | Owner, approval route, how to request new assets, review cadence |
| 47 | Changelog | Version, date, what changed, who approved |
| 48 | Back cover | Contacts and download link |

Startup books drop pages 18, 21, 26, 27-28 and half the applications (about 28 pages). Enterprise books add brand architecture (master brand, sub-brands, endorsed brands), regional pages, channel playbooks as separate volumes, and legal pages (trademark notices and registered marks).

## Sources of truth

Every value in the book comes from one file. Never type a value into a page by hand.

| Value | Source of truth | Book shows |
| --- | --- | --- |
| Screen colors (HEX, RGB) | The token file (`library/tokens/dist/tokens.resolved.json` or the project's own) | Generated from tokens at build time |
| CMYK | A conversion with the printer's ICC profile for the paper and press (for example PSO Coated v3 / FOGRA51 in Europe, GRACoL 2013 / CRPC6 in the US), then adjusted against a signed press proof | Values from the signed proof, with the profile named |
| Pantone | Picked visually from a current physical Pantone guide under D50 light, not from a software conversion. Name the guide edition; Pantone values change between editions (verify against the current guide) | Pantone C and U, guide edition |
| RAL or NCS | Matched by the sign maker against physical fan decks | Code and the match date |
| Type | Font files and license records | Family, version, license, where to get it |
| Logo geometry | The native master file | Exported art, never redrawn for the book |

The kit's tokens hold screen values only. Keep CMYK, Pantone and RAL values in a print spec data file next to the tokens (one row per color, with profile, proof date and approver) and generate page 20 from it. When the screen and print values disagree, the screen token wins on screen, the signed proof wins in print, and the book says so.

## Production pipeline

1. **Lock inputs.** Approved strategy copy, logo masters, tokens, print spec data, licensed fonts and images with [provenance records](../../../library/knowledge/ASSETS-LICENSES.md#provenance-record).
2. **Build the print master** from the kit's collateral templates in `library/examples/collateral/` (HTML and CSS pages that read the tokens and render to PDF). Use its page size, bleed and crop-mark settings; follow its README for the PDF/X output and preflight.
3. **Render the screen PDF** from the same source with RGB output, no bleed or marks, and PDF tags and bookmarks.
4. **Inspect.** Open both PDFs at 100% and 400%: check overset text, widows, image resolution (300 ppi at print size, 150 ppi minimum for large images seen from a distance), and that swatches match the spec table. Preflight the print PDF.
5. **Build the editable twin in Canva.**
   - Recurring pages and templates (business card, letterhead, social posts, deck): rebuild each once in Canva as a Brand Template with named fields, then fill it through the Canva connector or API. Autofill and brand templates need a Canva Pro, Teams or Enterprise plan per Canva's current API spec (2026-10-22); older Canva guide pages still say Enterprise only.
   - The book itself: import the screen PDF as a starting point (Canva PDF import: up to 500 pages, 300 MB, about 1,400 elements; whether text stays editable is inconsistent across Canva Help pages, so check). Fix fonts and grouping by hand.
   - Upload logos, icons and fonts to the client's Canva brand kit. Canva's REST API has no brand-kit endpoints; the Canva connector can list brand kits (verify write access per plan).
6. **Approve** (below), then publish: PDFs to the portal or shared drive, the twin shared with editors only.

Canva is the editable twin, not the print master. Canva's API PDF export has no CMYK, bleed or crop-mark options. If someone edits in Canva and needs print, they export by hand with PDF Print, CMYK, crop marks and bleed (CMYK export is reported to need a paid plan; unverified) and preflight again. The kit's PDF stays the reference for print.

## Who approves

| Item | Drafted by | Approved by | Evidence kept |
| --- | --- | --- | --- |
| Foundation and voice pages | Strategist or writer | Client CEO, founder or CMO | Signed-off copy deck |
| Logo, lockups, misuse | Designer | Brand owner; legal confirms trademark status before publication | Approved master files and the trademark note |
| Color specification | Designer with the printer | Brand owner for screen values; production lead signs the press proof | Proof photo or scan, profile, date |
| Typography and licenses | Designer | Brand owner; procurement for paid licenses | License records |
| Imagery and icons | Designer | Brand owner; legal for people, trademarks and paid licenses | Provenance records |
| Whole book, each version | Project lead | Brand owner | Changelog entry with approver and date |

Mark anything not yet approved "provisional" on the page itself. Never ship a book with unapproved pages unlabeled.

## Common failures

- Values typed by hand into pages drift from tokens → generate color and type pages from the token and print spec files.
- CMYK copied from a converter with no profile named → convert with the printer's profile and keep the proof.
- Pantone picked on screen → pick from the physical guide; name the edition.
- Canva twin treated as the master and sent to print from the API export → print from the kit's PDF/X master.
- Misuse pages with only red crosses → a text label on each.
- Book with no file paths or download link → every rule page names the file that satisfies it.
