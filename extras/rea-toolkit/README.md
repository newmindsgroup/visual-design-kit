# REA Toolkit

Version-Timestamp: 2026-10-27 07:45:42 AST

Full REA 6.8.0 investigation instructions for Codex and Claude Code, with all
seven shipped references. Use the namespaced `rea-toolkit:rea` skill with a
prepared local REA CLI/MCP runtime. A skill install alone does not add MCP tools.

Source: [morluto/rea](https://github.com/morluto/rea), MIT, copyright 2026 morluto.
The shipped release is commit `160d821ac9a0310afcb8d1fc427862dd6508add5`.
[PROVENANCE.json](PROVENANCE.json) records original and adapted hashes.
[LICENSE](LICENSE) preserves the original license. Upstream third-party
licenses remain separate from rights in an investigation target.

## Capability coverage

The full 229-tool release is retained. Select workflows by the question:

| Target or job | REA workflow | Additional requirements |
| --- | --- | --- |
| Web UI, flows and behavior | DOM/accessibility inspection, selected screenshots, passive observation, declared browser scenarios, comparisons | Supported Chrome-family browser and an explicitly selected loopback CDP endpoint, or a declared temporary browser launch |
| Electron and JavaScript | Inert source/bundle analysis, module/IPC relationships, runtime reconciliation, feature tracing and reconstruction coverage | Supported Node; a selected app/runtime endpoint for dynamic work |
| Mac applications | Mach-O/plist/signature inspection, bundle/asset/Interface Builder inspection, native UI/call observation | macOS tools; Screen Recording/Accessibility or debugger access only for selected workflows |
| Deep native binaries | Pseudocode, assembly, symbols, call relationships, comparisons | Separately configured Hopper, Ghidra, IDA, or another supported engine |
| Packaged/managed/mobile artifacts | Archive inventory/extraction, .NET, Android, Flutter and artifact metadata | Several static readers are built in; JADX/JDK, adb, Apktool, JEB or platform tools are needed for selected advanced workflows |
| Runtime instrumentation | Frida, debugger and process scenarios | Relevant bindings, tools, host support and explicit target/action scope |
| Recorded traffic and agent environments | HAR/SAZ inspection, capture comparison, recorded API environment export | Captures must be approved for local/provider processing; exported environments include recorded content |
| Evidence and reconstruction | Evidence IDs, retained views, unknown ledger, source/build comparisons, reconstruction obligations and coverage | Preserve observed facts, inferences, limits and target identity |

No wrapper removes runtime functions. Prerequisite failures remain visible.
Tool discovery and `doctor` are readiness evidence. They do not demonstrate all
229 tools, OS permissions, real browser captures or an application reconstruction.


```text
/plugin install rea-toolkit --marketplace newmindsgroup/visual-design-kit
```

## Prepare an isolated runtime

Use an approved supported Node runtime: `^22.23.4 || ^24.22.1 || >=26.12.1`.
Do not change the global Node default as a side effect of adopting this plugin.
For a new Mac ARM64 runtime, download the exact Node archive and its
`SHASUMS256.txt` from `https://nodejs.org/dist/v24.22.1/`, verify the archive's
SHA-256 against that official HTTPS file, then extract into a new owned directory.
The Node 24.22.1 Darwin ARM64 `.tar.gz` SHA-256 is
`89c682593d76cd44233fa53b1563264e7de9cbb189cad169135c5b4fadfbc0a7`.
Use the correct official archive for another architecture or OS.

Create a new owned REA runtime directory outside the plugin cache. Copy
[runtime-package.json](runtime-package.json) to `package.json` and
[runtime-package-lock.json](runtime-package-lock.json) to `package-lock.json`
in that directory. Run the prepared Node's npm CLI there:

```sh
/absolute/node/bin/node /absolute/node/lib/node_modules/npm/bin/npm-cli.js ci --ignore-scripts --omit=dev --no-audit --no-fund
/absolute/node/bin/node /absolute/node/lib/node_modules/npm/bin/npm-cli.js audit --omit=dev --ignore-scripts
```

The lock pins `rea-agents@6.8.0`, `fast-uri@3.1.9` and `zod@4.6.6`.
The two overrides address advisories found during this adoption. Do not replace
them with a mutable `@latest` invocation. Record the actual audit on the receiving
computer. The package-lock integrity must match the official registry package.

Create an owned `nmg-rea` launcher that executes the exact prepared Node and
`node_modules/rea-agents/scripts/rea.mjs`, forwarding `"$@"`. Put it in an
already available local bin directory only when that name is absent. Never
overwrite another launcher. The launcher's Node and entrypoint paths must be
absolute and remain available when an agent starts. Validate with `nmg-rea --version`.

`--ignore-scripts` avoids dependency lifecycle execution. Frida's optional
native binding may therefore be unavailable, while the CLI, MCP catalog and
static JavaScript analysis can still work. A Frida build or other engine
installation needs its own vetted, authorized setup and verification.

## Register Codex and Claude Code

Use the existing launcher. First inspect the exact proposed changes:

```sh
nmg-rea setup --client codex --client claude_code --skill=false --dry-run --json
```

Review the REA-only entries, paths and backups. When those exact writes are
already authorized, apply the same scope:

```sh
nmg-rea setup --client codex --client claude_code --skill=false --yes --json
```

Keep `--skill=false` so setup preserves this plugin. Omit `--install-hopper`;
this baseline registers REA without adding an analysis engine. Retain unrelated
MCP entries, approval policies, permissions and authentication.

REA 6.8.0's Unix setup can register its env-node shebang without binding the
supported Node used during setup. Read back both new REA registrations. When
the client PATH would select a different Node, correct only their `command`
and `args` to this exact shape, using the receiving machine's actual paths:

```json
{
  "command": "/absolute/node/bin/node",
  "args": ["/absolute/rea-runtime/node_modules/rea-agents/scripts/rea.mjs", "mcp"],
  "env": {"REA_MCP_OUTPUT_SCHEMA_PROFILE": "off"}
}
```

For Codex this is the `mcp_servers.rea` table in its selected configuration;
for Claude Code it is `mcpServers.rea` in its selected configuration. Keep any
timeouts or pre-existing REA policies and verify unrelated settings are unchanged.
Do not patch other servers or replace the whole configuration from an old backup.

Set `REA_MCP_OUTPUT_SCHEMA_PROFILE=off` only for the REA registrations. This
shipping-supported option omits output-schema advertisements while retaining
all 229 tool names, identical input schemas, local canonical result validation
and complete structured results. In the adoption check it reduced the catalog
frame from 3,505,030 to 302,268 bytes. This is a byte measurement, not a model-token
claim. REA 6.8.0 supports `full` and `off`; current-main `compact` is unavailable
in this pinned release and makes startup fail. Do not hide tool families to
claim the complete toolkit is connected.

Then run:

```sh
nmg-rea doctor --client codex --client claude_code --skill=false --json
```

Restart or reconnect the affected clients. Verify the actual REA tools appear
there. Independently exercise stdio `initialize`, `tools/list` and one small
owned synthetic artifact before using project data. A direct protocol test is
separate from an agent-host acceptance test.

## Data, effects and reuse boundaries

Use local stdio MCP for this baseline. It does not require an HTTP listener,
remote service or account. No external target is selected during registration.
Analysis targets, browser origins, actions and outputs come from the current
authorized task. The engine and tools are not a sandbox.

The agent receives REA results in its context, so local analysis does not mean
that all model processing remains local. Screenshots, accessibility text, source,
query strings, captures and recorded response bodies may contain confidential
information. Apply the project's provider/data permission before processing.
Source-map fetching, active network requests, process execution and UI actions
are explicit workflow capabilities with their own effects. Do not treat the
skill's guidance as a runtime permission interceptor.

Reconstruct behavior from evidence and keep design choices explicit. Preserve
rights, licenses and provenance for code, fonts, icons and assets. Use owned,
licensed or otherwise authorized sources within scope. No skill grants rights
to protected assets or authorizes bypassing authentication or license checks.

## Rollback

Close owned REA sessions and stop only owned REA processes. Remove only the
`rea` registration that this adoption created in each selected client, after
verifying its command still identifies this runtime. Preserve newer unrelated
settings. Keep private setup backups until recovery is confirmed; do not commit
them. Remove a convenience symlink only when it still resolves to this runtime.
Archive or remove the owned runtime directories only after confirming no other
project or session depends on them. Removing the plugin alone does not remove
its separately prepared runtime or MCP registrations.

## Retained runtime notices

The upstream third-party notice inventory and its linked license texts are retained for attribution, without bundling those engines or binaries. Website-only and installation documentation links point to the pinned release. A separately installed Node24 runtime retains its own archive LICENSE; the upstream Node22 notice describes a different distribution context.

License wording is retained. Trailing whitespace and tab indentation in four imported notice files are normalized for repository checks; the upstream MIT LICENSE is unchanged.
