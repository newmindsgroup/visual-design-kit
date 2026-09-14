# Proposed design-process blueprint

Version-Timestamp: 2026-09-10 20:14:15 AST

Status: proposed for adoption by the adopting project owner. This is a process specification, not an adopted lifecycle or implemented agent architecture. It serves any client. Active methods and tool contracts are client-agnostic. The adopting project instructions, scope and approvals govern.

## Approach and scope

Use six repeatable stages: understand the problem, establish direction, explore, design, validate, and hand off. Feedback can return work to the earliest assumption it invalidates. Maintenance starts from a new bounded change request against an approved baseline. This is an original synthesis, not a claim that a particular book prescribes these exact six stages; source provenance belongs to the pinned source version.

UX runs through every stage: identify whose activity matters, where it occurs, what they need to understand or do, and what evidence would show improvement. For a logo or passive sign, comprehension and recognition may matter more than completing an interface task. For a touchscreen, the physical setting and recovery from interruption are part of the experience.

In scope: stage contracts, generic local validators, draft capabilities and selective usage. This process does not select or authorize pilot execution, production runtimes, installations, publication or final architecture.

## Brand research routes

Use [RESEARCH-CAPABILITIES.md](RESEARCH-CAPABILITIES.md) to select the research scenario before collecting references: supplied established identity, no-kit pitch, fragmented/conflicting material, commissioned formalization/evolution/rebrand, new brand, campaign adaptation, or delta-only revision. Its shared evidence backbone and selectable brand, audience/market and retail/context methods feed stages 1 to 3 and reference-based validation. Research can stand alone or reuse current evidence. Identity guidelines and UI design systems are distinct downstream authoring outputs.

Exploratory pitch concepts may proceed from adequate public evidence and permitted assets with explicitly provisional rules. A full official kit is not a blanket prerequisite. Production resolves exact assets, product/copy truth and use rights; inferred rules never become client-approved by repetition. The companion defines these gates and the actual candidates assessed.

## Persona and AI execution outputs

Use [capability contracts](CAPABILITY-CONTRACTS.md), [the persona guide](templates/persona.md) and [the stage packet](templates/stage-execution.md) to turn each stage into a bounded AI task. The canonical persona structure is captured in [field definitions](templates/persona-fields.json) and [component definitions](templates/persona-components.json), with 118 source fields and 35 component representations. Research produces or reuses evidence-linked personas/proto-personas, separating buyer, user and operator where needed. Each relevant need traces through use case, requirement, design decision and validation criterion. Unresearched profiles remain hypotheses.

Each stage consumes a compact execution packet and returns artifact references, evidence, decisions, checks, readiness and resume instructions. Canonical files supply shared truth; tool access and permissions must be checked in the actual Codex or Claude Code runtime. Prompt completeness does not prove generated design quality.

## Shared handoff record

Every stage passes the same compact record, supplemented only where needed:

- Objective, intended audience/activity, context of use, scope, and success measure.
- Source IDs and evidence status: observed, reported, inferred, assumed, or unresolved. State rights and authorized recipients for assets.
- Baseline path and version/hash, approval reference if any, requested change, and invariants. An unapproved reference is not an approved baseline.
- Deliverable path/version, owner, decision and rationale, rejected alternatives worth preserving, dependencies, and open risks.
- Checks actually performed with result/evidence location; gaps; readiness status; reviewer/decision owner; next stage or loop-back reason.

Use readiness labels `ready for next stage`, `needs revision`, or `blocked by prerequisite`. Record approval separately: `not requested`, `pending`, `approved by [person/reference]`, or `rejected`. Tool success and model confidence cannot award human approval. For phase-only work, supplied prior-stage evidence can fulfill the contract without recreating its documents.

## Stage contracts

| Stage | Required inputs | Output and decisions preserved | Review and evidence | Ready or loop back |
| --- | --- | --- | --- | --- |
| 1. Understand the problem | Request; audience and activity; context; available source assets; known constraints; scope | Qualified brief; research scenario and source/asset register; brand/audience/context findings and gaps; applicable persona/proto-persona records and traceability; measurable objective; constraints, assumptions, exclusions and decision owner | Inspect relevant originals; separate stated preference from observed need; establish how success will be measured and who can judge it | Ready when the problem and constraints support the next decision. Missing access can permit an explicitly provisional concept; unsupported critical assumptions cannot pass as verified. Return here when findings invalidate the problem or audience |
| 2. Establish direction | Brief; research handoff with source status, continuity rules and opportunities; brand truth; medium constraints; rights; success measures | Recommended strategic direction; design principles; content priorities; evaluation plan; tradeoffs and rejected directions | Trace each principle to the objective or a declared hypothesis; check feasibility and conflicts before visual investment | Ready when decision owner accepts direction at the agreed authority level. Return to understanding if objectives conflict; keep unapproved options labeled proposed |
| 3. Explore | Direction or authorized exploratory brief; invariants; highest-risk questions | Distinct concept candidates, sketches/wireframes or rough prototypes; comparison; selected candidate and why | Use the cheapest representation that answers the question; evaluate alternatives against shared criteria. Preserve useful rejected ideas and unresolved hypotheses | Ready when evidence distinguishes a viable candidate and remaining uncertainty is suitable for detailed design. Loop to direction if every option fails the premise |
| 4. Design | Selected candidate; baseline; content/assets; technical constraints; state and variant requirements | Coherent editable candidate and required variants; component/identity rules; change log; implementation handoff where applicable | Check hierarchy, content, interaction states, geometry and invariants as work develops. Record material departures and their approval status | Ready for validation when required artifacts and states are inspectable. Return to exploration for a conceptual defect; repair craft defects here |
| 5. Validate | Candidate; success criteria and test plan; representative tasks/context; baseline; target environment | Findings with severity and evidence; revisions; retest results; remaining limitations; accept/revise recommendation | Separate human usefulness/comprehension, reference-based brand fidelity and campaign/message fit, visual craft, technical behavior, accessibility, and destination checks. Report actual test context, participants where applicable, and coverage. Planned goals and metrics support evaluation; checks alone do not prove user success | Advance when agreed criteria are met or the authorized decision owner explicitly accepts a documented residual risk. Missing mandatory evidence stays pending. Route each failure to the earliest affected stage |
| 6. Hand off | Reviewed candidate; approvals appropriate to recipient/use; rights; editable/export artifacts; validation record | Versioned manifest; source/export references; usage instructions; owner; limitations; replacement/rollback reference; maintenance trigger | Confirm recipient can open/use the package, assets resolve, and permitted dependencies travel with it. Distinguish prepared, reviewed, accepted, and released | Ready for the agreed recipient/use only after required acceptance. A review handoff may be complete while deployment is pending. Return to design for broken packaging or validation for destination failure |

Maintenance is event-driven: changed user needs, content, brand, environment, defects, or measured outcomes produce a new request. Record the trigger, affected baseline, owner, priority, and new acceptance evidence. Reuse valid prior evidence; retest what the change invalidates. Do not introduce scheduled automation by implication.

A critical assumption is one whose failure changes the objective, permitted use, rights, safety, or feasibility of the next deliverable. Give each such assumption an owner, verification action, consequence if wrong, and review point. Unsupported means no identified evidence sufficient for that decision. A craft defect can be repaired within the accepted direction; a conceptual defect invalidates that direction or its user premise. For example, poor contrast may be a local repair, while an illegible required palette may require a direction decision.

## Entry paths and proportional rigor

| Entry | Minimum prerequisites | Work performed | Escalation trigger |
| --- | --- | --- | --- |
| Whole project | Objective, decision owner, permitted sources and scope; unknowns explicitly listed | All six contracts, iterating as evidence requires; depth depends on consequence | Broader audience, delivery medium, data exposure, or release scope requires revisiting the brief |
| Phase only | Named phase/output; relevant prior decisions/evidence; target constraints; acceptance criteria | Verify prerequisite completeness, then execute the requested phase and its affected checks | Missing direction is a bounded discovery task, not permission to invent approval or silently run a whole project |
| Precise revision | Exact baseline; requested delta; invariant list; authorized edit scope; comparison method | Inspect baseline, make separate candidate, compare delta and preserved properties, check affected behavior, hand off review result | If the delta changes concept, geometry, dependencies, rights, or user flow beyond scope, expand the plan and obtain the necessary direction before that work |

Example: changing one approved sign headline requires source copy, authorized replacement text, layout constraints, and readability checks. It does not automatically require new brand exploration. If the replacement no longer fits at the intended viewing distance, return to layout or content direction instead of shrinking text without review.

Example: changing a touchscreen button label also checks wrapping, target behavior, accessible naming, related instructions, and the resulting state. A small visual delta can have wider behavioral consequences.

For an internal sketch, use light critique and explicit assumptions. For client delivery or an interactive/physical installation, require proportionate user, accessibility, technical, rights, and destination evidence. No universal numerical quality score or fixed participant count is adopted. Define thresholds before evaluating; record context and limitations of small studies.

## Delivery paths

| Path | Understand and direct | Explore and design | Validate and hand off |
| --- | --- | --- | --- |
| Brand and logo | Positioning, audience perception, identity continuity, naming/content ownership, intended applications | Distinct identity ideas; wordmark/symbol relationships; typography/color; master geometry and usage rules | Recognition/comprehension against objective; small/large and single-color uses; accurate masters and exports; licensed assets. Specialist clearance remains separate where required. Historical style research is not identity-production validation or legal clearance |
| Web and apps | User tasks, information architecture, content/data needs, platform, access and error risks | Flows then appropriate prototypes; responsive layouts; design system; empty/loading/error/success and keyboard states | Representative task evidence; rendered desktop/mobile and interaction checks; accessibility checks against an explicitly selected current standard; applicable engineering checks before release. Design approval and working implementation are distinct |
| Digital signage | Audience activity, dwell/viewing distance, ambient conditions, content priority, exact display/player and rights | Hierarchy and still concepts before motion when useful; exact aspect/crop; purposeful motion and fallback | Actual rendered files, readability in context, playback/startup/loop and intended device evidence. Browser results do not establish display acceptance. Package masters, fallbacks, device record, ownership and replacement instructions |
| Public touchscreens | Shared-use context, standing/seated access, reach, privacy, interruption, cleaning/environment, device/connectivity | Task flow and physical placement together; touch feedback, timeout/reset, recovery, offline/error states | Test representative users at actual or justified physical setup; reach/readability/touch reliability; session privacy and recovery; sustained target-device behavior. Mobile UI guidance is insufficient to certify a kiosk |

Fixture/rendering is an optional extension: lock dimensions, proportions, shelves, material and graphic placement; identify what a render can establish versus what requires physical/engineering validation. Neither lighting-first nor increased resolution is adopted as a universal repair method.

## Local capability implementation

Use [capabilities.json](capabilities.json) for selected entry paths; establish actual destination status through [software readiness](SOFTWARE-READINESS.md). Historical method assessment is excluded from this package and is not an execution dependency.

## Reference discovery and system adoption

During direction/exploration, use [REFERENCE-SELECTION.md](REFERENCE-SELECTION.md) to compare style, typography and motion against the task. Use [SYSTEM-ADOPTION.md](SYSTEM-ADOPTION.md) only for a component/token/platform decision. These methods extend the existing lifecycle rather than replacing its research and validation contracts. Retain source evidence and limits in the adopting project research register.

## Content writing

Select the `content` capability using [the content workflow](CONTENT-WORKFLOW.md). It connects brand language, website/SEO, UX writing, campaigns and editorial content to the existing lifecycle and packs. Reuse accepted foundations and load only the relevant writing guide; no new visual pack or installed runtime is required.
