---
name: design-web-migration
description: Website redesign and migration for scoped website projects and revisions.
---

# Website redesign and migration

Version-Timestamp: 2026-09-12T11:35:16-04:00

## Inputs and scope

Read the [website workflow](../../WEBSITE-WORKFLOW.md). Reuse accepted `web-audit` inputs and the relevant [website work sections](../../templates/website-work.md). Record intended outcome, audience evidence, exact source versions, platform constraints and allowed change. Dependencies express information needs, not a compulsory restart of approved work.

## Method

Inventory known URLs, content, inbound destinations and integrations. Propose retain, improve, merge or retire per item. Map redirects individually and detect chains or loops. Keep old content recoverable. Do not change domains, DNS or live routes from planning authority.

## Deliverable

Migration map, dependency inventory and cutover/recovery plan. Attach to the existing design-work record with stable page/component/content IDs. Hand off actual file paths, candidate status, assumptions, unexecuted checks and next owner. Proposed filenames are not produced files. Missing tools hold dependent execution only.

## Acceptance

Validate target pages, retained journeys and redirect behavior in staging before launch. Preserve prior approved work. A specification, sample or simulated interaction is not proof of production behavior. Use [acceptance scenarios](../../examples/website-workflow/README.md) and project-specific checks; no external changes or installation are implied.

Complete the [stage handoff](../design-stage-handoff/SKILL.md) with actual files, version, checks, unknowns and next owner.
