---
name: design-project-start
description: >-
  Start, resume or hand off a client brand or design project with continuity records: pinned kit version, selected
  capabilities, decisions, approvals and RESUME.md, for existing-brand or new-brand work in a separate project folder.
  Use when opening a client project, resuming across sessions, recording approvals or preparing a handoff. To choose
  a design direction use design-director; for craft use the discipline skills.
license: MIT
metadata:
  version-timestamp: "2026-10-20 02:05:00 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 02:05:00 UTC"
---

Version-Timestamp: 2026-10-20 02:05:00 UTC (0.5.0 routing); 2026-09-27 14:19:56 AST (continuity contract)

## Where the design work happens (0.5.0)

This skill owns project continuity: records, pins, approvals, resume and handoff. The design itself happens in the registered skills, which carry concrete defaults and do not require these records to run:

- `design-director` turns the brief into scored, rendered directions using the [Design Space Atlas](../../library/atlas/README.md).
- Discipline skills: `brand-identity`, `typography`, `color`, `layout`, `imagery`, `motion`, `ux-design`, `ui-design`, `web-design`, `native-app-design`, `design-system`, `data-visualization`, `print-packaging-social`.
- `design-critique` renders, screenshots, scores and revises every visible deliverable.

Use the records below for client projects that need traceable approvals across sessions. For a quick exploration or a one-off asset, skip them and say so. Each registered skill lists the catalog IDs it covers, so `SELECTED-CAPABILITIES.json` can still record selections against [the catalog](../../library/capabilities.json).

## Role and objective
Coordinate a scoped brand/design project through evidence, selected instructions, actual deliverables and review. Read [current readiness](../../READINESS.md) first, then [project launch](../../PROJECT-LAUNCH.md). All relative paths resolve from this skill file, never the current working directory.

## Context and requirements
The library root is ../../library relative to this file. It is read-only. Use the adopting project's instructions and authorized output folder. Never put brand assets or project outputs in the plugin. Verify the pinned payload checksums before executing bundled scripts. Read [usage](../../library/USAGE.md) and [contracts](../../library/CAPABILITY-CONTRACTS.md). For Google Vids marketing, sales, brand or product video requests, select `google-vids` and read [its native video workflow](../../library/draft-skills/design-google-vids/SKILL.md). Look up exact capability IDs and entry paths in [the catalog](../../library/capabilities.json); read selected entries explicitly. Do not expect nested reference skills to be registered commands. Select prerequisites as input contracts, not mandatory repeated work. Check actual tools and authority for the next operation.

For a new project record, use the bundled `scripts/adopt_template.py` from its absolute library location. Dry-run is the default; use `--apply` only after confirming the project root and a new relative destination. It pins instruction links to the installed library and leaves project placeholders for the adopting project to fill. Use project-root `RESUME.md` as the canonical continuity record. A retained `CURRENT.md` may only point to it.

Start with packaged instructions, task-relevant original [method cards](../../library/knowledge/README.md), and authorized project inputs. Books are optional source evidence, not model training or a prerequisite for ordinary design. Do not claim the package synthesizes every book or that a ready library has been consulted.

Use the verified packaged `library/scripts/reference_library.py` helper. For auto selection, run `python3 TOOL status --mode auto --config /absolute/project/private/reference-library.local.json`, substituting the actual adopting project path. Bare `status --mode auto` is only equivalent when the command runs from that project root; it must not look for the project configuration relative to this skill or the kit checkout. The ignored config contains `reference_library_root`. Explicit `--mode standalone` skips config and corpus access, including stale configuration. `auto` selects standalone when no usable library is available; explicit `local-library` also falls back with a reason. Run `python3 TOOL --root ROOT verify` before `python3 TOOL --root ROOT search QUERY --limit 5` when using sources. Follow [project launch](../../PROJECT-LAUNCH.md) for setup and failure handling.

Record requested/effective mode, fallback reason and only actual inspected source IDs in the existing project records. Standalone records no consulted book sources. Do not invent reference records to satisfy a source schema. If a task requires source evidence, `status --require-source` holds unavailable source-dependent work; it does not prove a specific source exists or was read. Continue independent work with supported inputs. Preserve integrity failures as failures and stop bundled-code execution for a package pin failure. Never copy books into the plugin or project.

Existing brand: inventory authoritative guidelines, approved assets, market evidence and constraints; distinguish supplied rules from inferred rules; preserve locked marks and copy. Missing guidelines may support clearly provisional exploration, never fabricated official standards.
New brand: establish audience, offer, differentiation and naming status before identity concepts. Existing accepted strategy can be reused. Do not invent research, personas, legal clearance or approvals. Limit exploration to the agreed deliverable and develop distinct supported directions when needed.

## Outputs and evaluation
Follow [project launch](../../PROJECT-LAUNCH.md) for project-owned records. Produce the requested artifacts, inspect them, record actual checks, and retain failures. Technical passes do not establish visual approval. Preserve baseline versions and unresolved decisions at each handoff. At a meaningful failure or learning milestone, use [feedback](../../FEEDBACK.md); do not auto-edit the shared library. Provider use, spending, sharing and client approval remain scoped to explicit authority. Never transfer approval between projects.

## Astro and website motion

Version-Timestamp: 2026-10-14 11:13:07 AST

For explicitly selected Astro builds use catalog ID `web-astro`. For website effects, transitions, scroll and original component specimens use `web-motion-library` alongside accepted `motion`/`web-frontend` inputs. Read [the motion library](../../library/MOTION-LIBRARY.md) selectively. Copy source examples to the adopting project before installation/build; do not write into the installed kit.
