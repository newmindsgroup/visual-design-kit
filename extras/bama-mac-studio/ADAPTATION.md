# BAMA derivative execution and source record

Version-Timestamp: 2026-10-27 17:02:30 AST
Agent-Attribution: computer=NMG-MBP-M5; tool=Codex; version=0.160.0; timestamp=2026-10-27 07:44:20 AST

Source: [BAMA](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310), copyright 2026 Dave Ebbelaar, MIT. [LICENSE](LICENSE) is retained verbatim. [DERIVATION.json](DERIVATION.json) maps each packaged source to its origin and both hashes. This derivative retains all 21 skills, all their references/templates/assets, and the 12 example specifications. Names use bama-* and host-neutral invocation. Capability preservation does not imply successful runtime acceptance.

The owning Design Kit installs this package for Codex and Claude Code. Use its existing installation and update flow, keeping both host exports in parity. There is no second BAMA global install. Native capture, browser access, developer tools, provider access and permissions depend on each host. Read the project's instructions, canonical DESIGN.md and token files before any design work. BAMA briefs, galleries, kit docs and glossary files are subordinate implementation evidence.

## Commands and authorization

- Scaffold: `skills/bama-new-mac-app/scripts/new-app.sh AppName com.example.app /existing/parent`. Requires a fresh destination; validates names; never initializes Git, stages or commits. Existing briefs are copied into the fresh project afterward.
- Build: `./build.sh` stages in the project's `.build/bama-stage`; uses full icon tooling when the .icon source exists. `--no-icon` omits that optional pipeline. Both preserve compiler failure status. Default staging is unsigned. `--sign-identity -` opts into ad hoc signing, or explicitly name the authorized identity. The helper never enumerates certificates or clears extended attributes.
- Install: `./build.sh --install` explicitly moves a successful app into ~/Applications and preserves any previous bundle as a backup. Failed replacement restores the prior bundle where possible. Report the actual backup path. `--open` opens the output without quitting any other app. These flags require the current task to authorize those actions.
- Tests: `tools/selftest.sh /explicit/staged/binary` and `tools/snap.sh /explicit/staged/binary` use a fresh marked private bama-test-* temporary root with APP_TEST_ROOT and APP_STORE. No real store or Saved Application State is deleted. A snapshot without PNG output fails. The template's central AppPreferences adapter uses a fresh unique UserDefaults suite for a marked test root, routes AppStorage and explicit preferences to it, and clears only that test domain on normal termination. Production keeps UserDefaults.standard. The standalone Swift 6 test verifies normal-domain preservation and test-domain cleanup; a forced crash may leave its uniquely named test domain for later cleanup. Evidence is retained in that isolated root. Do not directly reuse legacy /tmp store commands from upstream examples.
- CLI/MCP: `skills/bama-agent-cli/scripts/add-agent-cli.sh /app/folder cli-name` modifies app-local code only and rolls back its known file changes on failure. It does not link PATH, register MCP or edit host permissions. Build the staged app, then enable the app-local listener with APP_AGENT_ENABLED=1. It defaults to read commands. APP_AGENT_WRITES=1 separately enables writes for that authorized app session. Destructive commands still require their own confirmation. The socket limits request bytes and serves one client at a time, validates command argument keys/types, refuses non-socket replacement and symlink socket targets. Same-user processes share its trust boundary. This is a local utility adapter, not tenant isolation or strong caller authentication.
- CLI check: `skills/bama-agent-cli/scripts/check-agent-cli.sh /explicit/staged/binary` creates a private marked temporary root, starts its own test process, checks schema/read commands/default write denial/MCP coverage and stops only that owned process. It never calls a hosted agent over real records.
- Image measurement: set task-local `skill_dir` to the selected SKILL.md's resolved directory, then run its scripts. Measurement validates command arity, scale and image/region bounds. Compare requires equal dimensions and a new output directory; optional `--threshold <percent>` makes an exceeded pixel-difference metric fail. Region comparison requires explicit --scale N for the capture's pixels per logical point, including 1x and 2x. Full-image comparison uses raw pixels. Validate scale and viewport before comparing. Pixel similarity is one diagnostic, never proof of accessible behavior or design suitability.
- Grid: layout checking requires a positive unit, supplied files and nonempty probes. The 4 pt source convention can be adapted to the approved project's grid.
- Icon design: source .icon/SVG authoring, concept work and small-size review remain available. Compilation uses actool and rendering uses Icon Composer ictool. No automatic app installation, Dock restart or permission/system-setting change is part of icon design.
- Capture: observe only the authorized app/reference and permitted data. Prefer a supported scoped window/browser tool. A full-screen screenshot may include unrelated data and needs scope. Do not change accessibility, Screen Recording, VoiceOver, display, appearance or other system settings merely because an upstream checklist mentions the check.

The 21 adapted entry contracts govern legacy source examples. Use actual project paths and the staged binary, not the upstream ~/Applications placeholders. The skill text grants no commit, install, permission change, hosted fresh-agent session or unrelated refactor authority. Current task/repository authorization can already cover scoped story commits; stage explicit paths and include required attribution. Existing session authorization remains valid; do not repeatedly seek approval for actions already in scope.

## Validation and limits

Eighteen automated cases pass: six scaffold/isolated-runner cases, eleven synthetic image/layout cases and one actual Swift 6 preference-isolation case. Scaffold regressions were observed failing against upstream before repair. Three standalone Swift helpers compiled, and eleven synthetic image/layout CLI cases passed, including threshold failure, bounds, invalid scale and empty-input failures. Python compilation and shell syntax are checked separately.

A fresh full SwiftUI/SwiftData template scaffold was attempted with --no-icon and correctly failed. Selected Command Line Tools could not locate SwiftUIMacros.StateMacro and SwiftDataMacros.PersistentModelMacro plugins. Full Xcode and its icon tools are a remaining host prerequisite. No Xcode install/selection, signing identity, installed app, system permission or user data was changed. Full app selftest, CLI/MCP runtime, screenshot UI acceptance and Icon Composer output remain unverified until that prerequisite is available. Do not describe source/package validation as a working native app.

Standalone capture, icon and CLI helper paths require proportionate project validation before production. The CLI socket hardening has source and syntax evidence, not a successful native app execution on this host. Install/rollback code has not replaced a real application during this preparation.

## Independent-review source repairs

Version-Timestamp: 2026-10-27 08:25:55 AST

The final source review found and repaired inherited behavior, not just wording:

- Socket connections have monotonic read/write/connect deadlines, SIGPIPE protection and descriptor cleanup. Requests are bounded to 64 KiB, responses to 8 MiB. Oversize replies give an explicit error. Lost replies never cause an automatic replay of a possibly completed write.
- MCP validates original JSON value types, required arguments, unknown keys and boolean confirmation before conversion. Its advertised additionalProperties rule matches enforcement.
- App mutation methods share title normalization and a clean-context save boundary. Agent writes refuse pending interface edits. UI commands preserve those edits if their initial save fails. Failure rolls back only the operation-owned changes; selection changes only after success.
- The template honors its deletion-confirmation setting, supports cancel and exposes recoverable errors. Custom detail content has actual layout probes.
- Snapshot acceptance requires the independently declared page/theme matrix, actual distinct Settings identity, native capture status and structurally valid bounded PNGs. Missing or degraded captures fail, including direct app exit. Inherited modes are cleared and output remains inside the owned root.
- Image info without a declared scale reports pixels and unknown logical scale. Coordinate operations require measured --scale or explicit --pixels. Area-only, duplicate and uninstrumented layout records cannot report a verification pass.
- Scaffolding claims its destination atomically and only cleans a directory whose identity it owns. Another creator's files are preserved.
- Workflow descriptions now match staged unsigned builds and app-local CLI integration. Faithful reconstruction is preserved; native-control substitutions require a declared adaptation.

The BAMA suite now has 77 passing tests on the authoring Mac, including standalone
Swift 6 transport, preferences and model-guard components. Full SwiftData/UI runtime
is still a separate check. The parent macOS 26 CI job builds the full template,
compiles icons, runs core tests and a synthetic self-test, then compiles the app
CLI/MCP integration. Its actual result must be read back; source tests do not
predict a pass. No real user database or installed application is exercised.

## Follow-up repairs and current host evidence

Version-Timestamp: 2026-10-27 09:23:35 AST

Bounded mutation receipts report completed outcome and full identity without
serializing unbounded notes after a save. Lists use a 4 MiB serialized page budget,
advance by actual returned rows, and explicitly summarize an oversized record.
The generic transport preserves ok:true/completed:true when a successful
handler's result must be omitted, rather than reporting a failed mutation.
A private lifetime advisory lease prevents competing listeners from replacing
a live socket; stale reclamation requires a definite refused endpoint and
identity/owner checks. The lease coordinates same-user processes, not callers.

Self-tests start failed and require a bounded atomic completion receipt with all
required checks passed. Early normal exits cannot pass. New and existing test
stores normalize existing ancestors with realpath before appending missing names;
private-var aliases, symlink escapes, traversal, relative paths and NUL are tested.
Pixel crops use explicitly sized CGContexts and verify their encoded dimensions;
actual 1x/zoom/asymmetric content checks pass independently of display scale.

All 77 BAMA tests pass locally. These include real standalone Swift 6 components
and fixture contracts, not full SwiftData/UI acceptance. Native CI and actual
rendered UI/capture inspection remain separate. The current Codex task did invoke
REA 6.8 tools over its own two-file synthetic fixture and export Evidence, with
complete selected syntax and explicit semantic/application unknowns.

## Toolbar theme follow-up, 1.0.0-adapted.2

Version-Timestamp: 2026-10-27 17:02:30 AST

The historical macro prerequisite above is resolved on the authoring Mac with
Xcode 27.1. A fresh repaired starter on macOS 26.6.2 passed a code-only build,
four parameterized core cases, nine isolated self-test checks and eight native
snapshot contract checks. No signing or app installation was performed.

The native toolbar title could inherit a dark appearance in an active light
window. The template now passes its window color scheme to `.toolbarColorScheme`
for `.windowToolbar`, retaining native titles and semantic colors. Separate
foreground verification covered both pages and both Settings tabs in light to
dark and dark to light runs. Each capture recorded the owned process/window,
active application, key window and matching foreground process. Command-N created
and selected a new item. The controlled All Items title region changed from
1.119:1 to 14.938:1 in light; dark measured 12.561:1. These pixel diagnostics are
regression evidence, not a complete accessibility audit.

Foreground captures used an already authorized external controller over only the
owned window. Only a diagnostic snapshot driver added gates and native-view
inspection; application, model and theme code remained the production version.
Its incomplete in-app capture manifests remain distinct from the untouched
production snapshot suite, which passed all eight captures. No OS privacy or
global appearance settings were changed. Existing generated apps require the same
focused patch and project-specific verification; plugin updates do not rewrite them.
