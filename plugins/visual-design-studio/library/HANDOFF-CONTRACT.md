# JSON handoff subjects, current results and migration

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

New handoffs use `schema_version: "2.0"`. This format records the exact candidate artifact paths and lowercase SHA-256 hashes, then binds every current criterion result to that full candidate set. The validator recomputes every declared hash from exact file bytes. A missing file, stale hash, unsafe path, or incomplete candidate binding fails validation. Pin the package edition and validator source hash or commit in the work record before preparing handoffs. Run both persona and bounded-actor regression cases with that validator. A structural pass does not create factual, creative, legal, user, device, or approval evidence.

`subject_type` selects `persona` or `bounded_actor`. Explicit null, nontext values and any other strings are invalid; only omission chooses the persona default. Other validation kinds retain their existing versions.

## Candidate-bound current results

`candidate.artifacts` is a nonempty list of local `{ "path", "sha256" }` records. Paths must stay inside the declared workspace and hashes must be lowercase SHA-256 over exact bytes. Every `current_checks` row has one registered `criterion`, a `status`, and a `candidate_artifacts` list that exactly matches the declared candidate set, including both paths and hashes.

There is exactly one current result for every registered criterion. `current_checks` is the only collection used to evaluate a current completion or readiness claim. For `completion: "complete"` or `readiness: "ready"`, every current result must be `passed` and include a locally hash-bound `evidence` record. A failed, pending, not-applicable, missing, or duplicate current result keeps the claim invalid. Complete handoffs also require actual output files.

`historical_checks` is an explicit separate list. It preserves prior passed, failed, pending, or not-applicable results and can include a nonempty `superseded_by` reference. Historical checks are structurally validated but never satisfy, invalidate, replace, or add to current criterion coverage. Record a repair as a historical failure plus the single repaired current result. Do not relabel old evidence as current for a new candidate.

## Persona route

Use the existing [persona handoff template](templates/handoff-record.json). `subject_type: "persona"` is optional. Keep the nonempty `registry.personas` list of IDs and each trace row's `persona` reference. Neither `registry.actors` nor an `actor` trace field is permitted, even if empty or null.

Selecting a persona still requires a complete upstream record. Use [persona.md](templates/persona.md) as the authoring guide and [the field inventory](templates/persona-field-inventory.md) as the coverage contract; validate the filled JSON record separately. Handoff validation checks registered IDs, file references, hashes and check evidence. It does not load or validate a complete persona simply because a persona ID appears. Validate actual persona records separately with the existing persona validator and preserve their evidence status. A handoff pass is not persona, research or design approval.

## Bounded actor route

Use [handoff-actor-record.json](templates/handoff-actor-record.json) when the selected pack justifies omitting a full persona. Explicitly set `subject_type: "bounded_actor"`; do not include `registry.personas` or any trace-row `persona` field.

`registry.actors` is a nonempty array of definitions. Each definition has exactly these fields:

| Field | Contract |
| --- | --- |
| id | Unique nonempty actor ID used by trace rows |
| role | Descriptive role within the scoped task |
| goal | What this actor is trying to accomplish |
| context | Bounded situation in which the task occurs |
| evidence_class | observed, supplied, inferred or proposed |

Descriptions cannot be blank or unresolved placeholders such as REQUIRED, unknown, TBD or N/A. Classification is declared provenance, not a verified fact. This authoring vocabulary follows the UX detail extension; it is separate from the evidence validator's status vocabulary and must not be automatically mapped to it. The validator cannot determine whether prose is substantively meaningful; the author/reviewer must check it against the brief. Extra fields such as `full_persona` are rejected rather than silently accepting an unsupported claim.

Each trace row uses `actor`, `use_case`, `requirement`, `decision` and `criterion`. All references must resolve. Every registered actor, use case, requirement, decision and criterion must appear in at least one actor-route trace row. This coverage rule applies to the new bounded-actor route; it does not retroactively strengthen the legacy persona route. Register only the selected items for this handoff. A pending check is permitted in a partial handoff; it does not excuse a missing trace.

Validation can stop after an invalid subject mode or malformed registry rather than accumulating every later error. This is a fail-closed structural check, not a promise to enumerate all faults. IDs are matched exactly; authors must preserve their spelling and whitespace rather than relying on normalization.

Keep the existing `inputs`, `outputs`, file hashes, scope, readiness and baseline approval rules. A partial specification handoff can honestly use `completion: "partial"`, `readiness: "provisional"`, and current checks with `status: "pending"`. Readable “not run” maps to JSON `pending`; “not applicable” maps to `not_applicable`. Readiness and approval remain separate.

## Migration and evidence preservation

Schema `1.0-proposed` records remain readable only when they are partial and draft, provisional, or blocked. The validator returns a `handoff_schema_migration` warning for these legacy records. A legacy record cannot claim `completion: "complete"` or `readiness: "ready"`; it must migrate explicitly to schema 2.0. No implicit conversion can invent candidate bindings.

To migrate, preserve prior `checks` as `historical_checks`, declare the current candidate artifacts and their exact hashes, then author one new `current_checks` row for every criterion. To author a bounded-actor record, also add the explicit mode, replace the persona registry with actual actor definitions, and change trace subject fields to `actor`. Do not merely rename a full persona or remove required audience evidence. Mixed actor/persona handoffs are outside this minimal contract; split the selected scope into explicit records when needed.

The package test manifest must verify both persona and bounded-actor routes before claiming compatibility. No renderer, user study, production permission or downstream execution follows from a structural pass.
