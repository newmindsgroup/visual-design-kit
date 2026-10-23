---
name: design-google-docs
description: Design and audit native Google Docs for clear, attractive, easy-to-skim reading. Use for pageless reports, questionnaires, department workbooks, document tabs, typography, spacing, tables, and visual cleanup. Preserves answers and source evidence; complements the Google Docs connector skill rather than replacing its editing safeguards.
---

# Google Docs editorial design

Version-Timestamp: 2026-10-05 13:07:59 AST

## Outcome

Produce a native, editable document that makes its purpose, next action, section boundaries, and evidence status easy to find. Use restrained editorial design and progressive disclosure. These are general readability practices, not a claim of clinical ADHD validation.

Use this method with the installed Google Docs skill for trusted reads, native controls, revision guards, and exact API operations. Do not use website-generation or image-generation tools for ordinary document styling.

## Inputs and boundaries

1. Confirm target document IDs, account, audience, declared viewing context (desktop, split panel or mobile), tab roles, approved brand guidance, and whether wording may change. Reuse answers already in the conversation. For a styling-only request, preserve wording by default. Record the user's authorized scope and any approved content delta in the work packet.
2. Read project brand/design guidance when present. The neutral starter tokens below are a fallback, never a substitute for approved client tokens. After any token override, repeat contrast, style read-back and rendered checks.
3. Save a rich before snapshot and a semantic baseline in the private project work packet. Inventory every tab, table shape, merged cell, answer area, native chip, link, and protected control. A plain-text export is not a safe reconstruction source.
4. Inspect the rendered document before deciding the treatment. Select a pilot containing the main tab roles and the densest relevant table. Record viewport, zoom and selected text-width setting.
5. Keep client content and screenshots in its approved workspace. The reusable skill and external method reviews contain generic examples only. Do not change sharing, send documents, or publish a plugin as a side effect.

## Design decisions

### Structure and hierarchy

- One tab should have one clear purpose. Use descriptive tab names, one title, native section headings, and short action labels.
- Give the reader a starting point: purpose, what to do, and what is still unvalidated. Reuse existing text when rewriting is outside scope.
- Use a compact introduction. Avoid putting a full instruction manual ahead of the first useful question.
- Use native Title and Heading styles so navigation and future editing work. Update named-style defaults before range-specific exceptions. Verify actual API support and read back the result.
- Separate primary content, actions, pending decisions, and source evidence. Use text labels as well as color. Preserve uncertainty and source limits visibly.
- Do not bold entire paragraphs by default. Emphasize the question or decision and short labels. Preserve legally or operationally meaningful emphasis unless a reviewed change is authorized.
- Long evidence passages need semantic chunking. If wording changes are allowed, use short finding blocks with statement, source, implication, and open decision. If wording is fixed, use spacing and headings; propose content restructuring separately rather than silently abridging evidence.

### Typography and rhythm

Use [tokens and layout rules](references/tokens.md) as a neutral starting point. Body text should usually be 11.5 to 12pt. Keep metadata readable, usually 10pt or larger. Do not reduce text size to force a table to fit.

Use more space before a section than between its heading and text. Body prose may use 6pt after, while table paragraphs and lists usually need only 3 to 4pt. Remove oversized blank-paragraph styling without deleting content or answer space. Do not compress intentionally blank response areas.

Keep left alignment and avoid long all-caps passages. Use color sparingly. Decorative rules may be light only if heading text and spacing independently communicate the boundary. All text must meet a measured 4.5:1 contrast ratio against its background.

### Pageless width and tables

Pageless mode and viewer text width are different. Google's Text width preference affects the viewer's pageless documents, not a guaranteed layout setting for recipients. Page margins and page-size changes are not a pageless width solution. Explain this distinction when widening a document.

Measure available reading space with the tab sidebar open. Use a comfortable prose measure; a wider data table does not justify unlimited prose width. Verify both normal desktop and the actual constrained workspace.

Classify each table before styling:

| Table role | Treatment |
| --- | --- |
| Questionnaire or form | Short question heading, ordinary context text, clearly labeled response area, consistent restrained answer fill. Do not zebra rows mechanically or pin a question as a data header. |
| Evidence or comparison | Clear header row, deliberate column proportions, light alternating fills only when useful, top alignment, pinned header where supported. |
| Introduction or callout | Compact padding and concise hierarchy. No oversized decorative box. |

Resolve widths from fresh table anchors, not text searches or guessed offsets. A typical starting padding is 9pt vertical and 12pt horizontal. Tune it from actual screenshots. Verify that every response region has a visible text label. Compare empty-cell and blank-paragraph counts before and after; retain usable answer space at body size, not a tiny spacer size.

When a table overflows: first reduce excess padding, then rebalance columns. Prefer stacked content for forms or split/transposed comparisons when content restructuring is authorized. If fixed structure must remain, document horizontal scrolling honestly and provide a practical viewer-width/sidebar adjustment. For required mobile delivery that fails the fit check, obtain authorization for the necessary restructuring before declaring it ready. Never claim mobile readiness from a desktop viewport. Do not make every table wider by a universal constant.

## Execution and verification

1. Create a reviewed styling plan and preserve the before snapshot. Make a recoverable pilot first.
2. Use native connector requests with tab IDs, narrow field masks and required revision IDs. Validate nonempty UTF-16 ranges. Apply defaults before explicit exceptions. Do not rebuild a form from Markdown or plain text.
3. On an uncertain write result, read the current state and reconcile before another mutation. An explicit rejected atomic batch may be repaired; an unknown result must not be replayed blindly.
4. Read back every modified tab. Compare ordered text, link targets, chip type and target/date/person properties, list IDs/nesting/glyphs, table row and column counts, merged-cell map, and per-cell content. Ignore only intended visual style fields. When explicit text edits are authorized, compare against the approved delta rather than ignoring all text changes.
5. Verify tab mode, heading semantics, named styles and intended exceptions, cell widths, padding, header treatment and answer areas.
6. Visually inspect title/intro, a dense question with its answer, an evidence section, the widest data table, and a feature/status block. Check desktop and the constrained viewer, plus zoom or mobile when those are delivery requirements. Record actual regions and dimensions. Sampling is not exhaustive inspection.
7. Only after the pilot passes, apply the same role-based rules to other documents. Inventory exceptions first, verify every document structurally, and sample materially different layouts visually.
8. Save screenshots privately and provide a useful preview and direct document links. Report defects that remain, including content density and untested devices.

## Model and review choice

Use the active tool-capable Codex model to coordinate native edits, structural checks and visual inspection. Select effort through model-governor for the current stage; do not claim prose changes the running model. A capable independent reviewer such as approved Fable 5.1 can critique the generic method and skill. Use confidential screenshots with another model only when project-specific data approval exists. Model choice does not replace rendering, contrast checks or preservation tests, and there is no verified universal best model for Google Docs aesthetics.

## Deliverables and acceptance

Return updated native documents, a private before/after audit, style tokens, preservation results, screenshot coverage, limitations and next action. Add the actual Version-Timestamp to the work record and newly authored artifact metadata. Preserve source-version metadata rather than falsely re-dating the underlying evidence.

Pass only when the authorized documents were edited, content/control preservation passed, intended styles were read back, sampled rendering is acceptable for the declared viewing context, and required independent review is resolved. If access fails, name the exact completed subset and resume point. Do not call a specification or API success alone a beautiful, verified document.

For future work, invoke `$design-google-docs` with the document links, audience and permitted content changes. Combine it with the native Google Docs connector skill.
