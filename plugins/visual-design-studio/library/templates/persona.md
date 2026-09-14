# Persona / proto-persona template

Version-Timestamp: 2026-09-07 09:16:31 AST

The user-selected [canonical persona structural contract](persona-field-inventory.md) is canonical. Start from [persona-record.json](persona-record.json): fill every one of the 118 fields defined in [persona-fields.json](persona-fields.json), preserve all W01 to W35 components, and add the AI extensions below. The [bilingual field inventory](persona-field-inventory.md) provides source mapping. Never replace the complete record with this shorter instruction sheet.

All source fields must be present, including age, income, quote and portrait. When irrelevant or unsupported, fill their status as unknown or justified not_applicable instead of inventing values. Repeatable objects retain item IDs across sibling fields. Profile fields may be factually unknown while the record is structurally complete. Do not add biography to make a profile look complete.

## Identity and scope

- REQUIRED ID, version, owner, review/refresh date or trigger:
- REQUIRED role archetype: buyer/decision-maker / end user/shopper / operator/service staff / other justified role
- REQUIRED status: proto-persona hypothesis / research-backed for stated scope
- REQUIRED decision/use scope, market/context and evidence limitations:
- REQUIRED source IDs, review status and approval reference (or pending):
- OPTIONAL account/organization context, buying group, influence and procurement constraints:

## Additional AI/design fields and review lens

For each row record: **finding; evidence ID and locator or explicit assumption; confidence and reason; contradiction/gap; design implication**. A blank field is not verified. Confidence never substitutes for source evidence.

| Dimension | Finding, evidence/status, confidence, gaps and implication |
| --- | --- |
| Goals/jobs and desired progress | REQUIRED |
| Tasks/use cases and scenarios | REQUIRED |
| Triggers, motivations, needs/pains and barriers | REQUIRED |
| Current alternatives, including workarounds or no action | REQUIRED |
| Decision criteria and objections | REQUIRED or justified not applicable |
| Knowledge/literacy and information needs | REQUIRED |
| Language/market and digital familiarity | REQUIRED |
| Functional access needs relevant to design | REQUIRED; unknown is valid; no invented diagnosis |
| Physical environment, device and constraints | REQUIRED |
| Journey and touchpoints | REQUIRED |
| Brand relationship and messaging needs | REQUIRED or justified not applicable |
| Success, failure, recovery and service needs | REQUIRED |
| Demographic detail | Source fields always present; factual values only with evidence and design relevance |

## Traceability and conflicts

| Persona need ID | Use case ID | Requirement ID and status | Proposed/approved design decision ID | Validation criterion ID and evidence needed |
| --- | --- | --- | --- | --- |
| REQUIRED | REQUIRED | REQUIRED | REQUIRED or pending | REQUIRED |

- REQUIRED other applicable personas, shared/conflicting needs and prioritization owner:
- OPTIONAL excluded/non-target roles and task-based reason:
- REQUIRED validation plan, unresolved questions and refresh trigger:
- REQUIRED changes from prior version and affected downstream records (or initial record):

Record source-backed direct quotes only when permitted and useful, with exact locator; otherwise summarize. No invented testimonial or composite quotation. Keep real participant identities in the authorized research store, not in this reusable profile.

## Execution instruction

Build or revise the complete canonical persona record for the named role and scope. Read the source-linked research brief, relevant evidence and existing persona version. Fill every canonical field and component status; retain unknown/not-applicable entries with reason and research action. Keep source facts, assumptions, proposed messaging and generated recommendations distinct. Link needs to use cases, requirements, design decisions and validation criteria. Return the full record, parity check, gaps, validation/refresh plan and stage handoff. If evidence is insufficient, produce a proto-persona without claiming research validation. Do not copy source-client values or invent quotes, portraits, demographic details or permissions.
