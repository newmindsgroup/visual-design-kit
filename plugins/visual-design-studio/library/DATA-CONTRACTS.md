# Implemented data contracts

Version-Timestamp: 2026-09-07 11:15:48 AST

This document describes the source implementation pinned in the package manifest. Verify these behaviors against the exact assembled validator and destination before relying on them. Historical corrections are not independent review of this new package.

Contract version `1.0-proposed` is explicit. Unsupported versions fail instead of silently migrating. Older record kinds retain/ignore unknown extra metadata; the reference-decision contract rejects unknown fields. Canonical persona field and component sets are exact. This is semantic validation, not a claim to validate every future extension.

| Kind | Implemented core checks | Interpretation limit |
| --- | --- | --- |
| persona | 118 exact field keys; 35 components; status/value/list shape; repeated item identity; evidence IDs resolved through an embedded validated register; required AI traceability fields | Field content, psychology, research adequacy and rendered component behavior require separate review |
| evidence | Source ID uniqueness, local hashes/path containment, retrieval/expiry dates, current status, finding refs/status, asset-use permission records, unresolved readiness conflict | Does not retrieve URLs, authenticate permission or decide whether a claim is true |
| handoff | Required scope/stage/owner; local input/output references; precise-change baseline hash and declared delta/invariants; conditional baseline approval; registry trace IDs; completion output/check evidence | Approval strings and check narratives are records, not authenticated approvals or proofs of quality |
| manifest | File inventory IDs, paths, SHA-256, recorded permitted use, medium/toolchain status, evidence file for verified native reopen claim | Byte reopening is not application reopening; evidence still needs examination |

All references are relative to explicit --root. Absolute paths, parent traversal, escaping symlinks and missing files fail. JSON duplicate keys, nonfinite numbers and inputs above 16 MiB fail. Files referenced for hashing are streamed; callers should use trusted workspaces, not adversarial concurrent filesystem mutation. No network, shell execution or record mutation is performed by validators.

For precise changes, preparation is allowed with an unapproved candidate. If execution explicitly requires an approved baseline, the baseline must carry approved status, by and reference. This does not authorize execution. Completion is separate from readiness: `completion: complete` requires outputs plus each criterion covered by a passed check with local evidence. Creative and external review gates still apply.

Templates contain REQUIRED placeholders and are intentionally incomplete. Preserve optional metadata and explicit unknowns rather than guessing. Migration should use a separate reviewed change and retain the prior record; no migration is currently implemented.

## Corrections retained from the source implementation

Precise-change records require an explicit boolean `requires_approved_baseline`. This is a caller-recorded policy requirement, not authenticated authorization: false permits provisional work, true plus execute requires baseline reviewer/reference text. A passing record never grants permission to run an action. Candidate approval remains independent.

All handoff input/output references and passed-check evidence require hashes. Completion checks use registered criterion IDs and supported statuses. Canonical persona definitions load from the trusted package directory, independently of the caller's --root; all three definition files and counts are checked. Missing/inconsistent definitions return config_error. Local read failures return io_error. Other malformed record shapes remain malformed_record. Package/source authenticity still needs distribution review; counts do not prove external source parity.

Dates require exactly YYYY-MM-DD and a real calendar date across interpreters, including --as-of. Invalid dates produce structured errors. Embedded evidence errors include the evidence_record prefix and list-member paths. Known repeated siblings are checked by item ID; an unknown sibling yields linkage_partial, not a fabricated row. Malformed repeated groups fail shape checks and skip duplicate linkage diagnostics.

The bundle checker covers explicitly listed source folders/extensions and a short known-reference pattern list. It does not certify absence of every client identifier or secret. Human scope review remains necessary. Hashing streams all bytes with no asset-size ceiling; large files take proportional time. --root contains path resolution, not hardlink provenance or hostile concurrent replacement.

## Reference decisions

The `reference-decision` kind adds pinned immutable baseline values, declared derivations, source/evidence provenance, rights holds, operation-scoped cost evidence, budget conflicts and pending verification. See [the contract](REFERENCE-CONTRACT.md) for the schema, field semantics and assurance limits. The Markdown view is preserved; it is not parsed by the validator.
