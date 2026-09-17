# Select the craft work the task actually needs

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

Owner: [UI system](draft-skills/design-ui-system/SKILL.md). Use within the existing [stage packet](templates/stage-execution.md), not as another mandatory phase. Record one compact table before producing a new composition or revising one. Every row is selected, reused, or not applicable, with a reason and an exact input or output reference.

| Decision | Select when unresolved | Reuse when already valid |
| --- | --- | --- |
| Art direction | Audience, visual character, composition or medium needs a decision. Choose `reference-direction`, then the relevant `web-art-direction`, `display-art-direction` or `media-art-direction` | Approved direction and permitted variation, including explicit counterexamples |
| Type | Family, hierarchy, reading distance, line balance or language support changes. Select `typography` | Exact font files, license, roles, sizes and rendered fit evidence for unchanged conditions |
| Color | Palette, contrast, semantic roles or environment changes. Select `color` | Current role tokens and measured relevant foreground/background pairs |
| Copy fit | Message or available space changes. Select `content`, and `web-copy-fit` for web | Approved exact text, hierarchy and destination; recheck wraps after changes |
| Image | Need a new photograph, illustration, crop or faithful product adaptation. Select appropriate media route and evaluation | Authorized exact asset with hash, crop and factual limits |
| Motion | Movement communicates sequence, hierarchy, state or atmosphere worth the cost. Select `motion` and the relevant display/web method | Accepted timing, holds, identity constraints and reduced-motion alternative |
| Visual review | Any visible output changes. Select `design-taste` and appropriate format review | Prior checks only for regions and conditions demonstrably unaffected |

These are catalog IDs, not automatic execution. Resolve actual entries and dependencies through `capabilities.json`. A missing upstream decision may be reused or marked provisional for a bounded experiment; it must not be invented as approved. Record dependencies in [selection](SELECTION-CONTRACT.md). Never load every capability to do a small edit.

## Two selection examples

**New landing page:** select art direction, typography, color, copy fit, imagery and visual review. Select motion only if its purpose is clear. Research and audience inputs can be supplied or reused; missing facts hold only dependent claims. Deliver a complete composition with a primary action and responsive evidence, not a token sheet alone.

**Change an approved heading:** reuse identity, palette, photography and layout. Select copy fit, typography fitting and visual review. Preserve the logo, other copy and asset hashes. Recheck relevant breakpoints and exports. Do not restart identity exploration or replace the photograph.

## Positive quality, beyond lack of errors

Use the same brief and content to compare alternatives. Name the specific visual idea, how hierarchy carries the message, what is recognizably this brand, and which details make the result feel considered. A correct but interchangeable template is a repair candidate when distinctiveness is required. An attractive design with wrong facts is rejected. A sober information graphic can be excellent without photographic decoration.

Use [the shared benchmark](examples/quality-benchmark/README.md) to practice this distinction. It is a calibration collection, not a universal style preset or evidence of customer preference. Stop when the scoped criteria are satisfied and remaining preference belongs to the human design owner.
