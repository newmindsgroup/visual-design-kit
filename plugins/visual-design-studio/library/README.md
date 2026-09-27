# Visual design library

Version-Timestamp: 2026-09-27 13:45:10 AST

This library contains 130 selectable design capabilities, templates and local validators. It is part of the Visual Design Studio package. Use it with human supervision and inspect the requested outputs. The capability count describes reference coverage, not 130 completed production workflows.

## Start a project

Keep the complete package in a trusted local checkout. Create a separate project directory for each brand's assets, decisions and deliverables. The AI host needs access to both locations. A repository URL alone does not load the files.

Use the package's [starting skill](../skills/design-project-start/SKILL.md) and [project launch contract](../PROJECT-LAUNCH.md). The entry selects only the relevant capabilities from `capabilities.json`. Read [usage](USAGE.md) for validator commands and [package readiness](../READINESS.md) for the current scope. Dated candidate records elsewhere in this folder remain historical evidence.

The repository's project starter supports an explicit entry in Codex or Cursor `AGENTS.md`, or Claude Code `CLAUDE.md`. Existing instructions and approvals remain authoritative. Cursor and Claude Code native-session acceptance is unverified. Each host must demonstrate which package it reads and where it writes.

## Requirements

Python 3.9 or newer is required for the bundled command-line helpers; they use the standard library. A browser is needed for rendered examples, and Node.js for the JavaScript tests. Design apps, authenticated provider accounts and export tools are selected for the actual deliverable. No account, media credit or subscription is included.

Book retrieval is optional and needs an authorized compatible local collection. Full books and a public reference download are not bundled. Continue without book evidence when the selected capability's required inputs are otherwise available, and record that limitation.

## Verify before use

Obtain the expected SHA-256 of the package's `PAYLOAD.sha256` from the trusted current pin record. From this `library` directory on macOS:

```sh
shasum -a 256 ../PAYLOAD.sha256
```

Compare it with the expected digest. Then run the full package check from its parent directory:

```sh
cd ..
shasum -a 256 -c PAYLOAD.sha256
```

On Linux, use `sha256sum` and `sha256sum -c PAYLOAD.sha256`. Stop on an unavailable expected digest, a mismatch, a missing file or unexplained checkout modifications. The checksum verifies listed bytes; it does not authenticate an unknown source or approve the content.

`PACKAGE-MANIFEST.json` inventories the library. `CHECKSUMS.sha256` contains the library's internal checksums; the outer `PAYLOAD.sha256` covers the complete plugin. Keep all three files with the package. After verification, `python3 -m design_system plan ui` from the library directory is a bounded selection check. It does not generate or approve artwork.

## Updates and feedback

Review a newer edition in a separate checkout. Preserve the prior version and project pin, then deliberately adopt the new one and rerun affected checks. Keep the shared library read-only during project work. Report improvements through [the feedback contract](../FEEDBACK.md), using sanitized examples and actual results.

Final delivery still requires the requested editable files, exports, output inspection and a truthful project handoff. Human approval, accessibility, provider behavior and target-device tests remain specific to the project. PowerPoint and backup setup are outside the currently verified scope.
