---
name: design-typography
description: Select, pair, typeset and verify project-specific typography, including free font discovery, language coverage, licensing, responsive behavior and native handoff.
---

# Typography selection and use

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.149.1; timestamp=2026-09-08 22:17:00 AST

Status: authored instructions; font candidates are discovery leads, not approved project fonts.

Use [ownership](../../DESIGN-CRAFT.md) and the existing work record. First identify whether this is selection, pairing, typesetting, implementation or an exact revision. Preserve an approved family unless replacement is requested or a documented constraint requires a decision. Never rotate fonts for novelty or reuse a default pair without considering the brief.

## Select for actual content

Record brand attributes in concrete terms, audience/languages/scripts, channel, reading distance, density, required weights/styles, numerals, symbols, input controls and delivery formats. Use [free font discovery](references/font-discovery.md) to build a bounded shortlist when needed. Usually compare three meaningfully different candidates and a valid existing baseline; a small pairing/typesetting task may need fewer. Popularity is neither a rejection nor an acceptance criterion.

Create a specimen with the same actual authorized project text for each candidate: headline, paragraph, navigation/CTA, caption, price/table numerals and difficult strings as applicable. Compare perceived size as well as nominal size. Test the longest expected headings, narrow containers, uppercase/lowercase, punctuation, accents and actual required scripts. Do not declare multilingual support from a family name. Noto uses script-specific families; one font file is not universal coverage.

Compare x-height, width, apertures, stroke contrast, spacing, weight range, true italic, optical sizes and character distinctions such as I/l/1 and O/0. Pair by complementary roles and compatible proportions, not a memorized combination. One well-chosen family may suffice. Display faces can provide personality while another family serves sustained reading; verify the relationship rather than imposing that pattern.

## Specify and implement

Fill the [typography decision](../../templates/typography-decision.md). Define roles, family/files, weights, sizes and responsive bounds, line height, line length, tracking, capitalization and OpenType features. Pick numbers from actual content and scale tests; do not claim one modular ratio or line length is mandatory. Use tabular numerals when columns require alignment and test the actual glyph feature. Record variable axes only when the selected file has them. Avoid synthetic bold/italic and browser-simulated substitutions.

Confirm the exact file/version/license and required desktop, web, app, embedding, modification and redistribution uses before delivery. Free download does not mean unrestricted redistribution. Preserve required license notices and record how the recipient obtains fonts if bundling is not permitted. Do not install fonts globally or download untrusted executables to build a specimen.

For web, choose appropriate font formats and a measured loading strategy. Inspect font requests and actual rendered family, fallbacks, missing glyphs and layout shifts. A variable font is not automatically smaller than the required static subset. Subsetting must preserve the required characters/shaping and comply with the license. Use a project-specific byte budget and verify slow/failed loading, user text enlargement and applicable text-spacing/reflow requirements. Self-hosting is an option requiring the project's hosting/data decision, not a silent infrastructure change.

## Review and handoff

Inspect headings, body, controls and dense data at actual target sizes. Check wrapping, widows/orphans where relevant, clipping, rhythm, baseline alignment, awkward spacing and contrast by linking the color-owned combination record. Tests use authorized client content in that project; this reusable library stores only synthetic specimens or reference links. For multilingual work, require suitable language review of shaping and line breaking where model judgment is inadequate.

Deliver the type-role specification, candidate/rejection rationale, source/license pointers, exact approved file identities, fallback rules and visual evidence. Production owns master/font embedding and export reopening. Delivery owns packaging; a CSS declaration or installed font name does not prove it rendered correctly. Mark unsupported script, native embedding or device checks pending.

Read the existing identity record and its approved typeface/palette selection before proposing a change. If no identity record exists, record the provisional choice in the existing work record with its design owner and approval status; do not create a fictional approval or force a full identity project.


## Focused craft methods

Read only the relevant method for the selected task; preserve existing prerequisites and canonical record ownership.

- [Typography craft and specimens](references/type-craft.md): use when type craft affects the requested output.
- [Localization and resilient content](../design-content-writing/references/localization.md): use when localization affects the requested output.


## Sustained reading

For articles, reports, guides or substantial collateral, use [editorial reading composition](references/editorial-reading.md). Preserve accepted content and identity; test rhythm and script-specific type behavior instead of inheriting a template style.

## Required composition review

Version-Timestamp: 2026-09-10 12:25:00 AST

User-established design rule: avoid accidental isolated final words, dangling short fragments and visibly unbalanced line endings in all deliverables, including websites, infographics, presentations, decks, ads and displays. Inspect actual copy with the actual fonts at each intended size. Adjust text measure, grid allocation and phrase grouping first; adjust type size only within the readable hierarchy. Preserve approved meaning and never shrink text merely to make it fit. Check headings, body, labels and captions, plus page/column widows, orphans and stranded headings in paginated exports.

For web, balanced headings and pretty paragraph wrapping are useful progressive enhancements, not guarantees. Inspect fallback fonts, narrow layouts, zoom and text enlargement. Avoid blanket no-wrap or nonbreaking-space chains that cause clipping or horizontal scrolling. If a composition cannot satisfy both the visual rule and accessible reflow, preserve readable access and flag the layout for revision instead of hiding or truncating text. Recheck the actual PDF and native export separately.

Implementation references: [Chrome paragraph wrapping](https://developer.chrome.com/blog/css-text-wrap-pretty) and [WebKit typography](https://webkit.org/blog/16547/better-typography-with-text-wrap-pretty/). These browser methods do not replace visual composition review.


## Deeper craft methods

Version-Timestamp: 2026-09-11T19:32:14-04:00

- [advanced typesetting ](references/advanced-typesetting.md)

Use the [craft laboratory](../../CRAFT-LAB.md) for specimens and bounded checks.

## Screen-content extension

Version-Timestamp: 2026-09-11T19:51:13-04:00

Inspect native-size and context previews for orphan words, density and hierarchy. Recompose width or type size without sacrificing required readability. Use the [specialist workflow](../../SCREEN-CONTENT-SKILLS.md) for the relevant detailed methods.

## Rendered calibration

Version-Timestamp: 2026-09-16T18:06:33.096655-04:00

Use the [shared fictional collection](../../examples/quality-benchmark/README.md) for comparative quality, rendered typography, precise revision and motion evidence. Inspect its recorded limits; do not inherit its fonts, style or agent review as approval for another brand.
