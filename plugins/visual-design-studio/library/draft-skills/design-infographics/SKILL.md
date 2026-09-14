---
name: design-infographics
description: Plan and produce evidence-based infographics with deliberate layout, visual style, accurate data encoding and editable handoff for web, print, decks and displays.
---

# Infographic design

Version-Timestamp: 2026-09-12T11:36:30-04:00

Project-local authored skill. Use for visual explanations and data stories, including conceptual infographics without quantitative data. Reuse existing research, content, brand and production records. This is not permission to invent statistics or require a full brand/UX project for one graphic.

## Inputs and sequence

1. Read the project work record: audience and evidence status, takeaway or action, channel, viewing distance/time, exact dimensions, brand tokens, approved copy/data, citations and required editable master. Ask only for missing choices that change the result. A quick retail display needs a different information density from a report page.
2. Use the research capability for unsupported factual claims. Record actual versus estimated values, units, denominator, population, period, source/page, transformations and uncertainty. Unknown data stays unknown; fictional examples stay visibly fictional. Use content writing to establish headline, explanation, labels and source notes before polishing artwork.
3. Read [layout and style selection](references/layouts.md). Separate information structure from visual style. When direction is open, propose two genuinely different, brief layout treatments and explain their reading order and fit. When direction is approved, preserve it. Do not generate many paid variants by default.
4. Fill the [infographic specification](../../templates/infographic-spec.md) in the project workspace. Use stable element IDs to connect evidence, exact text, chart values, composition and alternatives. Sketch hierarchy before detailed illustration. Label a conceptual flow as conceptual; widths or areas must not imply quantities without supporting data.
5. Select production using [software routing](../../SOFTWARE-PRODUCTION.md). Code/SVG or plotting tools suit accurate charts and repeatable layouts; Illustrator suits detailed vector masters; Figma suits native reusable screen components when available; a deck editor suits editable slides. Generated imagery may supply illustrative assets, but does not replace verified chart geometry, exact typography or editable source. Use the selected media CLI skill only if that route improves the required result and its access is verified.
6. Inspect the rendered output at the intended size. For a web presentation, inspect desktop/mobile reflow and reading order rather than shrinking a poster; verify keyboard, focus and reduced-motion behavior when interactive. For print or displays, inspect target dimensions, profile, safe areas, type size and actual viewing conditions when available. Document conditions that remain untested.

## Acceptance and handoff

Recalculate totals, percentages, ranks and transformations from the source. Verify labels, dates, spelling, units, proportional marks, legend and reading direction against element IDs. Bars normally start at zero; any nonzero axis must be clearly disclosed and justified. Keep interval spacing truthful, avoid misleading 3D/area effects and avoid using a decorative funnel as a quantitative conversion chart. Use non-color cues and direct labels where possible.

Check hierarchy, alignment, whitespace, consistent icon treatment, image quality and brand fit. Review color contrast and legibility in the actual export. Provide concise alternative text plus a meaningful long description and accessible data table when needed; do not assume embedded text makes a flattened image accessible. For animation, preserve a complete static equivalent and enough time to read. W3C explains [complex-image alternatives](https://www.w3.org/WAI/tutorials/images/complex/).

Deliver the selected editable master, source data, specification, reviewed exports, accessible equivalents, citations, fonts/asset licenses and manifest. Keep approval status, unresolved checks and revision invariants explicit through the existing handoff and delivery capabilities. An authored skill is not proof of an executed infographic or user comprehension.

For web delivery targeting WCAG AA, use [text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) of at least 4.5:1, or 3:1 for large text (18 pt regular or 14 pt bold, measured at rendered size). Apply [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) of at least 3:1 against adjacent colors to graphical parts needed to understand the information, considering the criterion's exceptions. Contrast alone is not accessibility. Set and verify a project-specific minimum type size for the actual medium and distance; there is no single universal display/print size. Raster text is not machine-readable text.

For numeric work, preserve the underlying values as a project data artifact keyed to element IDs, with transcription checks if the supplied source is an image. Do not require committing private source data to the reusable repository. Capability entry paths resolve through [the catalog](../../capabilities.json).


## Focused craft methods

Read only the relevant method for the selected task; preserve existing prerequisites and canonical record ownership.

- [Information design and explanation](references/information-design.md): use when information design affects the requested output.

## Provider selection

For a justified generated asset, use [media route selection](../design-media-route-selection/SKILL.md) before selecting [ChatGPT images](../design-chatgpt-images/SKILL.md), [Higgsfield](../design-higgsfield-cli/SKILL.md) or [OpenArt](../design-openart-cli/SKILL.md). Tool access and operation authorization remain separate.
