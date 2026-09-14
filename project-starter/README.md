# Add the startup entry to a separate project

Version-Timestamp: 2026-09-14T15:07:17.389420-04:00

Copy the instructions from AGENTS.md.template into the adopting project's AGENTS.md, replacing {{ABSOLUTE_PACKAGE_ROOT}} with the actual trusted package root. Preserve and reconcile any existing instructions; do not overwrite an existing AGENTS.md. The package root contains READINESS.md, library/ and skills/.

For Claude Code, add the same entry to CLAUDE.md while preserving its existing instructions. Claude startup behavior remains to be verified separately. A file template alone does not establish execution.

Use a pinned package checkout or release directory rather than a mutable install cache. Verify PAYLOAD.sha256 using an independently trusted source/digest before running packaged scripts. Record the chosen version and digest in the project. Each teammate sets their own local path; never commit another person's absolute home path to a shared starter.

This avoids relying on an oversized global skill catalog. It does not reduce that catalog or establish automatic skill discovery. The first independent project still supplies its brand brief and deliverable.

Replace the trusted-digest placeholder with the independently trusted SHA-256 of PAYLOAD.sha256. Use exactly one marked entry block. On updates, replace only that block after reviewing the new pin; never append duplicate blocks or change unrelated project instructions. Check unresolved placeholders before starting.

## Optional downloaded book library

Use [local reference setup](../resources/LOCAL-SETUP.md) and [the reference workflow](../resources/REFERENCE-WORKFLOW.md) from this trusted kit checkout. The book folder is separate from the pinned plugin payload and each client project. Supply its local path when starting the project. This optional workflow does not change the pinned package or install book content into the plugin.
