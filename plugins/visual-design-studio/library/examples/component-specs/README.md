# Four filled component specification examples

Version-Timestamp: 2026-09-10 20:28:53 AST

These are completed generic teaching documents. They show the detail an AI should produce after selecting an inventory item. They are not approved project specifications, a UI library or tested components. The 193-entry neutral master is unchanged. No client, product or fictional end-to-end project is represented.

| Exact inventory item | Filled example | What it teaches |
| --- | --- | --- |
| C-001 Button, action family | [Button](button.md) | One action, distinct focus/busy/unavailable behavior and duplicate prevention |
| C-005 Text field, input family | [Text field](text-field.md) | Validation timing, preserved input and unresolved domain constraints |
| C-051 Dialog, overlay family | [Modal dialog](dialog.md) | Modality, focus lifecycle and a native-sheet decision boundary |
| C-038 Data table, data family | [Data table](data-table.md) | Semantic relationships, data states and an alternate narrow/native representation |

Each item owns its anatomy, variant/state IDs and expected behavior. [WORK-EX-01](work-record.md) owns criterion IDs, test methods, decisions and approval boundaries. [Specimen records](specimens.md) refer to them without repeating requirements. [sources.json](sources.json) is the machine-readable authority for this set's precise source locators and verification limits; it extends references to the existing inventory source IDs rather than replacing that register. Historical source-document checks are not bundled and confer no passed status on this package.

## Start with proportional instructions

Use the [selection guide](selection-guide.md) before copying an example. Each item now separates core from conditional task behavior. A simple button does not inherit reconciliation or a status service. Applicable accessibility and recovery requirements remain mandatory.

## How Codex or Claude should use an example

1. Read the real brief and existing work record first. Select the exact item and [family contract](../../inventory/families.md), then one relevant example. Do not load all examples for a one-button change.
2. Use its selection table to record selected, omitted and held sections plus criterion branches. Treat the example's explicit teaching choices as candidates. Get action meaning, allowed data, users, platform/version, languages, token authority, permissions, failure/retry policy and supported test matrix from the brief or existing approved sources. Ask the named owner for missing decisions that affect behavior.
3. Create a project-specific item record using [system-item.md](../../templates/system-item.md) and the existing [work record](../../templates/design-work.md). Assign project IDs and preserve a mapping back to these example IDs. Copy only relevant requirements. Explain excluded states and platform differences.
4. Record conflicts as unresolved decisions with an owner, consequence and next step. Do not silently guess a backend limit, legal action, focus destination, breakpoint or native presentation. Generic examples remain complete as teaching material even where project adoption is held.
5. Link the approved baseline and allowed changes through the existing [reference contract](../../REFERENCE-CONTRACT.md) and [handoff controls](../../CAPABILITY-CONTRACTS.md). Neither this guide nor a filled spec approves a candidate or authorizes execution.
6. If implementation is separately requested, select its stack, build the exact approved variants, execute the linked tests in the chosen environment and record actual evidence. Update the production manifest and shared handoff for real outputs. Do not count repository tests as component tests.

A useful instruction is: “Using C-005 and TF-EX-01 as a method example, draft the selected field's project specification against the approved brief. Preserve baseline tokens. Report missing data limits and validation authority as unresolved. Do not implement until the work record's prerequisites and authorized scope permit it.” This is a prompt example, not an instruction to start a project now.

## Built, checked and pending

**Written:** four filled web-oriented examples, explicit native adaptation boundaries, shared reproducible acceptance procedures and four honest specimen records with no rendered artifact.

**Checks to record:** source locators, inventory names/families and document consistency. Record actual package checks separately from implementation tests. No source-review approval or component test result is inherited.

**Pending for any real use:** project decisions and approval, exact browser/OS/assistive-technology versions, token values, implementation, screenshots, measured accessibility, user findings and component test results. No such evidence is fabricated here. Passive display, print and shared public touch installations are excluded because their use, privacy and physical constraints need different briefs.

Start with the example closest to the next real task. There is no need to complete all 193 specifications before using this system.
