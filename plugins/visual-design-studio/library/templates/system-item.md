# System item specification template

Version-Timestamp: 2026-09-07 15:07:47 AST

Replace this timestamp with the actual revision time. This blank record is not a completed specification. Use it inside the existing [design work record](design-work.md), not as a replacement approval or baseline contract.

## Identity and scope

- Project and work-record ID: [fill]
- Inventory or extension ID, name and version: [fill]
- Owner and reviewer: [fill]
- Selected profiles, platform/version and intended users: [fill]
- Choice: [required / optional / not-applicable / needs-discovery]
- Project rationale, need and requirement IDs: [fill]
- Shared family contract and entry notes reviewed: [link]
- Included variants and explicit exclusions: [fill with reasons]

## Anatomy, behavior and content

Describe the parts and their relationships. Specify action versus navigation, activation, value/data model, validation timing, content length, labels, terminology, errors and recovery. Include representative boundary content, localization and RTL behavior. Explain when to use this item and when another entry fits better.

| Variant | Anatomy and content | Behavior | Token roles | Dependency IDs |
| --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [roles; actual values from approved token source] | [fill] |

## States and acceptance

Review the family slots and entry-specific notes. Add domain states and mark irrelevant ones with a reason. Do not assume every item has every state.

| State | Applicable and why | Trigger and visible result | Keyboard/focus/assistive result | Recovery | Criterion ID and evidence reference only |
| --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [pending] |

Consider default, hover where available, focus, pressed, selected, mixed, unavailable, read-only, invalid, loading, empty, partial, error, offline, permission-denied, success, expanded/open, collapsed/closed, idle and reset as relevant. Include reduced motion, text scaling and sensory alternatives when needed.

## Platform contract

| Platform in scope | Navigation and dismissal | Input, keyboard and focus | Adaptive layout and safe areas | Permissions and lifecycle | Actual verification |
| --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [pending] |

Distinguish web links/buttons and ARIA patterns from native controls. Specify phone/tablet back stacks and section state; keyboard appearance and safe areas; permission denial and return from settings. For touch installations specify reach, alternative input, timeout warning, privacy clearing and recovery. For passive displays specify readable content, dwell, scheduling and failure behavior. Print needs production and reading-order checks rather than interactive states.

## Evidence and handoff

Link source and rights records, the [reference-decision contract](../REFERENCE-CONTRACT.md), accepted baseline and permitted changes in the existing work record. Record actual output versions in the production manifest and acceptance evidence in the shared handoff.

Keep four states separate: inventoried; specification completed/reviewed; implemented; tested. For each claimed state provide date, owner and evidence. An approved specification is not proof of an implemented or accessible product.

Open questions, exclusions, test gaps, refresh trigger and next owner: [fill].

## Specimen and implementation representation

Use a [specimen record](specimen-record.md) when a visual example or implementation mapping is needed. Pair anatomy/token roles, usage and counterexample, variant/state, responsive conditions, snippet type and actual evidence at the same candidate version. Label static illustrations, simulated interactions and working implementations separately.

For the expected level of detail, see the [four filled teaching examples](../examples/component-specs/README.md). Adapt selected requirements through the work record; do not inherit teaching choices as approved project decisions.

When adapting those examples, record the [core/conditional selection](../examples/component-specs/selection-guide.md) and applicable criterion branches in the existing work record. Select from task evidence; do not copy every optional behavior into a simple component.
