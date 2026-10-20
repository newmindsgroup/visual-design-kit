# Forms

Version-Timestamp: 2026-10-20 02:04:32 UTC

The best form asks fewer questions. Every field must earn its place: remove it, infer it, defer it, or explain why it is needed. Then make what remains easy to read, easy to fill and hard to get wrong.

## Layout defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Columns | One column | Short related pairs (city + postcode, expiry + CVC) may share a row |
| Label position | Above the field | Dense settings tables: labels left at 1/3 width, still programmatically linked |
| Label to field gap | `--space-1` to `--space-2` (4-8px) | |
| Field to field | `--space-4` to `--space-6` (16-24px) | Compact density: `--space-3` |
| Section to section | `--space-8` to `--space-12` (32-48px) with a heading | |
| Form width | Content column of about 40-60ch | Wide data entry in apps: grid of fields with clear grouping |
| Field width | Matches expected input: postcode 8-10ch, CVC 4-5ch, phone 15-20ch, full name 20-30ch | Full width on phones |
| Control height | 40px (md), 48px on touch-first and consumer mobile | Dense tools: 32px with 24px+ target |
| Submit button | Left-aligned with the fields, below the last field | Dialog forms follow the dialog button rule |

Single-column forms keep the eye on one path: CXL Institute's testing found them completed faster than multi-column versions, and Baymard Institute's checkout research recommends a single column. Top-aligned labels need the fewest eye movements (Matteo Penzo's 2006 eye-tracking study; Luke Wroblewski, *Web Form Design*, 2008).

## Labels, hints and placeholders

- Every field has a visible label, linked with `for`/`id` (or wrapping). Placeholders disappear on input, fail contrast and are read inconsistently; use them for examples only.
- Hints go between label and input, linked with `aria-describedby`, so they are read before typing: "Must be at least 15 characters" or "We'll only use this for delivery updates".
- Mark the minority: if most fields are required, mark optional ones "(optional)" in the label (GOV.UK pattern). If most are optional, mark required fields with an asterisk and explain the asterisk at the top. Always set `required` or `aria-required`.
- Group related controls in `fieldset` with a `legend` (radio groups, checkbox groups, date parts, address).

## Input types and attributes

| Data | Markup | Notes |
| --- | --- | --- |
| Email | `type="email" autocomplete="email" spellcheck="false" autocapitalize="none"` | Offer a correction for common domain typos ("gmial.com") |
| Phone | `type="tel" autocomplete="tel"` | One field; accept spaces, dashes, brackets and +country code |
| One-time code | `inputmode="numeric" autocomplete="one-time-code"` | One field, not 6 boxes; allow paste; iOS and Android offer the SMS code |
| Numeric identifiers (card, postcode, account) | `type="text" inputmode="numeric"` | Not `type="number"`: it adds spinners, drops leading zeros and scroll-changes values |
| Quantities | `type="number"` with min, max, step, or a stepper with large buttons | |
| New password | `type="password" autocomplete="new-password"` | Show/hide toggle; allow paste; show rules up front; no composition rules beyond length (NIST SP 800-63B-4) |
| Current password | `autocomplete="current-password"` | Never block password managers or paste (WCAG 3.3.8) |
| Name | `autocomplete="name"` | One "Full name" field unless a downstream system truly needs parts |
| Address | `autocomplete="address-line1"`, `address-line2`, `address-level2` (city), `postal-code`, `country-name` | Offer address lookup with a "Enter address manually" link |
| Card payment | `cc-name`, `cc-number`, `cc-exp`, `cc-csc` | Use the payment provider's hosted fields to limit PCI DSS scope |
| Memorable date (birth date) | Three text fields: day, month, year, `inputmode="numeric"` | GOV.UK pattern; date pickers are slow for distant dates |
| Scheduling date | Date picker plus typed input | Show the day of week; block unavailable dates with a reason |
| Long free text | `textarea` with a visible character count when there is a limit | Count announces at thresholds, not every keystroke |

`autocomplete` tokens satisfy WCAG 1.3.5 (identify input purpose) and save mobile users most of their typing.

## Choosing a choice control

| Options | Control |
| --- | --- |
| 2-5, single choice | Radio buttons, all visible (no default unless one is truly safe and common) |
| Yes/no question | Two radios ("Yes" / "No"), not a checkbox, when "no answer" must be distinguishable |
| 6-15, single choice | Select |
| 15+ or unknown (countries, airports, people) | Combobox with type-ahead filtering; put likely choices first |
| Several choices | Checkboxes (up to about 10), or multi-select combobox |
| Immediate setting | Switch, outside of forms with Save |

## Validation

**Timing ("reward early, punish late"):**

1. Do not validate while the user is still typing in a field for the first time.
2. Validate format on blur (when they leave the field).
3. Validate required fields on submit.
4. Once a field is in error, re-validate on each input so the error clears the moment it is fixed.
5. Live validation while typing only where it helps: password requirements, character limits, username availability (debounced 300-500ms).

In Luke Wroblewski's 2009 study with Etre (A List Apart), inline validation after leaving a field reduced errors and completion time and raised satisfaction compared with validating only on submit; verify the exact percentages in the article before quoting them.

**Presentation:**

- Message directly below the field (or below the label, GOV.UK style), with an icon and text in `--color-danger-fg`, border in `--color-danger-border`. Never color alone.
- `aria-invalid="true"` on the field; message linked with `aria-describedby`.
- On submit with errors: an error summary at the top listing each error as a link to its field, focus moved to the summary, and the page title prefixed with "Error: ".
- Error text follows the [content design](../../ux-design/references/content-design.md) formula: what happened and how to fix it.
- Keep every value the user typed, including in fields with errors (except card security codes where the provider requires clearing).

## Submission

- Do not disable the submit button to signal incomplete fields; people cannot tell what is missing. Let them submit and show the summary.
- After a valid submit, block duplicates: set a busy state with `aria-disabled="true"` and ignore further activation until the request settles. The server must also be idempotent for payments and orders.
- Busy label stays the same width: "Saving..." with an inline spinner.
- On failure, keep the data and say what to do. On lost connection with an unknown outcome, say so and check status before allowing a retry.
- On success, move focus to the confirmation heading or show inline confirmation next to the button.

## Multi-step forms

- Split when there are more than about 7-10 fields or clearly separate topics. For public services and complex eligibility, GOV.UK's "one thing per page" pattern performs well.
- Show "Step 2 of 4: Delivery" with step names; 3-5 steps is typical, more than 7 feels endless.
- Back never loses data. Save progress automatically for long forms and let people resume (email link or account).
- End with a "Check your answers" page with a Change link per answer, then the final submit.
- Conditional questions reveal inline below the triggering choice, announced to screen readers.
- Do not ask for information already given earlier in the process (WCAG 3.3.7 Redundant Entry); prefill or offer "Same as billing address".

## Complex inputs

- **File upload:** button plus drag-and-drop zone; state accepted types and maximum size before upload; per-file progress, cancel and retry; thumbnails for images; keyboard-accessible.
- **Repeating groups** (add another person, line item): "Add another" button below the group, Remove per item, focus moved to the new item's first field.
- **Masks:** format as the user types only when the format is fixed (card numbers in 4-digit groups); never block characters silently.
- **CAPTCHA:** prefer invisible checks, honeypot fields and rate limiting. If a challenge is unavoidable, provide a non-cognitive alternative (WCAG 3.3.8).
- **Timeouts:** warn at least 20 seconds before expiry with a way to extend (WCAG 2.2.1); keep data across re-authentication.

## Mobile specifics

- 16px minimum font size in inputs to avoid iOS zoom on focus.
- Correct keyboard via `type` and `inputmode`; `enterkeyhint="next"` or `"send"` where useful.
- Sticky submit bars must not cover the focused field (WCAG 2.4.11); use `scroll-padding-bottom`.
- Targets 44-48px tall; radios and checkboxes get full-row tap areas.

## Field spec template

| Field ID | Label | Hint | Type and autocomplete | Required | Validation rule and timing | Error messages | Data use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-email | Email address | We'll send your receipt here | `email`, `autocomplete="email"` | Yes | Format on blur; required on submit | "Enter your email address" / "Enter an email address in the correct format, like name@example.com" | Receipt, account |

For lead-generation forms and how field count affects conversion, see `web-design` [conversion](../../web-design/references/conversion.md).
