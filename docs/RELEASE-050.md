# Visual Design Studio 0.5.0: edition evidence

Version-Timestamp: 2026-10-20 04:00:00 UTC

Agent-Attribution: computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 04:00:00 UTC

Status: public supervised evaluation candidate on branch `feat/claude-native-design-studio` (PR #5). Not yet merged or tagged.

## Why this edition exists

An audit of 0.4.1 (October 2026) found:

- **Not Claude-native.** Only a Codex manifest; 1 of 133 skills was discoverable, and Claude Code users had to wire a project entry by hand.
- **Process over craft.** Across the core craft files, governance terms outnumbered design terms about 3.3 to 1. "record" appeared 444 times in the skills, "type scale" and "cubic-bezier" zero times. Ten statements refused to give numbers by policy ("no universal ratio, line count or minimum type size").
- **No map of the design space.** Most styles, industries, markets and audiences had zero or one mention, and there was no method for choosing among directions.
- **One aesthetic register.** Every example was quiet editorial (cream, serif, navy), and the kit declined to name generic-AI design tells.
- **Discipline gaps.** No native app design, no implemented design tokens or components, no Figma workflow, no Lottie/Rive/Remotion, no print, packaging or social specs.
- **No CI.**

## What changed

| Area | 0.5.0 |
| --- | --- |
| Packaging | `.claude-plugin/plugin.json` plus a repository marketplace for Claude Code, claude.ai and Claude Desktop; Codex manifest kept and version-synced; optional Astro plugin listed |
| Registered skills | 16: `design-director`, 13 discipline skills, `design-critique`, `design-project-start` (111 Markdown files, about 12,500 lines) |
| Design Space Atlas | 125 entries (37 styles, 32 industries, 17 markets, 10 audiences, 12 archetypes, 5 tiers, 12 channels; about 12,600 lines) with `atlas.py` query, combine, validate and build |
| Tokens | DTCG source, 345 tokens, 2 brands x 3 modes; CSS, Tailwind v4, resolved JSON and Figma outputs; `tokens.py` lint (336 contrast pairs), `color_tools.py`, `type_scale.py` |
| Examples | 12 stylescapes, AI-tells gallery (18 tells), React reference system (16 components plus a billing screen), stylescape template |
| Quality loop | `render_review.mjs` (overflow, orphans, clipping, fonts, contrast, axe), critique rubric and AI-tells catalog, 12 `claude plugin eval` cases |
| Tooling | `tools/validate_plugin.py`, CI workflow (Python 3.9 and 3.13, validators, payload integrity, Claude validation, example and React builds with browser and axe checks), maintainer `CLAUDE.md` and authoring skill |
| Policy | Ten "no universal numbers" statements replaced with defaults plus documented overrides |

## Verification (2026-10-20, this container: Linux, Python 3.13.16, Node 22.22.0, Claude Code 2.1.304)

| Check | Result |
| --- | --- |
| Repository tests | 92 passed |
| Library tests | 123 passed |
| `tools/validate_plugin.py` | Valid: 16 skills, listing 8,261 characters, every relative link in the plugin resolves |
| `claude plugin validate` | Passed for the marketplace, `visual-design-studio` and `astro-website-studio` (locally and in CI) |
| Local install | Marketplace added and plugin installed and enabled at 0.5.0 in an isolated Claude Code configuration; `claude plugin details` reports about 2,934 always-on tokens for 16 skills |
| Atlas | `validate --complete`: 125/125; index regenerated and current |
| Tokens | `lint`: 0 errors, 336 contrast pairs across both brands and all modes; `check`: dist current |
| React system | 11 unit tests, type check, build; browser suite 46/46 including 28 axe runs (1440 and 390, every brand and mode, plus RTL), dialog focus trap and return, tabs arrow keys, keyboard reach, reduced motion |
| Astro example | 7 runtime tests, 43-page build |
| Screen and touch examples | 5 and 6 Node tests |
| Visual review | Every stylescape, the AI-tells gallery, the token specimen and the React screens were rendered and inspected by eye |
| Payload integrity | Rebuilt with `tools/build_plugin.py` and checked with `--check` and `sha256sum -c`; digest recorded in [VERIFIED-PIN](VERIFIED-PIN.md) as a candidate |

## Evals

| Case | With plugin | Without | Note |
| --- | --- | --- | --- |
| `no-fire-git-undo` | 1.00 | n/a | Design skills stay out of unrelated work |
| `typography-longform-defaults` | 1.00 | 1.00 | No lift; Claude knows these defaults when asked directly. Kept as a regression guard |
| `direction-genz-neobank-brazil` | 0.00, then 1.00 | 0.00 | First run exposed two `design-director` defects (fixed below) |

One run per arm, about $0.30 in total. This is a smoke test; run `--runs 3` with ablation across all 12 cases before claiming lift.

## Defects found and fixed during integration

- **Status border tokens failed WCAG 1.4.11.** At 1.7-2.2:1 against canvas in light and dark modes, they would have failed as invalid-input borders, which the UI skill recommends. They moved to ramp step 500 (3.6-4.6:1), and lint now enforces 3:1.
- **Placeholder text failed WCAG 1.4.3.** `--input-placeholder` mapped to `fg-subtle` (4.43:1 in Meridian light). It now maps to `fg-muted`, the component rule requires 4.5:1, and the contract restricts `fg-subtle` to decorative text.
- **`design-director` answered in the client market's language** (Portuguese for an English brief) **and dropped specifics when asked to be concise.** A "Non-negotiables" section fixed both; the eval case moved from 0.00 to 1.00.
- **FORM/TIDAL benchmark index page.** Headline orphans at 390 and 768 px, arrow glyphs falling back to another font, undersized link targets. Fixed; render review is now clean at all three widths with 0 axe violations.
- **`color_tools.py ramp`** silently returned white for out-of-range steps; it now rejects them.
- **Atlas parser** did not strip quoted frontmatter values; it does now, and the schema documents that colons need no quoting.
- **Corrected claims:** the Swiss-style exemplar's "red fails on white" claim (it passes at 4.88:1) and three OKLCH values; uncoated ink limits (now 260-300% by press profile); Outlook animated-GIF behavior; iPhone Duo screenshot versus native panel sizes; required iPhone screenshot sets flagged as conflicting across sources.

## Known limits and unverified items

- Every atlas and skill statement marked "verify" (volatile regulation dates, platform specs, social formats, some reading-speed and safe-zone figures) needs a primary-source check before client use.
- Arabic, Japanese, Portuguese and Spanish copy in the stylescapes needs native-speaker review.
- Browser automation ran in Chromium only; there was no Safari, Firefox or screen-reader pass.
- claude.ai and Claude Desktop installation follows the documented route but was not exercised in a receiving workspace; Codex installation of 0.5.0 needs receiving-host verification.
- The Figma import script was exercised against a mock Plugin API, not a live Figma file.
- Automated checks prove structure, links, contrast math and builds, not taste. Human art direction and client approval remain required.

See [BACKLOG](../BACKLOG.md) for follow-ups, including the proposed second wave and private companion.
