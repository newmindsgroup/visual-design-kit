---
name: design-web-accounts
description: Membership and account websites for scoped website projects and revisions.
---

# Membership and account websites

Version-Timestamp: 2026-09-12T11:35:16-04:00

## Inputs and scope

Read the [website workflow](../../WEBSITE-WORKFLOW.md). Reuse accepted `web-forms` inputs and the relevant [website work sections](../../templates/website-work.md). Record intended outcome, audience evidence, exact source versions, platform constraints and allowed change. Dependencies express information needs, not a compulsory restart of approved work.

## Method

Specify registration, sign-in, recovery, entitlement and session states. Enforce permissions at the server; hiding UI is insufficient. Avoid account enumeration in public messages. Use verified authentication components and define recovery without weakening identity checks.

## Deliverable

Account journeys, permission matrix and security test scope. Attach to the existing design-work record with stable page/component/content IDs. Hand off actual file paths, candidate status, assumptions, unexecuted checks and next owner. Proposed filenames are not produced files. Missing tools hold dependent execution only.

## Acceptance

Test unauthorized access and session expiry in isolation; no real account mutations implied. Preserve prior approved work. A specification, sample or simulated interaction is not proof of production behavior. Use [acceptance scenarios](../../examples/website-workflow/README.md) and project-specific checks; no external changes or installation are implied.

Complete the [stage handoff](../design-stage-handoff/SKILL.md) with actual files, version, checks, unknowns and next owner.
