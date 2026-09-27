# Standalone design and optional local references

Version-Timestamp: 2026-09-27 14:19:56 AST

Start in standalone mode with the packaged design instructions, original [method cards](../plugins/visual-design-studio/library/knowledge/README.md), and authorized project inputs. Books are optional. The kit does not train a model on them or claim to have synthesized an entire collection.

A compatible local library adds deeper, traceable source evidence when a task benefits from it. It is a separate input, supplied by you or provided separately by an authorized collection owner if available. This public repository includes no books or public book download. A complete production run across every capability and host has not been verified.

## Choose the reference mode

| Mode | Use | When a library is unavailable |
| --- | --- | --- |
| Standalone | Packaged guidance and authorized client inputs | Continue ordinary design work and record that no book source was consulted. |
| Local library | The same foundation plus selected, inspected sources | Record the reason and continue standalone where inputs suffice. Hold only a claim or task that requires the missing source. |

The helper's default `auto` setting selects between these modes. Explicit `standalone` skips local configuration and corpus checks, including stale configuration. Library availability never means a source was consulted. Failed package verification remains a stop before executing bundled code, regardless of reference mode.

## Add a library when useful

Follow [local setup](LOCAL-SETUP.md) for acquisition, ignored configuration and commands, then the [reference workflow](REFERENCE-WORKFLOW.md) for bounded retrieval. The helper accepts a compatible catalog and manifest, not an arbitrary PDF folder. Keep books, extracted text and machine paths outside shared project files.

A compatible library separates source identity and availability in `catalog/`, permitted source files in `originals/`, searchable units in `extracted/`, and file-integrity records in `manifests/`. Optional `methods/` notes should be independently written and explicit about review limits. Extracted text keeps the source's use restrictions. A checksum establishes integrity against a manifest, not ownership, quality, redistribution permission or full review.

The [historical implementation record](LIBRARY-IMPLEMENTATION.md) describes the author's separate collection and dated checks. Its counts do not describe this release or establish current availability. The kit license covers its stated original work, not external books, private examples, third-party assets or material you add.

[Local setup](LOCAL-SETUP.md) | [Reference workflow](REFERENCE-WORKFLOW.md) | [Acceptance checklist](TEAM-READINESS.md)
