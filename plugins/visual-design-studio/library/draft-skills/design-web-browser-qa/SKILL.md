---
name: design-web-browser-qa
description: Cross-browser website QA for scoped website projects and revisions.
---

# Cross-browser website QA

Version-Timestamp: 2026-09-12T11:35:16-04:00

## Inputs and scope

Read the [website workflow](../../WEBSITE-WORKFLOW.md). Reuse accepted `prototype` inputs and the relevant [website work sections](../../templates/website-work.md). Record intended outcome, audience evidence, exact source versions, platform constraints and allowed change. Dependencies express information needs, not a compulsory restart of approved work.

## Method

Select agreed browsers, devices and critical journeys. Cover intermediate widths, keyboard/touch, zoom, slow loading and failed media. Capture reproducible defects and exact environment evidence. Preserve negative cases and retest only affected scope after fixes.

## Deliverable

Browser matrix, runnable checks and defect log. Attach to the existing design-work record with stable page/component/content IDs. Hand off actual file paths, candidate status, assumptions, unexecuted checks and next owner. Proposed filenames are not produced files. Missing tools hold dependent execution only.

## Acceptance

Emulation does not certify every physical device; mark unsampled combinations pending. Preserve prior approved work. A specification, sample or simulated interaction is not proof of production behavior. Use [acceptance scenarios](../../examples/website-workflow/README.md) and project-specific checks; no external changes or installation are implied.

Complete the [stage handoff](../design-stage-handoff/SKILL.md) with actual files, version, checks, unknowns and next owner.
