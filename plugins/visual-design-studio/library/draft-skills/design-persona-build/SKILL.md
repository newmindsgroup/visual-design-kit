---
name: design-persona-build
description: Build, revise and render complete evidence-linked personas with six detail tabs, comparison, mapping and print export. Preserve all 118 canonical fields, component representations and explicit unknowns.
---

# Complete design personas

Version-Timestamp: 2026-10-22 08:30:00 AST

Reusable capability with a working private HTML renderer. Resolve a host-entry symlink to its real location before following relative links. Read this library's shared resources through the verified checkout; copying only this SKILL.md is insufficient. Availability through a plugin or host entry must be verified on that machine.

## Contract

Input: research brief, role/use scope, permitted evidence references, existing persona version if any, intended decision and output workspace. Distinguish buyer/decision-maker, end user/shopper and operator where their goals differ. Account/buying-group details are conditional, not invented biography.

Read [persona instructions](../../templates/persona.md) and the [component contract](../../templates/persona-components.json); use [field definitions](../../templates/persona-fields.json) and copy [the complete blank record](../../templates/persona-record.json) into the authorized output workspace. Read only relevant source evidence. Reuse a current persona for narrow work when valid, rather than regenerating it without reason.

Populate every canonical field and W01 to W35 representation, including unknown or justified not_applicable values. Keep repeated-object item IDs aligned. Preserve Spanish/English label mappings and source/inferred/proposed status across translations. Collection/navigation components can reference shared records; when not relevant, record why instead of omitting them. No invented quotes, demographics, protected traits, diagnosis, participant portraits or research facts. When the owner explicitly requests illustrative persona imagery, original fictional composites may be generated and visibly labeled AI-generated illustrations. Keep presentation-only imagery separate from research evidence; appearance must not imply typical audience demographics.

Keep AI extensions: owner/version, functional needs/context, contradictions, validation/refresh plan and persona need -> use case -> requirement -> decision -> criterion. A proto-persona remains hypothetical until appropriate research review supports the stated use. Structural completion is not research validation.

For revision: inspect the exact prior version, requested delta and invariants. Preserve unrelated fields/status/evidence. If an approved-baseline preservation claim is requested but approval is absent, report that gap; do not invent approval. An explicitly requested provisional update can still produce a separate unapproved candidate within scope.

Output: full record plus concise change/evidence/gap/validation handoff. Check exact field-set equality, all component IDs, meaningful status/reasons, item linkage and traceability; describe checks actually performed. Stop only the dependent work when required sources, scope or authority are missing. Shared acceptance cases and version handling: [CAPABILITY-CONTRACTS.md](../../CAPABILITY-CONTRACTS.md).

## Reference-depth presentation and repeatable delivery

For a complete persona deliverable, read [the presentation contract](references/presentation.md). The minimum is the owner-selected reference depth: all six detail tabs, contextual sidebar and other profiles, two-to-three persona comparison, page/section mapping, translation state, evidence/unknown states and complete print/export. A JSON field count or a Markdown audience brief does not satisfy a requested visual workbench.

Use the original [workbench builder](../../scripts/persona_workbench.py) with canonical records, or its explicit legacy importer for permitted nested data. It includes original HTML/CSS/JS assets here and a fictional demonstration fixture. Use approved project tokens and assets; preserve the structure without copying another client's wording, claims or portraits. Keep supplied reference snapshots private and hash-bound; never ship them in the shared skill.

Run the real canonical validator, not only field-set equality. Repeated-object fields use linked item_id and text. Evidence IDs must resolve in the embedded source register. The builder also invokes canonical validation before rendering. Its optional --project-root sets the authorized evidence root. Preserve partial translations, dictionary-shaped competitor perceptions and unknown fields through import. Validate joins before displaying targeting weights. Mapping, research validation, owner visual acceptance, implementation and launch remain separate.

Build a new version without overwriting an existing output. Render and inspect desktop/mobile, all tabs, keyboard/focus, all2-to3 selection states, full comparison text, mapping and empty/unknown/error/recovery, source-language fallback and print/PDF. Verify actual exported text includes the inactive tabs and later comparison columns. Record those checks and remaining gaps. An HTML file, source inspection or schema pass alone does not prove reproduction.

Version-Timestamp: 2026-10-22 13:32:00 AST
