# Visual Design Studio

Version-Timestamp: 2026-10-20 02:05:00 UTC

Design anything with Claude: a design director that turns a brief into scored, rendered directions; a Design Space Atlas of 125 styles, industries, markets, audiences, archetypes, price tiers and channels; 14 discipline skills with concrete defaults; DTCG design tokens with contrast linting; and a render-and-critique quality loop.

Install in Claude Code:

```text
/plugin install visual-design-studio --marketplace newmindsgroup/visual-design-kit
```

In claude.ai or Claude Desktop: Customize > Plugins > Add > Add marketplace > `newmindsgroup/visual-design-kit`. Codex and pinned client-project setup: see the repository's [installation guide](https://github.com/newmindsgroup/visual-design-kit/blob/main/INSTALLATION.md).

## Contents

- `skills/`: 16 registered skills. Start with `design-director` for any new brief; `design-critique` reviews any visible output; `design-project-start` keeps client-project records.
- `library/atlas/`: the [Design Space Atlas](library/atlas/README.md) and `library/scripts/atlas.py` to query it.
- `library/tokens/`: [DTCG tokens](library/tokens/README.md), built with `library/scripts/tokens.py`.
- `library/examples/`: [stylescapes](library/examples/stylescapes/README.md), [AI tells](library/examples/ai-tells/README.md), the [quality benchmark](library/examples/quality-benchmark/README.md), and reference code.
- `library/draft-skills/`, `templates/`, `knowledge/`: the deep process library for client delivery ([usage](library/USAGE.md)).
- `evals/`: [behavioral evals](evals/README.md) for `claude plugin eval`.

## Status and integrity

Supervised evaluation; see [readiness](READINESS.md). `PAYLOAD.sha256` pins every packaged file (sorted relative POSIX paths, excluding itself); its digest must come from a trusted source such as the repository's pin record. New editions get new pins and never change existing project pins. Improvements flow through the [feedback contract](FEEDBACK.md).

Public reuse is governed by [MIT](LICENSE) for original work and the [third-party notices](NOTICE.md).
