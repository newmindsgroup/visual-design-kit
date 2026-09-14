# Use the portable design library

Version-Timestamp: 2026-09-12T11:33:59-04:00

This is a manually selected instruction library with a standard-library Python validator. It is not an installed plugin, an autonomous agent service or proof of tool readiness. Keep the library separate from project outputs and client data.

## Start and select

Declare the read-only library root and project output root. Read the adopting project instructions and current state, then [capability contracts](CAPABILITY-CONTRACTS.md). Use [starter packs](PROJECT-STARTER-PACKS.md) for a whole project, or select only the relevant capability in [the catalog](capabilities.json). Existing valid prerequisites can be reused. Resolve conflicting or missing requirements only where they affect the next work.

From the package root, `python3 -m design_system plan ui` returns instruction dependency IDs. Read their entry files; the planner does not execute them, build personas or grant access. For bounded work, follow the audience selection contract. A required full persona retains every canonical field and representation.

Fill [the stage packet](templates/stage-execution.md), [work record](templates/design-work.md) and selected content/UX extensions. Inputs, approval, source authority, actor/persona IDs, baseline/delta and unknowns must survive each handoff. Use [workflow continuity](WORKFLOW.md) to resume without repeating partial actions.

## Validate actual records

Run from the package root with actual paths, replacing placeholders:

```sh
python3 -m design_system validate manifest /absolute/project/manifest.json --root /absolute/project
python3 -m design_system validate handoff /absolute/project/handoff.json --root /absolute/project
python3 -m design_system validate persona /absolute/project/persona.json --root /absolute/project
python3 -m design_system validate reference-decision /absolute/project/reference.json --root /absolute/project
python3 -m design_system validate system-inventory inventory/master.json --root .
```

The inventory command reads the bundled inventory and its specification reference from the library without writing to it. To validate a project inventory, supply its absolute file path and authorized project root instead.

For personas, persona.md is the authoring guide, persona-field-inventory.md defines coverage, and the completed JSON record is validator input. These are distinct artifacts.

Exit 0 means the implemented structural contract passed. It does not verify factual truth, approval, editability, accessibility, rights or output quality. Read [handoff semantics](HANDOFF-CONTRACT.md), [reference decisions](REFERENCE-CONTRACT.md) and [inventory scope](SYSTEM-INVENTORY.md) before interpreting results. Blank templates are not valid completed records. Validate evidence with the evidence kind when required. Only test files enumerated in PACKAGE-MANIFEST.json are included. Run the bounded screen-campaign tests with python3 -m unittest discover -s tests -p test_screen_campaign.py. The source repository full regression suite is not bundled and must not be claimed verified from this package.

## Produce, check and hand off

Use [creative direction](CREATIVE-DIRECTION.md), [context readiness](AI-DESIGN-CONTEXT.md) and [creative continuity](CREATIVE-CONTINUITY.md) for selected exploration and revision needs. Typography, color, motion, content and infographics have their own catalog entries; they do not force rebuilding accepted work.

Choose [production software](SOFTWARE-PRODUCTION.md) by the required editable master and output. Discover actual destination access. Apply [quality gates](QUALITY.md) and [delivery preflight](DELIVERY-PREFLIGHT.md) to the actual candidate, then record recipient instructions and unresolved checks. Passing a validator never authorizes sending or publishing. PowerPoint is deferred unless specifically needed. Media generation requires action-specific permission and entitlement.

Use [reviewed skill improvement](SKILL-IMPROVEMENT.md) only for a reusable observed gap. Preserve source/version, test the original and a contrasting case, review, and scope adoption. This does not train the base model or install changes globally.

Required package layout retains draft-skills/ as the canonical instruction tree, templates/ for schemas and records, inventory/ for the catalog, and design_system/ for validators. The draft prefix identifies instruction maturity; it is not a machine-specific location. Do not rename paths independently of catalog and link updates.

## Version provenance

The header timestamp identifies the file revision. Older section stamps and attribution identify the source section or authoring event, not destination-machine readiness. Directory naming does not enforce runtime discovery: these instructions are manually referenced here, and any installation must be deliberately scoped and verified.


## Reproduce the bundled model checks

From the verified library root:

```sh
node --test examples/screen-production/player.test.mjs
node --test examples/media-quality-recipes/touch-session/session.test.mjs
python3 -m unittest discover -s tests -p test_screen_campaign.py
```

Expected counts are five, six and eight tests respectively. These commands do not run browser, native-tool, provider or hardware acceptance. All three test files are manifest-listed. Read RELEASE-NOTES.md for the authoring machine's Illustrator bridge limitation before selecting a native route.

## Exact capability references

When recording selected, deferred, excluded or prerequisite capabilities, copy `id` exactly from capabilities.json. Store its `entry` path separately. A skill directory name or SKILL.md frontmatter name is not a catalog ID. Do not invent IDs by adding or removing a prefix.

For example, catalog ID `ux` maps to `draft-skills/design-ux-architecture/SKILL.md`; `design-ux` is not a valid catalog ID. Catalog ID `research` maps to `draft-skills/design-evidence-research/SKILL.md`.

Use `pattern` rather than `id` for an intentionally broad group such as `media-*`. Expand patterns in every category against the complete current catalog at validation time, before selection or execution. Before handoff, check every explicit ID in every category against the catalog, confirm its entry exists, and always record the exact catalog version/hash and selected entry hashes. A corrected record must retain repair provenance; do not label assisted repair as first-pass agent success.

Resolution procedure: match an input to a current catalog `id` first. For a supplied full entry path, match the catalog entry field exactly. For an exact skill-directory name, match the immediate parent directory of that entry path, such as design-touchscreen-design in draft-skills/design-touchscreen-design/SKILL.md. Require exactly one match and copy its ID, recording that lookup. Zero or multiple matches remain unresolved and visible. Frontmatter names are not lookup keys. A descriptive or near-match name such as `design-ux` is unresolved unless a human or implementing agent explicitly repairs it with a recorded rationale; examples above are not automatic aliases. Never silently strip prefixes.

Validate the transitive `depends_on` closure against the complete catalog and verify every entry file exists. A catalog excerpt cannot establish that a missing dependency is absent from the full catalog. Patterns match complete catalog ID strings only (`*` means zero or more characters). If expanded exclusions intersect either the selected IDs themselves or any member of their transitive depends_on closure, record a conflict and hold the affected selection. A deferred dependency holds only the affected work when a relevant required input is missing. Record accepted input reuse or a justified not-applicable disposition for bounded scope; deferring new production does not discard an existing accepted input. Reconcile scope or prerequisite evidence explicitly. Do not silently override exclusions or regenerate accepted prerequisite work.

At handoff, always record the catalog hash/version and selected entry hashes. Repair provenance includes original input, resolved ID/path, resolution basis, repair actor and catalog hash. Record absent categories as empty arrays. Unknown IDs and selection/exclusion conflicts remain visible failures, not successful normalizations.

## Input disposition for bounded work

The planner orders instruction reading, not production tasks. For each dependency, identify the input information relevant to the requested scope and record reuse, required creation, specifically authorized provisional use, or not applicable with a reason. It does not require every output of an upstream skill. Logo refinement can use a supplied accepted master; identity refresh preserves accepted positioning; evaluation reads delivery criteria before judging a concept without first delivering it. Strict project/persona requirements still apply. An exclusion conflict holds only the affected use until its relevant input disposition is resolved; it never silently forces execution of an excluded skill.

The pattern media-* matches only IDs beginning media-. Provider IDs chatgpt-images, higgsfield-cli and openart-cli are separate exact IDs; do not assume the pattern includes them.
