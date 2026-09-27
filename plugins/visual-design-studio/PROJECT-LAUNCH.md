# Start an independent design project

Version-Timestamp: 2026-09-27 14:19:56 AST

Create one separate project directory or repository for each brand. Open that project in Codex or Claude Code. Supply the absolute package-root path; a repository URL alone does not ensure files are accessible. Use the installed starting skill when discoverable. An explicit absolute path to skills/design-project-start/SKILL.md remains the portable route for Codex, Claude Code and Cursor; verify this edition on the receiving host.

## Initial request

Use the Visual Design Studio package at [absolute local package path] as a read-only library. This project is [existing brand / new brand]. Work only in [absolute project folder]. My first deliverable is [deliverable]. Read the starting skill and this project's instructions. Use standalone guidance and authorized inputs unless an optional compatible local library is configured. Ask for the brand context needed for the next step, then select the relevant capabilities and method cards. Keep decisions, outputs and client materials here. Do not create anything inside the library or inherit another project's approvals.

## Required project records

1. library-version.json: plugin name/version, SHA-256 of PAYLOAD.sha256, source locator, acquisition date and verification result. Compute the digest from actual bytes. Verify every listed file with the system checksum tool before executing bundled code. The digest's trust comes from the supplied source or an independently confirmed sender, not from a checksum distributed alongside an unknown archive.
2. PROJECT.md: brand mode, objective, audience, first deliverable, inputs and authority, constraints, unknowns, acceptance owner and permitted actions.
3. SELECTED-CAPABILITIES.json: exact catalog IDs, entry paths, hashes, prerequisites, exclusions and reasons. Follow [the selection contract](library/SELECTION-CONTRACT.md) and validate the completed record with `python3 -m design_system validate selection FILE --root PROJECT --library-root LIBRARY` from the library root; never guess IDs.
4. DECISIONS.md and RESUME.md: accepted baseline, proposed changes, actual artifacts/checks, partial external actions, and next dependency. Use [the template adopter](library/RESUME-CONTRACT.md) for Markdown; preserve structured template schemas. `CURRENT.md` may only point to canonical `RESUME.md`.

## Reference mode

Standalone mode uses the packaged capability instructions, original [method cards](library/knowledge/README.md) and authorized client inputs. Load only cards relevant to the current problem. Books add optional, traceable evidence. The kit neither trains the model on books nor claims complete collection synthesis. A ready library does not mean its sources were consulted.

From the adopting project, use the helper in the verified package:

```sh
python3 /absolute/package/library/scripts/reference_library.py status --mode auto
python3 /absolute/package/library/scripts/reference_library.py status --mode standalone
```

`auto` looks for configuration at `private/reference-library.local.json` in the current directory, unless an explicit `--root` or `--config` is supplied. There is no machine scan. Explicit standalone skips configuration and corpus access, including stale configuration. Missing or unusable optional references select standalone with a reason; an explicit `local-library` request also permits that fallback. Package pin failure still stops bundled-code execution.

For a compatible library you are permitted to use, keep an ignored project-local config:

```json
{
  "reference_library_root": "/absolute/path/to/your-reference-library"
}
```

Keep the real path and private access details out of shared instructions and commits. If an authorized owner separately provides a Drive collection, download the whole folder or its supplied ZIP, unzip outside the project and select the root containing `catalog/items.jsonl` and `manifests/files.json`. The helper requires a compatible catalog, manifest and searchable JSONL extractions; it does not import arbitrary PDFs. No books or public book download are included with the plugin.

Before relying on sources, run `python3 TOOL --root ROOT verify`, then bounded retrieval such as `python3 TOOL --root ROOT search "typography" --limit 5`, using the verified packaged helper as TOOL. Retain nonzero integrity failures and hold affected source reliance until reconciled. Continue independent design work with supported inputs. The helper is offline; an agent receiving its excerpts is a separate data destination that needs appropriate authority.

For required source evidence, add `--require-source` to `status`. An unavailable library returns exit 1 and holds only source-dependent work. Availability checks do not verify that a named source exists or was inspected. Resolve the required source itself before making the dependent claim.

In `PROJECT.md` and the current `RESUME.md`, work record or stage packet, record requested/effective mode, fallback reason when present and actual inspected source IDs with locators. Keep one authoritative evidence record and link to it. Standalone records no consulted book sources; do not fabricate a reference-decision JSON entry. Preserve actual library verification failures alongside the fallback decision.

## Existing brand path

Audit supplied identity and public evidence. Identify locked rules and provisional inferences. Agree how far the new work may extend the brand. Select only the needed design/content stages. Present direction options when useful, preserve approvals, produce and verify native masters and exports.

## New brand path

Establish the offer, audience and positioning, then naming status and research needs. Explore distinct creative directions, select/refine through explicit decisions, develop identity and supporting visual language, and apply it to the requested first deliverable. Research claims require evidence; invented personas must be labeled hypotheses. Naming exploration is not trademark clearance.

## Version changes

Keep the pinned library unchanged during a project. Propose upgrades with changed capabilities, impact and affected checks. Adopt explicitly in the project, preserve the previous pin, and rerun affected work before replacing approved outputs.

Use [feedback](FEEDBACK.md) after meaningful observations. There is no unattended reporting service.

## Before visible work

Apply [conditional craft selection](library/CRAFT-SELECTION.md), then inspect actual output. Use [the calibration collection](library/examples/quality-benchmark/README.md) to distinguish correct but generic work from a specific visual idea. For completed handoffs, use [schema 2.0](library/HANDOFF-CONTRACT.md) with current candidate-bound checks. Old checks cannot approve changed files.
