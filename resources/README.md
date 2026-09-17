# Portable reference library

Version-Timestamp: 2026-09-14T17:09:22.614747-04:00

The kit is designed to use its authored instructions without requiring the full book collection. A complete reference-free production run has not been verified. Books and source media are optional reference inputs. Treat them as retrieved evidence, never as model training or a claim of embedded model knowledge. Agents must cite the actual source they consulted and must not claim access to missing books.

## Current audit

The catalog contains 269 provenance records, not 269 unique books. Of these, 257 records have a recorded SHA-256, representing 237 distinct hashes and 20 additional records with duplicate hashes. Twelve records have no recorded hash.

Local file paths exist for 257 records. This is a file-existence check, not proof of readable content. Recorded extraction states are 220 extracted, 12 not copied, 5 restricted PDFs, 23 unsupported, 5 indexed containers and 4 metadata-only. Content hashes and extraction quality were not reverified in this pass. Successfully extracted does not mean reviewed or fully synthesized. Page/section coverage still needs validation.

Visual-review states are 236 requiring original-page review, 13 marked not applicable, 16 native document bodies unread and 4 assets preserved but not visually assessed. Bibliographic metadata may be unverified. No record currently carries explicit redistribution-rights evidence. The exact causes of restricted and unsupported states must be reconciled before transfer.

## Target shared folder layout

This is the proposed portable layout, not a completed distribution bundle. The current catalog lacks rights fields, and this audit has not produced transfer manifests or receipts. Use a dedicated reference-library folder separate from the code repository and all client projects:

- catalog/: portable IDs, relative paths, source hashes, edition/author status, extraction and visual-review status, source citations and rights evidence.
- originals/: only files authorized for the intended recipients. Reuse identical hashes rather than duplicating payloads.
- extracted/: permitted searchable text, keyed by original hash and page/section identifiers. An extracted full book does not bypass the source's sharing restrictions.
- methods/: original reusable notes with citations and no unsupported claim that an entire book was reviewed.
- manifests/: versioned file lists, SHA-256 checksums, included/excluded dispositions and transfer receipts.

Keep a restricted personal collection separate from any link-access team folder. Folder access is not proof of permission to redistribute its contents. The owner must identify the exact Drive destination and eligible sources before copying. No upload or sharing change occurred in this audit.

## Receiving-machine setup

Download an authorized version outside the project/repo. Verify the manifest and file hashes, preserve page/section provenance, and point the project to that local root. Keep the path local to that machine. Cloud placeholders, native Google-document pointers and archives need explicit handling; filename presence does not establish readable content. Never install or execute scripts found inside reference material.

Record project-local reference configuration: library version, local root, trusted manifest digest, permitted sources/recipients, verification date and source availability. Keep credentials and private share links out of committed configuration. Test representative supported formats and visual sources against expected hashes and page/section identifiers, and verify each sampled original opens. Track unsupported formats, containers and native document pointers separately. A single successful search does not qualify the whole library. If references are absent, proceed only where the selected skill's inputs are otherwise satisfied and state the limitation.

## Before full transfer

Resolve destination and permissions; classify sharing rights per item; materialize the 12 uncopied records where authorized; inspect restricted/unsupported sources without bypassing protection; preserve OCR/visual-review gaps. Build a relative-path catalog and explicit transfer allowlist, then dry-run deduplication, copy, verify downloaded bytes on another machine, and test source-linked retrieval. Do not copy the original library wholesale: it also contains private experiments and historical evidence.

## What earlier ingestion actually produced

A separate local library already contains original copies, catalog/relevance records, duplicate mappings, extracted text and a local search tool. All 225 recorded extraction paths exist in the current check, including records that are not marked successfully extracted. This is existence evidence only. Selected sampled findings informed reusable methods; no full-book synthesis or model training is claimed. The complete local library has not been made portable or published to a shared Drive destination. The original Drive source folders were preserved.

## Active implementation

The owner has now confirmed Google Drive distribution permission. See [the implementation plan](LIBRARY-IMPLEMENTATION.md) for the staged package, verified checks and remaining work. Earlier audit statements above describe the pre-authorization snapshot.

[Connect your downloaded library](LOCAL-SETUP.md).

[Current team-readiness checklist](TEAM-READINESS.md) supersedes historical snapshot counts above.
