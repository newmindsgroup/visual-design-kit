# Codex, Cursor and Claude Code

Version-Timestamp: 2026-09-14T17:05:40.280598-04:00

The same read-only kit can serve separate projects across these IDEs. The Codex plugin manifest is not a universal IDE installer. The project entry is the portable interface.

| Host | Project entry | Current proof |
| --- | --- | --- |
| Codex | Merge configured project-starter/AGENTS.md.template into project AGENTS.md | Native install and explicit project startup/integrity checked; global catalog discovery omitted the entry |
| Cursor | Merge configured entry into project AGENTS.md, following current Cursor rules support | Official documentation supports project rules; actual kit session untested |
| Claude Code | Merge the configured entry into project CLAUDE.md | Official documentation supports project instructions; actual wrapper session untested |

Preserve existing instructions, use exactly one marked entry and supply the trusted package-root/digest placeholders. Never copy the unconfigured template and call setup complete. Keep one authority for the project entry; avoid conflicting duplicated AGENTS.md, CLAUDE.md or Cursor rules. Start a fresh session after setup. Use a separate pinned checkout for kit instructions and a project-owned folder for all outputs.

For optional books, use the [reference-library contract](../resources/README.md). IDE access to a folder does not establish rights, successful extraction or full source understanding.

## Acceptance per host

Observe startup reading the intended pinned entry; verify all payload hashes; select exact catalog IDs; create a requested artifact only in the project; revise a specific delta while preserving the baseline; restart and recover next actions; test missing-source and wrong-pin behavior. Check actual model, file access and tool permissions. A documentation-compatible setup is not an executed acceptance test.

Official references checked for this guidance: [Cursor rules](https://docs.cursor.com/context/rules-for-ai), [Cursor CLI instructions](https://docs.cursor.com/en/cli/using), [Claude Code project memory](https://code.claude.com/docs/en/memory). These pages establish supported instruction mechanisms, not this kit's observed runtime behavior.
