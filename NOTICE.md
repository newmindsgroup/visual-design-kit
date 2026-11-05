# Licensing and provenance

Version-Timestamp: 2026-09-27T13:47:24-04:00

Original code, skills, schemas, instructions and documentation are available under the accompanying MIT license. This grant covers New Minds Group's rights in this work. It does not relicense third-party material or grant rights in referenced brands.

## Included third-party assets

The fictional quality examples include Archivo, Barlow Condensed and Newsreader fonts under the SIL Open Font License 1.1. Each font's complete copyright and license notice is included beside it in `plugins/visual-design-studio/library/examples/quality-benchmark/assets/`. Preserve these notices when redistributing the fonts or example bundle. The MIT license does not replace the OFL. Provenance and hashes are in that directory's `provenance.json`.

The FORM and TIDAL images are original AI-generated fictional concept examples, recorded in that provenance file. They are not real products, customer installations or evidence of commercial performance. The permission grant covers any rights New Minds Group holds in them; it does not promise exclusive rights or third-party clearance for a particular commercial use.

## Fonts bundled with the 0.5.0 examples

Version-Timestamp: 2026-10-20 03:30:00 UTC

All are licensed under the SIL Open Font License 1.1; each family folder contains its `OFL.txt` next to the font files, and some are subset to the glyphs a page uses. Subsetting is a modification under the OFL; the subset families (Amiri, IBM Plex Sans Arabic, Shippori Mincho, Zen Kaku Gothic New) declare no Reserved Font Name in their copyright notices, so the subsets keep their original names. Preserve these notices when redistributing.

- `plugins/visual-design-studio/library/examples/stylescapes/fonts/`: Amiri, Anton, Archivo, Atkinson Hyperlegible Next, Big Shoulders Display, Bodoni Moda, Bricolage Grotesque, Courier Prime, Fredoka, IBM Plex Mono, IBM Plex Sans Arabic, IBM Plex Sans Condensed, Instrument Sans, La Belle Aurore, Libre Caslon Display, Libre Caslon Text, Libre Franklin, Martian Mono, Newsreader, Public Sans, Saira, Shippori Mincho, Unbounded, Young Serif, Zen Kaku Gothic New.
- `plugins/visual-design-studio/library/examples/react-system/src/fonts/`: Figtree, Fraunces, IBM Plex Mono, JetBrains Mono, Schibsted Grotesk, Source Sans 3.
- `plugins/visual-design-studio/library/examples/ai-tells/fonts/`: Anton, Archivo, Bodoni Moda, Bricolage Grotesque, Fraunces, JetBrains Mono, Newsreader, Public Sans, Space Grotesk.

The stylescape brands (Vibra, Little Harbor, Kiyomi House, Gridline, STATIC, Finca Alba, Harlow & Vance, Tidewater Collective, Apex Wolves, CareFill, Noor Atelier, Forge) and the AI-tells examples are fictional. Their artwork is original CSS and inline SVG made for this repository. Atlas entries name real brands, designers and design systems only as public reference anchors; no third-party logos, artwork or proprietary copy are included.

## Referenced resources and private materials

Links and bibliographic references identify external sources. No license to a linked website, standard, repository, trademark, book or provider service follows from this repository's MIT license. Upstream assets and substantial source excerpts are not included. Consult the source's own terms if you want to copy its material.

Original books, private extraction bundles, filled client records, private source presentations, account credentials and licensed provider subscriptions are excluded. A separately obtained local reference library stays under its own access and reuse terms. Optional retrieval tools do not grant access or redistribute that library. Generic persona and component taxonomies abstract user-supplied examples; their source-specific layouts, brand data and imagery are excluded.

## BAMA and REA adaptations

Version-Timestamp: 2026-10-27 07:43:23 AST

Native design, icon and reconstruction methods adapt MIT-licensed BAMA and REA. Complete notices and source pins are packaged in [design method provenance](plugins/visual-design-studio/library/knowledge/third-party/README.md). Optional full workflow companions live under `extras/bama-mac-studio` and `extras/rea-toolkit`; retain each companion's LICENSE and provenance records. No upstream trademark or asset rights follow from these code licenses.

## MotionSites cinematic web adaptations

Version-Timestamp: 2026-11-05 18:10:00 UTC

Copyright (c) 2026 MotionSites. Released under the MIT License (part 1 of the upstream LICENSE); the complete notice is preserved in [MOTIONSITES-LICENSE.txt](plugins/visual-design-studio/library/knowledge/third-party/MOTIONSITES-LICENSE.txt).

Source: [Motionsites-AI/claude-skill](https://github.com/Motionsites-AI/claude-skill/tree/faa30d512e3973e58675c72101a7ef42ed37ae83) at commit `faa30d512e3973e58675c72101a7ef42ed37ae83` (2026-10-26), skill folder `plugins/motionsites-web-builder/skills/motionsites-web-builder/`.

Adapted in Visual Design Studio 0.10.0, each file marked "Adapted from MotionSites claude-skill (MIT), see NOTICE.md.":

- `SKILL.md` workflow, `references/spec-template.md`, `references/craft.md`, `references/builders.md`, `references/review.md` and `references/assets.md`, rewritten into `skills/web-design/references/cinematic-landing.md`, `landing-spec-template.md`, `cinematic-craft.md` and `builder-prompts.md`, `skills/design-critique/references/cinematic-addendum.md` and `skills/imagery/references/media-for-web.md`.
- `references/techniques/*.md`, adapted into `library/knowledge/web-techniques/` with kit token wiring, pinned library versions and added accessibility code.
- The QA ideas in `scripts/shoot.py` (early first-paint frame, video readiness, broken images), reimplemented in Node inside `skills/design-critique/scripts/render_review.mjs`. No Python from the script is included.

Excluded: the upstream `examples/` folder (example prompts), the `media/` folder (contact sheets and media URLs) and `preview-media.jpg`. Those are not MIT-licensed and may not be redistributed as a collection; nothing from them, and no link to that media, is in this repository. The upstream sponsorship and upgrade behavior was removed entirely. The MIT license covers the adapted text and code only; it grants no rights in the MotionSites name or marks.

