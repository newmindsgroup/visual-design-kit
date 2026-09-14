# Page and screen templates

Version-Timestamp: 2026-09-07 14:29:54 AST

Generated from master.json. Listed concepts and shared specification starters only. No completed component specifications, implementation or testing is supplied. Profile selections are starting recommendations, not approved project scope.

[Index](index.md) | [Specification template](../templates/system-item.md)

<a id="t-001"></a>

## T-001: Content page

Presents a focused body of information.

Kind: template. Shared contract: [web-page](families.md#web-page).

### Variants to specify

- Article
- Policy
- Documentation

### Entry-specific states and behavior

- Reading order, long content and missing media.

### Project decisions still required

- What content model and primary task does this page serve?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | optional | Include when the project needs content page. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-027: Editorial storytelling and evidence](patterns.md#p-027)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-002"></a>

## T-002: Home and landing page

Introduces a site, offer or campaign and its next steps.

Kind: template. Shared contract: [web-page](families.md#web-page).

### Variants to specify

- Corporate home
- Campaign
- Product landing

### Entry-specific states and behavior

- Content priority and loading behavior vary by viewport.

### Project decisions still required

- What should visitors understand and do first?
- Which document metadata, social preview and indexing policy apply, and what can be exposed publicly?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | optional | Include when the project needs home and landing page. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-023: Header and application bar](ui.md#c-023)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation. Original generic documentation refinement; comparison disposition is recorded in EXAMPLE-COMPARISON.md.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-003"></a>

## T-003: Listing and search page

Collects browsable or searchable items.

Kind: template. Shared contract: [web-page](families.md#web-page).

### Variants to specify

- Directory
- Search results
- Resource index

### Entry-specific states and behavior

- No results, pagination/filter state and missing items.

### Project decisions still required

- Which item types and finding methods are needed?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | optional | Include when the project needs listing and search page. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-005: Search results and no results](patterns.md#p-005)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-004"></a>

## T-004: Detail page

Explains one item, service or content subject.

Kind: template. Shared contract: [web-page](families.md#web-page).

### Variants to specify

- Service
- Product
- Resource
- Profile

### Entry-specific states and behavior

- Unavailable subject, long content and related items.

### Project decisions still required

- Which details answer the reader's decision?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | optional | Include when the project needs detail page. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-035: Card and tile](ui.md#c-035)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-005"></a>

## T-005: Contact and lead form page

Collects a bounded inquiry or lead.

Kind: template. Shared contract: [web-page](families.md#web-page).

### Variants to specify

- Contact
- Request demo
- Inquiry

### Entry-specific states and behavior

- Validation, consent, submission and receipt.

### Project decisions still required

- What minimum fields and follow-up expectations are appropriate?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | optional | Include when the project needs contact and lead form page. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-001: Form validation and recovery](patterns.md#p-001)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-006"></a>

## T-006: Pricing and comparison page

Explains commercial choices when an offer needs them.

Kind: template. Shared contract: [web-page](families.md#web-page).

### Variants to specify

- Pricing plans
- Comparison
- Quote-led

### Entry-specific states and behavior

- Uncertain price, localization and feature differences.

### Project decisions still required

- Are prices public, conditional or quote-based?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | optional | Include when the project needs pricing and comparison page. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-017: Product discovery and comparison](patterns.md#p-017)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-007"></a>

## T-007: Help and support page

Organizes support information and escalation.

Kind: template. Shared contract: [web-page](families.md#web-page).

### Variants to specify

- FAQ
- Help center
- Status
- Contact support

### Entry-specific states and behavior

- No matching article and unavailable support.

### Project decisions still required

- What are the most common support tasks?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | optional | Include when the project needs help and support page. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-026: Help and support](patterns.md#p-026)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-008"></a>

## T-008: Confirmation and receipt page

Summarizes a completed or pending action.

Kind: template. Shared contract: [web-page](families.md#web-page).

### Variants to specify

- Success
- Pending
- Reference number

### Entry-specific states and behavior

- Unknown outcome must not be shown as success.

### Project decisions still required

- What proof and next steps are useful?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | optional | Include when the project needs confirmation and receipt page. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-003: Review, confirm and receipt](patterns.md#p-003)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-009"></a>

## T-009: Not-found and service-error page

Provides useful navigation or recovery after failure.

Kind: template. Shared contract: [web-page](families.md#web-page).

### Variants to specify

- 404
- Unavailable service
- Access denied

### Entry-specific states and behavior

- Avoid exposing private diagnostics or losing context.

### Project decisions still required

- Where can users safely continue?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | optional | Include when the project needs not-found and service-error page. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-022: Error, offline and retry](patterns.md#p-022)

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-010"></a>

## T-010: Application shell

Provides the persistent navigation and workspace around tasks.

Kind: template. Shared contract: [app-screen](families.md#app-screen).

### Variants to specify

- Single pane
- Sidebar
- Split
- Responsive

### Entry-specific states and behavior

- Route changes, loading, offline and permissions.

### Project decisions still required

- Which parts persist and which belong to individual screens?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs application shell. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs application shell. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs application shell. |
| [Web app](profile-web-app.md) | optional | Include when the project needs application shell. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-025: Primary navigation](ui.md#c-025)

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-011"></a>

## T-011: Dashboard and overview screen

Summarizes relevant activity and next actions.

Kind: template. Shared contract: [app-screen](families.md#app-screen).

### Variants to specify

- Metrics
- Task overview
- Status
- Personalized

### Entry-specific states and behavior

- Empty, stale and partial panels should not imply complete data.

### Project decisions still required

- What decisions should the overview support?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs dashboard and overview screen. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs dashboard and overview screen. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs dashboard and overview screen. |
| [Web app](profile-web-app.md) | optional | Include when the project needs dashboard and overview screen. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-041: Metric and statistic](ui.md#c-041)

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-012"></a>

## T-012: Collection and management screen

Helps users find and act on many records.

Kind: template. Shared contract: [app-screen](families.md#app-screen).

### Variants to specify

- List
- Table
- Grid
- Bulk actions

### Entry-specific states and behavior

- Filtering, no results, selected items and partial data.
- Native phone lists use the app-screen platform contract; specify selection, optional swipe actions and drill-down without requiring a new template ID.

### Project decisions still required

- Which record operations are actually needed?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs collection and management screen. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs collection and management screen. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs collection and management screen. |
| [Web app](profile-web-app.md) | optional | Include when the project needs collection and management screen. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-036: List and list item](ui.md#c-036)

Related concepts: [T-018: Mobile detail and drill-down screen](templates.md#t-018)

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-013"></a>

## T-013: Record detail and workspace

Combines the information and actions for one record.

Kind: template. Shared contract: [app-screen](families.md#app-screen).

### Variants to specify

- Read-only
- Editable
- Split detail
- Activity

### Entry-specific states and behavior

- Missing record, access restriction, unsaved edits and conflicts.

### Project decisions still required

- What information and actions belong together?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs record detail and workspace. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs record detail and workspace. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs record detail and workspace. |
| [Web app](profile-web-app.md) | optional | Include when the project needs record detail and workspace. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-004: Inline editing and autosave](patterns.md#p-004)

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-014"></a>

## T-014: Create and edit screen

Collects or changes structured information.

Kind: template. Shared contract: [app-screen](families.md#app-screen).

### Variants to specify

- Single form
- Multi-step
- Draft

### Entry-specific states and behavior

- Validation, saving, conflict, cancellation and recovery.

### Project decisions still required

- What counts as a committed record?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs create and edit screen. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs create and edit screen. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs create and edit screen. |
| [Web app](profile-web-app.md) | optional | Include when the project needs create and edit screen. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-001: Form validation and recovery](patterns.md#p-001)

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-015"></a>

## T-015: Authentication and recovery screen

Provides an optional account-access flow.

Kind: template. Shared contract: [app-screen](families.md#app-screen).

### Variants to specify

- Sign-in
- Register
- Verify
- Recover

### Entry-specific states and behavior

- Invalid, locked, expired and alternate method states.

### Project decisions still required

- Is authentication required for this part of the product?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs authentication and recovery screen. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs authentication and recovery screen. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs authentication and recovery screen. |
| [Web app](profile-web-app.md) | optional | Include when the project needs authentication and recovery screen. |
| [Website](profile-website.md) | optional | Include when the project needs authentication and recovery screen. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-010: Sign-in and authentication](patterns.md#p-010)

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-016"></a>

## T-016: Account and settings screen

Organizes user-controlled account and preference settings.

Kind: template. Shared contract: [app-screen](families.md#app-screen).

### Variants to specify

- Personal
- Organization
- Security
- Preferences

### Entry-specific states and behavior

- Permission differences and unsaved or failed changes.

### Project decisions still required

- Which settings belong to which owner?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs account and settings screen. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs account and settings screen. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs account and settings screen. |
| [Web app](profile-web-app.md) | optional | Include when the project needs account and settings screen. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-013: Account settings and profile](patterns.md#p-013)

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-017"></a>

## T-017: Onboarding and setup screen

Guides first-use setup where needed.

Kind: template. Shared contract: [app-screen](families.md#app-screen).

### Variants to specify

- Welcome
- Setup tasks
- Permission education

### Entry-specific states and behavior

- Skip, resume, incomplete and returning-user states.

### Project decisions still required

- What setup is essential before value is available?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs onboarding and setup screen. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs onboarding and setup screen. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs onboarding and setup screen. |
| [Web app](profile-web-app.md) | optional | Include when the project needs onboarding and setup screen. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-009: Onboarding and first use](patterns.md#p-009)

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-018"></a>

## T-018: Mobile detail and drill-down screen

Presents a focused phone task with native navigation.

Kind: template. Shared contract: [app-screen](families.md#app-screen).

### Variants to specify

- Push navigation
- Modal task
- Native form

### Entry-specific states and behavior

- System Back, safe areas, keyboard and interrupted activity.

### Project decisions still required

- Which navigation preserves the user's task context?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs mobile detail and drill-down screen. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs mobile detail and drill-down screen. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-029: Back and close control](ui.md#c-029)

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-019"></a>

## T-019: Tablet list-detail workspace

Uses expanded space for related content and tasks.

Kind: template. Shared contract: [app-screen](families.md#app-screen).

### Variants to specify

- Two pane
- Three pane
- Compact fallback

### Entry-specific states and behavior

- Resize, orientation, keyboard, pointer and selected record persistence.

### Project decisions still required

- What collapses when the available window becomes narrow?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs tablet list-detail workspace. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | optional | Include when the project needs tablet list-detail workspace. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [C-026: Sidebar, drawer and navigation rail](ui.md#c-026)

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-020"></a>

## T-020: Notification center screen

Provides a durable list of updates.

Kind: template. Shared contract: [app-screen](families.md#app-screen).

### Variants to specify

- Unread
- All
- Filtered
- Grouped

### Entry-specific states and behavior

- Empty inbox, expired actions and denied notification permission.

### Project decisions still required

- Which updates remain useful over time?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs notification center screen. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs notification center screen. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs notification center screen. |
| [Web app](profile-web-app.md) | optional | Include when the project needs notification center screen. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-024: Notifications and preferences](patterns.md#p-024)

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-021"></a>

## T-021: Display message layout

Presents a readable unattended information message.

Kind: template. Shared contract: [display-layout](families.md#display-layout).

### Variants to specify

- Announcement
- Schedule
- Wayfinding
- Static fallback

### Entry-specific states and behavior

- Dwell, stale data, image failure and panel constraints.

### Project decisions still required

- What viewing distance and orientation govern the layout?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs display message layout. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs display message layout. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-031: Display scheduling and attract loop](patterns.md#p-031)

Related concepts: See shared family and dependencies.

Source basis: [SMI](../INVENTORY-SOURCES.md#SMI), [ADA](../INVENTORY-SOURCES.md#ADA), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-022"></a>

## T-022: Touch welcome and task screen

Starts and guides a shared public interaction.

Kind: template. Shared contract: [display-layout](families.md#display-layout).

### Variants to specify

- Welcome
- Task menu
- Guided task
- Assistance

### Entry-specific states and behavior

- Idle warning, accessible extension, session reset and help.

### Project decisions still required

- Can a first-time user recover without staff intervention?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs touch welcome and task screen. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-032: Shared touch session and idle reset](patterns.md#p-032)

Related concepts: See shared family and dependencies.

Source basis: [SMI](../INVENTORY-SOURCES.md#SMI), [ADA](../INVENTORY-SOURCES.md#ADA), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="t-023"></a>

## T-023: Optional commerce screen set

Assembles catalog, cart, checkout and order views.

Kind: template. Shared contract: [app-screen](families.md#app-screen).

### Variants to specify

- Browse
- Cart
- Checkout
- Order status

### Entry-specific states and behavior

- Payment and stock outcomes must reflect authoritative state.

### Project decisions still required

- Which commercial features are in scope?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs optional commerce screen set. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs optional commerce screen set. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs optional commerce screen set. |
| [Web app](profile-web-app.md) | optional | Include when the project needs optional commerce screen set. |
| [Website](profile-website.md) | optional | Include when the project needs optional commerce screen set. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: [P-018: Cart and checkout](patterns.md#p-018), [P-019: Payment and refund](patterns.md#p-019)

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

