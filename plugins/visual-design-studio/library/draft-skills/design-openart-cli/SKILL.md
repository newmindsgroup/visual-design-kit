---
name: design-openart-cli
description: Use the official OpenArt CLI for scoped image or video generation and image edits, checking model forms, account access, dry runs, credit costs and output handoff.
---

# OpenArt CLI production

Version-Timestamp: 2026-09-10 20:21:06 AST

Read the [shared media contract](../../MEDIA-GENERATION.md). This is an authored operating procedure with conditional execution. Discover destination installation, access and operation status through [software readiness](../../SOFTWARE-READINESS.md). No account or generation result is inherited.

## Establish access

Check `command -v openart`, then inspect `openart version` and `openart --help` if installed. Verify publisher/release integrity before credentials or client data are involved. If absent, record setup pending and use the official source linked in the shared contract for a separately authorized installation. Browser login is `openart login`; `openart account` reports access and credits. Keep account identifiers private and never read or print credential storage.

## Inspect the selected mode

Official documentation describes these commands; installed help must confirm them before use:

- `openart model list` for available models.
- `openart model form MODEL_ID text2image` for a mode's inputs. Discover the appropriate mode for edits or video rather than reusing this image example.
- `openart model cost --model MODEL_ID --mode text2image` for a quote.
- `openart generate image PROMPT --model MODEL_ID` or `openart generate video PROMPT --model MODEL_ID` for explicit media selection.
- `openart creation get JOB_ID` and `openart creation wait JOB_ID` to reconcile a known submission.

Placeholders require real verified values and shell-safe argument handling. The documented `--dry-run` rehearses writes, and `--async` submits without waiting. Async cannot be combined with output download. Verify these semantics for the installed version before using them.

## Prepare and execute

Select the tool for its verified reference/edit controls, output requirements and total cost, not a universal model recommendation. For illustrations, define subject, hierarchy and reserved text areas. For reference edits, specify what may change and what must remain. For video, use the approved shot plan, duration, aspect ratio and continuity requirements; choose audio only when supported and requested.

Prepare one scoped candidate specification in the existing work record. Before a rehearsal with private assets, inspect whether the installed command processes/uploads references while constructing its request. A dry run must not be assumed to keep files local without verified behavior. Obtain upload scope before any such path is supplied. Inspect the quote against the total authorized budget and stop on ambiguity about entitlement or additional charges.

Submit only within that scope, capture the job ID and use status retrieval after uncertain results. Do not rerun a submission because a wait timed out. Workspace selection, project creation, uploading, deletion and sharing are separate changes; an existing login is not blanket permission for them. Keep output URLs private when signed or sensitive and download only the selected job's results.

## Review and handoff

Inspect dimensions, actual image/video content, exact brand/product invariants and motion continuity. Review spelling and facts independently from the generation. Keep essential infographic labels and data-driven marks editable in the composition tool. Deliver the accepted media with prompt/model/parameter provenance and the shared production manifest. A successful download is not native editability, rights clearance or target-device acceptance. If access is unavailable, deliver the prepared specification with the missing prerequisite clearly stated.

Verify installed command syntax and parameter support before each selected mode; dry-run construction does not prove server acceptance or absence of upload. For an authorized setup, resolve the repository through the current vendor page and verify the selected release identity before installation.


Version-Timestamp: 2026-09-11T23:21:42-04:00

## Media quality extension

Version-Timestamp: 2026-09-11T21:08:20-04:00

Before composing a job, use [route selection](../design-media-route-selection/SKILL.md) and the [production packet](../../templates/media-quality-packet.md). After download, apply [quality evaluation](../design-media-quality-evaluation/SKILL.md), then record observed execution as a [recipe](../design-media-production-recipes/SKILL.md). Current model forms determine controls; this extension does not verify new provider features.

## Required next stage

Version-Timestamp: 2026-09-11T21:30:44-04:00

After generation, send the candidate files, baseline/reference hashes, prompt/parameters, job status and unresolved issues to [media quality evaluation](../design-media-quality-evaluation/SKILL.md). A successful job cannot skip this review. Product/factual drift or missing required evidence holds the candidate for repair or rejection. If accepted for composition, continue to the relevant compositing/animation owner, then finishing and display evaluation. Final exports require another review because assembly and compression can introduce new defects. Follow the [stage routes](../../examples/media-quality-recipes/README.md#ordered-stage-routes); never encode downstream review as an upstream generation dependency.
