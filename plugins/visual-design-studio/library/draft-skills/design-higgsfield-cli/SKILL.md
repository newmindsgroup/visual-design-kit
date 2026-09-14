---
name: design-higgsfield-cli
description: Use the official Higgsfield CLI for scoped creative-media production, checking installed commands, model inputs, account access, uploads and credit costs before submitting and reviewing jobs.
---

# Higgsfield CLI production

Version-Timestamp: 2026-09-08 19:56:22 AST

Read the [shared media contract](../../MEDIA-GENERATION.md) and selected production record first. This skill authors and executes a bounded media route when available. It does not install the vendor's companion skills, authorize spending or activate unrelated website/game features.

## Discover before composing the command

Use `command -v higgsfield`, `higgsfield version` and `higgsfield --help`. Verify binary origin and version before authenticated use. If absent, record setup pending and provide the official vendor installation reference; do not execute an installer automatically. In a requested setup, inspect the pinned release/installer and checksum, then use official browser authentication. Never run `higgsfield auth token`, which prints a secret.

Installed 0.1.40 local help was inspected on 2026-09-08. These are observed command families, not an authenticated test:

| Purpose | Command to inspect/use within authorization |
| --- | --- |
| Browser sign-in | `higgsfield auth login` |
| Access/plan/credits | `higgsfield account status` |
| Model discovery | `higgsfield model list` then `higgsfield model get MODEL_ID` |
| Estimate | `higgsfield generate cost MODEL_ID` with verified parameters |
| Explicit reference upload | `higgsfield upload create FILE` |
| Candidate submission | `higgsfield generate create MODEL_ID` with verified parameters |
| Reconcile known job | `higgsfield generate get JOB_ID` or inspect `generate wait --help` |

MODEL_ID, FILE and JOB_ID are placeholders, not literal valid values. Use subcommand help and the selected model's schema to determine actual flags. Do not transplant OpenArt's hyphenated parameter conventions into Higgsfield.

**The installed cost command can auto-upload local media paths.** Estimate without private media first, or use a specifically authorized reference upload. A no-job quote is not an offline operation. Generation also auto-uploads local media paths. Inspect the exact requested files and disclosure permission before either operation.

## Select the creative route

For an illustration, specify composition, negative space, palette roles and intended placement. For a photo edit, preserve product geometry, colors and legally required details; compare against the baseline. For motion, establish the storyboard, first/last frame requirements, duration and audio constraints before choosing a supported model. Marketing Studio/product photoshoot commands may enhance prompts: inspect their supported inputs and keep the original brief authoritative when judging the result.

Soul/character training, voice or likeness work and advanced workflows require explicit rights, persistent-data scope and current command support. Newer online commands absent from local help remain unavailable until separately approved setup and verification. Do not auto-update or switch to an unofficial wrapper.

## Produce and finish

Build a model-specific argument list from the approved asset specification, inspect cost/credit budget, submit once and retain the job ID. Follow the shared timeout/reconciliation rules. Download into the project workspace, inspect actual output and preserve provenance. Route accepted imagery to the owning composition/master and apply delivery checks. Report what ran, credits if known, output paths and remaining checks. No general visual-quality or production-readiness claim follows from successful help output.

## Media quality extension

Version-Timestamp: 2026-09-11T21:08:20-04:00

Before composing a job, use [route selection](../design-media-route-selection/SKILL.md) and the [production packet](../../templates/media-quality-packet.md). After download, apply [quality evaluation](../design-media-quality-evaluation/SKILL.md), then record observed execution as a [recipe](../design-media-production-recipes/SKILL.md). Current model schemas determine controls; this extension does not verify new provider features.

## Required next stage

Version-Timestamp: 2026-09-11T21:30:44-04:00

After generation, send the candidate files, baseline/reference hashes, prompt/parameters, job status and unresolved issues to [media quality evaluation](../design-media-quality-evaluation/SKILL.md). A successful job cannot skip this review. Product/factual drift or missing required evidence holds the candidate for repair or rejection. If accepted for composition, continue to the relevant compositing/animation owner, then finishing and display evaluation. Final exports require another review because assembly and compression can introduce new defects. Follow the [stage routes](../../examples/media-quality-recipes/README.md#ordered-stage-routes); never encode downstream review as an upstream generation dependency.
