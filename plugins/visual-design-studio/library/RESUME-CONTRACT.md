# Resume continuity contract

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

Project-root `RESUME.md` is the sole canonical state record for continuity. It must identify the objective, bounded scope, approved baseline, active candidate and status, actual checks, unresolved blockers, and one exact next action. Use the packaged [resume template](templates/resume.md) through [template adoption](scripts/adopt_template.py).

`CURRENT.md` is a compatibility pointer only. If retained, it must identify `RESUME.md` as canonical and must not add state, approval, baseline, candidate or next-action claims that differ from it.

An approved baseline requires its path, version or hash, approver and approval evidence. A candidate requires a path, version or hash and a distinct status. A rejected candidate remains available for comparison and its rejection evidence is retained, but it cannot become the approved baseline without a new recorded approval. On resumption, inspect the canonical record and named files before repeating an action.

This contract records project state. It does not authorize a release, external action, replacement of a project pin, or modification of the read-only library.
