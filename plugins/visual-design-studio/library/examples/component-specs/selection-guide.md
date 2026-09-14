# Select the instructions the task actually needs

Version-Timestamp: 2026-09-10 20:21:45 AST

Start with the selected component's core. Add task behavior only when its trigger applies. “Optional” means the task might not need the behavior, not that its safety rules can be skipped after the behavior is chosen.

The authoritative trigger, dependency and state mapping is in each item: [Button](button.md#select-core-and-task-behavior), [Text field](text-field.md#select-core-and-task-behavior), [Dialog](dialog.md#select-core-and-conditional-behavior), [Data table](data-table.md#select-core-and-task-behavior). The [work record](work-record.md) still owns the fourteen criterion IDs and named procedure branches. If a compact example and an item table ever disagree, use the item table, record the inconsistency and correct the example before adoption. This guide selects them; it does not restate their requirements or create another approval process.

## Instructions for Codex and Claude

```text
Role: act as the specification editor for the selected inventory item.
Objective: produce the smallest complete set of instructions for the actual task.
Context: read the real brief, existing approved work record, item selection table
and applicable family contract. Do not load unrelated component examples.
Requirements: include core, then evaluate every conditional trigger against
available evidence. Include required dependencies. A safety condition that can
occur cannot be omitted just because the first example does not show it.
When selected components interact, run the composition check below and record
its decisions in the existing work record and handoff.
Missing required behavior or recovery makes the affected action held. It never
licenses unsafe retry, discarded input, hidden errors or inaccessible content.
Recommend the appropriate selection yourself. Request factual missing inputs
from their owner only when needed; do not ask the user to design technical structure.
Output: item/version and intended task; selection rows with section ID,
selected/omitted/held, trigger evidence, dependency or missing input, rationale,
applicable state IDs and criterion ID plus named branch; affected hold/next owner.
Evaluation: no unselected feature implied by copied anatomy or test instructions;
no safety requirement dropped; no duplicate requirement authority; no claim that
omission is a test pass. Preserve baseline, source, rights and handoff controls.
```

Resolve scope using evidence already available. Do not make the user choose async architecture or test taxonomy. Unknown data limits, action consequences, service recovery or native OS requirements are factual inputs for their owners. Record the bounded hold and continue independent documentation work. A held module blocks its affected behavior, not unrelated safe work.


## Selection output completeness

Before returning a selection, check the following against the existing item table:

- Carry SH-01 and SH-02 into the selected core criterion list for these four web examples. Their checks remain pending; do not silently drop one while summarizing.
- Filter states and criterion branches to the actual selected variant. A read-only variant does not imply disabled or editable behavior. List only applicable branches, not the entire family catalog.
- Omitted means the trigger cannot occur in this task. It is not a hold. Put a behavior in holds only when a required input or safety contract is missing.
- Selection-ready means enough information exists to write the scoped specification. Absence of implementation or unexecuted acceptance tests is expected at this stage and does not by itself hold selection or imply approval. Record future tests as pending evidence.
- For an uncertain mutation with missing safe recovery, explicitly name initiation/adoption of the affected action and its retry as held. Independent core documentation may continue; that does not permit sending the mutation.
- Treat facts already supplied by the brief as supplied. Do not create missing-input requests for omitted features or hypothetical future scope. If the brief itself is ambiguous, name that exact ambiguity rather than inventing a value.

These checks clarify existing selection and evidence rules. They do not add a component, change source requirements or certify model output.

## Check components that work together

Run this check when one selected component opens, closes, submits, updates, disables or removes another, or when they share focus, data or feedback. Mere visual proximity does not require a composition record. For a standalone task with no such interaction, record not applicable with a short reason in the existing work record; include that disposition in the handoff and revisit it under the change triggers below.

Use the existing [design-work record](../../templates/design-work.md), its decision and criterion sections, and the existing handoff. This is a review step, not a new schema, component, skill or source of component requirements.

1. **Identify the transition and its owners.** Name the component instances, their source versions and selected states/criterion branches. Record what initiates the transition, what changes and which component or existing task/service handler owns each effect. Include nested controls and non-button routes such as Close, Submit, Escape and cancellation.
2. **Reconcile the interaction.** Check the affected concerns below against the actual item tables. Record not applicable where the concern cannot occur; do not invent missing services or new features. Unspecified behavior is not evidence that a concern cannot occur; record the uncertainty and resolve it through step 3.

| Concern | Questions to resolve for the selected transition |
| --- | --- |
| Focus and availability | Where does focus start and finish? What happens if its target disappears, becomes unusable or is unavailable? Which owner restores it or provides a safe fallback? |
| Feedback | Who communicates the result, error or progress? Do the selected components disagree or duplicate announcements? Synchronous results can still need the settled-result criterion branch. |
| Dismissal and data | What do Close, Escape, cancellation or removal do to pending work and user input? Are draft preservation and return context defined where needed? |
| Activation and recovery | Could multiple handlers repeat the same action? Can a failure or lost acknowledgement leave the result uncertain? Carry forward only applicable operation/recovery requirements and affected-action holds. |

3. **Resolve conflicts explicitly.** Do not silently copy incompatible example behavior. In the existing decision record, name the source conflict, proposed task-specific adaptation, rationale, affected requirements/states/criterion branches, approval status and responsible owner. Preserve accepted invariants and applicable safety requirements. A proposal is not authority to relax them or edit the shared source. If accepted invariants conflict, do not choose a winner or relax either silently: hold the affected transition and ask their authorized owners to resolve or explicitly revise the acceptance boundary. For every hold, the author records the affected action, responsible decision owner, missing input or evidence, and exact release condition in the existing work record and handoff. A proposed fix or elapsed time does not release it. Continue independent work.
4. **Carry the result forward.** Include each selected decision in the work record and handoff with resolvable IDs and applicable acceptance mappings. Specify how the combined transition will be checked, including relevant failure and target-removal paths. Reuse source procedures; document only the adaptation and its additional checks. Keep pending runtime checks separate from document review or structural validation. Revisit affected records and prior evidence when a source, transition or accepted decision changes.

For example, an action opening a modal must reconcile its result-focus behavior with the modal's opening and restoration contract. The supervised exercise (historical source-version evidence, not bundled or inherited) documents one proposed adaptation; it is not a universal rule or a tested reusable implementation.

## Compact selection examples

These are original selection records, not running demonstrations or project approvals. Criteria are instructions still pending execution. SH-01/SH-02 apply throughout to the selected content and controls.

| Task and known condition | Selected | Omitted or held, with reason | Criteria and missing input |
| --- | --- | --- | --- |
| Local action restores a nonpersistent view arrangement synchronously, with a known immediate result | BTN-CORE, labeled variant | BTN-ASYNC and BTN-UNCERTAIN omitted: no deferred result or uncertain mutation. BTN-UNAVAILABLE omitted only if unavailability cannot occur | BTN-01; BTN-02 settled-result branch only if feedback is reported. Action meaning and token mapping still come from the brief; no request/status service |
| Remote save can commit before its acknowledgement is lost | BTN-CORE, BTN-ASYNC, BTN-UNCERTAIN | Hold the save/retry until DEC-01 has safe result/reconciliation authority. BTN-I2 query route held if status capability/deadline is missing; no guessed resend | BTN-01 and all relevant BTN-02 branches. Add BTN-03 only if a precondition exists. Backend contract belongs to engineering, not visual styling |
| Display an existing read-only field value | TF-CORE, TF-LOCKED read-only variant | TF-VALIDATE and TF-DOMAIN omitted: this task does not edit or submit a value | TF-01 label/semantics branch, TF-04 read-only branch. No editable keyboard, blur validation or remote-check requirement inherited |
| Editable required field, local required check only | TF-CORE, TF-VALIDATE | TF-DOMAIN omitted: no service rule. TF-LOCKED omitted only if read-only/unavailable conditions cannot occur | TF-01 editable branches and TF-02. Missing actual storage constraints stay DEC-02, not invented defaults |
| Same editable field also requires a server-domain check | TF-CORE, TF-VALIDATE, TF-DOMAIN | Hold required domain checking if revision/error/recovery authority is missing; failure is not a valid result | TF-01/TF-02/TF-03; service and data owners provide missing facts |
| Fixed complete local read-only table, source order is sufficient | TBL-CORE | TBL-SORT and TBL-REMOTE omitted: no ordering controls or fetch. TBL-ALTERNATE omitted if comparison table remains appropriate | TBL-01 relationships; TBL-02 static-data branch for possible zero/invalid input. No aria-sort, request IDs or Retry; invalid local data still needs truthful core error handling |
| Remote complete batch with locally applied sort | TBL-CORE, TBL-REMOTE, TBL-SORT | Alternate is not automatic. If “remote sort” actually means server-side pagination/order, hold that extension: this example does not define it | TBL-01 relationships/sorting and TBL-02 remote/combined clauses; adapter locale, freshness and identity required |
| Short read-only web modal | DLG-CORE; evaluate DLG-OVERFLOW under supported settings | Native/consequential adaptations omitted because they are not this task. Overflow handling cannot be omitted when text enlargement makes it necessary | DLG-01 core and applicable overflow checks, DLG-02, SH-02; no dirty-form workflow inferred |

After selection, draft only the relevant project record. Preserve example IDs as provenance and assign project IDs normally. Selected criterion branches remain pending until a real authorized implementation supplies evidence. The guide is complete as instructional documentation; it does not select a stack or initiate a pilot.
