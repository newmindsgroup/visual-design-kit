# Media production packet

Version-Timestamp: 2026-09-11T21:08:20-04:00

Parent: [workflow](../MEDIA-QUALITY-WORKFLOW.md). Supplement the existing stage record; do not create a competing approval record.

## Brief and composition

Record project ID, audience hypothesis/evidence, message, use case, screen pixels/aspect ratio, distance and dwell assumptions, approved direction and baseline hash. Define focal hierarchy, copy/product zones, crop tolerances, lighting, materials, palette roles and prohibited changes. Mark absent requirements unknown or not applicable with rationale.

## Reference and route manifest

For every reference: ID, source/version/hash, role, authority, upload rights and intended influence. For each candidate route: installed version, model/mode/schema date, supported controls, cost quote, cumulative budget, limits and evidence. Record chosen route and why. Unsupported controls remain absent from commands.

## Prompt to adapt to supported inputs

```text
Role: Create supporting imagery for the specified screen composition.
Objective: Produce the asset described in the brief, with one clear focal hierarchy.
Context: Use reference IDs only for their declared roles; product-truth references govern factual details.
Requirements: Preserve listed invariants. Use the specified light, material treatment, crop and negative-space zones. Change only the allowed elements. Keep required final copy out of the generated image unless explicitly requested.
Output: Requested image or clip, in supported dimensions/duration. Do not invent tool controls or claims about the depicted product.
Evaluation: Compare the complete output against invariants and composition criteria. Return the candidate for inspection, not automatic approval.
```

Fill this with concrete values before use. The orchestrating agent retains evaluation and provenance instructions if the generator accepts only visual prompts.

## Execution and revision

Record candidate ID, prompt version, job ID/status, actual parameters, output path/hash, cost if known, defects, repair choice, accepted baseline and next step. Unknown job outcome requires reconciliation, not blind resubmission. Every revision specifies permitted changes and checks unchanged regions.

## Recipe evidence

Record maturity (prepared/executed/reviewed/target-validated), originals, contact sheet, rubric, editable master, export/player specification, checks, unresolved findings and contrasting-case results. Never fill evidence fields with predicted outcomes.
