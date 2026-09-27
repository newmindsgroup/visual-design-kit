# Contributing

Version-Timestamp: 2026-09-27T13:47:24-04:00

Start with [README](README.md) and [development checks](docs/DEVELOPMENT.md). Keep changes scoped to an existing capability before adding another one. Include the problem, the affected workflow, before/after behavior and the checks you ran. Synthetic examples should be clearly labeled.

By submitting original contributions, you agree they may be distributed under this repository's MIT license. Preserve separately licensed third-party notices and identify the source and license of any new dependency or asset. Do not submit client information, proprietary books or extracts, credentials, private share links, or material you cannot redistribute. Use fictional or sanitized cases for issues and pull requests.

Skill changes need explicit inputs, outputs, prerequisites and review criteria. Test a meaningful original case and a contrasting case. Do not turn one client's preference into a universal design rule. Passing validation is not proof of visual quality, provider access or client approval.

Change package metadata only through `tools/build_plugin.py`. A changed payload requires a new edition and a new trusted digest; never silently replace an existing project's pin. Preserve version timestamps and include factual tool attribution in commits. Maintainers review and merge changes; submitting a report does not run tools, publish a design or update another project.

Report security problems using [SECURITY.md](SECURITY.md), without posting sensitive details publicly.
