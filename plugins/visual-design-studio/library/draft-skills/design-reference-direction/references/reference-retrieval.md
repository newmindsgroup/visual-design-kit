# Problem-based reference retrieval

Version-Timestamp: 2026-09-27 14:19:56 AST

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.149.1; timestamp=2026-09-08 22:17:00 AST

Search by the communication problem, medium and constraint before choosing style. A query such as "portrait crop subject clarity" is more decision-useful than "beautiful website". Use the existing source register and its original authority/rights status. An annotation can explain a technique without copying a source asset or promoting its claims.

Start with the selected capability, task-relevant original [method cards](../../../knowledge/README.md) and authorized project inputs. Book retrieval is optional and has no bundled annotation catalog. It adds source evidence; it does not train the model or establish that every book was synthesized.

Invoke the verified packaged `library/scripts/reference_library.py` helper with `status --mode auto` from the adopting project, or supply an explicit `--root` or `--config`. Its default configuration is ignored `private/reference-library.local.json` with `reference_library_root`; it does not scan the machine. Explicit `status --mode standalone` skips config and corpus access, including stale configuration. A missing or unusable optional library falls back to standalone with a reason, even after a local-library request. Record that reason and continue supported ordinary work. If evidence is required, `--require-source` holds only unavailable source-dependent work; separately confirm and inspect the named source.

For local retrieval, run `python3 TOOL --root ROOT verify`, then `python3 TOOL --root ROOT search QUERY --limit 5`, with TOOL pointing to the verified helper. Retain nonzero integrity failures and hold affected source reliance until reconciled. Standalone fallback is not an integrity pass. Package pin failure remains a stop before bundled-code execution. The helper reads a compatible catalog and manifest, makes no network request and creates no persistent index. It does not import an arbitrary PDF folder. Agent consumption of returned excerpts is a separate data destination and must be authorized.

For each selected reference retain identity, source/date/status, problem fit, what to learn, when to avoid it and asset rights. The lookup may nominate candidates; the agent must inspect the actual resource before using current facts or downloading assets. Duplicate sources should be enriched through their existing identity rather than registered repeatedly. Keep negative teaching examples out of normal selection; show them only for explicit critique with their warning intact.

Select the smallest useful set, compare approaches and extract principles rather than copying compositions. Save selection rationale, requested/effective mode, fallback reason and actual inspected source IDs with locators in the existing work record or stage packet. Record standalone with no consulted book sources; do not invent a reference-decision JSON entry to satisfy a source schema. Keep uninspected candidates separate from consulted sources. Library availability and catalog search are not source review, license approval or visual inspection.

Use the existing [design-work record](../../../templates/design-work.md) and [stage packet](../../../templates/stage-execution.md). Research basis: knowledge audit (optional provenance in the pinned source version; not bundled). Worked artifacts and limits: knowledge laboratory (optional provenance in the pinned source version; not bundled).

The supported search matches the supplied query against locally extracted text and returns source ID, title, excerpt, original path and available page or section fields. It does not refresh websites. Search results are candidates to inspect, not source review, rights approval or a design decision.


## Inspect what a resource actually contains

Before adoption, distinguish a complete method, a rendering template, a catalog pointer, a reference asset and an executable integration. Record the exact version, actual side files and unresolved upstream dependencies. A pointer may be a useful research lead without providing an executable skill. Trace imported catalogs to their existing upstream identity instead of counting them again. Check licenses for the selected material, not only the enclosing repository. See Open Design findings (optional provenance in the pinned source version; not bundled).
