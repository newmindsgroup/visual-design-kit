# Visual Design Agent

Version-Timestamp: 2026-09-14T11:33:51.300274-04:00

Private reusable design library and Visual Design Studio plugin candidate. Contains 130 selectable reference capabilities and one starting skill. Client projects belong in separate repositories.

Start with [package readiness](plugins/visual-design-studio/READINESS.md), [project setup](plugins/visual-design-studio/PROJECT-LAUNCH.md) and [feedback](plugins/visual-design-studio/FEEDBACK.md). See the [completion backlog](BACKLOG.md).

This is a curated first GitHub snapshot, not the full local research workspace or its history. Private books, client sources, generated experiments and provider receipts are excluded. The plugin is not yet installation-tested. Use the explicit starting-skill file path for supervised evaluation only; fresh-project execution remains to be verified.

The library lives inside plugins/visual-design-studio/library. Preserve paths when editing. PAYLOAD.sha256 covers raw payload bytes, excluding itself; update it deliberately after approved changes. Keep release versions immutable and pin a reviewed version in each adopting project. Improvements enter through reviewed, sanitized proposals rather than client-data synchronization.

Checks: plugin and skill schema validation, 322 payload hashes and ZIP byte roundtrip passed locally. Eight packaged Python tests and eleven JavaScript tests passed. These are bounded structural/behavior checks, not all-skill or creative acceptance.

## Installation checkpoint

Version-Timestamp: 2026-09-14T15:03:31.772234-04:00

Codex local installation and enabled-state readback now pass for 0.1.0; all installed payload hashes match. See [installation instructions](INSTALLATION.md). Automatic discovery failed under the host skill-context budget; explicit-path reading and bounded selection passed. Full project execution remains pending. Earlier uninstalled wording describes the initial snapshot.
