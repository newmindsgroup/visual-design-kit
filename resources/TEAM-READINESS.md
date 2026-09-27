# Reference modes: acceptance checklist

Version-Timestamp: 2026-09-27 14:19:56 AST

Check the chosen mode on the receiving machine. The public release supplies original guidance and an offline helper. An authorized collection may be provided separately by its owner, but books and public book downloads are not part of the kit. Historical checks of the author's collection do not qualify another library or host.

## Standalone acceptance

1. Verify the package pin before executing bundled code. A failed package check remains a stop in every reference mode.
2. Run `status --mode standalone` through the verified helper. Confirm that it selects standalone without accessing local configuration or the corpus, including when stale local configuration exists.
3. Use authorized client inputs and task-relevant packaged guidance. Record the mode and no consulted book sources in the existing project work record.
4. Produce, inspect, revise and resume a bounded artifact in the intended host. Record actual checks and unresolved limitations. Missing optional books must not stop ordinary design work; missing required client facts or source evidence holds the dependent work.

## Optional local-library acceptance

1. Identify permitted sources, intended uses and recipients. Keep originals and extracted text outside the kit and client repositories. Confirm whether the selected agent may receive excerpts.
2. Follow [local setup](LOCAL-SETUP.md). For an owner-provided download, extract the whole folder or ZIP outside the project and choose the compatible root containing `catalog/` and `manifests/`. Use its manifest, not another collection's fixed count, to check the transfer.
3. Store the root in ignored `private/reference-library.local.json`. Run `status --mode auto` through the verified helper from the project, or supply `--config` explicitly. Record effective mode and reason. Availability alone is not consultation.
4. Run `verify` and retain its actual exit result. Reconcile missing files, changed hashes and unsupported formats before relying on affected sources. Standalone fallback does not erase an integrity failure. Check source-required behavior separately: an unavailable library with `--require-source` holds source-dependent work, while independent work may continue.
5. Retrieve a known passage and open the original page. Record the inspected source ID, library version, manifest digest and locator. Check OCR, numbers and visual interpretation against the original.
6. Complete a bounded task in the intended IDE: use the evidence for a decision, inspect the artifact, revise it and resume from saved records. A successful search does not establish that entire workflow.

For any transfer, establish recipient permission and repeat relevant checks on the receiving host. Keep machine paths and access details local.

## What acceptance means

Record the mode, machine, sources and tools actually used, plus remaining gaps. Integrity and retrieval checks do not establish complete design knowledge, source quality, ownership, redistribution rights, full-book review, accessibility conformance, provider access or production acceptance.

The [historical implementation record](LIBRARY-IMPLEMENTATION.md) preserves dated author-only collection counts and unresolved limitations. Those are neither a public distribution promise nor current acceptance evidence.

[Local setup](LOCAL-SETUP.md) | [Reference workflow](REFERENCE-WORKFLOW.md) | [Main backlog](../BACKLOG.md)
