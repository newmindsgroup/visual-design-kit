---
name: design-ui-system
description: Specify or implement reusable interface components, tokens and responsive behavior for web, apps or touch interfaces.
---

# UI design system

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.149.1; timestamp=2026-09-08 22:17:00 AST

Project-local instruction draft. Manual selection does not install a tool or grant permissions.

## Inputs

Task flows, identity tokens, platform constraints, content examples, state inventory and implementation stack if selected. Reuse valid existing prerequisites; missing research may remain an explicit hypothesis when the named use permits it.

## Method

When a reference or reuse decision is needed, use [reference direction](../design-reference-direction/SKILL.md). Reuse an existing accepted decision; this optional route does not force a new research phase.

Map tokens to semantic roles rather than scattering raw styling values. Specify components with anatomy, content rules, variants, keyboard behavior and default/hover/focus/disabled/loading/empty/error/success states when applicable. Define responsive layout and content overflow rules. Include typography scaling, contrast, reduced motion and touch target criteria. Use realistic bounded sample content and long/translated/error cases. Reuse existing project components before adding alternatives. If implementing, inspect the actual stack and run project tests plus rendered desktop/mobile interaction checks. A component table alone does not establish a working UI.

## Output contract

Fill [design work](../../templates/design-work.md), selecting the sections relevant to this capability. Include: Semantic token file, component inventory/specification, layout rules, interaction state matrix, implementation references and check evidence. Refer to stable IDs and paths rather than pasting full research or personas.

## Acceptance

Tokens are consistent; user flows retain recovery; responsive and keyboard behavior have actual evidence when implemented; untested states remain pending. Apply [quality boundaries](../../QUALITY.md). Unsupported checks remain pending with an owner and next action. For a revision, load [stage handoff](../design-stage-handoff/SKILL.md) and compare only the authorized delta.

## Shared inventory

Use the [inventory](../../SYSTEM-INVENTORY.md) for relevant entry IDs, variants, state prompts and profile choices. Complete the [item specification](../../templates/system-item.md) only for selected scope. Keep existing reference decisions, work records, baselines and handoff contracts authoritative. An inventory entry is not an implemented or tested component.

## Example and evidence discipline

Document selected examples through the [specimen record](../../templates/specimen-record.md). Distinguish static, simulated and working examples; pair their visual, token, snippet and implementation versions. Describe composition slots and responsive transformations using existing entry IDs rather than adding decorative variants as new universal components.


## Type, color and motion decisions

Use [typography](../design-typography/SKILL.md), [color](../design-color-system/SKILL.md) and [motion](../design-motion-effects/SKILL.md) for selected unresolved decisions. Apply [craft review](../../DESIGN-CRAFT.md) to actual rendered work. These optional specializations do not force redesign of approved components.


## Focused craft methods

Read only the relevant method for the selected task; preserve existing prerequisites and canonical record ownership.

- [Composition across formats](../design-foundations/references/adaptive-composition.md): use when adaptive composition affects the requested output.
- [Localization and resilient content](../design-content-writing/references/localization.md): use when localization affects the requested output.


## Moving a design system between tools

For import/export or an actual adapter, use [system portability and token evidence](references/system-portability.md). Keep canonical values, approval and evidence distinct; runtime metadata is not automatically supported.

## Website specialization

Version-Timestamp: 2026-09-11T20:48:53-04:00

Select relevant [website methods](../../WEBSITE-WORKFLOW.md) for scoped website work. Reuse accepted foundation records and preserve this capability as their owner.

## Conditional craft selection

Version-Timestamp: 2026-09-16 18:05:00 AST

Apply [the compact craft selection](../../CRAFT-SELECTION.md) before new composition or visible revision. Record selected, reused or not-applicable decisions in the current stage packet. This makes specialist depth explicit without redoing accepted foundations.
