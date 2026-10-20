# Visual Design Studio 0.6.0: edition evidence

Version-Timestamp: 2026-10-20 12:10:00 UTC

Agent-Attribution: computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 12:10:00 UTC

Status: public supervised evaluation candidate on branch `feat/wave-2-design-ops` (PR #6).

## Why this edition exists

0.5.0 gave Claude design knowledge. 0.6.0 adds the operations around it:

- parallel exploration and specialist review
- a Figma round trip
- proof that a build matches the approved design
- an eval-driven loop that measures whether the kit helps
- a radar for claims that go out of date

## What changed

| Area | 0.6.0 |
| --- | --- |
| Agents | Six in `agents/`. `direction-explorer` builds one direction per position in parallel. The read-only review panel is `art-director`, `accessibility-auditor`, `copy-editor`, `brand-guardian` and `frontend-engineer`, with a score merge and conflict ladder in `design-critique/references/review-panel.md`. Hosts without plugin agents use the single-context fallback. |
| Skills | 17 registered. `figma-workflow` is new: token import as variables, bound variant components, push and pull, Code Connect, Dev Mode handoff and a no-connector fallback. Eight descriptions were rewritten to say when to load first. `design-director` gained non-negotiables: at most 4 questions, a distinctness line and a sensitivity line. |
| Build fidelity | `design-critique/scripts/compare_build.mjs`: pixel and computed-style diff of design versus build at real widths, with masks, element scope and exit codes for CI. The default color tolerance is 0.05, because 0.1 let a brand-color swap pass. |
| Evals | 32 cases, up from 12. The no-lift typography case was replaced. Maintainer skill `.claude/skills/design-kit-eval-loop/` adds `summarize_eval.py`. |
| Spec radar | `tools/spec_radar.py` found 288 "verify" claims in 106 files. `docs/SPEC-RADAR.md` describes the monthly primary-source review. |
| Always-on cost | About 4,125 tokens for 17 skills and 6 agents, up from about 2,934. |

## Verification (2026-10-20, Linux, Python 3.13 and 3.9, Node 22, Claude Code 2.1.304)

| Check | Result |
| --- | --- |
| Repository tests | 97 passed on 3.13 and 3.9 |
| Library tests | 123 passed on 3.13 and 3.9 |
| `tools/validate_plugin.py` | Valid: 17 skills; listing 8,416 characters; every relative link resolves |
| `claude plugin validate` | Passed for the marketplace, `visual-design-studio` and `astro-website-studio` |
| Local install | Isolated config: marketplace added, 0.6.0 installed. `plugin details` lists Skills (17) and Agents (6). |
| Atlas, tokens | 125/125 entries. Lint: 0 errors across 336 contrast pairs. Dist is current. |
| `compare_build.mjs` | Same stylescape: 0% changed, exit 0. Font and color swap: 25-35% changed, exit 1, with font drift named. Color-only swap: about 5% changed, exit 1. |
| CI | Every job is green on PR #6 |
| Payload | Rebuilt and checked. 990 files. Digest is in [VERIFIED-PIN](VERIFIED-PIN.md). |

## Evals

The [eval README](../plugins/visual-design-studio/evals/README.md#060-results-2026-10-20-claude-code-21304-judge-haiku) has the full tables.

**First full run, one run per arm: 0.64 overall.**
- Lift on Japanese vertical setting (+0.80), Arabic RTL (+0.75), Pix checkout (+0.60) and the bilingual annual report (+0.25).
- The biggest defect was that skills often didn't load: 8 of 21 tracked runs.

**Re-run of the 15 affected cases after the fixes:**
- Skills loaded in 14 of 15.
- Six more cases reached 1.00, including the fixed question-count regression.
- Eight cases still miss one clause of strict all-of rubrics. They are queued for grader hardening and `--runs 3`.

Spend was about $5.70 against the $15 cap.

## Known limits and unverified items

- One run per arm is a sample, not a certificate. Run `--runs 3` on cases that are low, split or near the bar before claiming lift per case.
- No live Figma MCP call was made. The Figma plan limits the skill names are marked "verify".
- The agent invocation name (`visual-design-studio:<agent>`) is not confirmed on every host. Codex probably ignores plugin agents.
- claude.ai, Claude Desktop and Codex installs of 0.6.0 need receiving-workspace confirmation.
- `figma-workflow/references/no-connector.md` is shorter than the other references.
- Every claim marked "verify" needs a primary-source check before client use. The spec radar tracks them.
- Automated checks prove structure, contrast math, builds and sampled behavior, not taste. Human art direction and client approval remain required.
