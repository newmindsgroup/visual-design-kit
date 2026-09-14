# C-005 Text field: filled specification example

Version-Timestamp: 2026-09-10 20:21:45 AST

## Identity and scope

Record TF-EX-01, candidate 1.0; inventory [C-005 Text field](../../inventory/ui.md#c-005), family [input](../../inventory/families.md#input). Owner Codex; document review: checks (historical source-version evidence, not bundled or inherited); criterion authority [WORK-EX-01](work-record.md). Optional inventory item, selected solely to teach plain single-line validation for web website/web-app use. The fictional label “Reference name” is a bounded data fixture, not a product design or personal-data collection proposal.

Use when a short free-text value is needed. Use a textarea for multiline prose; a select for a genuinely closed set of choices. Email, telephone, URL, password, autocomplete suggestions, masked and numeric inputs are excluded: their keyboards, parsing and security requirements differ.

## Select core and task behavior

This table owns applicability; retain core access and feedback for every selected behavior. The required Reference name fixture is one variant, not a rule that every text field must be required.

| Section | Activation condition and dependencies | Included states and criteria | Omission or hold |
| --- | --- | --- | --- |
| TF-CORE | Every single-line field: label, value, editing, input method, data meaning and layout | TF-S1/S2/S3 for editable variants; TF-LOCKED replaces editing states for its variants; TF-01 applicable branches and SH-01/SH-02 | Required-state assertion in TF-01 applies only to required fields. An optional plain field must be identified as optional, not silently subjected to TF-V1's required rule |
| TF-VALIDATE | Required or other local constraints exist; depends on TF-CORE and actual constraint authority | TF-S4, TF-02; apply the required-value fixture only for the required variant | Omit local error states only when no local constraint applies. Missing domain limits remain DEC-02; do not invent a maximum or silently remove a required constraint |
| TF-DOMAIN | A service/domain check is required; depends on TF-CORE, declared local constraints if any, and revision/result authority | TF-S5/S6 and TF-03; shared blur/submit trigger applies | Omit for a local-only field. A required check with no service/recovery contract is held, not considered valid. Preserve input on network failure |
| TF-LOCKED | Read-only or unavailable behavior is needed | TF-V2/V3, TF-S7/S8, relevant TF-04 branches | Omit unused variants. If an implemented transition disables a focused field, its focus/reason requirements are mandatory |

The core field does not own an API. TF-DOMAIN is the containing task's optional service behavior; when selected, its stale-response, error and focus requirements are not optional.

## Anatomy, variants and data contract

| Variant ID | Anatomy/content | Roles and dependencies |
| --- | --- | --- |
| TF-V1 editable required | Persistent label “Reference name,” textual required indication, input, help “Enter a reference name,” associated inline error region; error wording identifies the failure rather than repeating help | field.surface, field.text, field.border, field.border.invalid, text.help, text.error, focus.indicator, space.field, type.input; F-001/F-002/F-003/F-009 |
| TF-V2 read-only | Same label/value, explanation “This value is managed elsewhere” | Same roles with field.readonly.surface; distinct from disabled |
| TF-V3 unavailable | Same label and adjacent reason, disabled control | field.disabled roles; no implication that its submitted value is retained automatically |

Role names require mapping to the existing approved token source, not new raw values. Core accepts a string and preserves user entry exactly while editing. Only the required TF-V1 with TF-VALIDATE treats an empty or all-whitespace string as missing for its required check. No silent trimming, case folding or normalization is applied to stored data. Validation and storage rules must agree before project adoption.

Teaching fixtures: empty string, three spaces, “Reference A,” “  Reference A  ”, “Référence 例”, mixed RTL/LTR text and 200 repetitions of “Long reference ” for overflow testing. The long fixture is a stress input, not an allowed maximum. A real maximum, unit of length, allowed characters and newline-paste policy are deliberately unresolved in DEC-02. Do not reject non-Latin characters by default. Values are plain text, not markup. No raw field value belongs in diagnostic logs by default.

### Core editing and selected validation timing

For this example, native text editing and IME composition are preserved. Only with TF-VALIDATE or TF-DOMAIN selected, validation starts only on blur after editing or on a submit attempt. An edit cancels/invalidates an in-flight check but does not start another check until the next blur/submit. After an invalid result, re-evaluate on the next blur/submit; do not announce each character. A containing form must select one coordinated validation presentation rather than native popups plus duplicate custom announcements. Server validation remains authoritative for domain rules, and client validation is not a security boundary.

## State catalog for selected sections

| State ID | Trigger and visible result | Focus/assistive behavior | Recovery and criterion |
| --- | --- | --- | --- |
| TF-S1 pristine empty | Initial mount shows label/help, no premature error | Label programmatically associated; required state exposed only for the required variant | Focus to S2. TF-01 |
| TF-S2 focus/editing | Typing/paste/composition changes draft without submitting | Native cursor, selection, undo and composition; no automatic focus jump | Blur/submit validates only with TF-VALIDATE or TF-DOMAIN selected; otherwise retain the draft without an inferred check. TF-01 always; TF-02 only with TF-VALIDATE; TF-03 only with TF-DOMAIN |
| TF-S3 filled | Nonempty draft is displayed; filled does not mean validated | No gratuitous success announcement or universal “valid” claim | Edit returns S2. TF-01; a selected TF-VALIDATE check separately uses TF-02 |
| TF-S4 invalid | Edited blank/all-space value on blur or submit: “Reference name is required” | Associated error plus aria-invalid=true; blur does not pull focus back; submit coordinator focuses this field if first invalid | Correct then blur/submit clears error and invalid state. TF-02 |
| TF-S5 pending external validation (TF-DOMAIN) | Adapter starts a domain check for a draft revision; “Checking reference name” | Field stays editable; adjacent status, no spinner-only meaning | Edit invalidates prior request; accept only matching revision result. TF-03 |
| TF-S6 validation service error/offline (TF-DOMAIN) | Cannot establish domain result; preserve exact draft and say check unavailable | Do not mark the value invalid solely because network failed; no focus theft | Retry is explicit; submit remains held if that domain check is required. TF-03 |
| TF-S7 read-only | V2 selected: readable existing value, explanatory text | Native readonly, focus/select/copy permitted; no editing | External permission change may restore V1; do not assume field validation/submission equals editable mode. TF-04 |
| TF-S8 unavailable | V3 selected: disabled plus external reason | Native disabled behavior; help is readable without focus on field. If a live state change disables this currently focused field, first move focus to its adjacent reason text (programmatically focusable, tabindex=-1); otherwise do not move focus. The focused reason has a visible focus indicator, exposes its full reason text to assistive technology and is scrolled into view if needed; it is not presented as an actionable control. The adopter chooses a compatible focus/description mechanism for its browser/assistive matrix; the required observable outcome is visible focus and the reason being conveyed once | Precondition restores V1 without stealing focus; adapter handles data inclusion explicitly. TF-04 |

A stale reply never replaces a newer error/draft. Hover/pressed do not establish validation; selection is native text selection, not a component selected state. Mixed/expanded states are excluded because this is not a multi-value or suggestion control. Form-level submit success, permission denial and persistent storage belong to the containing flow, with a linked requirement rather than an invented backend here.

## Platform, layout and handoff

SRC-HTML-INPUT and SRC-FORMS support the web distinction among label, value, error and native editing. Use type=text for this plain variant. Do not invent a personal-data autofill token from the label; purpose and autocomplete policy need the actual field intent. Enter follows the containing form's documented submit policy, not an extra field-level command.

For native adoption, specify actual iOS/Android text control, input purpose/keyboard, return action, accessibility value/error announcement, autofill and secure-entry policy if applicable. DOM attributes are not native APIs. Keyboard occlusion, safe areas and restoration after backgrounding must be tested on named versions. Native details and personal/secure fields remain out of scope.

Keep the label and error visible when text grows. A single-line input may scroll its value internally; surrounding help/error must wrap and reflow. Preserve cursor and draft through resize. Use logical alignment, test mixed direction values independently of surrounding RTL UI, and avoid forced LTR for general text. Apply SH-01/SH-02 without clipping focus, help or error; reduced motion must not delay feedback.

Handoff: TF-01 to TF-04 methods and TF-SP-01 specimen. Written example is complete; project-specific data constraints remain held under DEC-02. Product/data owner resolves constraints, engineer reconciles client/server handling, and accessibility reviewer records real results after implementation. No input has been submitted or tested in a live product.
