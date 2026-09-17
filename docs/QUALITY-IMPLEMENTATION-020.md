# Quality improvement implementation

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

User authorization: implement all recommendations in the September 16 audit. Baseline 319b555. The working source becomes a new 0.2.0 candidate; preserve installed 0.1.0 and baseline provenance. No new client data, book uploads, additional paid provider jobs, PowerPoint work or backup setup.

## Outcome and order

1. G01: current-result handoff reconciliation, candidate-version binding, explicit historical checks, meaningful regression tests.
2. G02: selection record schema/validator with exact IDs, patterns, file hashes, exclusions and prerequisite dispositions.
3. G03/G04/G09: canonical RESUME.md, portable template adoption, correct wrapper status, optional configured local-reference workflow and fresh-host checks.
4. G06/G07/G08: conditional craft selection, positive-quality comparative critique, real-font wrap/accessibility cases.
5. G05/G10/G11: one shared fictional example set, two contrasting brand applications, generic/correct and attractive/wrong controls, precise revisions and resumed work, one directed motion sequence with editable source and full review.
6. Package new bytes, verify hashes/links/tests, security and independent Claude review, publish draft/release appropriate to actual evidence and migrate installation only after relevant checks. Human aesthetic acceptance and real hardware remain distinct.

## Implementation boundary

Use the curated GitHub checkout as source for this edition. Do not edit the installed cache or original research workspace. Existing v0.1.0 is recoverable from its pinned commit and hash manifest. New packaging records this source mapping explicitly. Additive optional book integration retains original books outside plugin/GitHub. The reference utility is packaged from one canonical source with a byte-equality check, not maintained as divergent copies.

## Work allocation and method

Handoff worker owns validation.py, handoff templates/contract and focused tests. Selection worker owns selection.py, selection schema/template, CLI integration and focused tests. Adoption worker owns template adopter and continuity/startup/reference instructions plus focused tests. Coordinator owns integration, packaging, visual examples, craft refinements, browser/export checks and progress. Workers are not alone; do not revert others.

TDD for deterministic behavior, defect reproduction before repairs, frontend-design for actual examples, prompt-engineering-expert for rewritten agent instructions, engineering quality gate plus security review and actual visual review. Model-governor recommends Terra Medium for bounded implementation and current coordinator for integration; Ultra was requested for the preceding audit, not silently imposed on all coding.

## Acceptance

Each gap links actual changed files, tests/artifacts, limitations and next consumer. No passing checksum is visual approval. No fabricated approvals. Capture failures and repair evidence. Agent review, human preference, host startup and device acceptance remain separate. Do not change a project pin without explicit adoption; user authorized the local kit update after checks.

## Current status

Approach reviewed independently by Claude Fable 5.1. Corrections below accepted before implementation.


## Frozen integration contract and review disposition

Version-Timestamp: 2026-09-16 17:53:00 AST

The numbered order is integration precedence, not a prohibition on independent implementation. Selection and handoff are distinct artifacts. Selection uses the existing catalog planner and file-reference conventions; it does not import new handoff internals. Existing public validation API remains `validate(kind, data, root, as_of=None)`. SHA-256 is lowercase hexadecimal over exact file bytes. No packaging step normalizes capability bytes after selection generation. Selection validation recomputes hashes and rejects drift; release examples are generated after final source edits.

Ownership, all on implementation/quality-020, with independent new test files:
- Handoff worker: `library/design_system/validation.py`, `library/templates/handoff-record.json`, `library/templates/handoff-actor-record.json`, `library/HANDOFF-CONTRACT.md`, `library/tests/test_handoff_current.py`. Existing tests can be read, not edited without coordination.
- Selection worker: `library/design_system/selection.py`, `library/design_system/__main__.py`, `library/templates/selected-capabilities.schema.json`, `library/templates/selected-capabilities.json`, `library/tests/test_selection.py`, `library/SELECTION-CONTRACT.md`. It reuses catalog_plan/file conventions after inspection; module split keeps a separate bounded contract and avoids concurrent changes to validation.py.
- Adoption worker: `library/scripts/adopt_template.py`, `library/tests/test_adopt_template.py`, `library/WORKFLOW.md`, `library/RESUME-CONTRACT.md`, wrapper `READINESS.md`, wrapper entry `skills/design-project-start/SKILL.md`, `library/draft-skills/design-reference-direction/references/reference-retrieval.md`. Root owns actual repo RESUME/progress records, PROJECT-LAUNCH, and all other craft instructions. Agent may create a template resume record.
- Coordinator: all other files, packaging, reference utility generated copy, tests under root tests, visual examples and evidence. Workers do not regenerate manifests, stage, commit, install or publish. Integration order: handoff, selection, adoption, craft/examples, package, review, installation/publication.

Compatibility: new handoff schema 2.0 has candidate-bound current checks. Old 1.0-proposed partial/draft records may remain readable with a migration warning, but cannot assert complete/ready under the new validator. No implicit conversion invents candidate bindings. Selection schema 1.0 is new and only exact supported versions pass. Existing 0.1.0 projects remain pinned and unchanged. Local installation adoption does not change project pins. The pre-implementation source 319b555 and installed baseline 412e628 are distinct; installed payload hash is dcca91274b676de49a0d4ee086aa7f4d6264c7ce8428cb259cdd0123c6683e4e. Verify the preserved cache and recovery from the pinned baseline before installation.

Only open-license fonts will be vendored, alongside licenses. Fictional example assets are generated or existing original fictional material, never client derivatives. Reference utility byte equality is verified after packaging against `tools/reference_library.py`. This approach review does not replace final independent review or human visual acceptance. Model labels in routing records describe actual runtime selection, not evidence of review independence.
