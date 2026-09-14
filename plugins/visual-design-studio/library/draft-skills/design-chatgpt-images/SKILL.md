---
name: design-chatgpt-images
description: ChatGPT Images production for original display media, controlled revisions and reusable campaign production.
---

# ChatGPT Images production

Version-Timestamp: 2026-09-11T21:08:20-04:00

## Inputs and workflow

Read the [media workflow](../../MEDIA-QUALITY-WORKFLOW.md) and reuse accepted upstream inputs. Use the [production packet](../../templates/media-quality-packet.md) for concrete inputs and outputs. Missing evidence stays explicit; tool availability is not production acceptance.

Use the available image-generation interface for original imagery and image edits. First inspect every supplied reference and assign its role. The current tool's documented input contract governs attachment selection; never assume the ChatGPT UI, Codex image tool and API have identical controls or subscription billing. Do not invent seeds, masks, negative-prompt fields or model parameters. If an operation is unsupported, route it to a verified editor.

For creation, provide the composition brief and reserved copy zones. For edits, identify the exact baseline and permitted change, and request preservation of all other details. Inspect the entire returned frame, not just the requested area: edits can alter other regions. Compare logos, packaging, geometry, colors and text to originals. Never describe a generated raster as a layered or vector master. Preserve each candidate separately with its actual references and prompt. Return accepted candidate or specific repair findings to compositing. Follow the shared media contract for uploads, rights and scope.

## Handoff and acceptance

Return artifact locations, exact baseline, candidate status, observed checks, remaining defects and next owner through the existing [handoff](../design-stage-handoff/SKILL.md). Apply the [rubric](../../templates/media-quality-rubric.md). Preserve original assets and follow the [media execution contract](../../MEDIA-GENERATION.md). Stop at the agreed revision/budget limit and report an unresolved result rather than silently changing the brief.

## Required next stage

Version-Timestamp: 2026-09-11T21:30:44-04:00

After generation, send the candidate files, baseline/reference hashes, prompt/parameters, job status and unresolved issues to [media quality evaluation](../design-media-quality-evaluation/SKILL.md). A successful job cannot skip this review. Product/factual drift or missing required evidence holds the candidate for repair or rejection. If accepted for composition, continue to the relevant compositing/animation owner, then finishing and display evaluation. Final exports require another review because assembly and compression can introduce new defects. Follow the [stage routes](../../examples/media-quality-recipes/README.md#ordered-stage-routes); never encode downstream review as an upstream generation dependency.
