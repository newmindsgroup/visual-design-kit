# Small multiples: comparison guidance

Version-Timestamp: 2026-09-15T06:49:26.770300-04:00

Status: source-supported supplemental guidance, pending independent review and rendered application testing. The pinned plugin payload is unchanged.

Use the existing infographic capability and its layout selection first. Small multiples already exist in its inventory; this note explains when and how to use them.

Choose repeated panels when the question asks how the same measure varies across time, places or groups. Hold the encoding, panel dimensions, units and comparison scales constant. Give panels a meaningful order and explicit labels. Show missing observations as missing rather than silently dropping them. If scales must differ, make the difference unmistakable and reconsider whether this layout supports the intended comparison.

Before artwork, specify the comparison question, source data, panel dimension, common domain, legend, missing-data behavior and intended reading order. Check at least one panel against source data, then verify every transformed value. Check that a viewer can identify what stays constant and what changes.

For a glanceable display, a dense grid may be the wrong choice. Reduce the scope or use a simpler comparison while preserving critical qualifications. For touchscreens, a detail view can supplement the overview. If animation is used, preserve orientation and a static comparison alternative. These are applications to this kit's delivery contexts, not claims made by the source example.

Evidence: The Visual Display of Quantitative Information, library source IDs 53ac2c723822eb26 and 5ab408e72cf93c09 (duplicate source bytes). PDF page 166, printed page 170, was read and visually inspected. The example repeats mapped data using a stable panel design. This bounded inspection supports the comparison technique; it does not validate the historical data or establish full-book review.

Acceptance still needed: render an actual application at intended sizes, recalculate values, inspect labels and common scales, and evaluate whether the intended audience can make the comparison. Do not promote a familiar-looking grid as proven effective without these checks.

[Reference workflow](REFERENCE-WORKFLOW.md) | [Existing infographic skill](../plugins/visual-design-studio/library/draft-skills/design-infographics/SKILL.md)
