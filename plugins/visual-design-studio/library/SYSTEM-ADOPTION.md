# Discovering and adopting a UI system

Version-Timestamp: 2026-09-10 20:14:15 AST

Use this method only when the task includes choosing or extending a UI system, a component source or a design-token format. Use [reference selection](REFERENCE-SELECTION.md) for visual direction first when needed. Identity guidelines describe the brand across media; a UI system additionally owns component behavior, state, semantics and implementation conventions.

## Inventory before choosing

Locate the project's actual token authority, component library, framework/version, supported platforms, accessibility behavior, licenses, tests and maintenance owner. Separate declared rules from repeated values that merely happen to exist. Reuse the established system where it serves the task; do not introduce a second theme beside it or change approved values because a reference uses different ones.

Compare each candidate at its real layer:

| Layer | What to inspect | What it cannot establish alone |
| --- | --- | --- |
| Reference gallery or style preset | Rendered examples, derivation, scope, asset rights | Official brand authority or working component behavior |
| DESIGN.md or token format | Versioned specification, semantics, converters and loss | Complete UI implementation or brand approval |
| Component source/registry | Exact package/commit, variants, keyboard/state behavior, dependencies | Suitability of every third-party registry item |
| Platform guidance | Official target/version documentation and conventions | Equivalent behavior on another platform |
| Agent implementation skill | Actual instructions, linked resources, scripts and permissions | Safe execution merely because the file is public |
| Agent UI protocol or renderer | Host capabilities, allowed actions, validation, state and fallback | A complete visual system or authorization for side effects |

Record publisher, exact license file, intended-use compatibility, transitive assets, freshness and cost boundary. A license badge without its text is unresolved. An MIT wrapper does not relicense its embedded platform documents. Free code can still require paid hosting, inference, export or API use. Confirm the particular operation and quota; never equate a web subscription with API, MCP or CLI entitlement.

## Make a reversible adoption decision

Choose reuse, extend, evaluate separately, reference only, or reject. Explain the task-specific reason, minimum imported surface, owner and rollback to the prior baseline. Review dependency and executable behavior before any authorized installation. A discovery recommendation itself executes nothing.

For a proposed system, first specify one representative vertical slice: a real content layout plus an interactive component with error, empty, loading, keyboard and narrow-screen states as applicable. Compare against the existing system and accessibility/performance requirements. Approve broader adoption only on that evidence; do not migrate every screen merely because an example looks attractive.

## DESIGN.md compatibility

The filename alone does not identify a schema. Declare whether the document is project prose, a vendor export or a particular version of a format specification. A source-era Google alpha specification combined YAML tokens and ordered prose sections; recheck the exact current format and version before claiming compatibility. Do not silently overwrite an existing project convention or claim conformance from a similar heading count.

Map source token roles to destination semantics explicitly. Primary may mean text ink in one system and an action color in another. Keep a designated canonical source; document conversion direction, unsupported values, state variants and round-trip losses. If the project's token file is authoritative, generated prose must reconcile to it. Preserve unknown content when the chosen format requires it.

Record format/lint checks, token comparison, export checks, computed rendered styles and human judgment separately. Read the tool's actual exit semantics. Successful export is not proof that lint passed, and a contrast warning or structural pass is not full accessibility acceptance. No third-party CLI is required or installed by this method.

## Generative and collaborative UI

Choose fixed components, a constrained declarative catalog, or generated code according to the task's variability and consequence. These are options, not a maturity ladder that always ends in arbitrary code. A catalog constrains vocabulary; validate generated properties and authorize each action on the server. Event transport, rendering and MCP delivery can coexist and must not be conflated.

For an embedded or shared artifact, establish host support, sandbox/CSP boundaries, allowed data flows, revision ownership, stale-state handling, undo/cancel and a text fallback. A sandbox does not make generated content correct or authorize transactions. In a future implementation, verify these boundaries and recovery with the actual host before calling the integration complete. This research does not select a runtime.

Record system decisions in the [structured contract](REFERENCE-CONTRACT.md) as well as the authoring view when deterministic constraint checks are needed. For physical or closed-software contexts, identify current official device/platform guidance and actual access evidence separately. Reference lists do not replace that evidence.
