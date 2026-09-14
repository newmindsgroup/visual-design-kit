# C-001 Button: filled specification example

Version-Timestamp: 2026-09-10 20:28:53 AST

## Identity and scope

Record BTN-EX-01, candidate 1.0; inventory [C-001 Button](../../inventory/ui.md#c-001), family [action](../../inventory/families.md#action). Teaching owner: Codex; no reviewer record or passed review status is inherited by this package. Work record: [WORK-EX-01](work-record.md). Selection: required within this isolated action example, not a real project selection. Web website/web-app profiles are the detailed target; browser versions and any project adoption remain unselected. Intended task: a person invokes one named command and understands its result.

Use for an action such as “Apply changes.” Use C-002 Link for navigation. This example does not include toggle, menu, split, floating or destructive actions; those require different state and consequence decisions. No backend operation is implemented.

## Select core and task behavior

This selection table owns applicability. Later sections are a catalog, not a requirement to attach a server workflow to every button. Select only relevant variants. [Selection guide](selection-guide.md) explains the output record.

| Section | Activation condition and dependencies | Included states and criteria | Omission or hold |
| --- | --- | --- | --- |
| BTN-CORE | Every action control: name, anatomy, activation, focus, layout and safe immediate result | BTN-S1/S2/S3; BTN-S5 if a result is reported; confirmed-failure part of BTN-S6 if the action can fail. BTN-01 and SH-01/SH-02; BTN-02 settled-result branch when applicable | Never omit core. No busy indicator, request identity or status button for a synchronous local action. An action that can fail still needs truthful feedback and safe recovery |
| BTN-UNAVAILABLE | A real precondition can prevent activation | BTN-S7 and BTN-03 | Omit if no unavailable state exists; do not use disabled appearance as an authorization check |
| BTN-ASYNC | Result settles later; depends on BTN-CORE and an actual operation contract | BTN-S4; reuses core-owned settled BTN-S5/confirmed-failure BTN-S6; BTN-02 pending and settled-result branches | Omit only for synchronous work. Missing cancellation/result/duplicate policy holds the affected action, not the whole unrelated interface |
| BTN-UNCERTAIN | A mutation may have occurred despite lost acknowledgement; depends on BTN-ASYNC and DEC-01 reconciliation authority | Unknown part of BTN-S6 and reconciliation exits; BTN-02 uncertain-outcome branch. BTN-I2 only for the selected query-based recovery example; it reuses BTN-S1 to BTN-S6 as mapped below and does not use BTN-S7 | A remote read does not automatically need mutation reconciliation. Omitting this section never permits unsafe resend. If uncertainty is possible but recovery is missing, hold action adoption and any retry. A different approved recovery route replaces this query-specific example and requires its own acceptance mapping |

Core command meaning belongs to the action's owner. Busy/result/retry/reconciliation policy belongs to its task or service adapter, not to a visual button primitive. No automatic polling is prescribed: BTN-I2 uses explicit user status queries only.

## Anatomy, variants and content

| Variant ID | Parts and meaning | Behavior and token roles | Dependencies |
| --- | --- | --- | --- |
| BTN-V1 labeled primary | Hit area, persistent action label, optional decorative leading icon and focus indicator; adjacent result/progress only when the selected task needs it | One command. Roles action.primary.surface, action.primary.label, action.border, focus.indicator, space.control.inline/block, type.control | F-001/F-002/F-003; F-009 for focus; C-045 for progress semantics if needed |
| BTN-V2 labeled secondary | Same anatomy, lower visual emphasis for an alternative command | Identical operation contract; action.secondary.surface/label | Same foundations |
| BTN-V3 icon-only | Hit area, recognizable icon and an explicit accessible action name | Only for a context where its meaning is established; no hover-only explanation. icon.action and focus.indicator roles | F-015 iconography, same foundations |

Role names are illustrative semantic requests, not canonical token additions or values. Map them to the approved project token file before adoption. A visible text label supplies the accessible name for V1/V2. “Apply changes” and “Aplicar los cambios seleccionados” are bounded label fixtures, not a character limit. Missing/blank action names are invalid configuration. Never render raw HTML from a label.

### BTN-ASYNC: task adapter, only when selected

The action adapter supplies command ID, available/busy state, reason when unavailable, result category and operation identity. A request has one current identity; late responses cannot overwrite a newer operation. UI guards do not replace backend duplicate protection. When BTN-UNCERTAIN applies, unknown outcome after lost connectivity needs reconciliation before retry; do not promise idempotency without the real service contract.

## State catalog for selected sections

| State ID | Trigger and visible result | Input/focus/assistive result | Recovery and criterion |
| --- | --- | --- | --- |
| BTN-S1 ready | Command becomes available; label visible | Native web button, explicit type=button for this non-submit example; no toggle state | Synchronous action settles without a busy state; use S5/S6 feedback when applicable. BTN-ASYNC activation goes to S4. BTN-01 |
| BTN-S2 hover/focus | Pointer enters or keyboard reaches control; optional hover feedback, visible focus independent of hover | Tab reaches enabled controls; Enter/Space and completed pointer/touch activation invoke the same command once | Blur/leave removes only matching presentation. BTN-01, SH-01 |
| BTN-S3 pressed | Pointer/key is held; transient feedback only | Moving pointer away before release cancels this example's pointer action; no mutation on pointer-down | Release follows the S1 synchronous/async route; cancellation returns to S1/S2. BTN-01 |
| BTN-S4 busy | BTN-ASYNC accepted activation; progress text next to control, stable label and width | Keep focused button focusable with aria-disabled=true and suppress all further activations in handler; announce adjacent status once, do not depend on spinner alone | Settled success to S5; failure to S6. BTN-02 |
| BTN-S5 success | Confirmed result appears adjacent; control returns ready; this isolated repeated command remains applicable | Focus remains on action in this example; no automatic navigation; noninterruptive status | Later activation begins another action; request identity applies only to selected task adapters. BTN-02 |
| BTN-S6 error/unknown | Visible failure or “Outcome not confirmed”; never claim success on timeout | Preserve context and focus. Confirmed safe failure restores an enabled Retry action. Unknown outcome retains a focusable aria-disabled control with handler suppression and adjacent “Outcome not confirmed. Wait for status confirmation.” Do not show a ready or success state, or imply a reconciliation request ran when it did not | Confirmed safe failure may retry. Unknown outcome uses the selected recovery route; the query-based example exposes BTN-I2 below. Reconciliation confirmed-success goes to S5; confirmed-no-effect restores a safe Retry action in S6; still-unknown remains held. BTN-02 |
| BTN-S7 unavailable | Precondition false before activation; native disabled button and adjacent reason | Removed from normal tab order by native disabled behavior; explanation remains readable outside the control | Precondition update enables S1. BTN-03 |

## BTN-UNCERTAIN: optional query-based recovery example

Read only when BTN-UNCERTAIN is selected and query-based reconciliation is the chosen recovery route. Missing this module does not waive the hold against unsafe retry.

While the main action is held, the adjacent host status offers a separate non-mutating “Check status” C-001 action. It queries the existing operation identity; it never repeats the original command. If no reconciliation result arrives, the main action stays held with its reason, and the status action becomes available again when its finite request deadline expires. A failed or still-unknown check says “Status not confirmed. Check again”; no success is inferred. Prevent duplicate concurrent status checks, but permit a later explicit status query. DEC-01 requires the real adapter owner to supply that finite deadline and status capability before adoption. If no safe status capability exists, adoption is held for an owner-provided reconciliation route, not a guessed resend. Reconciliation updates status without stealing focus from the status action or elsewhere; it leaves focus on the main action only if focus was already there.

### Status action instance BTN-I2

Anatomy: BTN-V2 secondary button labeled “Check status,” plus the adjacent shared result/status text. This is another C-001 instance, not a new component. It appears when the first unknown outcome occurs, then remains mounted and usable for that known operation identity, including after resolution, so focus is never discarded merely because a result arrived. A later main operation updates the queried identity explicitly. It never queries its own query identity or spawns another status button.

| Existing state mapping | Status-instance behavior | Criterion reference |
| --- | --- | --- |
| BTN-S1/S2/S3 | Ready, focus and press reuse V2 rules; activation makes one read-only status query | BTN-01, BTN-02 |
| BTN-S4 | Query in flight: preserve “Check status” label and focus, expose aria-disabled=true with handler suppression and adjacent “Checking status.” Repeat activation does nothing | BTN-02 |
| BTN-S5 | Query returns a confirmed result: restore enabled status button, update main state as specified and expose result through the one adjacent noninterruptive status channel. Keep current focus | BTN-02 |
| BTN-S6 safe-query failure | Failure, deadline expiry or still-unknown result restores enabled status button with “Status not confirmed. Check again.” Main action stays held. This read-only query can safely be repeated; it does not enter the main action’s uncertain-mutation branch | BTN-02 |

BTN-S7 native-disabled presentation is not used for this status instance: unavailability while querying uses BTN-S4 so focus survives. The host announces each result once through the shared status channel, avoiding duplicate main/status announcements. For the future controlled test only, set statusDeadline to five seconds and advance its fake clock; that teaching fixture is not a production timeout recommendation. DEC-01 still requires the actual adapter’s finite deadline and status capability.

## Core boundaries and conditional state safety

If a real success removes or makes the action unavailable, its project spec must define a new focus destination before adoption; that post-completion flow is excluded here. Busy uses a different focus policy from pre-existing unavailability on purpose. aria-disabled alone does not suppress activation. It is not a permission check. Selected/mixed/read-only/empty value states do not apply to this momentary command; absent labels are configuration errors. Reduced motion removes nonessential spinner animation without removing progress text.

## Platform, layout and handoff

Web semantics follow source records SRC-BUTTON and SRC-HTML-BUTTON. Do not add duplicate key handlers that fire alongside native click activation. The adapter must distinguish this type=button action from an actual form-submit button. Touch has no hover prerequisite.

For iOS/iPadOS or Android adoption, choose a native button and native enabled/progress semantics; do not emit ARIA or impose web Space/Enter handling. Hardware keyboard, VoiceOver/TalkBack, focus after completion and hit-area units need an OS/version-specific work record and device checks. These native variants are not completed by this web example.

Let labels wrap or the control grow without clipping; preserve action order on stacking. Use logical inline spacing; mirror directional navigation symbols only when their meaning changes, not arbitrary icons. RTL labels and long translated labels must retain name/action identity. No fixed brand sizes or mobile breakpoint are selected. Apply shared SH-01/SH-02 criteria and [specimen BTN-SP-01](specimens.md#btn-sp-01).

Handoff: item/state IDs above plus BTN-01 to BTN-03 in WORK-EX-01. Actual implementation, tests and token mapping are pending. Before adoption, the product owner must resolve command consequences and the engineering owner resolves only the applicable task contracts under DEC-01. Local synchronous controls do not need a status service. Refresh on action, backend, platform or token change.
