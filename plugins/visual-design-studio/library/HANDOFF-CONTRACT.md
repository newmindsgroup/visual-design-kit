# JSON handoff subjects and migration

Version-Timestamp: 2026-09-10 19:59:06 AST

The handoff format remains `schema_version: "1.0-proposed"`. An additive reserved `subject_type` discriminator selects `persona` or `bounded_actor`. Explicit null, nontext values and any other strings are invalid; only omission chooses the default. Omission preserves the existing persona route. Other validation kinds and supported versions are unchanged. The new capability requires the updated validator even though the format remains 1.0-proposed; older validators reject the bounded-actor route. Pin the package edition and validator source hash or commit in the work record before preparing handoffs. Run both persona and bounded-actor regression cases with that validator. An older validator may reject the actor route; do not remove actor metadata or weaken the contract to obtain a pass. Previously ignored mixed actor metadata is now intentionally rejected, so compatibility means preserving valid persona records, not every formerly tolerated malformed shape.

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

Keep the existing `inputs`, `outputs`, file hashes, scope, readiness, baseline approval, completion and check rules. A complete handoff still needs actual outputs and passed evidence for every registered criterion. A partial specification handoff can honestly use `completion: "partial"` and checks with `status: "pending"`. Readable “not run” maps to JSON `pending`; “not applicable” maps to `not_applicable`. Readiness and approval remain separate.

## Migration and evidence preservation

Existing valid persona records need no edits. To author a new bounded-actor record, add the explicit mode, replace the persona registry with actual actor definitions, and change trace subject fields to `actor`. Do not merely rename a full persona or remove required audience evidence. Mixed actor/persona handoffs are outside this minimal contract; split the selected scope into explicit records when needed.

Preserve earlier input records and their checks when migrating. Current hashes belong to the new packet; old results must not be relabeled as current. The package test manifest must verify both persona and bounded-actor routes before claiming compatibility. No renderer, user study, production permission or downstream execution follows from a structural pass.
