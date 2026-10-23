# Package readiness

Version-Timestamp: 2026-10-23 11:31:41 UTC

Edition: 0.6.2, public supervised evaluation. 0.6.2 splits eight eval rubrics into weighted graders and fixes skill routing found by them; 0.6.1 added the prompt handoff to `prompt-engineering-expert` and scoped the spec radar to our markets. This page describes package scope, not the installation state of any computer.

## What 0.6.0 adds

- Six plugin agents: `direction-explorer` for parallel direction building, and a read-only review panel (`art-director`, `accessibility-auditor`, `copy-editor`, `brand-guardian`, `frontend-engineer`). Claude Code and Cowork load them; chat and Codex fall back to one context.
- `figma-workflow` (17th registered skill): token import to Figma variables, bound components, push and pull, Code Connect and a no-connector fallback.
- `design-critique/scripts/compare_build.mjs`: pixel and computed-style fidelity diff of approved design versus build.
- 32 `claude plugin eval` cases (replacing a case that showed no lift), with a maintainer eval loop skill outside the plugin.

## What 0.5.0 added

- Native Claude packaging (`.claude-plugin/plugin.json` and the repository marketplace) alongside Codex packaging, with versions kept in sync.
- 16 registered skills: `design-director` (brief to scored, rendered directions), 13 discipline skills with concrete defaults, `design-critique` (render, score and revise), and `design-project-start` (client-project continuity).
- The Design Space Atlas: 125 schema-validated entries across styles, industries, markets, audiences, archetypes, price tiers and channels, with a query tool.
- DTCG design tokens with light, dark and high-contrast modes, two reference brands, CSS/Tailwind/JSON/Figma outputs, and a linter that enforces WCAG contrast.
- A stylescape calibration set across 12 very different briefs, an AI-tells gallery, a render-review script and the first 12 `claude plugin eval` cases.
- The earlier "no universal numbers" guidance is replaced by defaults with documented override conditions.

## What stays the same

The 133-capability process library, templates, continuity contracts (selection, handoff, resume), reference-book mode and feedback process are unchanged and remain available through `design-project-start` and links from the registered skills. Existing project pins are not affected; projects adopt 0.6.0 deliberately.

## Limits

- Automated checks prove structure, links, contrast math and builds, not aesthetic quality. Human art direction and client approval remain required for every deliverable.
- Atlas regulatory notes are design guidance, not legal advice. Platform specs (social formats, store assets, OS conventions) are dated and must be confirmed before production.
- claude.ai and Claude Desktop installation follows Anthropic's documented route; confirm it in the receiving workspace. Codex installation of 0.6.0 needs receiving-host verification. No Figma MCP call was exercised for `figma-workflow`; plan limits it names are marked "verify".
- Earlier known holds remain: the local-model revision-fidelity and touchscreen-recovery cases are excluded from autonomous routing; PowerPoint and backup setup remain deferred.

No hooks, MCP servers, credentials, provider access or paid jobs are bundled. `distribution_scope: public`, `publication_review_required: true` and `production_accepted: false` in the package manifest keep publication review and real-project acceptance separate from a build.
