# Design-system portability and token evidence

Version-Timestamp: 2026-09-10 20:21:06 AST

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.149.1; timestamp=2026-09-08 22:17:00 AST

Status: authored instructions, not an implemented Open Design integration. Use for an actual system import, export, migration or adapter. Ordinary component use does not require another package or token database.

Identify the existing authoritative values, human/agent design guidance, implementation outputs and intended receiver. Preserve the project's declared token authority and the ownership in [design craft](../../../DESIGN-CRAFT.md). When canonical JSON produces CSS, the CSS is a derived output; a destination tool preferring tokens.css does not transfer authority. Never maintain two independently edited masters.

For each required destination role, record the original token ID/value, source file/version and selected mode; then the destination name/unit and any conversion. Keep evidence classification separate from approval: an observed CSS value is not automatically an approved brand value. Inferences and proposed fallback values retain those labels until the proper owner accepts them. An alias points to another token; it is a reference relationship, not independent evidence. Preserve alias chains and distinguish semantic roles that happen to share a value.

Inspect all modes relevant to the output, such as light/dark, density or platform. Record unresolved references, cycles, missing units, unsupported modes, collisions and lossy transforms. Never fill an unknown brand accent or typeface with a generic library default and describe the result as extracted. A temporary fallback must have a reason, intended use and replacement condition in the existing work record.

Before use, map declared package paths to actual files, load only relevant instructions and verify the receiver consumes the metadata relied upon. Readable SKILL.md syntax does not establish runtime support for forms, sliders, parameters or permission gates. Stage read-only references or explicit copies using the existing path/manifest contract; do not install symlinks or modify global agent configuration as a side effect.

Checks: compare requested versus loaded resources, canonical versus emitted values, unit/mode/alias behavior and representative component renders. A completeness percentage can describe mapping coverage but cannot prove identity fidelity, accessibility or approval. Apply the unavailable-resource rule in the existing stage packet. Report exact versions, conversion limits and the next owner through the existing [stage packet](../../../templates/stage-execution.md).

Derivation: original method informed by the [system package description](https://github.com/nexu-io/open-design/blob/bb9682a5f939cd44947300cd4c7f5195e4230250/design-systems/README.md), [token evidence model](https://github.com/nexu-io/open-design/blob/bb9682a5f939cd44947300cd4c7f5195e4230250/apps/daemon/src/design-systems/token-contract.ts) and [current skills protocol](https://github.com/nexu-io/open-design/blob/bb9682a5f939cd44947300cd4c7f5195e4230250/docs/skills-protocol.md). We retain our own token authority and statuses; no upstream schema, scoring system, defaults or runtime is imported. Assessment (optional provenance in the pinned source version; not bundled).
