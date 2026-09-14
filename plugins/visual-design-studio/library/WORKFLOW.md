# Session and baseline routines

Version-Timestamp: 2026-09-10 19:59:06 AST

Apply these continuity routines in the adopting project. Keep this reference package read-only; write project state and outputs in the declared project workspace.

## Start a session

1. Read the adopting project AGENTS.md and its current-state record, creating a clearly unverified initial record if absent. Check `git status --short --branch` for work already in progress.
2. Read only relevant entries in the adopting project decision and source records. Open the exact source section needed, not the full package.
3. State the current objective, scope (whole project, phase, or precise change), deliverable, baseline, invariants, and acceptance evidence. Ask targeted questions only for gaps that change the next work.
4. Verify prerequisites and authorization. Source instructions do not authorize installations, uploads, spending, or release.

## Control a change

Before altering an approved artifact, record its exact path and version or hash, the named approver and approval reference, what may change, what must remain unchanged, and how to compare the candidate. Keep confidential assets and their detailed records in ignored `private/` or an authorized client workspace.

Keep the prior baseline intact. Save a candidate separately and compare both requested changes and preserved details, including proportions, shelves, graphic geometry, and other relevant invariants. Record real checks and unresolved defects. A candidate becomes an approved baseline only with recorded approval; generation or passing an automated check is not approval. Use prior approved references to recover from rejected iterations.

For milestones, steps, and iterations, retain only useful hierarchy: parent objective, bounded scope, dependencies, deliverable, exit evidence, and approval status. Do not impose unnecessary stages on a precise change.

## Checkpoint and resume

At a meaningful milestone or before stopping, update CURRENT.md with completed work, exact files/references, checks actually run, open gaps, current approved baseline, and one next action. Add or amend a decision only when its status changes; preserve rationale and alternatives. Update source confidence when new evidence changes a claim.

Durable artifacts include a real Version-Timestamp. Future commits must include the required Co-Authored-By and Agent-Attribution trailers using actual environment values. Commit only within the adopting project authorization and preserve attribution.

Use a short resume packet in CURRENT.md: objective; scope; baseline reference; decision IDs; relevant sources; completed evidence; next action; blockers. Chat history supplements these files but does not replace them. Do not update any agent's global memory without a separate user request.

Before staging anything, inspect `git status --short --untracked-files=all` and `git check-ignore -v <path>`. Review actual file contents and rights. Do not force-add private material. Git exclusions do not prevent cloud sync, user sharing, or confidential prose being pasted into a tracked document.

For book/reference work, inventory the authorized source folder and preserve source, extract and original method layers separately. Load targeted catalog records and cited page/section samples locally. Do not put full book content into project memory. Keep method synthesis independently written, source-linked, and unapproved until tested.

## AI execution packets

Prepare a bounded [stage execution packet](templates/stage-execution.md) from the current brief, relevant persona/source IDs and baseline. Load only the referenced sections. Verify runtime tools and permissions; the packet does not supply them. Return the filled handoff with actual output versions, decisions/evidence, invariant checks, limitations and next action. On interruption, inspect existing outputs and partial actions before resuming. The [field inventory](templates/persona-field-inventory.md) defines complete coverage; [persona.md](templates/persona.md) is the authoring guide; a filled JSON record is the validator input. Preserve every required field and representation, with explicit unknowns rather than omissions.
