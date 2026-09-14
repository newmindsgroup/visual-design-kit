---
name: design-persona-build
description: Build or revise complete evidence-linked customer, user or operator personas using this project's canonical 118-field structure. Preserve all component representations and unknowns; do not substitute a short audience summary.
---

# Complete design personas

Version-Timestamp: 2026-09-07 09:16:31 AST

Project-local draft entry point, not installed or automatically discoverable. Uses this repository's shared canonical resources; copying this folder alone is insufficient.

## Contract

Input: research brief, role/use scope, permitted evidence references, existing persona version if any, intended decision and output workspace. Distinguish buyer/decision-maker, end user/shopper and operator where their goals differ. Account/buying-group details are conditional, not invented biography.

Read [persona instructions](../../templates/persona.md) and the [component contract](../../templates/persona-components.json); use [field definitions](../../templates/persona-fields.json) and copy [the complete blank record](../../templates/persona-record.json) into the authorized output workspace. Read only relevant source evidence. Reuse a current persona for narrow work when valid, rather than regenerating it without reason.

Populate every canonical field and W01 to W35 representation, including unknown or justified not_applicable values. Keep repeated-object item IDs aligned. Preserve Spanish/English label mappings and source/inferred/proposed status across translations. Collection/navigation components can reference shared records; when not relevant, record why instead of omitting them. No invented quotes, demographics, protected traits, diagnosis, portraits or research facts.

Keep AI extensions: owner/version, functional needs/context, contradictions, validation/refresh plan and persona need -> use case -> requirement -> decision -> criterion. A proto-persona remains hypothetical until appropriate research review supports the stated use. Structural completion is not research validation.

For revision: inspect the exact prior version, requested delta and invariants. Preserve unrelated fields/status/evidence. If an approved-baseline preservation claim is requested but approval is absent, report that gap; do not invent approval. An explicitly requested provisional update can still produce a separate unapproved candidate within scope.

Output: full record plus concise change/evidence/gap/validation handoff. Check exact field-set equality, all component IDs, meaningful status/reasons, item linkage and traceability; describe checks actually performed. Stop only the dependent work when required sources, scope or authority are missing. Shared acceptance cases and version handling: [CAPABILITY-CONTRACTS.md](../../CAPABILITY-CONTRACTS.md).
