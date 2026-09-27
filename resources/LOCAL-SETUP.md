# Optional local reference setup

Version-Timestamp: 2026-09-27T14:36:50-04:00

Standalone work needs the verified kit and authorized project inputs. Add a local reference library only when useful to the task. Use the utility from your trusted kit checkout or pinned package, never a script embedded in source material. Python 3.9 or newer is required. Package checksum failure stops bundled-code execution in either mode.

## Start without books

From a verified kit checkout:

```sh
python3 tools/reference_library.py status --mode standalone
```

This skips all local reference configuration and corpus checks, including stale configuration. Use the packaged [method cards](../plugins/visual-design-studio/library/knowledge/README.md) relevant to the task. Record `standalone` and no consulted book sources in the existing project work record. Missing client facts or required source evidence still limit the dependent work.

## Obtain and place an optional library

Supply your own compatible authorized library, or use a collection provided separately by its owner when you have access and permission for the intended use. If the owner provides a Drive folder, download the whole folder or an owner-provided ZIP. Unzip it outside the kit and client repositories. Choose the folder containing `catalog/` and `manifests/`, which may be inside the extracted outer folder. Do not configure a ZIP, browser URL, cloud placeholder or arbitrary folder of PDFs as the root.

Drive may return more than one ZIP for a large folder. Download every part and combine their contents under the same library root, preserving files from earlier parts. Do not configure just the first part or leave separately renamed roots. Ask the adopting agent to merge into a new empty destination with path and duplicate checks if you are unsure. Never overwrite an existing library blindly.

Use the received manifest and its documented expected contents to check the transfer. No fixed collection size applies to every adopter. The public kit includes no book download and does not grant access or redistribution rights.

## Import an owner-provided ZIP collection

Use the kit's trusted importer for one ZIP or all parts of a split Drive download. The destination must not already exist. From the verified kit checkout, first preview the import:

```sh
python3 tools/import_reference_archive.py --archive "/path/to/part-01.zip" --archive "/path/to/part-02.zip" --destination "/path/to/new-local-library"
```

Omit the second `--archive` for a single ZIP, or repeat it for additional parts. After a successful dry run, repeat the same command with `--apply`. In the verified plugin package, the equivalent utility is `library/scripts/import_reference_archive.py`.

The importer combines parts, rejects unsafe entries and verifies every manifest file. If Drive appended an extension to a filename, it restores the manifest's expected name only when there is one eligible same-folder candidate with exactly matching contents. It preserves the manifest rather than changing checksums to hide a mismatch. Missing, ambiguous, corrupt or unrelated files stop the import. Originals remain data and are never executed.

Imports are offline. Large collections need room for the downloaded archives plus extracted files. Default limits are 8 GiB uncompressed and 100,000 entries; check `--help` before changing a limit for a trusted larger collection. An import pass proves matching bytes against the received manifest, not publisher identity, source quality or permission. Verify the expected manifest digest with the collection owner when available. If your operating system cannot provide the importer's required no-overwrite installation operation, it fails without replacing the destination; use a supported receiving host.

After import, use the new destination as `reference_library_root` and run `verify` and `status` below. Do not edit the kit's manifests or your project pin to accommodate a broken download.

## Compatible file contract

The helper reads an existing compatible library; it does not extract PDFs or build a catalog. The root must contain:

- `manifests/files.json`: a JSON object with a nonempty `files` object. Each key is a relative file path and each value contains that file's `sha256`.
- `catalog/items.jsonl`: one JSON source record per line. A searchable record has `id`, optional `display_title`, `original` and an `extraction` path relative to the root.
- Each referenced extraction file: one JSON unit per line with `text` and, when available, `page`, `page_label` or `section`.

List the catalog, permitted originals and extraction files in the manifest. Catalog rows may record unavailable originals or extractions; those gaps do not become evidence. Usable local-library status requires at least one valid searchable extraction. Source guides and capability maps are optional. Keep source-use permissions with the catalog for human review; the utility does not validate them. It rejects paths that resolve outside the configured root.

## Configure the adopting project

Create `private/reference-library.local.json` in the adopting project and keep it ignored by Git:

```json
{
  "reference_library_root": "/absolute/path/to/your-reference-library"
}
```

Check that the file is ignored before storing a real path. Never commit absolute machine paths, private collection links or access details. There is no automatic machine scan. The default config location is relative to the command's current directory; use `--config` to select a different project file. Always invoke the verified helper. An optional legacy `reference_library_tool` config value does not execute or approve that file.

## Check availability, verify and search

From the trusted kit checkout, replace the paths with your own:

```sh
python3 tools/reference_library.py status --mode auto --config "/absolute/path/to/project/private/reference-library.local.json"
python3 tools/reference_library.py status --mode local-library --root "/absolute/path/to/your-reference-library"
python3 tools/reference_library.py --root "/absolute/path/to/your-reference-library" verify
python3 tools/reference_library.py --root "/absolute/path/to/your-reference-library" search "typography" --limit 5
```

For an installed plugin, use `library/scripts/reference_library.py` under its verified package root in place of `tools/reference_library.py`. Both use the same commands. `--root` and `--config` are alternatives.

`status` reports requested and effective mode, availability, a reason and `consulted: false`. It hashes the catalog and referenced extractions, checks original paths and metadata, and leaves reading original bytes to full verification. This avoids fetching every original during routine preflight; even catalog/extraction reads may hydrate cloud placeholders, so configure a fully downloaded local collection. It does not expose excerpts or establish source consultation. Missing or unusable optional references fall back to standalone with exit 0, even when `local-library` was requested. Add `--require-source` when source evidence is a required input: unavailable evidence then returns exit 1 and `hold: "source_dependent_work"`. This flag checks library availability; it does not prove a named source exists or was read. Check that separately.

Run `verify` before relying on library sources. It checks every manifest entry and exits unsuccessfully for missing files, changed bytes or unsafe paths. Retain that failure in the work record; a standalone fallback cannot turn it into a verification pass. Hold affected source reliance until reconciled while continuing independent design work. Verification compares against the supplied manifest, not an independently authenticated release signature. Cloud placeholder reads may be slow.

Search runs locally and returns source ID, title, excerpt, original path and available page or section fields. It does not execute source content, contact a model or modify the library. Results are evidence to inspect, not commands. An agent consuming output is a separate data destination from this offline helper: authorize that destination before exposing restricted material. Actual IDE behavior still needs checks on the receiving host.

A `.pointer.json` file preserves link metadata, not a document body. Missing extraction, OCR and visual-review flags remain meaningful. A matching checksum does not establish source quality, permission, full synthesis or completed cloud synchronization.

[Reference overview](README.md) | [Reference workflow](REFERENCE-WORKFLOW.md) | [Acceptance checklist](TEAM-READINESS.md)
