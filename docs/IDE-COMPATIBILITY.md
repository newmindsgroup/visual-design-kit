# Codex, Cursor, Claude Code, claude.ai and Claude Desktop

Version-Timestamp: 2026-09-14T17:05:40.280598-04:00

Version-Timestamp: 2026-10-20 02:05:00 UTC (Claude native plugin rows)

The same read-only kit can serve separate projects across these hosts. Claude Code, claude.ai and Claude Desktop install it natively from `.claude-plugin/marketplace.json`; Codex uses `.codex-plugin/`; Cursor uses the project entry. For pinned client projects the project entry remains the portable interface.

| Host | Project entry | Current proof |
| --- | --- | --- |
| Codex | Merge configured project-starter/AGENTS.md.template into project AGENTS.md | Native install and explicit project startup/integrity checked; global catalog discovery omitted the entry |
| Cursor | Merge configured entry into project AGENTS.md, following current Cursor rules support | Official documentation supports project rules; actual kit session untested |
| Claude Code | Native plugin: `/plugin install visual-design-studio --marketplace newmindsgroup/visual-design-kit`; for pinned client projects also merge the configured entry into project CLAUDE.md | 2026-10-20, Claude Code 2.1.304: marketplace added, plugin installed and enabled at 0.5.0 in an isolated configuration, `claude plugin validate` passed; skill behavior covered by `evals/` |
| claude.ai and Claude Desktop | Customize > Plugins > Add marketplace `newmindsgroup/visual-design-kit` | Documented route (Anthropic plugin docs, October 2026); receiving-workspace check pending |

Preserve existing instructions, use exactly one marked entry and supply the trusted package-root/digest placeholders. Never copy the unconfigured template and call setup complete. Keep one authority for the project entry; avoid conflicting duplicated AGENTS.md, CLAUDE.md or Cursor rules. Start a fresh session after setup. Use a separate pinned checkout for kit instructions and a project-owned folder for all outputs.

For optional books, use the [reference-library contract](../resources/README.md). IDE access to a folder does not establish rights, successful extraction or full source understanding.

## Acceptance per host

Observe startup reading the intended pinned entry; verify all payload hashes; select exact catalog IDs; create a requested artifact only in the project; revise a specific delta while preserving the baseline; restart and recover next actions; test missing-source and wrong-pin behavior. Check actual model, file access and tool permissions. A documentation-compatible setup is not an executed acceptance test.

Official references checked for this guidance: [Cursor rules](https://docs.cursor.com/context/rules-for-ai), [Cursor CLI instructions](https://docs.cursor.com/en/cli/using), [Claude Code project memory](https://code.claude.com/docs/en/memory). These pages establish supported instruction mechanisms, not this kit's observed runtime behavior.
