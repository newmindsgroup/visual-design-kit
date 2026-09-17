# Logo, typography and color craft laboratory

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

Parent: [identity workflow](IDENTITY-WORKFLOW.md). [Specimen source](examples/craft-lab/specimen.json), [generated board](examples/craft-lab/index-v2.html), [pair report](examples/craft-lab/report-v2.json).

## Tools

Run `python3 scripts/craft_tools.py INPUT.json --report NEW-report.json --html NEW-board.html`. Existing output paths are refused. Optional `--previous OLD-report.json` identifies affected pair IDs. Input uses title/text plus palettes containing unique IDs, six-digit opaque sRGB tokens and pairs with id/fg/bg/minimum. Use declared thresholds appropriate to the actual role; numeric passing does not establish accessibility.

The board generator accepts optional fonts entries with label/family for installed font-family comparisons; it defaults to system serif/sans/mono families and palette applications using the same text. It is a starter specimen, not a free-font discovery or installation tool. For shortlisted exact font files, follow the existing typography decision and extend the generated project specimen with verified font declarations; capture actual loaded files separately. No source fonts are downloaded by this tool.

Use [browser wrap diagnostics](scripts/wrap-diagnostics.js) in a rendered page after fonts load. It returns Latin whitespace-based single-word-last-line and overflow candidates for selected text nodes. Inspect every candidate; short labels, scripts without spaces, transforms and complex inline layout need separate review. It does not automatically modify content or certify absence of all orphans.

## Deeper methods

- [Lettering and optical corrections](draft-skills/design-logo-refinement/references/lettering-and-optics.md).
- [Similarity and physical reproduction](draft-skills/design-logo-evaluation/references/screening-and-reproduction.md).
- [Multilingual microtypography and renderer fidelity](draft-skills/design-typography/references/advanced-typesetting.md).
- [Palette scales, composition and role translation](draft-skills/design-color-system/references/palette-craft.md).
- [Proofing and palette maintenance](draft-skills/design-color-system/references/proofing-and-maintenance.md).

## Example interpretation

The shape comparison illustrates equal bounds versus a proposed optical adjustment; neither is an approved logo. Type specimens deliberately share content. Palette examples test complete foreground/background applications. Inspect the report for failures; do not hide failing examples. These are synthetic studies, not proof of reader preference or physical reproduction.

## Acceptance

Meaningful unit checks cover known contrast, invalid colors, missing tokens, duplicate pairs, output escaping and token-change invalidation. Browser and final review results are recorded below after execution. Physical supplier proof, language review, exact-font cross-app tests, wide-gamut hardware and independent review are separate acceptance evidence. Previously failed Claude authentication remains an unresolved review dependency; no repeated call is made without changed access.

## Historical execution evidence for the original craft board

Ten focused Python tests pass, including font-family injection rejection and custom-family rendering. Existing output refusal and separate report/page destinations protect prior artifacts. Input uses no network and HTML text is escaped. The browser refused the local file URL under its URL policy; no workaround was attempted. Actual responsive screenshots and browser wrap-diagnostic execution remain pending. The generated board is a local candidate, not visually accepted. Independent Claude review remains pending due to the previously observed subscription authentication failure.

Optional `--logo /path/to/authorized-logo.svg` embeds the supplied SVG/PNG/JPEG as an image and creates unchanged-source size/background stress views. This does not parse vector structure, verify image validity or convert to monochrome. Use separately approved variants for monochrome tests.

Earlier [board](examples/craft-lab/index.html) and [report](examples/craft-lab/report.json) are preserved as initial output.

## Executed typography comparison in edition 0.2.0

The [two-brand collection](examples/quality-benchmark/README.md) adds exact licensed fonts, real copy, candidate and revised compositions, five widths, text-spacing and font-fallback cases, deliberate wrap/clipping controls, PDF proofs and an editable motion export. Its [evidence](examples/quality-benchmark/EVIDENCE.md) records actual results and limits. This supplements the original board; it does not retroactively mark that earlier board or its pending review as accepted.
