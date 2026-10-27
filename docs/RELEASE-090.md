# 0.9.0 native design and reconstruction candidate

Version-Timestamp: 2026-10-27 07:59:12 AST

Agent-Attribution: computer=NMG-MBP-M5; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 07:59:12 AST

This candidate adds complete BAMA and REA companion workflows to the same
marketplace used by Codex and Claude Code. The main plugin now has 19 skills,
including icon-design and reference-reconstruction. Existing UX, UI, native-app
and design-system methods gain macOS, placement, measured reconstruction and
state-gallery depth. It remains brand-agnostic; adopting projects own their
identity, data, components, stack, scope and acceptance.

BAMA Mac Studio preserves all 21 upstream skills, references, templates and
12 example specifications in a flat, namespaced tree. Guarded helpers add fresh
scaffolds, staged builds, explicit install/signing, isolated stores/preferences,
scale-aware comparisons and opt-in app CLI access. Upstream automatic global
links, broad staging, masked build/signing failures and destructive real-store
cleanup are replaced. Marketing banners and the standalone upstream marketplace
are omitted; the parent marketplace owns installation. MIT/source notices remain.

REA Toolkit preserves the complete shipping 6.8.0 skill 49 and seven references.
The separate exact runtime uses verified Node 24.22.1 and npm integrity, pinned
fast-uri 3.1.9/Zod 4.6.6 overrides and disabled lifecycle scripts. Final npm audit
reported zero vulnerabilities. No bulk server copy or machine path is published.

## Capability acceptance on the authoring Mac

| Capability | Status | Evidence and limit |
| --- | --- | --- |
| All 21 BAMA skills and resources | Packaged; host activation pending final checks | Same files for both manifests; project behavior not yet demonstrated |
| Native scaffold and isolated runners | Demonstrated | Seven scaffold/runner guard regressions; no automatic Git operation or installed-app replacement |
| Image and layout helpers | Demonstrated | Twenty image/layout cases including 1x/2x regions, required scale, bounds and threshold failures |
| Isolated preferences | Demonstrated | Foundation check preserves normal domain and cleans owned test suite |
| Complete SwiftUI/SwiftData template | Blocked | Selected CLT lacks macro plugins; --no-icon build failed correctly |
| Icon Composer output | Blocked | Full Xcode actool/ictool prerequisites not available |
| App UI, app CLI/MCP, signing and install rollback | Installed source but untested | Requires a successful native build and selected project acceptance |
| Full REA catalog | Demonstrated discovery | All 229 names and input schemas retained; not 229 execution tests |
| REA static JavaScript analysis | Demonstrated | Owned two-file fixture, zero parse failures and complete syntax examination |
| REA Codex/Claude registration | Demonstrated configuration/connection | Codex enabled; Claude native CLI Connected; Current Codex MCP analysis passed; Claude model-led invocation remains untested |
| REA browser, native and capture workflows | Installed but untested | Need selected targets and applicable OS permissions |
| REA deep engines and Frida | Blocked or unconfigured | Frida native binding absent; Hopper/Ghidra/IDA and other advanced providers not configured |
| New design methods | Instruction/package checks | Four behavioral eval cases added; no model-lift or client visual acceptance claim |

The idle REA session advertised 110 available tools, 72 needing a target, 36 needing
providers and 11 unsupported on this host. Some prerequisites are deferred until
invocation. Its shipping-supported output profile off reduces the catalog frame
from 3,505,030 to 302,268 bytes while preserving every name/input schema and the
tested result. This is 91.4 percent fewer bytes, not a measured token claim.

## Checks

148 repository tests, 191 library tests and 77 BAMA helper tests passed. Atlas 125/125,
token build/lint/check, main skill links/catalog, two-host parity and Claude
manifest validation passed. Optional toolkit payloads have deterministic integrity
checks. The root/companion hashes are recorded in the candidate pin after build.

The paid eval harness was not run. Independent native reviews checked the approach and source, identifying ten initial defects and four follow-up defects. Their repairs add bounded transport, typed MCP input validation, safe shared mutations, real deletion confirmation, complete snapshot receipts, explicit scale and actual layout coverage. Those findings were resolved with additional regression checks. Reviewers did not rerun the repaired code; real framework and visual acceptance remain separate. No real
client data, application deployment or production acceptance is part of this change.

## Next validation

1. Supply a working full Xcode toolchain and repeat the fresh native template build, isolated self-test, native screenshots and icon appearances.
2. Reconnect the receiving hosts and run an owned reconstruction task through the installed skills and REA tools.
3. Add optional analysis engines only when a concrete target requires them, then verify that exact path.

Setup, source pins and complete skill coverage: [TOOLKITS.md](TOOLKITS.md).

The new macOS26 CI job uses the runner's full Xcode to compile a fresh template, run core tests and compile the optional app CLI/MCP adapter. Its result must be read back from the PR. It does not install Xcode on the authoring Mac or certify native screenshots. Runner image reference: [GitHub macOS26 image](https://github.com/actions/runner-images/blob/main/images/macos/macos-26-Readme.md).

The follow-up repairs also close early self-test success, competing socket listeners, post-save oversized responses and display-scaled pixel crops. A real native isolation-path fixture uncovered and fixed `/var` versus `/private/var` normalization for a new store, while preserving escape rejection. Full local application compilation remains blocked on the selected CLT macro plugins.
