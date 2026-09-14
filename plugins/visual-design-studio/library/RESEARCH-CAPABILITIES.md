# Research scenarios and reusable records

Version-Timestamp: 2026-09-10 20:02:52 AST

Research answers a scoped decision. Select brand/product/campaign, audience/market/category, or context-of-use inquiry; share one source register across them. Record target, market/language, question, intended use, permitted retrieval, owner and freshness trigger before acquisition. Do not collect unnecessary client or participant data.

| Scenario | Start and method | Required distinction |
| --- | --- | --- |
| supplied-kit | Inventory supplied versions, owner, scope and expiry; reconcile with current product/campaign facts | Supplied authority applies only within its stated scope; file receipt is not production permission |
| no-kit | Gather attributable relevant public or permitted sources; identify recurring patterns and gaps | Inferred brand rules remain provisional; reference assets are not automatically reusable |
| conflict | Keep competing claims and source IDs; compare authority, date, market and subject | An unresolved material conflict blocks ready status; record resolution owner and rationale |
| new-brand | Begin with audience/problem/category hypotheses and commission constraints | Proposed identity and strategy are proposals; no invented historic brand truth |
| formalization | Document a coherent existing practice into explicit rules | Separate observed consistency from a newly recommended rule |
| evolution or rebrand | Identify what to retain, why change, affected touchpoints and transition risks | Evolution preserves named equity; rebrand scope must explicitly authorize replacement |
| campaign-adaptation | Reuse current master rules plus campaign facts and intended channels | Campaign exceptions do not silently overwrite brand defaults |
| refresh | Recheck changed/expired sources and dependent findings | Preserve unchanged IDs; record supersession and reason; do not rerun unrelated research |
| precise-change | Retrieve only facts needed for the authorized delta | Protect baseline invariants and unaffected decisions; escalate only material new conflicts |

Brand inquiry covers identity, voice, offers/product truth, audience, competitive alternatives and channel/context. Audience inquiry uses explicit research questions, sampling limitations and consent; findings may inform full [personas](templates/persona.md). Context inquiry records viewing/interaction conditions, environment, accessibility and constraints without assuming a hardware profile.

The evidence record stores schema version, record ID, scenario, requested use, readiness, sources, findings, conflicts and asset uses. Sources have stable ID, local path/hash or HTTPS URL, retrieved_at, optional valid_until, current status, authority, rights and allowed_uses. Remote URL content is not verified by the local CLI. Set valid_until according to volatility and refresh triggers; absence of an expiry is not proof of indefinite freshness.

A finding has ID, claim, status, source IDs and reason. Evidenced/supplied/observed/inferred findings require sources; hypotheses/proposals/unknowns keep their uncertainty. Conflicts preserve source IDs, status, owner, competing claims and resolution rationale when resolved. Asset incorporation requires explicit production authorization for the named use, independently of confidence or publication on the web.

Use [evidence-record.json](templates/evidence-record.json). Validate before claiming structural handoff acceptance; unavailable validation remains a named hold. Persona-field source IDs must resolve through an embedded evidence_record. Run the persona validator on the actual record to check that linkage; the instruction alone does not prevent dangling citations. Reuse relevant current records across stages; preserve superseded material in project history instead of treating it as current.
