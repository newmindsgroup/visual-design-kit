# Specimen documentation record

Version-Timestamp: 2026-09-07 14:29:18 AST

Fill this only for a selected inventory item or composition. Replace the timestamp with the actual revision time. This is a blank documentation record, not a specimen implementation. Keep the [item specification](system-item.md) and [design work record](design-work.md) authoritative.

## Identify the example

Specimen ID and item/composition IDs: [fill]. Purpose and intended user task: [fill]. Variant and state: [fill]. Candidate version: [fill]. Accepted baseline and allowed delta: [link existing work record]. Owner and reviewer: [fill].

Choose the representation honestly:

- Static illustration: shows appearance only; no behavior evidence.
- Simulated interaction: demonstrates declared transitions with bounded sample data; no backend or native integration claim.
- Working implementation: links actual source and runtime; only observed checks count as evidence.

## Pair the representations

| Representation | Exact path or locator and version | What it demonstrates | What it does not prove |
| --- | --- | --- | --- |
| Visual specimen | [fill or pending] | [fill] | [fill] |
| Token role and anatomy | [canonical roles and parts] | [fill] | [fill] |
| Usage example or snippet | [fill or pending] | [fill] | [fill] |
| Implementation or builder mapping | [actual target/version, or unselected] | [fill] | [fill] |
| Interaction and accessibility evidence | [criterion ID, result, evidence] | [fill] | [fill] |

Use the same candidate version across the specimen, token source, snippet and implementation. If they differ, record the mismatch rather than treating a screenshot as implementation proof. A class name, marker, widget list or pseudocode is a locator or sketch unless a runnable implementation has actually been supplied and checked. Copy/export labels must identify exactly what the user receives.

## Usage, composition and counterexample

State when to use the example, when to avoid it and why. Pair a recommended example with a bounded counterexample when it clarifies a real requirement. Keep aesthetic preferences project-specific. Do not turn a photography preference, layout trend or branded decoration into a universal rule.

For an assembled section, name its content slots, component IDs, reading order, primary task and optional proof/action blocks. Explain how it becomes stacked, simplified, reordered or removed as space changes. Record allowed combinations and duplication/conflict rules. A composition recipe reuses entries; it is not automatically another component.

## Authority and references

The item specification owns state IDs, expected behavior and platform requirements. The work record owns criterion IDs and verification methods. Reference those IDs here and record only the specimen's representation/context and observed evidence. Do not restate or re-approve their state matrix, expected results or methods. A mismatch becomes a linked issue in the owning record.

## Conditions and states

Record viewport/window, input method, locale/RTL, text scale, theme/background, sample-data case and network/device condition where relevant. Link the entry's authoritative state matrix and exclusions. Test an actual transition when claiming behavior; a label saying hover, focus or expanded is not evidence that those states work.

| Item state and criterion IDs | Specimen representation/context | Actual observation | Evidence reference | Gap/owner |
| --- | --- | --- | --- | --- |
| [fill] | [fill] | [pending] | [pending] | [fill] |

For an image or mark, verify the approved variant on its intended background and at actual size. Record source, license/permission and fallback. Do not recolor a mark or substitute a font merely because an extracted sample becomes illegible. Use the existing reference decision to resolve a permitted alternative.

## Delivery relationship

Link the existing manifest for editable source, exported files, dependencies and actual reopen/runtime checks. Record separately whether any copy/export action delivers source, a reference marker, an image or a tested package. This record grants no publication, installation or execution authority.
