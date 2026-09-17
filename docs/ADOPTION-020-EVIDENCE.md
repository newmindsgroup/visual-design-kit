# Adoption integration evidence

Version-Timestamp: 2026-09-16 18:26:45 AST

## Scope

This is a bounded integration check of the uninstalled 0.2.0 candidate. It exercised the template adopter against temporary independent project folders only. It does not establish package manifest validity, installation, registered-skill discovery, human acceptance, or a release.

## Actual checks

| Check | Result | Evidence and limit |
| --- | --- | --- |
| `stage-execution.md` adoption | Pass | A fresh project root and destination directories both contained spaces. Dry-run created no file. `--apply` created the new record and rewrote all five library-local instruction links to existing pinned absolute destinations. |
| `typography-decision.md` adoption | Pass | The same independent project flow copied the template. It contains zero Markdown library-local links, so no rewrite was required. Its record placeholders remained unchanged. |
| Nested and fragment links | Pass | The stage packet's nested `../HANDOFF-CONTRACT.md` reference resolved after adoption. A percent-encoded, angle-bracket destination with a fragment and title was rewritten to an angle-bracket absolute library path while preserving its fragment and title. |
| Output containment | Pass | The final eight-test adopter suite rejects traversal, an existing output, source-file and destination-directory symlinks, and a configured book-tool symlink. Output creation descends a directory-descriptor chain with no-follow flags, then uses descriptor-relative exclusive creation with `O_NOFOLLOW`; pathname replacement cannot redirect that opened chain. This is a deterministic local filesystem check, not hostile-kernel concurrency certification. |
| Resume recovery | Pass for documentation contract | A copied `RESUME.md` retained a named approved baseline and a separately named rejected candidate. A minimal `CURRENT.md` pointer contained no competing state. The contract says the rejected revision cannot replace the approved baseline. No validator currently enforces semantic promotion of arbitrary handwritten resume records. |
| Optional book configuration | Pass for absence | With no `private/reference-library.local.json`, resolution returned no book configuration and ordinary template adoption continued. |
| Focused adopter suite | Pass | `PYTHONPATH=plugins/visual-design-studio/library python3 -m unittest plugins/visual-design-studio/library/tests/test_adopt_template.py` passed all 8 tests. |
| Full library suite | Pass after repair | The earlier suite snapshot ran 36 tests successfully. A transient 41-test snapshot then had 3 `test_selection.py` errors on malformed catalog or disposition inputs. After the selection-worker repair, its focused 15 tests passed and the final `unittest discover` run passed all 41 tests. `py_compile` and `git diff --check` passed for the adoption work. |

## Book utility inspection

The canonical source is `tools/reference_library.py`, SHA-256 `e65933b72def2622d19ced7a73c6779e807e789834a8c6dbb4edac399301a51b`. It supports exactly `--root ROOT verify` and `--root ROOT search QUERY --limit 1..100`; a missing root returns JSON error and a nonzero exit. No `reference-techniques.json` exists in the candidate.

The minimal root-owned packaging step is to copy that source byte-for-byte to `plugins/visual-design-studio/library/scripts/reference_library.py`, verify equal SHA-256 bytes, then regenerate the package manifest/checksum through the existing release workflow. No book, annotation catalog, installer, automatic configuration reader, or execution of a configured tool is required for this step.

## Material integration holds

1. `plugins/visual-design-studio/README.md` still has a 0.1.0-era timestamp and only links to readiness and project launch. It does not show the adopter's dry-run and `--apply` startup command or the `CURRENT.md` legacy rule. The wrapper startup skill and library workflow contain those instructions, but the wrapper README is not yet a complete fresh-host startup path.
2. The packaged `library/scripts/reference_library.py` copy is absent. The optional book route remains unavailable unless a project supplies an explicit trusted tool path. This is correctly nonblocking for ordinary design work.
3. The semantic distinction between approved and rejected resume entries is a documented project-record contract. A handwritten `RESUME.md` has no schema validator, so a receiving human or agent must follow the contract until a separate validator is authorized and implemented.

## Resolved transient selection failure

The earlier 41-test red snapshot had three selection-validator error cases for malformed catalog or disposition inputs. That snapshot is retained above as historical evidence. The selection worker repaired those cases; final verification ran `test_selection.py` with 15 passing tests and the full library suite with 41 passing tests. It is no longer an integration hold.
