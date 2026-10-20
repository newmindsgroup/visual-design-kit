# Spec radar

Version-Timestamp: 2026-10-20 05:15:00 UTC

Agent-Attribution: computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 05:15:00 UTC

Regulations, platform specs, social formats, payment rails and market statistics change faster than design craft. The kit marks each volatile claim with the word "verify" next to it. The spec radar finds those claims and re-checks them against primary sources every month, so the atlas and skills don't quietly go out of date.

## Run it

```sh
python3 tools/spec_radar.py                          # full report, grouped by topic, oldest files first
python3 tools/spec_radar.py --topic regulation       # one topic
python3 tools/spec_radar.py --older-than 90 --json   # files not re-dated in 90 days, machine-readable
```

Topics: `regulation`, `payments`, `platform-specs`, `sources` (editions of guides and studies), `statistics`, `other`. The baseline on 2026-10-20 was 288 claims in 106 files: 110 regulation, 67 platform specs, 18 payments, 17 statistics, 15 sources and 61 other.

## Monthly review

A scheduled task starts a fresh Claude Code session at 08:56 UTC on the 2nd of each month. Until the tool reaches `main`, the run stops and says so. For each run:

1. **Pick the claims.** Branch `chore/spec-radar-YYYY-MM` from `main`. Run the radar and take up to 25 claims, with regulation and platform specs first and the oldest files first.
2. **Check the primary source.** Go to the official regulator, the platform's own documentation, the central bank or the original study. Secondary blogs only count as leads.
3. **Act on what you find:**

   | Finding | Action |
   | --- | --- |
   | Confirmed | Add the source name and the check date, for example "(App Store Connect Help, checked 2026-11-02)". Keep the "verify" marker only if the value is expected to change again soon. |
   | Changed | Correct the value, cite the source and date, and note the old value in the PR. |
   | Couldn't confirm | Leave the claim as it is, hedge it, and list it in the PR as unresolved. Never guess a replacement. |

4. **Validate.** Bump the edited files' `Version-Timestamp`. Run every command in `CLAUDE.md` "Before every commit", rebuild the payload integrity metadata, and run `--check`.
5. **Open a draft PR.** Title it `chore: spec radar YYYY-MM`. The body has three tables: confirmed, changed (old and new value, plus source), and unresolved. Never merge it; a maintainer reviews and merges.

## Rules

- **Primary sources only.** Every change cites a source a reviewer can open.
- **No legal advice.** Regulatory notes say what typically affects design and point to the regulator. Counsel confirms requirements for a specific product.
- **Nothing client-related.** Don't add client names, private references or confidential material. Don't send repository content to unvetted services.
- **Keep it small.** A run that finds nothing to change still opens a PR with the confirmed table, so the check is on record.

## Trend watch

The same run also looks for platform changes that would affect the kit's defaults, such as a new OS design language, a new required App Store screenshot size, a WCAG or EAA milestone, or a browser shipping a CSS feature the skills treat as progressive. It lists them in the PR under "Proposed follow-ups" and does not edit skills for them. These become BACKLOG items for a maintainer to schedule.
