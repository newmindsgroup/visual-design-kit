# Reusable system inventory

Version-Timestamp: 2026-09-10 20:14:15 AST

This is an original inventory of 193 reusable concepts across six layers and eight delivery profiles. It helps a project discover and select what it needs. It is not a universal product checklist, an implemented component library or a completed set of 193 specifications.

Start with the [index](inventory/index.md), then the relevant [profile](inventory/profiles.md). Each entry includes a short definition, variants, state notes, profile rationale, token dependencies, source basis and unanswered project decisions. Its linked [family contract](inventory/families.md) adds shared behavior, accessibility, content and platform prompts.

| Layer | Count | Purpose |
| --- | ---: | --- |
| [Foundations](inventory/foundations.md) | 22 | Token roles, identity principles, voice and adaptation rules |
| [UI](inventory/ui.md) | 60 | Controls, navigation, data, feedback, overlays and media |
| [Patterns](inventory/patterns.md) | 35 | Assembled tasks, recovery, account, optional commerce and physical use |
| [Templates](inventory/templates.md) | 23 | Reusable page and screen structures |
| [Assets](inventory/assets.md) | 33 | Brand, campaign, sales, print and environmental deliverables |
| [Governance](inventory/governance.md) | 20 | Ownership, accessibility, rights, evidence and handoff |

## Coverage and status

All 193 entries are inventoried. A common blank specification template and 30 shared family contracts are available. No approved project-specific specifications are claimed by the canonical inventory. Optional teaching examples are separate from the core inventory. Zero implementations or component tests are provided. Repository validation tests check the inventory machinery, not product behavior or accessibility conformance.

An entry can group recognizable variants, such as a select/picker or sheet, without treating platforms as interchangeable. Read both its variant/state notes and its family platform contract. Web semantics are not a substitute for native behavior. Tablet layouts, native back navigation, keyboards, safe areas, permissions and shared-device privacy need explicit project decisions and actual device evidence.

Tokens name roles; usage rules explain when to use them. Components are reusable parts; patterns coordinate tasks; templates arrange a screen; assets are editable communication deliverables. None of these layers replaces another. No palette, font, dimensions, logo, style pack or technology has been selected.

## Scope a future project

1. Fill the [blank scoping record](templates/system-scope.md) with the brief, audience, platforms, constraints and owners. Profiles can be combined.
2. Review required, optional, not-applicable and needs-discovery starting points. Record the project's own choice and reason. Required is a recommendation within this profile, not approval or a demand to ship the feature.
3. Reconcile dependencies and token roles. If a selected entry needs another item, include that prerequisite or document an alternative through the existing decision record. Do not automatically activate optional authentication, commerce or account features.
4. Copy the [item specification template](templates/system-item.md) only for selected entries. Specify anatomy, variants, states, platform behavior, content and measurable acceptance criteria. Record justified exclusions rather than inventing nonexistent states.
5. Add missing domain needs through the extension register. A finite inventory cannot enumerate every product. Use stable project IDs such as X-001 and record source, owner, dependencies and scope rationale.
6. Keep the existing [design work record](templates/design-work.md), [reference decision contract](REFERENCE-CONTRACT.md), handoff and production manifest authoritative for evidence, baselines, rights, cost and change authority. Inventory selection grants no execution permission.

## Maintain the shared inventory

[inventory/master.json](inventory/master.json) is canonical. Category, family and profile Markdown files are deterministic views. Edit canonical data, validate it, then regenerate; never edit generated views independently.

```sh
python3 -m design_system validate system-inventory inventory/master.json --root .
python3 scripts/render_inventory.py
python3 scripts/render_inventory.py --check
```

The validator checks structure, IDs, references, profile coverage, dependency coherence and cycles, required state/platform slots, source dates and explicit status boundaries. Its narrow claim check scans entries and families only and catches certain unsupported completed-assurance phrases; it is not a fact checker or a comprehensive language audit.

Source provenance belongs to the manifest's pinned source version. Validate the exact bundled master and generated views before relying on their counts. The capability catalog remains the method authority. Choose project entries only after the relevant brief and requirements are available; none of these concepts is an implemented component.

Optional teaching examples are separate packages. Their absence does not waive anatomy, state, accessibility or platform requirements in the selected family and item specification.
