# Problem-based reference retrieval

Version-Timestamp: 2026-09-16T18:27:08.062526-04:00

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.149.1; timestamp=2026-09-08 22:17:00 AST

Search by the communication problem, medium and constraint before choosing style. A query such as "portrait crop subject clarity" is more decision-useful than "beautiful website". Use the existing source register and its original authority/rights status. An annotation can explain a technique without copying a source asset or promoting its claims.

Book retrieval is optional and has no bundled annotation catalog. When the adopting project provides an ignored local configuration, resolve its `reference_library_root` and optional trusted `reference_library_tool` first. Otherwise use the packaged `library/scripts/reference_library.py` only after packaging has supplied it. The supported read-only commands are `python3 TOOL --root ROOT verify` and `python3 TOOL --root ROOT search QUERY --limit 1..100`. Verify before search. The tool reads the downloaded library's manifest and catalog, makes no network request, creates no persistent index and returns no fabricated recommendation for a nonmatch. If no local configuration or library is available, continue without book evidence and state that limit.

For each selected reference retain identity, source/date/status, problem fit, what to learn, when to avoid it and asset rights. The lookup may nominate candidates; the agent must inspect the actual resource before using current facts or downloading assets. Duplicate sources should be enriched through their existing identity rather than registered repeatedly. Keep negative teaching examples out of normal selection; show them only for explicit critique with their warning intact.

Select the smallest useful set, compare different approaches and extract principles rather than copying compositions. Save the selection rationale in the existing reference-decision/work record. Do not report a catalog search as a full source review, license approval or visual inspection.

Use the existing [design-work record](../../../templates/design-work.md) and [stage packet](../../../templates/stage-execution.md). Research basis: knowledge audit (optional provenance in the pinned source version; not bundled). Worked artifacts and limits: knowledge laboratory (optional provenance in the pinned source version; not bundled).

The supported search matches the supplied query against locally extracted text and returns source ID, title, excerpt, original path and available page or section fields. It does not refresh websites. Search results are candidates to inspect, not source review, rights approval or a design decision.


## Inspect what a resource actually contains

Before adoption, distinguish a complete method, a rendering template, a catalog pointer, a reference asset and an executable integration. Record the exact version, actual side files and unresolved upstream dependencies. A pointer may be a useful research lead without providing an executable skill. Trace imported catalogs to their existing upstream identity instead of counting them again. Check licenses for the selected material, not only the enclosing repository. See Open Design findings (optional provenance in the pinned source version; not bundled).
