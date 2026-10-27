# BAMA Mac Studio

Version-Timestamp: 2026-10-27 16:58:23 AST

Agent-Attribution: computer=NMG-MBP-M5; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 07:55:46 AST

Complete 21-skill BAMA workflow for researching, observing, planning, designing,
scaffolding, building, profiling and testing native Mac applications. This is a
guarded derivative of [Dave Ebbelaar's BAMA](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310), not an upstream release.
All capability resources and 12 example specifications are retained. Two marketing
banners are omitted. Preserve the complete [MIT license](LICENSE).


```text
/plugin install bama-mac-studio --marketplace newmindsgroup/visual-design-kit
```

## Start

Install `bama-mac-studio@visual-design-team` with the existing Design Kit marketplace
in Codex or Claude Code. Both host manifests load the same `skills/` tree. Do not
also install unchanged upstream BAMA globally. Start a fresh host session and ask
to use `bama-router` for the selected Mac application task.

Read [ADAPTATION.md](ADAPTATION.md) before running helpers. It defines staged
builds, fresh scaffolds, isolated stores and preferences, image scale checks,
explicit installation/signing operations and the optional app CLI trust boundary.
Project instructions, approved DESIGN.md and canonical tokens remain authoritative.
The source map and file hashes are in [DERIVATION.json](DERIVATION.json).

## Workflow and skills

| Stage | Skill |
| --- | --- |
| Native app workflow | [bama-agent-cli](skills/bama-agent-cli/SKILL.md) |
| Native app workflow | [bama-app-brief](skills/bama-app-brief/SKILL.md) |
| Native app workflow | [bama-app-icon](skills/bama-app-icon/SKILL.md) |
| Native app workflow | [bama-build-and-verify](skills/bama-build-and-verify/SKILL.md) |
| Native app workflow | [bama-clone](skills/bama-clone/SKILL.md) |
| Native app workflow | [bama-design-from-app](skills/bama-design-from-app/SKILL.md) |
| Native app workflow | [bama-design-kit](skills/bama-design-kit/SKILL.md) |
| Native app workflow | [bama-design-system](skills/bama-design-system/SKILL.md) |
| Native app workflow | [bama-improve-architecture](skills/bama-improve-architecture/SKILL.md) |
| Native app workflow | [bama-improve-loop](skills/bama-improve-loop/SKILL.md) |
| Native app workflow | [bama-layout-grid](skills/bama-layout-grid/SKILL.md) |
| Native app workflow | [bama-mac-design](skills/bama-mac-design/SKILL.md) |
| Native app workflow | [bama-new-mac-app](skills/bama-new-mac-app/SKILL.md) |
| Native app workflow | [bama-os-integrations](skills/bama-os-integrations/SKILL.md) |
| Native app workflow | [bama-performance](skills/bama-performance/SKILL.md) |
| Native app workflow | [bama-research](skills/bama-research/SKILL.md) |
| Native app workflow | [bama-router](skills/bama-router/SKILL.md) |
| Native app workflow | [bama-swift-swiftui](skills/bama-swift-swiftui/SKILL.md) |
| Native app workflow | [bama-test-mac-app](skills/bama-test-mac-app/SKILL.md) |
| Native app workflow | [bama-user-stories](skills/bama-user-stories/SKILL.md) |
| Native app workflow | [bama-ux-design](skills/bama-ux-design/SKILL.md) |

## Prerequisites and acceptance

The upstream baseline is macOS26 and Swift6.2 or later. Pin each actual project's
minimum OS and supported APIs rather than silently raising an existing baseline.
The selected Apple toolchain must support the full SwiftUI/SwiftData macro build.
Icon Composer compilation additionally needs actool and its ictool.

The earlier Command Line Tools macro prerequisite is resolved on the authoring
Mac with full Xcode. A fresh repaired starter passed a code build, core tests,
nine isolated self-test checks and eight native snapshot contract checks.
The 1.0.0-adapted.2 template explicitly aligns its native toolbar with the window's
color scheme. Read the current follow-up in [ADAPTATION.md](ADAPTATION.md) for
visual evidence and limits. Signing, install/rollback and distribution remain
project acceptance. Installing skills does not install Xcode or grant OS permissions.

The three standalone Swift image/layout tools compile on the authoring Mac.
Use explicit capture scale for a region comparison; never assume2x from a filename.
Render native output and exercise keyboard, error and recovery behavior in a real
project before claiming an application milestone complete.

## Maintenance

Run the included Python regression tests and applicable Swift helper checks.
Use the parent kit's two-host validation and optional-toolkit integrity builder.
Keep upstream source attribution and adapted hashes current after changes.
Do not put client captures, real stores, build artifacts or private receipts here.

## Upstream resource credits

BAMA credits [REA](https://github.com/morluto/rea), [Matt Pocock's skills](https://github.com/mattpocock/skills) and `writing-for-agents`, [Paul Hudson's SwiftUI Pro skill](https://github.com/twostraws/SwiftUI-Agent-Skill), and [Antoine van der Lee's SwiftUI Expert skill](https://github.com/AvdLee/SwiftUI-Agent-Skill). These resource links are retained for discovery. The two supplementary SwiftUI collections and Matt Pocock collection are not installed by this companion; review their exact source, license and overlap before selecting one. The full BAMA and REA workflows are already included in this kit.
