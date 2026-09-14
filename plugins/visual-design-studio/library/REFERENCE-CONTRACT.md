# Reference-decision contract

Version-Timestamp: 2026-09-10 20:14:15 AST

Use the [Markdown authoring view](templates/reference-decision.md) to reason through a direction, then record the constraints in a project JSON record following the schema; the [synthetic fixture](examples/reference-decision.json) illustrates shape only. The [JSON schema](templates/reference-decision.schema.json) describes structure; the standard-library CLI also enforces cross-record constraints. Neither representation authorizes action.

```sh
python3 -m design_system validate reference-decision examples/reference-decision.json --root .
```

## What is checked

- Exact locked baseline values come from a separate local JSON file, pinned by SHA-256. Its `locked` object maps stable keys to JSON values. The proposed `values` map must retain every locked value and type. Recorded derivations from or targeting locked keys fail even when the original key remains unchanged. A separately authorized baseline revision belongs in a different decision.
- An existing-brand, dense-app or physical-display record requires a locked baseline. A new-brand record can explicitly record no baseline with a reason. No empty lock set can masquerade as preservation.
- Sources require stable IDs, publisher, location, checked date, version, section and limitations. Evidence links resolve to source IDs. Public URLs are recorded without fetching; local paths stay within `--root`. Synthetic findings cannot masquerade as observations in a real record.
- Rights are `documented`, `unknown` or `held`. Documented claims require linked supporting evidence. Unknown/held rights prohibit reuse/complement dispositions and require a pending or failed rights check with a next action. Reference-only/reject remain available without implying permission to copy an asset. Conservatively, unresolved rights on those dispositions still keep the overall record held and require a pending or failed rights check with a next action. Excluding rejected alternatives from that policy would require a future contract change.
- Every reuse/complement/held candidate records asset-production and playback costs separately, including an explicit zero-extra reason when no production is needed. Each known charge needs evidence scoped to that operation. Free playback evidence does not support production. A paid operation under a zero-extra budget must remain held, rejected or reference-only; unknown charges need a pending or failed cost check with a next action. Hosting, installation and other operations are added when relevant.
- Every candidate, including rejected and reference-only alternatives, has human-design and accessibility review entries; physical-display also requires device review. Passed checks need evidence declared for that check category. Pending/failed checks or rights/cost holds prevent `reviewable` readiness. Failed checks also emit a distinct `verification_failed` warning. Valid held records are useful: uncertainty is represented instead of erased.

Evidence `supports` categories declare which rights, baseline approval, operation or verification claim a source addresses. The checker resolves these declarations, not the truth or adequacy of their prose. IDs and field presence cannot establish an actual license, cost quote or completed test.

## Read the result correctly

`valid: true` means this recorded structure and its cross-references meet the local contract. `decision_status: held` preserves recorded open work. `reviewable` means no recorded hold remains, not that implementation, publication or purchase is approved. `executes` is always false for processed reference-decision reports. The only requested action supported by this contract is review. Human CLI output prints the decision status and no-execution field. A reviewable synthetic record also emits a `synthetic_record` warning.

The checker does not inspect design files, render tokens, discover undeclared CSS aliases, identify hidden derivations, compare images or authenticate an approver. The caller must select the trusted baseline and its approved hash; replacing both a file and its hash is not prevented by a self-contained record. Concurrent filesystem mutation is outside this trusted-local-workspace contract. Human review must reconcile Markdown, JSON and the actual candidate, including new values that could function as unauthorized replacements.

Unknown fields fail in this contract to avoid silently dropping constraints. This is intentionally stricter than older records that permit extra metadata. The bundled schema uses a small supported structural keyword set; unsupported keywords or types produce a configuration error. This is not a general JSON Schema engine. Cross-record checks remain in Python. The bundle checker also audits the supported schema configuration. Unsupported contract versions require an explicit future migration.

Synthetic fixtures do not establish source rights, device behavior or creative quality. Actual implementation still needs rendered checks at relevant widths/states, real device evidence when applicable, and the separately authorized review/release gates.
