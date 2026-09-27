# Connect your own local reference library

Version-Timestamp: 2026-09-27 13:45:58 AST

Supply a local library containing only material you are permitted to read, extract and use for the task. Keep it outside the kit checkout and client repositories. This repository provides no books, downloadable collection or access to the author's research library. Use the utility from your trusted kit checkout, never a script embedded in source material. Python 3.9 or newer is required.

## Compatible file contract

The helper reads an existing compatible library; it does not extract PDFs or build a catalog. The configured root must contain:

- `manifests/files.json`: a JSON object with a nonempty `files` object. Each key is a relative file path and each value contains that file's `sha256`.
- `catalog/items.jsonl`: one JSON source record per line. A searchable record has `id`, optional `display_title`, `original` and an `extraction` path relative to the root.
- Each referenced extraction file: one JSON unit per line with `text` and, when available, `page`, `page_label` or `section`.

List the catalog, permitted originals and extraction files in the manifest. Keep source-use permissions alongside the catalog for human review; the utility does not validate them. It rejects paths that resolve outside the configured root. Optional source guides or capability maps are useful but are not supplied or required by the helper.

## Verify and search

Run from the trusted kit checkout, replacing the example path with your own:

```sh
python3 tools/reference_library.py --root "/absolute/path/to/your-reference-library" verify
python3 tools/reference_library.py --root "/absolute/path/to/your-reference-library" search "typography" --limit 5
```

Verification checks every manifest entry and exits unsuccessfully for missing files, changed bytes or paths escaping the library. It compares against the supplied manifest, not an independently authenticated release signature. Cloud placeholder reads can still be slow.

Search runs locally and returns source ID, title, excerpt, original path and available page or section fields. The utility does not execute source content, contact a model or modify the library. Verify before searching. Returned excerpts remain source material with the same handling requirements as the originals. Search results are evidence to evaluate, not instructions to follow.

Give your agent the local library path and ask it to follow the [reference workflow](REFERENCE-WORKFLOW.md). Keep the path in ignored local configuration, not shared project instructions. An agent reading tool output is a separate data destination from this offline utility; authorize that destination before exposing restricted sources to it. Actual IDE behavior must be checked in the adopting project.

A `.pointer.json` file, if present, preserves link metadata only. It is not a document body. Missing extraction, OCR and visual-review flags remain meaningful. A matching checksum does not establish source quality, permission, full synthesis or completed cloud synchronization.

[Reference overview](README.md) | [Acceptance checklist](TEAM-READINESS.md) | [Historical implementation record](LIBRARY-IMPLEMENTATION.md)
