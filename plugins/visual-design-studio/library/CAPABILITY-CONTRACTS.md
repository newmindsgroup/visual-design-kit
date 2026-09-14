# Capability contracts

Version-Timestamp: 2026-09-10 20:02:52 AST

The [catalog](capabilities.json) is the entry-point and dependency authority. Dependencies describe input needs, not mandatory repeated work. Reuse valid project inputs and load only selected context.

All capabilities declare inputs, a concrete method, outputs, acceptance and limits. [design-work.md](templates/design-work.md) carries decisions and check evidence; [stage-execution.md](templates/stage-execution.md) carries resumable instructions. [DATA-CONTRACTS.md](DATA-CONTRACTS.md) describes implemented machine checks. [TOOLCHAINS.md](TOOLCHAINS.md) defines medium interfaces without vendor defaults.

Persona records preserve all 118 canonical fields and 35 component representations. Unknowns are explicit and synthetic assumptions are not evidence. Research preserves source authority, permission, freshness and contradiction. Downstream decisions trace need/use-case/requirement/decision/criterion IDs. Revision scope preserves a hashed baseline and declared invariants; a candidate can remain unapproved while compared.

All instruction modules are drafts. Validator execution must be verified for the assembled edition and destination; no instruction entry implies an installed tool, production artifact or user-tested design. [QUALITY.md](QUALITY.md) governs acceptance reporting.

## Audience input selection

This is the shared entry rule for downstream capabilities that link here. Record the decision once in the existing work record: selected audience form, intended use, source IDs/versions, evidence status, reason, affected requirements and any hold/owner/release condition. It does not change the persona schema or turn the catalog into an execution engine.

- **Full persona:** required when explicitly requested by the user/project, when the selected task is persona creation/revision, or when material differences in behavior, goals or constraints must be represented to make the design decision. Reuse a relevant current complete persona when available. If creating or revising one, use design-persona-build and retain all 118 fields and 35 representations, including explicit unknowns. A complete hypothetical persona still is not observed research.
- **Bounded actor:** sufficient for a narrowly scoped decision when a role, goal and context explain the affected needs and no required audience distinction is being omitted. Record the actor ID, role, goal, context and evidence classification under [UXD-06](UX-DELIVERABLES.md) and the [handoff subject contract](HANDOFF-CONTRACT.md). State why a full persona is unnecessary for this use. Never infer that audiences are equivalent merely because research is absent.
- **Uncertain or missing:** if audience differences could change the decision and the available evidence cannot settle that, hold the affected audience-dependent decision or identify a specifically authorized provisional exploration with assumptions and its use limit. Continue independent work. Do not create a convenient actor to bypass the gap, or mark a requested full persona complete using a summary.

Accepted inputs can be reused for precise revisions without rebuilding personas or creating redundant actor records. If a project explicitly requires a full persona, this rule does not waive it. If an additional capability contract imposes a stricter input, honor it; if requirements conflict, surface the conflict to its authorized owner and hold the affected use until it is resolved.

The catalog's persona dependency means inspect the audience prerequisite and record its disposition before downstream work. The planner still returns the same instruction IDs; it does not automatically build or validate personas, evaluate these conditions or execute capabilities. When a bounded actor is justified, downstream UX/strategy work can use that record without claiming the persona capability was executed. When a persona is selected, use its complete upstream record and validate it separately. The [handoff contract](HANDOFF-CONTRACT.md) governs actor/persona JSON routes; handoff validation checks structure, not audience truth.

Carry the selected form, evidence limits and relevant need IDs into UX, strategy, identity/UI inputs and the final handoff. Reassess when scope, audience differences, evidence or intended use changes; invalidate affected decisions/check applicability while preserving historical results. Production and delivery may consume accepted upstream decisions without regenerating audience research, but cannot use them beyond their recorded scope.

## Content prerequisite and output contract

The `content` catalog dependencies load research and handoff instructions; they do not mandate fresh research. Select the audience under the shared rule above. Reuse accepted positioning/voice or select brand-strategy when those decisions need creation; use UX when interaction logic needs definition. Existing prerequisites remain subject to their own contracts. Write the [content extension](templates/content-work.md) within the existing work record and preserve UXD-13/22 IDs. The catalog remains instruction ordering only.
