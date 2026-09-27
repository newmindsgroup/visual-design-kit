# Standalone guidance and optional references, edition 0.3.0

Version-Timestamp: 2026-09-27T14:50:36-04:00

## Change and scope

The kit can start from its original methods and authorized project inputs without a private book library. Eight [applied method cards](../plugins/visual-design-studio/library/knowledge/README.md) add worked decision procedures, fictional examples, failure repairs and existing-template handoffs. Thirteen capability entries link the relevant cards. The catalog still has 130 capabilities and one discoverable entry skill; no duplicate capability or new provider was added.

The offline reference helper now supports explicit standalone and local-library modes, optional ignored configuration, bounded availability reports and source-dependent holds. Explicit standalone ignores stale settings. Auto mode uses only explicit/default project configuration, never a machine search. Status hashes the catalog and referenced extractions, checks original paths and metadata without reading their bytes, and emits no source text. Bounded error codes explain unavailable or corrupt inputs. Full verify additionally checks every listed file. Search checks the referenced corpus before emitting excerpts. None of these actions changes model weights.

An available library is not a consulted library. A named-source request still requires locating and inspecting that source; the availability flag cannot satisfy it. No-book startup records an empty consulted-source list, not a fabricated source record. Missing optional books do not block ordinary work. Missing required evidence holds only dependent work. A failed package pin remains a hard stop.

## Verification

- Root Python suite: 76 tests passed under both Python 3.9.6 and 3.14.4, including 44 reference-helper cases, 25 archive-import cases and 7 package-builder cases.
- Library Python suite: 49 tests passed. Dormant duplicate reference configuration logic was removed from template adoption; its coverage moved to the canonical helper tests.
- Node suite: 11 tests passed.
- Plugin and entry-skill validators passed.
- Package generation check passed; canonical and packaged reference helpers and archive importers match.
- The new method-to-capability/template mapping is in the handbook index. Existing typography, color and motion records retain ownership; no duplicate schema was introduced.

The new tests cover explicit standalone without config reads, invalid/missing configuration, unavailable roots, declared incompatible metadata, catalog/extraction coverage, corrupt bytes, unsafe paths and symlinks, legacy partial metadata, empty results, source locators and availability distinct from consultation. Raw test logs are retained locally outside the public payload.

A fresh Codex CLI 0.154.0 session in a separate temporary project verified the 375-file payload, selected typography and the new method card, and produced a bounded orphan-word repair plan with no books. An intentionally malformed private reference config did not affect explicit standalone mode. Its command trace showed no corpus/config read or network command. It preserved locked copy, font, logo and palette and reported rendered checks as pending. This proves bounded startup and instruction use, not artwork quality. A second fresh session resumed the same fixture against the final 376-file pin, verified every payload hash before executing the helper, and appended a checkpoint without changing the earlier repair plan. Both runs used explicit standalone mode and reported `consulted: false`. Claude Fable 5.1 completed the approach and two bounded milestone reviews. The final delta review reported no release blockers; the implementing agent also verified the full import and final pinned resume. No new visual artwork is changed by this edition. Existing rendered fixtures are historical evidence for their tested versions, not visual acceptance of future outputs.

## Optional archive import

An actual signed-out Drive transfer exposed a filename extension change. The separate importer addresses that observed problem: combine all ZIP parts, validate paths and manifest hashes, restore only an unambiguous appended extension with exact hash agreement, and install only into a new destination. Dry run is the default. The read-only reference helper still does not mutate sources. Download links and private collection contents stay outside GitHub.

The actual anonymous download contained two ZIP parts. Dry run and installation into a new local folder passed, including one exact-hash filename normalization. An independent full verification then passed all 723 manifest entries. Availability returned `consulted: false`; a separate retrieval found a typography excerpt with a source locator. These checks used a signed-out receiving context on the authoring Mac, not a second physical computer. The importer has 25 tests, including unsafe paths, collisions, corrupt bytes, unexpected files, destination races and parent substitution. Apply was exercised on macOS; Linux support is implemented but was not exercised here. Windows apply fails closed. See [setup instructions](../resources/LOCAL-SETUP.md#import-an-owner-provided-zip-collection).

## Original guidance and source boundaries

The method cards use original prose and fictional teaching examples. They do not reproduce chapters, promise all book knowledge, or claim that every source was synthesized. Optional books, extracts, private collection links and machine-specific configuration remain outside GitHub. An authorized collection owner may provide their download separately. See [reference setup](../resources/LOCAL-SETUP.md).

A local Qwen review proposed six possible omissions. Checking existing templates showed that file/license/fallback fields, color state/contrast records and motion fallbacks already exist. Those duplicate suggestions were rejected. Concrete decision examples were the useful improvement. Model confidence was not treated as evidence of a missing field.

## Upgrade and remaining acceptance

Use [the current pin](VERIFIED-PIN.md) and [installation](../INSTALLATION.md) in a separate project. Existing projects keep their earlier pins until they deliberately upgrade. Installed caches and other computers were not silently changed. Versions 0.2.0 and 0.2.1 remain historical baselines.

Native Cursor/Claude Code production, actual artwork quality, provider access, source-specific interpretation and target-device testing remain project-specific. Standalone means no private books are required; it does not mean missing client facts or human review can be skipped.

## Follow-up from review

One pre-existing, non-blocking search issue remains: a case-folded match position can shift when Unicode case folding changes the character count. This can offset the excerpt window for some multilingual terms; source locators and original files remain available for confirmation. Track that bounded repair separately from this release. No review or test result proves that every book has complete extraction, that figures were understood, or that future designs meet human quality expectations.

## Public distribution check

Version-Timestamp: 2026-09-27T14:54:28-04:00

PR 3 merged into public main at `86650767431afae226620504da619879aaf6f696`. A separate HTTPS clone with Git credential helpers and headers disabled verified all 376 payload entries and ran explicit standalone status successfully. The package digest is recorded in [VERIFIED-PIN](VERIFIED-PIN.md). A collection-specific setup guide was delivered separately through the authorized Drive folder, with viewer access confirmed; neither the collection nor its access link is included here.
