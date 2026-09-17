# Install for independent projects

Version-Timestamp: 2026-09-14T15:03:31.772234-04:00

This private repository requires GitHub access. Clone it to a dedicated library directory, not a client project. From the clone root run:

```sh
codex plugin marketplace add .
codex plugin add visual-design-studio@visual-design-team --json
codex plugin list --marketplace visual-design-team --json
```

Open a new Codex task inside the separate brand project so it receives fresh plugin discovery. For the verified local cache location, use the explicit starting SKILL.md path. Automatic discovery failed in the authoring environment: Codex reported that 1,141 skills were omitted after the skills context budget was exceeded. An enabled plugin is not necessarily visible to the model. No global skill configuration was changed. Follow the package's PROJECT-LAUNCH.md and keep all brand data in that project. Never assume this existing task reloads its skills after installation.

On the authoring machine, Codex CLI 0.154.0 installed version 0.1.0 and reported enabled=true. All 322 installed payload hashes matched. This verifies this installation only, not every machine or a production project.

Claude Code native plugin installation is not provided by this Codex manifest. Its intended fallback is to read the starting SKILL.md using its absolute path. That route still needs a fresh execution check.

## Updates and removal

Pin a reviewed release or commit. Do not blindly pull a changing branch into a running project. Review changed capabilities and checks, preserve the old version and project pin, then deliberately reinstall the new published version. Upgrade and removal behavior still require a controlled test before being called verified. Removing the plugin must not delete project outputs.

## Scope

The marketplace adds one local instruction plugin, no connector credentials, hooks or provider subscriptions. Installation is not authorization to generate paid media or publish client work. Read [remaining work](BACKLOG.md).

## Reliable entry point under evaluation

Ask the agent: Read the absolute path to plugins/visual-design-studio/skills/design-project-start/SKILL.md in my trusted checkout, then follow its instructions for this independent project. Do not assume the library is auto-loaded.

A fresh Codex session successfully read the installed starting skill, followed its relative links, selected exact catalog IDs for a locked-logo typography case and an unresolved-name new-brand case, and preserved project/feedback boundaries. This was read-only selection, not artwork generation, full dependency execution or human acceptance.

## Project-level startup fix

Version-Timestamp: 2026-09-14T15:09:30.013404-04:00

Use [the project starter](project-starter/README.md) to merge a pinned entry into each independent project. A fresh session in a separate directory followed that entry without a library path in the task prompt. This bypasses the truncated catalog for project startup; it does not repair global auto-discovery. Never overwrite existing project instructions.

Final hardened entry check passed in a second separate read-only project: trusted manifest digest and all 322 payload hashes verified before entry use. No writes or network. An initial heredoc command was blocked by read-only temporary-file rules; an in-memory verification command succeeded. Wrong-digest, conflict and duplicate-merge behavioral cases remain untested.

## Verified 0.2.0 update

Version-Timestamp: 2026-09-16T18:44:50.670908-04:00

The authoring Mac installed and enabled 0.2.0 using `codex plugin add visual-design-studio@visual-design-team --json`. All 364 installed PAYLOAD.sha256 entries matched. The manifest digest is `43bde9afa9b57d8fd9264fea7645451d345b4ac2ad8c2d273d8787131f79f9d3`. Installed handoff and selection examples validate successfully. The optional reference helper matches its canonical repository source.

The native updater removed the 0.1.0 cache directory. Do not rely on the cache to preserve project pins. The old 322-entry payload is recoverable from commit `412e628bed1af9ae41bcad14784f1ebd8bdd3116`, and a verified separate recovery copy is retained in the author's ignored `private/quality-020/recovery-0.1.0`. Do not manually patch Codex's cache. For rollback, use a separate checkout of that trusted commit, verify its recorded digest and all payload files, then deliberately repoint the affected project's entry. Installation rollback would additionally require restoring the old marketplace source through the supported plugin command; that action has not been executed.

Existing project pins were not rewritten. If a historical project points at the removed cache, deliberately adopt the recovered fixed checkout or reviewed new version before continuing. New projects should use a pinned checkout or release directory as described in [the project starter](project-starter/README.md).

A new native Codex session's automatic discovery has not been proven for 0.2.0. Explicit-path navigation is verified; no claim that the current thread hot-reloaded the installed skill is made. Claude Code and Cursor native-session acceptance remain separate. [Edition evidence](docs/QUALITY-020-RELEASE.md).
