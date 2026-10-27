# 0.9.1 dependency repairs and local toolchain readiness

Version-Timestamp: 2026-10-27 12:38:31 AST

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 12:27:57 AST

This candidate patches the five vulnerable dependencies behind 16 existing GitHub
alerts in four examples. Every complete example lock now audits clean. CI audits
the locked dependencies before its example checks so new advisories remain visible.
No alert is dismissed. Default-branch alert closure requires the fix to land and
GitHub to rescan it; a clean candidate audit does not close default-branch alerts.

| Example | Dependency | Previous | Fixed |
| --- | --- | --- | --- |
| Astro motion | undici | 8.12.1 | 8.12.2 |
| Astro motion | fast-uri | 3.1.8 | 3.1.9 |
| React system | vite | 8.3.2 | 8.3.4 |
| Remotion motion | zod | 4.5.4 | 4.6.7 |
| PPTX deck | image-size | 1.2.1 | 2.0.3 |

The transitive fixes use exact overrides. Existing framework and composition
versions remain pinned. Install scripts were disabled during local installation.
Astro now declares Node22.19+ or Node24+ to match Undici's engine requirement,
with Node23 excluded. All 176 relevant resolved engine constraints match22.19
on macOS ARM64. This is a metadata check; actual local builds used Node24.22.1.
CI checks the current Node22 line separately.

PptxGenJS4.0.1's published JavaScript bundles do not import image-size. The example
still retains its dependency, so it is patched rather than ignored. Existing deck
tests/builds pass. An additional owned8x4PNG check passed image-size decoding plus
ESM/CommonJS, buffer/file inputs, contain/crop serialization and exact embedded
PNG bytes. This does not promise compatibility for arbitrary image-size1 consumers.

Advisory sources: [Undici](https://github.com/advisories/GHSA-xjj6-f33q-929c),
[fast-uri](https://github.com/advisories/GHSA-w74x-v6f9-j3xg),
[Vite](https://github.com/advisories/GHSA-587h-7wmj-h5pm),
[Zod](https://github.com/advisories/GHSA-mrhx-c7xc-m3w5),
[image-size](https://github.com/advisories/GHSA-5p2g-fcmc-qvqq).

## Receiving-machine readiness

Xcode27.1 was installed from Apple's free App Store on the authoring Mac. Its
Apple signing chain was verified, and the user personally accepted the Xcode/SDK
agreement. A fresh local native app/icon build, core test, nine self-test checks, eight
window captures and optional app CLI/MCP compile/runtime checks passed. Visual inspection found one bounded limitation: on Xcode27.1, the starter
window toolbar title stays pale in forced light captures even with the window
confirmed active. Dark mode, content, Settings and icon output were inspected.
No unproven color or timing workaround was shipped; resolve that title behavior
before treating a derived light-mode app as visually accepted. User-started simulator downloads are independent
of Mac app compilation and remain user-owned.

A prepared machine is not a prepared client project. Each project retains its
brand, tokens, version pins, data permissions, target identity and release checks.
Use an owned synthetic pilot before processing client targets. Optional paid
engines, other-platform tools and task-specific OS privacy permissions remain
separate from baseline local setup.

Setup and capability coverage: [TOOLKITS.md](TOOLKITS.md).

REA's free Mac baseline now includes Frida17.23.2, Ghidra12.1.4, signed
Temurin21.0.13+9 and WABT1.0.42, with isolated CMake4.2.3 for its source build.
Owned browser interaction, Frida instrumentation, Mach-O decompilation and WASM
validation passed. Both host entries retain their launch/policies and have matching
provider paths; unrelated settings were preserved. A fresh configured MCP process
discovered all229 tools, exercised native/WASM paths and closed cleanly. Claude
CLI reports Connected; a Claude model-led invocation was not performed. Existing
agent sessions must reconnect to load the new provider variables.

## Later toolbar repair

Version-Timestamp: 2026-10-27 17:02:30 AST

The light-mode toolbar limitation above was reproduced and repaired in
[BAMA 1.0.0-adapted.2](RELEASE-BAMA-ADAPTED2.md). That edition records the actual
foreground evidence, both transition directions and the unchanged package scope.
