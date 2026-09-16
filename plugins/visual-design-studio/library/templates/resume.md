# Project resume record

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

`RESUME.md` is the canonical project state authority. It records the active objective, bounded scope, approved baseline, candidate state, decisions, sources, checks actually run, blockers and the exact next action. Replace the timestamp when this becomes a project record.

`CURRENT.md` is a legacy pointer only. If a project retains it for compatibility, it must name `RESUME.md`, state that it does not override it, and contain no competing state.

## Active work

- Objective and intended recipient:
- Scope and exclusions:
- Project root and read-only library root:
- Approved baseline: path, version or hash, approver and evidence. Use `none` with reason when no baseline exists.
- Active candidate: path, version or hash and status (`draft`, `under review`, `rejected`, `accepted`).

## Decisions and evidence

- Decision IDs and authoritative records:
- Sources and confidence limits:
- Actual checks and evidence paths:
- Open blockers and owner:

## Recovery

- Exact next action and required input:
- If interrupted, inspect the approved baseline and candidate before repeating work.
- A rejected revision cannot replace the approved baseline. Keep it identifiable for comparison, record the rejection evidence, and resume from the approved baseline unless new authority selects another candidate.
