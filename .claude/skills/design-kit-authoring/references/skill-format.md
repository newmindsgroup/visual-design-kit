# Registered skill format

Version-Timestamp: 2026-10-20 01:42:00 UTC

Registered skills live in `plugins/visual-design-studio/skills/<name>/`. Claude Code, claude.ai and Claude Desktop load every registered skill's `name` and `description` into context at all times, and load the body only when the skill is used. The listing budget is about 1% of the context window, so descriptions must be tight.

## Frontmatter (only these keys, for claude.ai compatibility)

```yaml
---
name: typography                # lowercase, digits, hyphens; <=64 chars; must equal the folder name; never contains "claude" or "anthropic"
description: >-                  # <=600 characters. Third person. What it does + "Use when ..." trigger phrases.
  Choose, pair, size and set type for brand, web, app, print and motion work ... Use when ...
license: MIT
metadata:
  version-timestamp: "YYYY-MM-DD HH:MM:SS UTC"
  agent-attribution: "computer=<hostname>; tool=<tool>; version=<version>; timestamp=<same timestamp>"
---
```

Get real values with `hostname`, `claude --version` (or the tool you are) and `date -u "+%Y-%m-%d %H:%M:%S UTC"`. Write "unknown" for anything you cannot read.

## Body structure

```markdown
# <Title>

<One or two sentences: what excellent work in this discipline looks like.>

## Defaults
<The 8-15 numbers and rules Claude should apply unless the brief says otherwise. Table preferred.>

## Workflow
<Numbered steps from brief to verified output. Include the render-and-inspect step.>

## Decisions that change the answer
<Which brief variables (atlas axes, constraints) move the defaults, and how.>

## Common failures
<Specific failure -> specific fix.>

## References
- [Topic](references/topic.md): when to read it.
- Atlas: `python3 ../../library/scripts/atlas.py query "..."` when style/industry/market matters.
- Deep process (client projects): links to `../../library/draft-skills/...` and the catalog IDs this skill covers.
```

## Links

- Use paths relative to the SKILL.md file. Every link must resolve; `tools/validate_plugin.py` checks this.
- Link to library content with `../../library/...`.
- Reference files may link to each other and to the atlas with relative paths.

## Coverage of the existing catalog

Each registered skill ends its References section with a line: `Catalog IDs covered: id-one, id-two, ...` using exact IDs from `library/capabilities.json`, so client projects can still record selections against the catalog.

## Scripts

Put executable helpers in `skills/<name>/scripts/` or `library/scripts/`. Python must be standard-library only. Node scripts must resolve optional dependencies (Playwright, axe) at runtime and fail with a clear message if missing. Never add a top-level `bin/` directory: claude.ai and Cowork refuse plugins that contain one.
