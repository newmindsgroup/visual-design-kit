# Interaction and content patterns

Version-Timestamp: 2026-09-07 14:29:54 AST

Generated from master.json. Listed concepts and shared specification starters only. No completed component specifications, implementation or testing is supplied. Profile selections are starting recommendations, not approved project scope.

[Index](index.md) | [Specification template](../templates/system-item.md)

<a id="p-001"></a>

## P-001: Form validation and recovery

Coordinates field rules, error summaries and correction.

Kind: pattern. Shared contract: [form-flow](families.md#form-flow).

### Variants to specify

- Client feedback
- Server errors
- Cross-field rules

### Entry-specific states and behavior

- Preserve values and focus a useful error location.

### Project decisions still required

- Which errors can users fix themselves?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs form validation and recovery. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs form validation and recovery. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs form validation and recovery. |
| [Web app](profile-web-app.md) | optional | Include when the project needs form validation and recovery. |
| [Website](profile-website.md) | optional | Include when the project needs form validation and recovery. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-005: Text field](ui.md#c-005), [C-047: Inline validation message](ui.md#c-047)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-002"></a>

## P-002: Multi-step form and task list

Organizes a longer process into manageable parts.

Kind: pattern. Shared contract: [form-flow](families.md#form-flow).

### Variants to specify

- Wizard
- Task list
- Save-and-return

### Entry-specific states and behavior

- Progress, back navigation, incomplete steps and expired drafts.

### Project decisions still required

- Must steps be sequential or independently completed?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs multi-step form and task list. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs multi-step form and task list. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs multi-step form and task list. |
| [Web app](profile-web-app.md) | optional | Include when the project needs multi-step form and task list. |
| [Website](profile-website.md) | optional | Include when the project needs multi-step form and task list. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-001: Button](ui.md#c-001)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-003"></a>

## P-003: Review, confirm and receipt

Lets users check important details before and after completion.

Kind: pattern. Shared contract: [form-flow](families.md#form-flow).

### Variants to specify

- Review answers
- Confirmation
- Receipt

### Entry-specific states and behavior

- Edit, cancel, duplicate submit and failed confirmation.

### Project decisions still required

- What commitment is being made and what record is needed?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs review, confirm and receipt. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs review, confirm and receipt. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs review, confirm and receipt. |
| [Web app](profile-web-app.md) | optional | Include when the project needs review, confirm and receipt. |
| [Website](profile-website.md) | optional | Include when the project needs review, confirm and receipt. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-001: Button](ui.md#c-001)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-004"></a>

## P-004: Inline editing and autosave

Changes existing content while retaining context.

Kind: pattern. Shared contract: [form-flow](families.md#form-flow).

### Variants to specify

- Explicit save
- Autosave
- Undo

### Entry-specific states and behavior

- Editing, unsaved, saving, saved, conflicted and failed states.

### Project decisions still required

- When is a change committed and how can it be reversed?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs inline editing and autosave. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs inline editing and autosave. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs inline editing and autosave. |
| [Web app](profile-web-app.md) | optional | Include when the project needs inline editing and autosave. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-005: Text field](ui.md#c-005)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-005"></a>

## P-005: Search results and no results

Connects a query with useful results and recovery.

Kind: pattern. Shared contract: [discovery](families.md#discovery).

### Variants to specify

- Simple
- Suggestions
- Scoped
- Federated

### Entry-specific states and behavior

- No matches, partial results and unavailable index differ.

### Project decisions still required

- What helps users recover from an unsuccessful query?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs search results and no results. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs search results and no results. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs search results and no results. |
| [Web app](profile-web-app.md) | optional | Include when the project needs search results and no results. |
| [Website](profile-website.md) | optional | Include when the project needs search results and no results. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-008: Search field](ui.md#c-008)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-006"></a>

## P-006: Filter, facet and sort

Narrows and orders a result set.

Kind: pattern. Shared contract: [discovery](families.md#discovery).

### Variants to specify

- Facets
- Applied chips
- Sort menu
- Clear all

### Entry-specific states and behavior

- Applied state, zero results and hidden filters need clear summaries.

### Project decisions still required

- Which filters and sort orders are meaningful for the data?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs filter, facet and sort. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs filter, facet and sort. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs filter, facet and sort. |
| [Web app](profile-web-app.md) | optional | Include when the project needs filter, facet and sort. |
| [Website](profile-website.md) | optional | Include when the project needs filter, facet and sort. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-014: Select and picker](ui.md#c-014), [C-044: Badge, tag and chip](ui.md#c-044)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-007"></a>

## P-007: Load more and virtual scrolling

Reveals additional repeated content.

Kind: pattern. Shared contract: [discovery](families.md#discovery).

### Variants to specify

- Load-more
- Infinite
- Virtualized

### Entry-specific states and behavior

- Preserve position, accessible item context and reachable footer.

### Project decisions still required

- Why is this better than pagination for the task?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs load more and virtual scrolling. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs load more and virtual scrolling. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs load more and virtual scrolling. |
| [Web app](profile-web-app.md) | optional | Include when the project needs load more and virtual scrolling. |
| [Website](profile-website.md) | optional | Include when the project needs load more and virtual scrolling. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-036: List and list item](ui.md#c-036)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-008"></a>

## P-008: Bulk selection and actions

Applies an action to a known set of items.

Kind: pattern. Shared contract: [discovery](families.md#discovery).

### Variants to specify

- Visible page
- All results
- Select-all
- Partial selection

### Entry-specific states and behavior

- Distinguish visible selection from whole-dataset selection.

### Project decisions still required

- How will users understand the affected set and undo?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs bulk selection and actions. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs bulk selection and actions. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs bulk selection and actions. |
| [Web app](profile-web-app.md) | optional | Include when the project needs bulk selection and actions. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-011: Checkbox](ui.md#c-011), [C-001: Button](ui.md#c-001)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-009"></a>

## P-009: Onboarding and first use

Introduces only what users need to begin.

Kind: pattern. Shared contract: [account](families.md#account).

### Variants to specify

- Welcome
- Guided setup
- Contextual education

### Entry-specific states and behavior

- Skip, resume, first success and returning-user states.

### Project decisions still required

- What must be learned now versus at the point of need?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs onboarding and first use. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs onboarding and first use. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs onboarding and first use. |
| [Web app](profile-web-app.md) | optional | Include when the project needs onboarding and first use. |
| [Website](profile-website.md) | optional | Include when the project needs onboarding and first use. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-001: Button](ui.md#c-001)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APPLE](../INVENTORY-SOURCES.md#APPLE), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-010"></a>

## P-010: Sign-in and authentication

Establishes the claimed account identity.

Kind: pattern. Shared contract: [account](families.md#account).

### Variants to specify

- Password
- Passkey
- SSO
- Multi-factor

### Entry-specific states and behavior

- Invalid credentials, challenge, lockout, recovery and cancellation.

### Project decisions still required

- Is an account needed, and which methods are authorized?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs sign-in and authentication. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs sign-in and authentication. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs sign-in and authentication. |
| [Web app](profile-web-app.md) | optional | Include when the project needs sign-in and authentication. |
| [Website](profile-website.md) | optional | Include when the project needs sign-in and authentication. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-005: Text field](ui.md#c-005)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APPLE](../INVENTORY-SOURCES.md#APPLE), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-011"></a>

## P-011: Registration and verification

Creates an account and verifies required contact or identity claims.

Kind: pattern. Shared contract: [account](families.md#account).

### Variants to specify

- Invitation
- Self-registration
- Verification link

### Entry-specific states and behavior

- Duplicate account, expired invitation and unverified states.

### Project decisions still required

- What is the minimum information needed?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs registration and verification. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs registration and verification. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs registration and verification. |
| [Web app](profile-web-app.md) | optional | Include when the project needs registration and verification. |
| [Website](profile-website.md) | optional | Include when the project needs registration and verification. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-005: Text field](ui.md#c-005)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APPLE](../INVENTORY-SOURCES.md#APPLE), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-012"></a>

## P-012: Account recovery

Restores access through an approved recovery path.

Kind: pattern. Shared contract: [account](families.md#account).

### Variants to specify

- Reset
- Backup method
- Support-assisted

### Entry-specific states and behavior

- Expired link, unavailable factor and completed recovery.

### Project decisions still required

- How can access be restored without weakening identity checks?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs account recovery. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs account recovery. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs account recovery. |
| [Web app](profile-web-app.md) | optional | Include when the project needs account recovery. |
| [Website](profile-website.md) | optional | Include when the project needs account recovery. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-005: Text field](ui.md#c-005)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APPLE](../INVENTORY-SOURCES.md#APPLE), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-013"></a>

## P-013: Account settings and profile

Manages personal preferences and account details.

Kind: pattern. Shared contract: [account](families.md#account).

### Variants to specify

- Profile
- Preferences
- Security
- Deletion

### Entry-specific states and behavior

- Unsaved, saving, invalid and confirmation states.

### Project decisions still required

- What belongs to a person versus an organization?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs account settings and profile. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs account settings and profile. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs account settings and profile. |
| [Web app](profile-web-app.md) | optional | Include when the project needs account settings and profile. |
| [Website](profile-website.md) | optional | Include when the project needs account settings and profile. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-005: Text field](ui.md#c-005), [C-013: Switch](ui.md#c-013)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APPLE](../INVENTORY-SOURCES.md#APPLE), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-014"></a>

## P-014: Permission request and access denial

Explains and handles unavailable access.

Kind: pattern. Shared contract: [account](families.md#account).

### Variants to specify

- OS permission
- Role restriction
- Consent-dependent feature

### Entry-specific states and behavior

- Not asked, allowed, denied, restricted and revoked.

### Project decisions still required

- Which alternative remains useful if access is refused?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs permission request and access denial. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs permission request and access denial. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs permission request and access denial. |
| [Web app](profile-web-app.md) | optional | Include when the project needs permission request and access denial. |
| [Website](profile-website.md) | optional | Include when the project needs permission request and access denial. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-048: Banner and inline alert](ui.md#c-048)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APPLE](../INVENTORY-SOURCES.md#APPLE), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-015"></a>

## P-015: Session expiry and sign-out

Ends or renews an authenticated session.

Kind: pattern. Shared contract: [account](families.md#account).

### Variants to specify

- Warning
- Reauthentication
- Sign-out
- Revoked session

### Entry-specific states and behavior

- Preserve only appropriate unsaved data and clear private state.

### Project decisions still required

- What should survive expiry and what must be erased?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs session expiry and sign-out. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs session expiry and sign-out. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs session expiry and sign-out. |
| [Web app](profile-web-app.md) | optional | Include when the project needs session expiry and sign-out. |
| [Website](profile-website.md) | optional | Include when the project needs session expiry and sign-out. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-048: Banner and inline alert](ui.md#c-048)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APPLE](../INVENTORY-SOURCES.md#APPLE), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-016"></a>

## P-016: Consent and privacy choices

Collects and manages meaningful user choices.

Kind: pattern. Shared contract: [account](families.md#account).

### Variants to specify

- Cookie choices
- Communication preferences
- Data-use choice

### Entry-specific states and behavior

- Unanswered, accepted, declined and withdrawn choices.

### Project decisions still required

- What is optional and how can the user change a choice?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs consent and privacy choices. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs consent and privacy choices. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs consent and privacy choices. |
| [Web app](profile-web-app.md) | optional | Include when the project needs consent and privacy choices. |
| [Website](profile-website.md) | optional | Include when the project needs consent and privacy choices. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-011: Checkbox](ui.md#c-011)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APPLE](../INVENTORY-SOURCES.md#APPLE), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-017"></a>

## P-017: Product discovery and comparison

Helps people assess purchasable offerings.

Kind: pattern. Shared contract: [transaction](families.md#transaction).

### Variants to specify

- Catalog
- Detail
- Comparison
- Availability

### Entry-specific states and behavior

- Unavailable stock, variant selection and pricing uncertainty.

### Project decisions still required

- Is a commercial catalog part of this product?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs product discovery and comparison. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs product discovery and comparison. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs product discovery and comparison. |
| [Web app](profile-web-app.md) | optional | Include when the project needs product discovery and comparison. |
| [Website](profile-website.md) | optional | Include when the project needs product discovery and comparison. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-035: Card and tile](ui.md#c-035)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-018"></a>

## P-018: Cart and checkout

Collects a proposed order and its completion details.

Kind: pattern. Shared contract: [transaction](families.md#transaction).

### Variants to specify

- Guest
- Account
- Delivery
- Pickup

### Entry-specific states and behavior

- Validation, changed price, stock loss and duplicate submission.

### Project decisions still required

- Which order, pricing and fulfillment rules apply?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs cart and checkout. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs cart and checkout. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs cart and checkout. |
| [Web app](profile-web-app.md) | optional | Include when the project needs cart and checkout. |
| [Website](profile-website.md) | optional | Include when the project needs cart and checkout. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-005: Text field](ui.md#c-005), [C-001: Button](ui.md#c-001)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-019"></a>

## P-019: Payment and refund

Handles an authorized monetary transaction and recovery.

Kind: pattern. Shared contract: [transaction](families.md#transaction).

### Variants to specify

- Provider handoff
- Saved method
- Refund
- Retry

### Entry-specific states and behavior

- Pending, challenged, succeeded, failed and unknown outcome.

### Project decisions still required

- Which provider and controls establish transaction truth?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs payment and refund. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs payment and refund. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs payment and refund. |
| [Web app](profile-web-app.md) | optional | Include when the project needs payment and refund. |
| [Website](profile-website.md) | optional | Include when the project needs payment and refund. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-048: Banner and inline alert](ui.md#c-048)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-020"></a>

## P-020: Subscription and billing

Manages a recurring commercial relationship.

Kind: pattern. Shared contract: [transaction](families.md#transaction).

### Variants to specify

- Plan choice
- Upgrade
- Cancel
- Invoice

### Entry-specific states and behavior

- Renewal, proration, failed charge and cancellation dates.

### Project decisions still required

- Is recurring billing actually in scope?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs subscription and billing. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs subscription and billing. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs subscription and billing. |
| [Web app](profile-web-app.md) | optional | Include when the project needs subscription and billing. |
| [Website](profile-website.md) | optional | Include when the project needs subscription and billing. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-038: Data table](ui.md#c-038)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-021"></a>

## P-021: Loading, empty and partial content

Explains incomplete or absent content without misleading users.

Kind: pattern. Shared contract: [system-flow](families.md#system-flow).

### Variants to specify

- First load
- Empty dataset
- Partial
- Stale

### Entry-specific states and behavior

- Empty content is different from a failed request or denied access.

### Project decisions still required

- What useful next step exists for each state?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native tablet app](profile-native-tablet.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Website](profile-website.md) | required | Shared starter requirement for this profile; confirm in project scope. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-048: Banner and inline alert](ui.md#c-048)

Related concepts: [A-004: Icon and illustration asset set](assets.md#a-004)

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-022"></a>

## P-022: Error, offline and retry

Provides honest failure states and safe recovery.

Kind: pattern. Shared contract: [system-flow](families.md#system-flow).

### Variants to specify

- Network loss
- Service error
- Offline cache
- Retry

### Entry-specific states and behavior

- Distinguish unknown transaction outcomes before retrying.

### Project decisions still required

- Which actions are safe offline or safe to repeat?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native tablet app](profile-native-tablet.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Website](profile-website.md) | required | Shared starter requirement for this profile; confirm in project scope. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-048: Banner and inline alert](ui.md#c-048)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-023"></a>

## P-023: Destructive action and undo

Makes consequential changes understandable and recoverable where possible.

Kind: pattern. Shared contract: [system-flow](families.md#system-flow).

### Variants to specify

- Confirmation
- Undo
- Soft deletion
- Irreversible action

### Entry-specific states and behavior

- Pending action, canceled, completed and failed recovery.

### Project decisions still required

- Is extra confirmation necessary and is recovery real?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs destructive action and undo. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs destructive action and undo. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs destructive action and undo. |
| [Web app](profile-web-app.md) | optional | Include when the project needs destructive action and undo. |
| [Website](profile-website.md) | optional | Include when the project needs destructive action and undo. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-001: Button](ui.md#c-001)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-024"></a>

## P-024: Notifications and preferences

Coordinates relevant updates across channels.

Kind: pattern. Shared contract: [system-flow](families.md#system-flow).

### Variants to specify

- In-app
- Email
- Push
- Quiet mode

### Entry-specific states and behavior

- Permission denied, unread, duplicate and expired actions.

### Project decisions still required

- Which updates should be sent, stored or suppressed?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs notifications and preferences. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs notifications and preferences. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs notifications and preferences. |
| [Web app](profile-web-app.md) | optional | Include when the project needs notifications and preferences. |
| [Website](profile-website.md) | optional | Include when the project needs notifications and preferences. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-050: Notification item and inbox](ui.md#c-050)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-025"></a>

## P-025: File management and export

Supports a file from selection through delivery.

Kind: pattern. Shared contract: [system-flow](families.md#system-flow).

### Variants to specify

- Upload
- Preview
- Download
- Export
- Delete

### Entry-specific states and behavior

- Progress, format mismatch, failure and canceled operation.

### Project decisions still required

- What native format, export and rights evidence is needed?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs file management and export. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs file management and export. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs file management and export. |
| [Web app](profile-web-app.md) | optional | Include when the project needs file management and export. |
| [Website](profile-website.md) | optional | Include when the project needs file management and export. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-021: File upload control](ui.md#c-021)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-026"></a>

## P-026: Help and support

Provides help at the point of need.

Kind: pattern. Shared contract: [content-flow](families.md#content-flow).

### Variants to specify

- Context help
- FAQ
- Contact
- Support request

### Entry-specific states and behavior

- Unavailable help, escalation and resolved state.

### Project decisions still required

- What can be self-served and what needs a person?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs help and support. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs help and support. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs help and support. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs help and support. |
| [Web app](profile-web-app.md) | optional | Include when the project needs help and support. |
| [Website](profile-website.md) | optional | Include when the project needs help and support. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-048: Banner and inline alert](ui.md#c-048)

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-027"></a>

## P-027: Editorial storytelling and evidence

Structures information and claims into a clear narrative.

Kind: pattern. Shared contract: [content-flow](families.md#content-flow).

### Variants to specify

- Article
- Case narrative
- Explainer
- Proof block

### Entry-specific states and behavior

- Missing evidence and out-of-date claims need explicit handling.
- Specify reusable section slots, component IDs, reading order and responsive transformations for split, stacked, overlay, collage and proof compositions. Treat these as contextual variants, not mandatory aesthetics.

### Project decisions still required

- Which claims need verification before publication?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs editorial storytelling and evidence. |
| [Passive display](profile-display.md) | optional | Include when the project needs editorial storytelling and evidence. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs editorial storytelling and evidence. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs editorial storytelling and evidence. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs editorial storytelling and evidence. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs editorial storytelling and evidence. |
| [Web app](profile-web-app.md) | optional | Include when the project needs editorial storytelling and evidence. |
| [Website](profile-website.md) | optional | Include when the project needs editorial storytelling and evidence. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [F-018: Voice and tone](foundations.md#f-018)

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE), [SPECIMEN-SYNTH](../INVENTORY-SOURCES.md#SPECIMEN-SYNTH). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation. Original generic documentation refinement; comparison disposition is recorded in EXAMPLE-COMPARISON.md. The added specimen/composition advice is internally synthesized; SPECIMEN-SYNTH records the EX3 observation boundary, while other cited sources retain their narrower basis.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-028"></a>

## P-028: Scheduling and calendar workflow

Coordinates dates, times and availability when needed.

Kind: pattern. Shared contract: [form-flow](families.md#form-flow).

### Variants to specify

- Appointment
- Reservation
- Reschedule
- Cancel

### Entry-specific states and behavior

- Time-zone ambiguity, slot conflict and expired hold.

### Project decisions still required

- Is scheduling present and which availability system is authoritative?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | needs-discovery | Presence and specialist constraints depend on the brief; decide before inclusion. |
| [Native tablet app](profile-native-tablet.md) | needs-discovery | Presence and specialist constraints depend on the brief; decide before inclusion. |
| [Shared touch display](profile-touch.md) | needs-discovery | Presence and specialist constraints depend on the brief; decide before inclusion. |
| [Web app](profile-web-app.md) | needs-discovery | Presence and specialist constraints depend on the brief; decide before inclusion. |
| [Website](profile-website.md) | needs-discovery | Presence and specialist constraints depend on the brief; decide before inclusion. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-019: Date and date-range picker](ui.md#c-019), [C-020: Time picker](ui.md#c-020)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-029"></a>

## P-029: Map and location workflow

Uses geographic context when it serves the task.

Kind: pattern. Shared contract: [discovery](families.md#discovery).

### Variants to specify

- Map/list
- Search location
- Directions
- Region selection

### Entry-specific states and behavior

- Permission denied, uncertain location and missing map tiles.

### Project decisions still required

- Is a map necessary and what text alternative is useful?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | needs-discovery | Presence and specialist constraints depend on the brief; decide before inclusion. |
| [Native tablet app](profile-native-tablet.md) | needs-discovery | Presence and specialist constraints depend on the brief; decide before inclusion. |
| [Shared touch display](profile-touch.md) | needs-discovery | Presence and specialist constraints depend on the brief; decide before inclusion. |
| [Web app](profile-web-app.md) | needs-discovery | Presence and specialist constraints depend on the brief; decide before inclusion. |
| [Website](profile-website.md) | needs-discovery | Presence and specialist constraints depend on the brief; decide before inclusion. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-030"></a>

## P-030: Collaboration and activity history

Coordinates shared work and visible changes.

Kind: pattern. Shared contract: [system-flow](families.md#system-flow).

### Variants to specify

- Comments
- Presence
- Activity log
- Conflict resolution

### Entry-specific states and behavior

- Stale edits, permissions, conflict and reconciliation.

### Project decisions still required

- Who owns state and how are simultaneous changes reconciled?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs collaboration and activity history. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs collaboration and activity history. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs collaboration and activity history. |
| [Web app](profile-web-app.md) | optional | Include when the project needs collaboration and activity history. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-031"></a>

## P-031: Display scheduling and attract loop

Presents unattended content over time.

Kind: pattern. Shared contract: [physical-flow](families.md#physical-flow).

### Variants to specify

- Playlist
- Attract loop
- Scheduled
- Static fallback

### Entry-specific states and behavior

- Idle, stale content, offline and playback failure.

### Project decisions still required

- What dwell time, schedule and burn-in precautions fit the panel?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs display scheduling and attract loop. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs display scheduling and attract loop. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [ADA](../INVENTORY-SOURCES.md#ADA), [ICT](../INVENTORY-SOURCES.md#ICT), [SMI](../INVENTORY-SOURCES.md#SMI), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-032"></a>

## P-032: Shared touch session and idle reset

Keeps public interactive sessions usable and private.

Kind: pattern. Shared contract: [physical-flow](families.md#physical-flow).

### Variants to specify

- Start
- Active
- Idle warning
- Extend
- Reset

### Entry-specific states and behavior

- Warn before reset, allow accessible extension and clear session data.

### Project decisions still required

- What must be cleared between users and how is it verified?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-001: Button](ui.md#c-001)

Related concepts: See shared family and dependencies.

Source basis: [ADA](../INVENTORY-SOURCES.md#ADA), [ICT](../INVENTORY-SOURCES.md#ICT), [SMI](../INVENTORY-SOURCES.md#SMI), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-033"></a>

## P-033: Physical access and assisted alternative

Provides usable access to a physical display or kiosk.

Kind: pattern. Shared contract: [physical-flow](families.md#physical-flow).

### Variants to specify

- Seated
- Standing
- Assisted
- Alternative channel

### Entry-specific states and behavior

- Unreachable controls, glare and inaccessible input require an alternative.

### Project decisions still required

- Which site measurements and user checks are still missing?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs physical access and assisted alternative. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs physical access and assisted alternative. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [ADA](../INVENTORY-SOURCES.md#ADA), [ICT](../INVENTORY-SOURCES.md#ICT), [SMI](../INVENTORY-SOURCES.md#SMI), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-034"></a>

## P-034: Kiosk recovery and operator escape

Recovers unattended equipment without exposing protected operations.

Kind: pattern. Shared contract: [physical-flow](families.md#physical-flow).

### Variants to specify

- User recovery
- Operator exit
- Restart
- Offline fallback

### Entry-specific states and behavior

- Failed reset and restricted operator actions need explicit handling.

### Project decisions still required

- Who may exit kiosk mode and how is a lost user recovered?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs kiosk recovery and operator escape. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs kiosk recovery and operator escape. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [ADA](../INVENTORY-SOURCES.md#ADA), [ICT](../INVENTORY-SOURCES.md#ICT), [SMI](../INVENTORY-SOURCES.md#SMI), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="p-035"></a>

## P-035: Share, print and deep link

Preserves useful context across destinations or media.

Kind: pattern. Shared contract: [content-flow](families.md#content-flow).

### Variants to specify

- Copy link
- Native share
- Print view
- Deep link

### Entry-specific states and behavior

- Invalid destination, unavailable app and restricted content.

### Project decisions still required

- Which state and private data should be omitted from sharing?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs share, print and deep link. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs share, print and deep link. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs share, print and deep link. |
| [Web app](profile-web-app.md) | optional | Include when the project needs share, print and deep link. |
| [Website](profile-website.md) | optional | Include when the project needs share, print and deep link. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

