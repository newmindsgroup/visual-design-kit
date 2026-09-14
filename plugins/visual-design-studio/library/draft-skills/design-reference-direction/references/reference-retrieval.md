# Problem-based reference retrieval

Version-Timestamp: 2026-09-10 20:21:06 AST

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.149.1; timestamp=2026-09-08 22:17:00 AST

Search by the communication problem, medium and constraint before choosing style. A query such as "portrait crop subject clarity" is more decision-useful than "beautiful website". Use the existing source register and its original authority/rights status. An annotation can explain a technique without copying a source asset or promoting its claims.

The repository helper is a single offline Python file. It reads reference-techniques.json annotations, resolves original links from the named existing document and returns a derived view. It performs no network requests, embeddings, installation or persistent index writes. It is a lookup aid, not a selected agent architecture. Nonmatching searches return no result rather than a fabricated recommendation.

For each selected reference retain identity, source/date/status, problem fit, what to learn, when to avoid it and asset rights. The lookup may nominate candidates; the agent must inspect the actual resource before using current facts or downloading assets. Duplicate sources should be enriched through their existing identity rather than registered repeatedly. Keep negative teaching examples out of normal selection; show them only for explicit critique with their warning intact.

Select the smallest useful set, compare different approaches and extract principles rather than copying compositions. Save the selection rationale in the existing reference-decision/work record. Do not report a catalog search as a full source review, license approval or visual inspection.

Use the existing [design-work record](../../../templates/design-work.md) and [stage packet](../../../templates/stage-execution.md). Research basis: knowledge audit (optional provenance in the pinned source version; not bundled). Worked artifacts and limits: knowledge laboratory (optional provenance in the pinned source version; not bundled).

The offline helper matches query words against annotation tags only, orders by overlap then stable ID, and rejects ambiguous source labels. It does not search full book text or refresh websites.


## Inspect what a resource actually contains

Before adoption, distinguish a complete method, a rendering template, a catalog pointer, a reference asset and an executable integration. Record the exact version, actual side files and unresolved upstream dependencies. A pointer may be a useful research lead without providing an executable skill. Trace imported catalogs to their existing upstream identity instead of counting them again. Check licenses for the selected material, not only the enclosing repository. See Open Design findings (optional provenance in the pinned source version; not bundled).
