# Project starter packs

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

These are original manual starting recipes built from the existing [catalog](capabilities.json), [inventory profiles](inventory/profiles.md) and [UX deliverable contracts](UX-DELIVERABLES.md). They are not installed bundles, new skills or executable orchestration. No client, stack, hardware vendor or final plugin architecture is selected. Use one pack or combine complementary packs; reconcile shared inputs and conflicting requirements once.

## Shared starting instructions for Codex or Claude Code

```text
Task: [outcome, intended use, audience/context and authorized workspace]
Pack: [one or more pack IDs below]
Scope: [full project / selected stage / precise revision]
Execution authority: [assessment/specification only, or actual authorized work]
Existing inputs/baseline: [paths and approval references, or unknown]

Read the selected pack and applicable project instructions. Load only the named
capability entries and relevant UXD contracts. Check existing inputs before
requesting them. Treat dependency order as input needs, not a demand to redo
accepted work. Identify missing facts that change a decision and continue safe
independent work while the affected action is held.

Before declaring a selected deliverable ready, name the exact intended use.
A proposed flow or synthetic prototype can remain usable for exploration while
real data access, creation, modification or cancellation stays held. Resolve
permissions and failure/recovery behavior for each affected operation; a happy
path alone does not release that hold. Load the applicable catalog dependencies
and UXD contracts before choosing a substitute for a persona or state model.

For a precise revision, enumerate the preserved properties from the actual
baseline, including geometry, text, other colors and dimensions where relevant.
Record native reopen/edit/save verification separately from rendered/export
verification. A successful image or PDF check does not prove source editability.

For a passive display, omit interaction artifacts with a reason. If the scope
adds touch or other interaction, re-evaluate the TOUCH pack and its input,
session, recovery and accessibility requirements before continuing that work.
Do not carry passive-display acceptance forward as touchscreen acceptance.

First produce a compact create/reuse/omit/hold selection with each deliverable's
decision, evidence, dependencies, output format and next consumer. Use the
existing design-work record with templates/ux-deliverable.md detail blocks;
personas retain their full canonical structure. Generate only selected outputs.

Follow Understand, Establish direction, Explore, Design, Validate and Hand off.
Iterate when evidence invalidates an earlier decision. Apply the stage-to-stage continuity check below to each selected handoff.
Each stage receives
versioned inputs and returns actual outputs, criteria, evidence status and the
next action. Keep IDs across evidence, needs, requirements, flows, screens,
content, components and tests. A visual diagram must match its structured data.

Separate planned work from executed work, and readiness from approval. Do not
invent participants, research findings, brand authority, successful tests or
produced files. A missing tool is a pending execution step, not a passed check.
Preserve the approved baseline and authorized delta. For component work use
COMPONENT-START.md; for each stage use templates/stage-execution.md. Existing
authorization governs actions; selecting a pack grants no installation, upload,
publication, deployment, data collection or permission changes.

Return a plain-English progress summary, selected artifacts with actual paths,
checks/limits, affected holds and the next best action. Do not ask the user to
choose technical taxonomy already resolved by the pack and project evidence.
```

## Common selection rules

Route tokens matching `research`, `persona`, `handoff`, `reference-direction`, `brand-strategy`, `identity`, `ux`, `prototype`, `ui`, `production`, `delivery`, `content`, `infographics`, `higgsfield-cli`, `openart-cli`, `foundations`, `typography`, `color`, `motion` are the exact capability IDs in [capabilities.json](capabilities.json). Resolve each through its `entry` and `depends_on` fields; do not invent paths or treat prose arrows as automatic execution. Other route words such as composition, context, task and journey describe activities, not additional capability IDs. The catalog, not a duplicate mapping, owns dependencies. Seven packs cover eight profiles because NATIVE selects phone, tablet or both.

All UXD contracts remain available to every pack when their trigger applies; the lists below are starting selections, not exhaustive limits. In particular, select UXD-02 for unresolved research questions, UXD-04 for evidence synthesis, UXD-16 when IA/findability is uncertain, and UXD-27 when coherent delivery slices are needed. A pack can reuse these outputs rather than create new ones.

Select or reuse UXD-05 when behavioral audience differences require a full persona. Otherwise UXD-06 can identify a bounded actor role, goal and context without claiming a full persona has been produced. Whenever a persona is selected, retain the complete canonical record; a role description or summary cannot replace it.

## Stage-to-stage continuity check

Use the existing [stage packet](templates/stage-execution.md) and [UX work-record extension](templates/ux-deliverable.md). Record the source artifact ID/version, selected requirement or decision, destination artifact/consumer, intended use, relevant checks and open holds. Use the UX extension's Identity and decision fields for artifact versions/consumer, Common traceability table for downstream IDs/checks, and hold table for missing inputs and release conditions. The stage packet summarizes those records through Context to load and Next step / resume; do not create a parallel dependency register.

Before consuming an output, verify its actual location, version, authority, freshness, permitted use and readiness for the named decision. An authored hypothesis can support provisional exploration when its limits are retained; it cannot become approved brand authority, user research or production evidence by reuse. A hypothetical actor description is not factual support for a brand or campaign claim, or evidence of display context; preserve each statement's actual evidence classification and source. Missing approval blocks only the action that depends on it. A rendered diagram and its structured source must reference the same version.

Before handing off, check both directions: every selected requirement reaches a downstream decision/check or explicit hold, and each proposed screen, content item, component or export has an upstream purpose. Record justified omissions; do not invent a flow or screen for noninteractive work. Name the receiving role, the exact next action and any missing prerequisite/release condition. In the stage packet, summarize a work-record hold as blocked for the named use and affected item IDs, while stating which independent uses remain ready. This is human-readable scope, not a new JSON readiness value; use the target format's existing contract. Preparing a packet neither sends it nor grants access.

When an input or decision changes, use the work record's existing downstream IDs to identify affected content, flows, screens, components, exports and checks. Mark affected validity stale, preserve historical evidence and reassess only the dependent work. Recheck approval scope; neither prior approval nor a prior test result automatically applies to the new version.

The [shared audience input rule](CAPABILITY-CONTRACTS.md#audience-input-selection) now defines conditional actor/persona inputs for UX, brand strategy, handoff and delivery. A pack's optional persona selection does not override an explicitly stricter project or capability contract. The current catalog is an instruction-dependency plan, not a conditional execution engine. Inspect the selected entry: if it requires a full persona, supply a valid full record or hold that capability. A bounded stage can proceed only when its own requirements are satisfied and it does not claim completion of the held capability. Do not fabricate a persona or modify catalog dependencies to make a packet appear ready.

### What must survive each pack's handoff

These are receiving-stage checks that clarify the existing pack descriptions, not additional mandatory deliverables. Apply only selected scope and reuse the linked UXD/skill fields.

| Pack | Information the next stage must receive | Missing or changed information affects |
| --- | --- | --- |
| WEB | Need/requirement IDs; content and destination IDs mapped to navigation, flow states and screen regions where applicable; access/locale, message IDs, component criteria and real versus placeholder content. The UI/engineering receiver must distinguish a sitemap node from a task state | Missing content or unresolved paths hold the dependent screen/interaction. Changed hierarchy or wording triggers checks of linked navigation, screens, messages and acceptance scenarios |
| APP | Need and domain-object references; state/transition guards; actual permission/data/service contracts; user-visible messages; recovery and acceptance paths. UXD-17/21 carry the same transition IDs into screens and implementation | Unresolved access or uncertain mutation recovery holds the affected action and retry, not unrelated documentation. Service changes invalidate affected flows, content and checks |
| NATIVE | Shared app inputs selected for the native task (supplied directly or reused from valid records, with no separate APP project required) plus platform/version mapping, device/input context and applicable lifecycle/permission/offline behavior. The native implementation receiver gets platform-specific requirements and planned device checks | Missing required shared inputs, unselected platform or missing native behavior holds dependent adoption. Web examples are references, not substitute evidence; platform changes require affected mappings/checks to be reassessed |
| BRAND | Evidence-linked positioning and audience; selected direction with actual decision/approval scope; original master asset identity/version; typography/color/usage rules, rights and application/export matrix. The application designer or production owner gets real masters, or clearly labeled pending assets | Missing authority/rights or unselected masters hold dependent asset use/export. Direction/master changes require dependent rules, applications and exports to be reviewed; UI components still need their own pack |
| CAMPAIGN | Audience/outcome and source-backed message/claim IDs; offer and CTA destination/action where applicable; brand/version/rights; channel, format and presenter-led versus standalone context. The production receiver gets composition/content references and actual export/viewer criteria | Unsupported claims, unresolved destinations or format constraints hold affected content/delivery. Message, offer or channel changes trigger linked composition and format checks; activation stays separately authorized |
| DISPLAY | Physical context evidence and its uncertainty; message hierarchy; storyboard/frame references, duration/order/loop or still-content behavior as applicable; actual player/screen specifications, startup/fallback and export criteria | Unknown device/viewing facts hold field-performance claims and dependent production decisions. Context/schedule/player changes trigger affected layout, sequence, playback and field checks; a still need not invent motion |
| TOUCH | Context and role/need IDs; screen/content mapping; session, privacy, idle/reset, interrupted/offline states; device/input requirements and any staff/service handoff owner. The implementation/evaluation receiver gets linked transition and intended-device criteria | Missing session reset, privacy or recovery rules hold affected interaction/adoption. Device/service changes require affected flows, screens, reset and physical checks to be reassessed |

Where selected components interact, use the [composition check](examples/component-specs/selection-guide.md#check-components-that-work-together). It resolves component-level focus, feedback, dismissal and recovery; it does not replace the pack's research, content, brand or physical-context handoff.

## Pack WEB: websites

- **Start from:** [website profile](inventory/profile-website.md). Inputs: audience/tasks, outcome, existing brand/site/content, scope, target devices, ownership and available evidence. Select the appropriate [brand-research scenario](RESEARCH-CAPABILITIES.md); public no-kit work can be provisional.
- **Route:** research -> persona when audience differences matter -> ux; brand-strategy/identity only if not satisfied by accepted inputs; reference-direction when needed -> ui and prototype at useful fidelity -> production -> delivery. Actual input dependencies remain those in the catalog.
- **Deliverables:** UXD-01/03/06/12, UXD-13 for existing content, UXD-14/15/18 for multi-destination content, UXD-17 for interactive tasks, UXD-20/22/23, UXD-24/25/26 for selected risks, UXD-29. Select research protocols, journeys, blueprint and measurement only when their triggers apply. A one-page brochure does not need a fictitious sitemap or login flow.
- **Handoff:** accepted page/content inventory, navigation and task states -> screen/content/component specifications -> actual implementation/evaluation record. Verify content completeness, task completion, responsive/keyboard behavior and target accessibility evidence. SEO/migration/analytics requirements need explicit scope and appropriate technical owners; the UX pack does not authorize a site launch.

## Pack APP: web applications

- **Start from:** [web-app profile](inventory/profile-web-app.md). Inputs: actor roles, tasks, domain objects, data lifecycle, access rules and actual service contracts. Unresolved permissions or uncertain mutation recovery hold the affected actions.
- **Route:** research/persona -> ux -> prototype for risky tasks, ui with accepted identity -> production/delivery. Reuse brand and evidence inputs where valid.
- **Deliverables:** UXD-01/03/06/12, UXD-11/14/17/18/20/21/22/23, UXD-24/25/26/29. Add UXD-05 only when the shared audience rule requires full personas. Select UXD-10 for operational handoffs, UXD-27 for release slices and UXD-28 for planned learning. UXD-15 is a destination hierarchy where relevant, not a substitute for state/data behavior.
- **Handoff:** needs and task models -> domain/state/permission contracts -> screens and error/recovery content -> acceptance scenarios. Test actual empty/loading/error/success, access, interruption and recovery behavior. The current four web examples do not establish application completeness.

## Pack NATIVE: phone and tablet apps

- **Start from:** [phone](inventory/profile-native-phone.md) or [tablet](inventory/profile-native-tablet.md) profile. Inputs include OS/version, device/form factor, input modes, native navigation, permissions, connectivity and assistive technology.
- **Route:** Relevant shared APP research/UX inputs, supplied directly or reused from valid records without requiring a separate APP project, with native platform decisions before detailed UI/production. Do not substitute DOM/ARIA behavior or web components for native controls.
- **Deliverables:** APP's selected contracts plus explicit platform mapping in UXD-17/18/21/23/24/25/29. Record background/resume, interrupted work, offline/sync, keyboard occlusion and permissions when applicable. Use native guidance verified for the selected version.
- **Handoff:** platform-specific state/navigation and data contracts -> native screens/prototype -> actual device evidence. Web emulation does not certify native app behavior. No native implementation is supplied by this pack.

## Pack BRAND: identity and brand guidelines

- **Start from:** [brand profile](inventory/profile-brand.md). Inputs: business/audience, positioning, existing identity authority, intended applications, naming/content ownership and asset rights.
- **Route:** research -> persona where relevant -> brand-strategy -> identity; reference-direction for selected exploration; production/delivery for actual masters and exports. UX here can concern recognition, comprehension and use rather than interface tasks.
- **Deliverables:** selected UXD-01/03/06/07/08/12/19/23/25/26/29, with UXD-05 only when the shared audience rule requires full personas, plus the identity skill's positioning, concepts, logo/typography/color rules and application output matrix. Do not require screen flows for a logo. Do not claim brand guidelines alone are a complete UI component system.
- **Handoff:** accepted strategy/evidence -> original identity directions -> selected masters and usage rules -> scoped application/recognition/rights/export checks. UI systems for websites/apps attach their own pack and project tokens.

## Pack CAMPAIGN: marketing and sales materials

- **Start from:** [marketing/sales profile](inventory/profile-marketing-sales.md). Inputs: audience, offer/objective, funnel/channel, brand authority, content truth, format and usage rights.
- **Route:** research/brand-strategy as needed -> identity/reference-direction as needed -> selected composition and production -> delivery. Add WEB for a landing page or APP for an interactive service rather than copying their full process into this pack.
- **Deliverables:** UXD-01/03/06/07/12/19/22/23/25/29; UXD-09 for meaningful cross-touchpoint journeys and UXD-28 for authorized measurement planning. Include source-backed messaging and channel-specific creative/export specifications from existing work records.
- **Handoff:** audience need and message hierarchy -> original compositions/content -> actual format/viewer checks. Separate a presenter-led deck from a standalone document. No posting, sending, analytics collection or campaign activation is implied.

## Pack DISPLAY: passive digital displays and OOH

- **Start from:** [display profile](inventory/profile-display.md). Inputs: setting, actor activity, viewing distance/dwell, ambient conditions, screen/player, aspect/resolution, content schedule, connectivity and rights. Unknown physical facts remain explicit.
- **Route:** context/brand research -> hierarchy and concept exploration -> composition/motion if useful -> production/delivery on the selected player/viewer.
- **Deliverables:** UXD-01/03/06/08/12/19/22/23/25/29/30; journey only if multiple touchpoints matter. No navigation, sitemap or interaction flow for a genuinely passive surface. Add touch/WEB scope if interactions are introduced.
- **Handoff:** context and content-priority requirements -> still/storyboard/motion specification -> editable source and output -> actual readability, playback, startup/loop/fallback and intended-viewer checks. A desktop preview does not prove field performance.

## Pack TOUCH: shared touchscreens and physical services

- **Start from:** [touch profile](inventory/profile-touch.md). Inputs: physical setting, actors/roles, standing/seated use, input options, device, session/data boundaries, staff/service handoffs and recovery needs.
- **Route:** research -> persona/context/task/journey where useful -> ux with actual physical/service contracts -> prototype and ui together -> production/delivery with intended-device evaluation.
- **Deliverables:** UXD-01/03/06/08/12/17/20/21/22/23/24/25/26/29/30, plus UXD-05 only when the shared audience rule requires full personas; UXD-09/10 when staff or other channels affect service delivery. UXD-15/18 only for multi-destination experiences. An attract loop is content; its entry/reset behavior belongs to the state model when interactive.
- **Handoff:** context/service needs -> touch/session/privacy/idle/offline states -> screens/content/hardware mapping -> actual reach, readability, input, interruption/reset and recovery evidence. Session reset must address retained personal information when present. Neither a phone mockup nor web test certifies a kiosk.

## Completeness check before beginning a pack

Each selected artifact must have an input, a decision and a next consumer. Every relevant requirement must reach a design/state/content decision and a check, or remain explicitly held. Track missing facts once in the work record, not in competing pack-specific schemas. Reuse accepted prerequisites with references; do not create research, personas or diagrams only to populate folders.

These recipes are documentation, not tested model-routing automation. Book and public-source findings inform the UX contracts; empirical use of these packs, actual renderers and real-user/device acceptance remain separate milestones. The next internal rehearsal can follow a synthetic need through one selected pack without a client pilot or new client input.

## Machine handoff subject selection

Actor-only work can use the explicit bounded_actor route in the [shared JSON handoff contract](HANDOFF-CONTRACT.md), alongside the readable stage packet and validated manifest. Legacy persona traces remain supported. Do not invent a persona or treat a bounded actor as a substitute when the full persona contract is selected. Use `python3 -m design_system validate handoff` with the package CLI usage and required arguments. Pin the package edition and SHA-256 for `design_system/validation.py` from `PACKAGE-MANIFEST.json` in the work record, and verify both handoff modes; no historical exercise outcome is inherited.

## Content writing

Select the `content` capability using [the content workflow](CONTENT-WORKFLOW.md). It connects brand language, website/SEO, UX writing, campaigns and editorial content to the existing lifecycle and packs. Reuse accepted foundations and load only the relevant writing guide; no new visual pack or installed runtime is required.

For CAMPAIGN presentations and collateral, select the [deck and collateral guide](draft-skills/design-content-writing/references/decks-collateral.md) within `content`. Determine investor, sales, partnership or internal purpose, then hand off stable slide/page IDs, exact copy, evidence, notes and visual requirements to production.


## Creative exploration and visual-language continuity

Version-Timestamp: 2026-09-09 10:32:33 AST

During Establish direction and Explore, select [creative direction](CREATIVE-DIRECTION.md) when identity or supporting elements are unresolved. Reuse accepted direction for narrow work. Boards and family specifications are conditional deliverables that feed the existing identity, UI, content and production stages.


## Context and creative continuity

Version-Timestamp: 2026-09-09 10:35:51 AST

Before a selected stage, apply [AI context readiness](AI-DESIGN-CONTEXT.md) within the existing packet. For continuity evidence, select relevant cases from [the controlled exercise](templates/creative-continuity-exercise.md).


## Conditional craft selection

Version-Timestamp: 2026-09-16 18:05:00 AST

Apply [the compact craft selection](CRAFT-SELECTION.md) before new composition or visible revision. Record selected, reused or not-applicable decisions in the current stage packet. This makes specialist depth explicit without redoing accepted foundations.
