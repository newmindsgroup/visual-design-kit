---
name: design-touchscreen-design
description: Design shared public touchscreen journeys, attraction states and session recovery.
---

# Touchscreen design

Version-Timestamp: 2026-09-12T11:35:16-04:00

Status: authored project-local instructions; not installed or production-certified.

## Inputs

Read the relevant [display workflow](../../DISPLAY-WORKFLOW.md) and reuse accepted inputs from the [display brief](../../templates/display-design-brief.md). Dependencies identify information needed, not mandatory repetition of approved work. Preserve baseline locks for precise changes.

## Method

Use actual audience/task evidence and existing UX/UI methods. Map attract/idle, entry, active task, confirmation, error, help and exit states. Include visible home/back/cancel, immediate input feedback and alternatives to hidden gestures or hover. Size/spacing and reachable controls must be verified on intended hardware for seated and standing users; do not infer physical accessibility from CSS pixels.

Record inactivity warning, extension, timeout/reset and whether pending operations finish, cancel or remain uncertain. Clear personal data, search history and on-screen identifiers according to the session requirements. On lost network or uncertain transaction result, reconcile status rather than repeat an order/payment. Provide staff/help fallback without exposing prior-user data.

Keep attract-mode animation from interrupting active use. Specify language choice, keyboard/input alternatives and assistive technology needs according to deployment scope. Sensors, cameras, identity and payment require explicit privacy/access requirements and separate authorized integration, not an implied smart-display default.

## Output and acceptance

State/flow map, annotated screens, interaction prototype specification and privacy/recovery cases. Prototype evidence is separate from device, assistive technology and real-transaction acceptance.

Carry actual files, source versions, assumptions and remaining checks through the existing [stage handoff](../design-stage-handoff/SKILL.md).

## Physical access discovery

Identify applicable local accessibility requirements with the deployment owner and record which specialist checks remain. Consider tactile/audio or peripheral alternatives when needed, gloved or imprecise input and seated viewing angle. Do not assume every device supplies these controls or label the installation compliant from a browser test.

## Canonical session owner

This capability owns the project state table, state IDs, event ownership and inactivity schedule. Touch states/copy and touch media extend that same versioned table; neither creates a competing schedule. Preserve its path/hash in the handoff. State lists in skills are coverage prompts, not mandatory independent state machines.
