# Add the startup entry to a separate project

Version-Timestamp: 2026-09-27 14:19:56 AST

Copy the instructions from AGENTS.md.template into the adopting project's AGENTS.md, replacing {{ABSOLUTE_PACKAGE_ROOT}} with the actual trusted package root. Preserve and reconcile any existing instructions; do not overwrite an existing AGENTS.md. The package root contains READINESS.md, library/ and skills/.

For Claude Code, add the same entry to CLAUDE.md while preserving its existing instructions. Claude startup behavior remains to be verified separately. A file template alone does not establish execution.

Use a pinned package checkout or release directory rather than a mutable install cache. Verify PAYLOAD.sha256 using an independently trusted source/digest before running packaged scripts. Record the chosen version and digest in the project. Each teammate sets their own local path; never commit another person's absolute home path to a shared starter.

This avoids relying on an oversized global skill catalog. It does not reduce that catalog or establish automatic skill discovery. The first independent project still supplies its brand brief and deliverable.

Replace the trusted-digest placeholder with the independently trusted SHA-256 of PAYLOAD.sha256. Use exactly one marked entry block. On updates, replace only that block after reviewing the new pin; never append duplicate blocks or change unrelated project instructions. Check unresolved placeholders before starting.

## Start standalone; add references when useful

The default foundation is packaged guidance, task-relevant original [method cards](../plugins/visual-design-studio/library/knowledge/README.md) and authorized project inputs. Books are optional evidence, not model training or a prerequisite for ordinary design. Record the mode and no consulted book sources when working standalone. Missing required client facts or a named source holds only the dependent work.

Follow [local reference setup](../resources/LOCAL-SETUP.md) for the verified helper's `status --mode auto` check. Use `status --mode standalone` to skip all local configuration and corpus access, including stale configuration. Package checksum failure remains a stop before executing bundled code in either mode.

If an authorized collection is provided separately by its owner, download the whole folder or owner-provided ZIP, unzip outside the project and choose the compatible root containing `catalog/` and `manifests/`. Keep it separate from the pinned plugin and every client project. The public kit includes no books or public book download. An arbitrary PDF folder is not a compatible library.

Store `reference_library_root` in ignored `private/reference-library.local.json`; never commit the real machine path or private collection access details. Follow [the reference workflow](../resources/REFERENCE-WORKFLOW.md) to verify before reliance, inspect bounded evidence and record only actual consulted source IDs. A library that is available has not necessarily been consulted. Preserve unsuccessful integrity checks; optional fallback does not make them pass. Actual IDE, production and generation-tool acceptance remain separate checks.
