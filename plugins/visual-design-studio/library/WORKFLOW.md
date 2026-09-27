# Session and baseline routines

Version-Timestamp: 2026-09-27 14:19:56 AST

Apply these continuity routines in the adopting project. Keep this reference package read-only; write project state and outputs in the declared project workspace.

## Start a session

1. Read the adopting project AGENTS.md and its current-state record, creating a clearly unverified initial record if absent. Check `git status --short --branch` for work already in progress.
2. Read only relevant entries in the adopting project decision and source records. Open the exact source section needed, not the full package.
3. State the current objective, scope (whole project, phase, or precise change), deliverable, baseline, invariants, and acceptance evidence. Ask targeted questions only for gaps that change the next work.
4. Verify prerequisites and authorization. Source instructions do not authorize installations, uploads, spending, or release. Load only task-relevant original [method cards](knowledge/README.md) alongside the selected capability.
5. Select standalone or optional local-library mode using the verified helper's `status --mode auto`, or explicit `--mode standalone` to skip all local config and corpus checks. Record the effective mode and fallback reason in the existing work record. Missing optional books do not block ordinary design work. Package pin failure still stops bundled-code execution.

## Control a change

Before altering an approved artifact, record its exact path and version or hash, the named approver and approval reference, what may change, what must remain unchanged, and how to compare the candidate. Keep confidential assets and their detailed records in ignored `private/` or an authorized client workspace.

Keep the prior baseline intact. Save a candidate separately and compare both requested changes and preserved details, including proportions, shelves, graphic geometry, and other relevant invariants. Record real checks and unresolved defects. A candidate becomes an approved baseline only with recorded approval; generation or passing an automated check is not approval. Use prior approved references to recover from rejected iterations.

For milestones, steps, and iterations, retain only useful hierarchy: parent objective, bounded scope, dependencies, deliverable, exit evidence, and approval status. Do not impose unnecessary stages on a precise change.

## Checkpoint and resume

Use project-root `RESUME.md` as the canonical state authority. Adopt [the resume record](templates/resume.md) with the template adopter when needed. At a meaningful milestone or before stopping, update it with completed work, exact files/references, checks actually run, open gaps, current approved baseline, active candidate and one next action. A rejected revision remains a comparison record and cannot promote itself to the approved baseline. `CURRENT.md` is a legacy pointer only: it may point to `RESUME.md`, but it cannot carry competing state. Add or amend a decision only when its status changes; preserve rationale and alternatives. Update source confidence when new evidence changes a claim.

Durable artifacts include a real Version-Timestamp. Future commits must include the required Co-Authored-By and Agent-Attribution trailers using actual environment values. Commit only within the adopting project authorization and preserve attribution.

Use a short resume packet in `RESUME.md`: objective; scope; baseline reference; candidate status; decision IDs; relevant sources; completed evidence; next action; blockers. Chat history supplements these files but does not replace them. Do not update any agent's global memory without a separate user request.

## Adopt a portable template

Copy a selected Markdown template into an independent project only through the packaged adopter. It defaults to a dry run, requires `--apply` to write, refuses an existing destination, and rejects parent traversal or symlink escape. It keeps project placeholders unchanged and rewrites bundled instruction links to the installed library's absolute pinned files.

```sh
python3 /absolute/path/to/library/scripts/adopt_template.py stage-execution.md \
  --project-root /absolute/path/to/project \
  --destination records/stage-execution.md
python3 /absolute/path/to/library/scripts/adopt_template.py stage-execution.md \
  --project-root /absolute/path/to/project \
  --destination records/stage-execution.md --apply
```

Do not copy the whole library into the project. The output record belongs to the project. The library remains read-only.

Before staging anything, inspect `git status --short --untracked-files=all` and `git check-ignore -v <path>`. Review actual file contents and rights. Do not force-add private material. Git exclusions do not prevent cloud sync, user sharing, or confidential prose being pasted into a tracked document.

## Optional source evidence

Standalone work uses packaged guidance, original method cards and authorized project inputs. Optional books provide deeper evidence for selected decisions; they are not model training or proof of complete collection synthesis. Resolve only an explicit root or the adopting project's ignored `private/reference-library.local.json`; there is no machine scan. Invoke the verified `library/scripts/reference_library.py` helper, using an absolute tool path from the adopting project. See [project launch](../PROJECT-LAUNCH.md) for configuration and commands.

Run `status --mode auto` or the requested mode. Explicit standalone bypasses stale configuration and corpus access. An unavailable optional library falls back to standalone with a reason, including when local-library mode was requested. If source evidence is required, `status --require-source` returns a dependent hold when unavailable. Confirm the required source itself and inspect it before making the claim. Continue independent authorized work.

Before local-source reliance, run `--root PATH verify`, then `--root PATH search QUERY --limit 5`. Preserve nonzero integrity failures in the work record and hold affected sources until reconciled. Fallback never converts a failed verification into a pass. Separate source, extraction and original method layers. Inspect bounded passages and original pages when visual evidence matters. Keep full book content out of project memory and never place books in the plugin or project.

Record requested/effective mode, fallback reason, and only source IDs and locators actually inspected in `PROJECT.md`, `RESUME.md`, the design-work record or stage packet. Link to one authoritative record. A ready library or catalog match is not consultation. Standalone records no consulted book sources and does not require an invented reference-decision JSON entry. Reassess source availability when a later task needs it; keep ordinary artifact, host/runtime and generation checks separate.

## AI execution packets

Prepare a bounded [stage execution packet](templates/stage-execution.md) from the current brief, relevant persona/source IDs and baseline. Load only the referenced sections. Verify runtime tools and permissions; the packet does not supply them. Return the filled handoff with actual output versions, decisions/evidence, invariant checks, limitations and next action. On interruption, inspect existing outputs and partial actions before resuming. The [field inventory](templates/persona-field-inventory.md) defines complete coverage; [persona.md](templates/persona.md) is the authoring guide; a filled JSON record is the validator input. Preserve every required field and representation, with explicit unknowns rather than omissions.
