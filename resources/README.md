# Optional local references

Version-Timestamp: 2026-09-27 13:45:58 AST

The kit includes authored design instructions and a local reference utility. Books, source media, extracted text and the author's research collection are not included. No download link or access to that collection is offered by this public release.

You may supply your own local references when you have permission for the intended reading, extraction and use. A library is optional unless your task requires a particular source. If a required source is unavailable, record that limit; never claim to have consulted it. A complete reference-free production run has not been verified across every capability.

## Set up your own library

Keep source material outside the kit checkout and client repositories. The supplied utility expects a compatible catalog and manifest, not an arbitrary folder of PDFs. Follow [local setup](LOCAL-SETUP.md) for the file contract and commands, then use the [reference workflow](REFERENCE-WORKFLOW.md) to connect bounded evidence to a design decision.

A compatible library separates:

- `catalog/`: source IDs, relative original/extraction paths, edition and author details, source availability and rights records.
- `originals/`: only sources permitted for the intended use and recipients.
- `extracted/`: permitted searchable text with page or section locators.
- `methods/`: original reusable notes with citations and explicit review limits.
- `manifests/`: file paths and SHA-256 hashes for integrity checks.

Keep the local library path, private links and source-specific permissions in ignored project configuration. A checksum establishes file integrity against a manifest. It does not establish source quality, ownership, redistribution permission or full review. An extracted book retains the source's use restrictions.

## Historical author research

The [implementation record](LIBRARY-IMPLEMENTATION.md) documents the author's separate collection during September 2026. Its counts, extraction states, review attempts and transfer checks are historical author-only evidence. They do not describe files delivered with this repository, establish current availability or promise access to another user's books.

The public kit's license covers its stated original work. It does not license external books, private examples, third-party assets or any material you add. Check the terms for each source and intended use before extracting, transferring or sharing it.

[Local setup](LOCAL-SETUP.md) | [Reference workflow](REFERENCE-WORKFLOW.md) | [Acceptance checklist](TEAM-READINESS.md)
