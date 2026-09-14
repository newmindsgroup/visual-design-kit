# Check and prepare a delivery

Version-Timestamp: 2026-09-10 19:58:10 AST

Use after the selected design/production stage and before handing over files. This extends the existing delivery skill, work record and manifest. It is a manual procedure, not a new validator, release approval or automatic sender. Apply only the requirements of the named deliverable and intended use.

## Run the loop

1. **Confirm the requested package.** Read the brief, selected requirements, audience disposition and accepted source/version. Name the recipient, intended use, editable master, required exports and acceptance methods. For a revision, confirm baseline, allowed delta and invariants. Unknown requirements hold only the dependent delivery claim. Reuse valid research and approvals; a review copy may have different acceptance requirements from a production file.
2. **Freeze the candidate identity.** Preserve the baseline and identify the exact candidate version. Record canonical masters, linked assets, fonts and export dependencies in the existing work record. Resolve relative references and permitted use. Do not copy font files, client sources or private evidence into a package merely because the source document uses them. Record authorized acquisition/reference instructions when redistribution is not permitted.
3. **Inspect the editable source.** Reopen the actual candidate in the intended application. Check required layers, text, masks, vectors, artboards, components, variables or timeline relationships. Record the app/version and what was observed. A flattened preview, filename, hash or successful parser run does not establish native editability. Missing app access leaves this check not run.
4. **Export and inspect the actual bytes.** Use the chosen source version and documented settings. Select and record an available format-appropriate decoder/viewer, then inspect actual file format, dimensions/units, profile, transparency, text/geometry, linked content and relevant medium constraints. If unavailable, hold that check. The existing manifest CLI does not perform this inspection; any decoder dependency must be discovered on the destination; no particular image library is required by this contract. Reopen exports in a suitable viewer/runtime. Compare the authorized delta and preserved areas. Check desktop/narrow and interaction states for web work, playback for motion, and intended hardware conditions for touch/display claims. Use TOOLCHAINS.md and the selected app reference for applicable checks.
5. **Reconcile the package.** Every required output is present or explicitly held. Every delivered file has a purpose and a current source relationship. Keep diagnostic/rejected exports outside the delivery candidate. Generate the existing manifest from actual files and hashes; run the existing validator. A current hash does not establish that the export came from the latest master. Verify the recorded source-to-export relationship and appearance separately.
6. **Fix and recheck only affected work.** Missing dependencies, wrong formats, stale exports and failed required criteria prevent the affected delivery claim. Preserve failed evidence. Correct the source or export, regenerate dependent outputs and hashes, and rerun relevant checks. Any change after review invalidates affected results until rechecked. Do not regenerate a manifest simply to conceal stale or incorrect files.
7. **Prepare the receiving handoff.** Use the existing stage packet and work-record Handoff section. Name actual outputs, versions, source ownership, instructions for editing/opening, dependencies, results, unresolved limits and next action. Carry known conversion and metadata differences into recipient instructions, including profile/rendering-intent changes where applicable; do not hide them solely in an internal check report. Separate candidate readiness from human approval and permission to send. Delivery preparation never sends, publishes or changes access. Proceed with an already authorized external action only within its exact scope and after its prerequisites are met.

## Record once in the existing work record

| Information | Authoritative location |
| --- | --- |
| Native master, exports, dimensions/profile/settings, environment, ownership and conversions | Production specification |
| Requirement, target, method and applicability | Criterion basis |
| Passed / failed / not run / not applicable, actual source/export version, evidence, reviewer/date, affected gap | Checks and limits |
| Baseline, authorized changes and preservation requirements | Change boundary |
| Files, local hashes, recorded allowed use and evidence references | Existing manifest JSON |
| Recipient instructions, remaining holds, release condition/owner, next action and refresh trigger | Handoff, summarized in stage-execution packet |

An exception is a documented decision by the authorized owner, not an automatic waiver of a required condition. An unperformed applicable check is not not-applicable. Existing approval does not cover a changed version by default. Approval for an internal concept does not establish production permission.

## App-specific checks

| Route | Select when relevant | Destination status |
| --- | --- | --- |
| Illustrator | Native AI reopen; editable text, vectors, artboards, links and fonts; PDF/SVG/PNG geometry, outlined versus live text and color | Not run until evidenced for the candidate |
| Photoshop | Native PSD reopen; layers, masks and embedded or linked content identity; replacement fit and clipping; export dimensions, transparency, ICC profile and rendering intent | Not run until evidenced for the candidate |
| Figma | Required native desktop reopen; frames, components, instances, variables and prototype relationships; export bytes and cloud design/version identity | Not run until evidenced for the candidate |
| Canva | Editable design/version and element preservation; included-operation and asset rights; real export and editor reopen; cloud source limitations disclosed | Not run until evidenced for the candidate |
| Code/web/app | Source revision, build, target runtime, interactions, accessibility and dependency checks | Not run until evidenced for the candidate |

Use [destination readiness](SOFTWARE-READINESS.md). Reopen a saved candidate before claiming editability. Preserve failed exports outside the delivery package. Export profile differences and loss of editable structure must be disclosed, not hidden by new hashes. Restart or crash recovery is a separate test from normal save/reopen.

At assembly, enumerate the approved payload list and compare it with every actual file in the destination folder. Reject undeclared files, symlinks and special files at this assembly boundary. The existing manifest validator may follow a safe in-root symlink and does not discover extra files, so a manifest pass alone is insufficient. Compare actual source/export identity and intended-use evidence separately.

## Commands and their limits

```sh
python3 -m design_system validate manifest /absolute/project/manifest.json --root /absolute/project
```

Run from the assembled package containing design_system, with actual paths. This verifies the implemented structure, local references/hashes and declared allowed-use fields. It does not discover missing brief requirements, prove legal rights, verify file encoding, establish native reopen or compare current master and export semantics. Do not edit the schema to turn a missing check into a passing result.

Use the relevant existing validator for an actual evidence or handoff record; use structured comparison only where the supported contract matches the data. Visual and intended-context checks remain separate. Record actual rejection and success cases with the delivery record. No historical fixture result is inherited. Every new delivery requires its applicable source and export checks.
