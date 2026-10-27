# Native apps and reverse engineering toolkits

Version-Timestamp: 2026-10-27 07:39:56 AST

Agent-Attribution: computer=NMG-MBP-M5; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 07:39:56 AST

The toolkit has three complementary parts. Visual Design Studio owns reusable
design methods. BAMA Mac Studio supplies the complete 21-skill native Mac workflow
with guarded helpers. REA Toolkit supplies the REA skill and connects to a separately
installed, pinned REA CLI/MCP runtime. Install the optional plugins when needed.
Their names are distinct; do not also install an unchanged BAMA skill collection.

## Choose the entry

| Task | Entry | First useful output |
| --- | --- | --- |
| Design an interface from a brief | `design-director`, then `ux-design` and `ui-design` | Chosen direction, flows and complete states |
| Make a branded component kit | `design-system` | Token map, component APIs and forced-state gallery |
| Draw a coherent icon family or an app icon | `icon-design` | Geometry rules, optical sizes, registry and contact sheet |
| Reproduce an existing app or website | `reference-reconstruction` | Screen/state index, measurements and implementation slices |
| Research, clone, design, build or improve a Mac app | `bama-router` in BAMA Mac Studio | Correct next skill and verified milestone |
| Inspect and reverse engineer software using REA tools | `rea` in REA Toolkit | Target evidence and findings using the selected runtime tools |

Reconstruction follows the observed reference closely. Adaptation is an explicit
mode when the project calls for different branding, platform or behavior. A still
image supports visible appearance only. Observe interactions before claiming them.
Existing project locks take precedence over an imported design recipe.

## Install the skills in both hosts

Start from a reviewed checkout of this repository. Preserve project-specific pins.
The same skill files serve both hosts; host manifests differ.

```sh
# Codex, from the repository root
codex plugin marketplace add .
codex plugin add visual-design-studio@visual-design-team --json
codex plugin add bama-mac-studio@visual-design-team --json
codex plugin add rea-toolkit@visual-design-team --json

# Claude Code, from the repository root
claude plugin marketplace add .
claude plugin install visual-design-studio@visual-design-team
claude plugin install bama-mac-studio@visual-design-team
claude plugin install rea-toolkit@visual-design-team
```

If the marketplace already points at this checkout, keep that registration.
Use the host's supported update/reinstall command for an existing plugin, then
verify its reported version and hashes. Open a fresh session to discover new skills.
Installing a skill does not install REA, Xcode or native analysis utilities.

## BAMA capability coverage

Every upstream skill is retained in the optional plugin with namespaced names.
The router is `bama-router`; every companion skill begins with `bama-`.

| Upstream skill | Portable capability | Reusable design entry |
| --- | --- | --- |
| bama | Select the correct phase | Explicit Mac project router |
| app-brief | Goal, audience, constraints and scope | Existing project intake |
| new-mac-app | SwiftPM, SwiftData, snapshots, tests | Guarded fresh-directory scaffold |
| research | Market, user, feature, design and API research | Existing research methods |
| clone | Observe screens and record evidence | reference-reconstruction |
| user-stories | State-complete behavior and milestones | ux-design |
| swift-swiftui | Swift concurrency, state and bridges | Native implementation handoff |
| os-integrations | Menu bar, panels, shortcuts and OS APIs | macOS specialization |
| performance | Profile before optimizing | Existing quality loop plus native profiling |
| improve-architecture | Tested incremental refactors | Native architecture method |
| agent-cli | Shared app core behind CLI/MCP | Optional bounded agent interface |
| ux-design | Flow, placement, names and copy | ux-design surface placement |
| mac-design | Windows, toolbar, keyboard, type and appearance | native-app-design macOS reference |
| design-system | Native theme and tokens | design-system |
| layout-grid | Spacing lint, probes and overlays | Project grid plus measured exceptions |
| design-kit | Branded parts, type, icons and gallery | design-system component gallery |
| design-from-app | Measured visual extraction and comparison | reference-reconstruction |
| app-icon | Layered icon source and appearance checks | icon-design |
| build-and-verify | Staged build, snapshots and tests | Guarded native build helpers |
| test-mac-app | Swift Testing, self-test and optional bridge | Native test workflow |
| improve-loop | Ordered, verified milestone work | Explicit milestone execution |

The derivative removes automatic staging/commits, silent signing success and
unconditional replacement of installed apps. It preserves the intended workflow
with explicit operations and isolated test data. Read its README for exact helper
flags and verification limits. The source commit and changes are recorded there.

## REA runtime

REA is a software reverse-engineering runtime as well as an interface observation
toolkit. Its broader catalog remains available. Selecting a design task does not
need to run binary analysis, inspect credentials or invoke every tool family.
Use the exact 6.8.0 package and its release commit from the provenance record.
The audited main branch is a separate snapshot and has a different generated skill.

Install in an owned runtime directory with a supported Node version, an exact
package version, an npm lockfile and verified integrity. Disable dependency install
scripts initially, then test whether selected native dependencies require a separate
reviewed build. Do not reuse a chat subscription as API entitlement.

Run the supported client setup in dry-run mode first:

```sh
nmg-rea setup --client codex --client claude_code --skill=false --dry-run --json
# Inspect target entries and backups, then apply the same client scope.
nmg-rea setup --client codex --client claude_code --skill=false --yes
```

`--skill=false` preserves this kit's versioned REA instructions. Do not pass the
optional Hopper-install flag unless it is part of the selected setup. Preserve
unrelated MCP entries. Record the exact launcher, package integrity, lockfile,
audit, backup and readback on the receiving machine. Machine paths stay local.

## Verification and boundaries

Track each capability as demonstrated, installed but untested, blocked or excluded.
Skill coverage is not evidence of tool execution. Native build and icon composition
have separate prerequisites. A passing browser comparison does not certify native UI.

Before marking an installation usable, start the MCP server, discover its tools
and perform a harmless operation on an owned synthetic fixture. Check each host's
registration. A host session that cannot invoke the server remains unverified even
if a direct MCP protocol check passes. Record unavailable optional dependencies.

REA's broad tool permissions are capabilities, not a project data boundary.
Stdio transport, local file modes and input checks enforce specific properties.
Task scope, provider approval and host confirmations remain instructions unless a
separate runtime mechanism enforces them. Do not describe them as a sandbox.

For each actual project, render and inspect the output, test keyboard and error
states, and measure the selected reconstruction claims. Keep private screenshots,
client data and runtime receipts outside this public repository.

Sources and exact pins: [toolchain register](../resources/toolchains.json).
Design-method details live in the installed skills. This document is a portable
setup and coverage guide, not evidence that another computer has been configured.
