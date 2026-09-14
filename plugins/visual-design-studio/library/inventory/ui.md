# UI primitives and components

Version-Timestamp: 2026-09-07 14:29:54 AST

Generated from master.json. Listed concepts and shared specification starters only. No completed component specifications, implementation or testing is supplied. Profile selections are starting recommendations, not approved project scope.

[Index](index.md) | [Specification template](../templates/system-item.md)

<a id="c-001"></a>

## C-001: Button

Triggers an action.

Kind: component. Shared contract: [action](families.md#action).

### Variants to specify

- Primary
- Secondary
- Quiet
- Destructive
- Icon-only

### Entry-specific states and behavior

- Rest, focus, press, busy and unavailable states
- Icon-only buttons need a name; busy actions must not duplicate.

### Project decisions still required

- Which action is primary and can it be undone?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native tablet app](profile-native-tablet.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Website](profile-website.md) | required | Shared starter requirement for this profile; confirm in project scope. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE), [USW](../INVENTORY-SOURCES.md#USW). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation. USW component-index terminology was compared; no implementation was copied or tested.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-002"></a>

## C-002: Link

Navigates to a destination or resource.

Kind: component. Shared contract: [action](families.md#action).

### Variants to specify

- Inline
- Standalone
- External
- Download

### Entry-specific states and behavior

- Visited and current states may matter
- Do not use an empty link as a button; explain file or external destinations.

### Project decisions still required

- Where does it lead and should context be preserved?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native tablet app](profile-native-tablet.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Website](profile-website.md) | required | Shared starter requirement for this profile; confirm in project scope. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE), [USW](../INVENTORY-SOURCES.md#USW). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation. USW component-index terminology was compared; no implementation was copied or tested.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-003"></a>

## C-003: Button group and split button

Groups related actions, sometimes with a default action and menu.

Kind: component. Shared contract: [action](families.md#action).

### Variants to specify

- Horizontal
- Vertical
- Split
- Segmented action

### Entry-specific states and behavior

- Separate default action from menu trigger and focus targets.

### Project decisions still required

- Is this a set of actions or a choice control?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs button group and split button. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs button group and split button. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs button group and split button. |
| [Web app](profile-web-app.md) | optional | Include when the project needs button group and split button. |
| [Website](profile-website.md) | optional | Include when the project needs button group and split button. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-004"></a>

## C-004: Floating action button

Provides a prominent contextual primary action.

Kind: component. Shared contract: [action](families.md#action).

### Variants to specify

- Compact
- Extended
- Action menu

### Entry-specific states and behavior

- Must not cover content or compete with equally prominent actions.

### Project decisions still required

- Does a floating action fit the platform and task?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs floating action button. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs floating action button. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs floating action button. |
| [Web app](profile-web-app.md) | optional | Include when the project needs floating action button. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-005"></a>

## C-005: Text field

Collects a single line of text.

Kind: component. Shared contract: [input](families.md#input).

### Variants to specify

- Plain
- Email
- URL
- Telephone
- Password

### Entry-specific states and behavior

- Empty, focused, typing, filled, invalid, read-only and unavailable
- Choose correct keyboard and autofill intent.

### Project decisions still required

- What input type, validation and privacy rules apply?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs text field. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs text field. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs text field. |
| [Web app](profile-web-app.md) | optional | Include when the project needs text field. |
| [Website](profile-website.md) | optional | Include when the project needs text field. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE), [USW](../INVENTORY-SOURCES.md#USW). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation. USW component-index terminology was compared; no implementation was copied or tested.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-006"></a>

## C-006: Text area

Collects multiple lines of plain text.

Kind: component. Shared contract: [input](families.md#input).

### Variants to specify

- Fixed
- Auto-growing
- Character-limited

### Entry-specific states and behavior

- Show limits without losing input or trapping scroll.

### Project decisions still required

- How much text is useful and how does it resize?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs text area. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs text area. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs text area. |
| [Web app](profile-web-app.md) | optional | Include when the project needs text area. |
| [Website](profile-website.md) | optional | Include when the project needs text area. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-007"></a>

## C-007: Number input and stepper

Collects a numeric quantity.

Kind: component. Shared contract: [input](families.md#input).

### Variants to specify

- Integer
- Decimal
- Stepper
- Unit-bearing

### Entry-specific states and behavior

- Define bounds, step, parsing and locale
- Do not use for identifiers that only contain digits.

### Project decisions still required

- What unit, precision and valid range does the task need?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs number input and stepper. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs number input and stepper. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs number input and stepper. |
| [Web app](profile-web-app.md) | optional | Include when the project needs number input and stepper. |
| [Website](profile-website.md) | optional | Include when the project needs number input and stepper. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-008"></a>

## C-008: Search field

Collects a query for finding content.

Kind: component. Shared contract: [input](families.md#input).

### Variants to specify

- Submit
- Instant
- Scoped
- Clearable

### Entry-specific states and behavior

- Query, suggestions, loading, no-results and clear behavior are distinct.

### Project decisions still required

- When does searching run and is the query retained?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs search field. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs search field. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs search field. |
| [Web app](profile-web-app.md) | optional | Include when the project needs search field. |
| [Website](profile-website.md) | optional | Include when the project needs search field. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-009"></a>

## C-009: Field label, help and counter

Explains an input and its constraints.

Kind: primitive. Shared contract: [structure](families.md#structure).

### Variants to specify

- Label
- Hint
- Required indicator
- Counter

### Entry-specific states and behavior

- Associate label and help with the field; announce useful limits without noise.

### Project decisions still required

- What must users know before entering data?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs field label, help and counter. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs field label, help and counter. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs field label, help and counter. |
| [Web app](profile-web-app.md) | optional | Include when the project needs field label, help and counter. |
| [Website](profile-website.md) | optional | Include when the project needs field label, help and counter. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-010"></a>

## C-010: Fieldset and form group

Groups related fields or controls under one meaning.

Kind: component. Shared contract: [structure](families.md#structure).

### Variants to specify

- Legend
- Nested group
- Repeated group

### Entry-specific states and behavior

- Preserve semantic grouping and meaningful reading order.

### Project decisions still required

- Which inputs answer one shared question?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs fieldset and form group. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs fieldset and form group. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs fieldset and form group. |
| [Web app](profile-web-app.md) | optional | Include when the project needs fieldset and form group. |
| [Website](profile-website.md) | optional | Include when the project needs fieldset and form group. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-011"></a>

## C-011: Checkbox

Selects independent options or acknowledges a choice.

Kind: component. Shared contract: [selection](families.md#selection).

### Variants to specify

- Unchecked
- Checked
- Mixed
- Group

### Entry-specific states and behavior

- Mixed state is different from unchecked
- Do not preselect consent without an appropriate basis.

### Project decisions still required

- Can users choose multiple items and is a mixed state needed?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs checkbox. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs checkbox. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs checkbox. |
| [Web app](profile-web-app.md) | optional | Include when the project needs checkbox. |
| [Website](profile-website.md) | optional | Include when the project needs checkbox. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [GOV](../INVENTORY-SOURCES.md#GOV), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE), [USW](../INVENTORY-SOURCES.md#USW). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation. USW component-index terminology was compared; no implementation was copied or tested.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-012"></a>

## C-012: Radio group

Selects one option from an explicit set.

Kind: component. Shared contract: [selection](families.md#selection).

### Variants to specify

- Inline
- Stacked
- Card-like choices

### Entry-specific states and behavior

- Selected/unselected, focus and unavailable options need clear semantics.

### Project decisions still required

- Should there be a default or an explicit initial choice?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs radio group. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs radio group. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs radio group. |
| [Web app](profile-web-app.md) | optional | Include when the project needs radio group. |
| [Website](profile-website.md) | optional | Include when the project needs radio group. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [GOV](../INVENTORY-SOURCES.md#GOV), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE), [USW](../INVENTORY-SOURCES.md#USW). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation. USW component-index terminology was compared; no implementation was copied or tested.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-013"></a>

## C-013: Switch

Turns a setting on or off.

Kind: component. Shared contract: [selection](families.md#selection).

### Variants to specify

- On
- Off
- Pending change

### Entry-specific states and behavior

- Clarify whether the change takes effect immediately; show failure and revert if needed.

### Project decisions still required

- Is this an immediate setting rather than form submission?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs switch. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs switch. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs switch. |
| [Web app](profile-web-app.md) | optional | Include when the project needs switch. |
| [Website](profile-website.md) | optional | Include when the project needs switch. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [GOV](../INVENTORY-SOURCES.md#GOV), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-014"></a>

## C-014: Select and picker

Chooses an option from a list using a platform control.

Kind: component. Shared contract: [selection](families.md#selection).

### Variants to specify

- Single
- Native picker
- Grouped options

### Entry-specific states and behavior

- Placeholder, selected, unavailable and long-option states
- Use native semantics where possible.

### Project decisions still required

- How many options and which platform picker is appropriate?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs select and picker. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs select and picker. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs select and picker. |
| [Web app](profile-web-app.md) | optional | Include when the project needs select and picker. |
| [Website](profile-website.md) | optional | Include when the project needs select and picker. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [GOV](../INVENTORY-SOURCES.md#GOV), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-015"></a>

## C-015: Combobox and autocomplete

Combines text entry with a list of suggestions.

Kind: component. Shared contract: [input](families.md#input).

### Variants to specify

- Editable
- Select-only
- Async
- Creatable

### Entry-specific states and behavior

- Open/closed list, active option, loading and no match
- Typed text and selected option are not automatically equivalent.

### Project decisions still required

- Must a value match an option, and how are suggestions announced?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs combobox and autocomplete. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs combobox and autocomplete. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs combobox and autocomplete. |
| [Web app](profile-web-app.md) | optional | Include when the project needs combobox and autocomplete. |
| [Website](profile-website.md) | optional | Include when the project needs combobox and autocomplete. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-016"></a>

## C-016: Multiselect

Chooses several items from a larger option set.

Kind: component. Shared contract: [selection](families.md#selection).

### Variants to specify

- Checklist
- Tokenized
- Searchable

### Entry-specific states and behavior

- Selected count, limits, removal, no results and unavailable options.

### Project decisions still required

- How will users review and clear the complete selection?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs multiselect. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs multiselect. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs multiselect. |
| [Web app](profile-web-app.md) | optional | Include when the project needs multiselect. |
| [Website](profile-website.md) | optional | Include when the project needs multiselect. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [GOV](../INVENTORY-SOURCES.md#GOV), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-017"></a>

## C-017: Segmented control

Switches among a small set of related choices or views.

Kind: component. Shared contract: [selection](families.md#selection).

### Variants to specify

- Single choice
- Multiple choice
- View switch

### Entry-specific states and behavior

- Selected state and action semantics must be explicit.

### Project decisions still required

- Is this selection, filtering or navigation?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs segmented control. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs segmented control. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs segmented control. |
| [Web app](profile-web-app.md) | optional | Include when the project needs segmented control. |
| [Website](profile-website.md) | optional | Include when the project needs segmented control. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [GOV](../INVENTORY-SOURCES.md#GOV), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-018"></a>

## C-018: Slider and range slider

Chooses one value or a bounded interval along a scale.

Kind: component. Shared contract: [selection](families.md#selection).

### Variants to specify

- Single thumb
- Multiple thumbs
- Discrete
- Continuous

### Entry-specific states and behavior

- Keyboard increments, bounds, active thumb and value labels
- Provide a precise-entry alternative when useful.

### Project decisions still required

- Can users choose accurately without dragging?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs slider and range slider. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs slider and range slider. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs slider and range slider. |
| [Web app](profile-web-app.md) | optional | Include when the project needs slider and range slider. |
| [Website](profile-website.md) | optional | Include when the project needs slider and range slider. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [GOV](../INVENTORY-SOURCES.md#GOV), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-019"></a>

## C-019: Date and date-range picker

Collects a calendar date or date interval.

Kind: component. Shared contract: [input](families.md#input).

### Variants to specify

- Text entry
- Calendar
- Range
- Native picker

### Entry-specific states and behavior

- Invalid date, unavailable dates, open calendar and range boundaries
- Date formats and time zones require explicit choices.

### Project decisions still required

- Is the date historical, approximate or constrained?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs date and date-range picker. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs date and date-range picker. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs date and date-range picker. |
| [Web app](profile-web-app.md) | optional | Include when the project needs date and date-range picker. |
| [Website](profile-website.md) | optional | Include when the project needs date and date-range picker. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-020"></a>

## C-020: Time picker

Collects a time of day.

Kind: component. Shared contract: [input](families.md#input).

### Variants to specify

- Text
- Clock
- 12-hour
- 24-hour

### Entry-specific states and behavior

- Invalid time, daylight-saving ambiguity and time-zone labels.

### Project decisions still required

- Which clock, time zone and precision should apply?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs time picker. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs time picker. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs time picker. |
| [Web app](profile-web-app.md) | optional | Include when the project needs time picker. |
| [Website](profile-website.md) | optional | Include when the project needs time picker. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-021"></a>

## C-021: File upload control

Collects one or more files.

Kind: component. Shared contract: [input](families.md#input).

### Variants to specify

- Single
- Multiple
- Drop zone
- Native chooser

### Entry-specific states and behavior

- Queued, uploading, progress, canceled, rejected and retry states
- Provide a non-drag input path and disclose restrictions.

### Project decisions still required

- Which types, sizes, security checks and retention apply?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs file upload control. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs file upload control. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs file upload control. |
| [Web app](profile-web-app.md) | optional | Include when the project needs file upload control. |
| [Website](profile-website.md) | optional | Include when the project needs file upload control. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-022"></a>

## C-022: Rich-text editor

Collects formatted content rather than plain text.

Kind: component. Shared contract: [input](families.md#input).

### Variants to specify

- Formatting toolbar
- Markdown
- Structured blocks

### Entry-specific states and behavior

- Selection, formatting, unsaved, invalid content and paste behavior
- Editing shortcuts and output semantics need dedicated tests.

### Project decisions still required

- Which formatting is necessary and how is pasted content constrained?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs rich-text editor. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs rich-text editor. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | optional | Include when the project needs rich-text editor. |
| [Website](profile-website.md) | optional | Include when the project needs rich-text editor. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-023"></a>

## C-023: Header and application bar

Provides top-level identity, location and common controls.

Kind: component. Shared contract: [navigation](families.md#navigation).

### Variants to specify

- Website header
- Native app bar
- Compact
- Expanded

### Entry-specific states and behavior

- Scrolled, current route, expanded navigation and constrained width.

### Project decisions still required

- Which controls remain visible and which belong to the page?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs header and application bar. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs header and application bar. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs header and application bar. |
| [Web app](profile-web-app.md) | optional | Include when the project needs header and application bar. |
| [Website](profile-website.md) | optional | Include when the project needs header and application bar. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-024"></a>

## C-024: Footer

Provides secondary navigation and supporting information.

Kind: component. Shared contract: [structure](families.md#structure).

### Variants to specify

- Simple
- Multi-column
- Legal
- Utility

### Entry-specific states and behavior

- Long legal text and narrow layouts need readable order.

### Project decisions still required

- What supporting links and disclosures are actually necessary?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | optional | Include when the project needs footer. |
| [Website](profile-website.md) | optional | Include when the project needs footer. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-025"></a>

## C-025: Primary navigation

Provides access to top-level destinations.

Kind: component. Shared contract: [navigation](families.md#navigation).

### Variants to specify

- Horizontal
- Vertical
- Collapsible
- Native destinations

### Entry-specific states and behavior

- Current destination, narrow layout and overflow
- Do not disable native destination tabs just because content is empty.

### Project decisions still required

- Which destinations are truly top level?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs primary navigation. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs primary navigation. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs primary navigation. |
| [Web app](profile-web-app.md) | optional | Include when the project needs primary navigation. |
| [Website](profile-website.md) | optional | Include when the project needs primary navigation. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-026"></a>

## C-026: Sidebar, drawer and navigation rail

Provides side navigation suited to available space.

Kind: component. Shared contract: [navigation](families.md#navigation).

### Variants to specify

- Persistent
- Collapsible
- Modal drawer
- Rail

### Entry-specific states and behavior

- Expanded, collapsed, modal focus and selected destination.

### Project decisions still required

- When should navigation change form rather than merely shrink?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs sidebar, drawer and navigation rail. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs sidebar, drawer and navigation rail. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs sidebar, drawer and navigation rail. |
| [Web app](profile-web-app.md) | optional | Include when the project needs sidebar, drawer and navigation rail. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-027"></a>

## C-027: Native tab bar

Switches between major sections in a native app.

Kind: component. Shared contract: [navigation](families.md#navigation).

### Variants to specify

- iPhone tab bar
- iPad adaptable bar/sidebar
- Android navigation bar

### Entry-specific states and behavior

- Keep section state and distinguish navigation from toolbar actions.

### Project decisions still required

- Which platform navigation pattern fits phone and tablet?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs native tab bar. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs native tab bar. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-028"></a>

## C-028: Breadcrumb

Shows an ancestor path in a hierarchy.

Kind: component. Shared contract: [navigation](families.md#navigation).

### Variants to specify

- Full
- Collapsed
- Truncated

### Entry-specific states and behavior

- Current location, deep paths and narrow space.

### Project decisions still required

- Does the information architecture have a meaningful parent chain?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | optional | Include when the project needs breadcrumb. |
| [Website](profile-website.md) | optional | Include when the project needs breadcrumb. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-029"></a>

## C-029: Back and close control

Returns to prior context or dismisses a temporary view.

Kind: component. Shared contract: [navigation](families.md#navigation).

### Variants to specify

- History back
- Up to parent
- Modal close
- System Back

### Entry-specific states and behavior

- Previous context, unsaved work and end-of-history
- Back, cancel and close are not interchangeable.

### Project decisions still required

- What state survives and where does the user return?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs back and close control. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs back and close control. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs back and close control. |
| [Web app](profile-web-app.md) | optional | Include when the project needs back and close control. |
| [Website](profile-website.md) | optional | Include when the project needs back and close control. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-030"></a>

## C-030: Skip link and landmark navigation

Lets users bypass repeated page structure.

Kind: component. Shared contract: [navigation](families.md#navigation).

### Variants to specify

- Skip to main
- Skip to content
- Named landmarks

### Entry-specific states and behavior

- Becomes visible on focus; destination focus must work.

### Project decisions still required

- Which repeated regions should be bypassed?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | optional | Include when the project needs skip link and landmark navigation. |
| [Website](profile-website.md) | optional | Include when the project needs skip link and landmark navigation. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-031"></a>

## C-031: Pagination

Navigates through bounded result pages.

Kind: component. Shared contract: [navigation](families.md#navigation).

### Variants to specify

- Numbered
- Previous-next
- Compact

### Entry-specific states and behavior

- First/last page, current page, unavailable and loading
- Keep results and location understandable.

### Project decisions still required

- Is paging better than load-more or virtual scrolling?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs pagination. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs pagination. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs pagination. |
| [Web app](profile-web-app.md) | optional | Include when the project needs pagination. |
| [Website](profile-website.md) | optional | Include when the project needs pagination. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APPLE](../INVENTORY-SOURCES.md#APPLE), [MAT](../INVENTORY-SOURCES.md#MAT), [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-032"></a>

## C-032: Toolbar and command menu

Collects actions for the current context.

Kind: component. Shared contract: [action](families.md#action).

### Variants to specify

- Toolbar
- Overflow menu
- Context menu
- Command palette

### Entry-specific states and behavior

- Open menu, focused item, unavailable actions and active shortcut scope.
- Command-menu variants supplement action: open/closed, focused item, checked/unchecked where selectable and unavailable item. Specify roving focus where applicable and focus return on dismissal. Plain toolbar buttons do not inherit menu open/closed behavior.

### Project decisions still required

- Which actions are frequent and which need a searchable command path?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs toolbar and command menu. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs toolbar and command menu. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs toolbar and command menu. |
| [Web app](profile-web-app.md) | optional | Include when the project needs toolbar and command menu. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: [C-054: Tooltip and contextual help](ui.md#c-054)

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-033"></a>

## C-033: Tabs

Switches between related content panels in one context.

Kind: component. Shared contract: [disclosure](families.md#disclosure).

### Variants to specify

- Horizontal
- Vertical
- Scrollable

### Entry-specific states and behavior

- Active tab, focused tab and loaded panel are distinct
- Choose manual or automatic activation based on content response.

### Project decisions still required

- Is this in-context panel switching or top-level navigation?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs tabs. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs tabs. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs tabs. |
| [Web app](profile-web-app.md) | optional | Include when the project needs tabs. |
| [Website](profile-website.md) | optional | Include when the project needs tabs. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-034"></a>

## C-034: Accordion and disclosure

Shows and hides related content sections.

Kind: component. Shared contract: [disclosure](families.md#disclosure).

### Variants to specify

- Single-open
- Multi-open
- Details
- Expand-all

### Entry-specific states and behavior

- Expanded/collapsed, focused trigger and delayed content
- Do not conceal essential instructions.

### Project decisions still required

- Should users compare multiple sections at once?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs accordion and disclosure. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs accordion and disclosure. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs accordion and disclosure. |
| [Web app](profile-web-app.md) | optional | Include when the project needs accordion and disclosure. |
| [Website](profile-website.md) | optional | Include when the project needs accordion and disclosure. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [GOV](../INVENTORY-SOURCES.md#GOV), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-035"></a>

## C-035: Card and tile

Groups content about one subject.

Kind: component. Shared contract: [structure](families.md#structure).

### Variants to specify

- Informational
- Navigable
- Selectable
- Actionable

### Entry-specific states and behavior

- Interactive variants need separate focus and selection contracts; avoid nested competing click targets.
- Selectable/actionable cards supplement structure: focus, pressed, selected/unselected and unavailable as applicable. A static content card has only presentation states. Define its real link or button target rather than making an unexplained focusable container.

### Project decisions still required

- What is the single primary purpose of each card?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs card and tile. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs card and tile. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs card and tile. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs card and tile. |
| [Web app](profile-web-app.md) | optional | Include when the project needs card and tile. |
| [Website](profile-website.md) | optional | Include when the project needs card and tile. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-036"></a>

## C-036: List and list item

Presents repeated content in a readable sequence.

Kind: component. Shared contract: [data](families.md#data).

### Variants to specify

- Plain
- Structured
- Actionable
- Grouped

### Entry-specific states and behavior

- Loading, empty, partial, selected and reordered data where applicable.

### Project decisions still required

- Does each item navigate, select, expand or only present information?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs list and list item. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs list and list item. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs list and list item. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs list and list item. |
| [Web app](profile-web-app.md) | optional | Include when the project needs list and list item. |
| [Website](profile-website.md) | optional | Include when the project needs list and list item. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [CAR](../INVENTORY-SOURCES.md#CAR), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-037"></a>

## C-037: Description and key-value list

Pairs terms or labels with their values.

Kind: component. Shared contract: [structure](families.md#structure).

### Variants to specify

- Stacked
- Inline
- Summary
- Metadata

### Entry-specific states and behavior

- Missing, long and sensitive values need clear presentation.

### Project decisions still required

- Which relationships should remain understandable without layout styling?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs description and key-value list. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs description and key-value list. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs description and key-value list. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs description and key-value list. |
| [Web app](profile-web-app.md) | optional | Include when the project needs description and key-value list. |
| [Website](profile-website.md) | optional | Include when the project needs description and key-value list. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-038"></a>

## C-038: Data table

Displays information in rows and columns.

Kind: component. Shared contract: [data](families.md#data).

### Variants to specify

- Read-only
- Sortable
- Selectable
- Expandable

### Entry-specific states and behavior

- Headers, row identity, sort state, empty/partial data and overflow
- Preserve cell-header relationships.

### Project decisions still required

- Is this static tabular content or an interactive grid?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs data table. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs data table. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs data table. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs data table. |
| [Web app](profile-web-app.md) | optional | Include when the project needs data table. |
| [Website](profile-website.md) | optional | Include when the project needs data table. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [CAR](../INVENTORY-SOURCES.md#CAR), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE), [USW](../INVENTORY-SOURCES.md#USW). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation. USW component-index terminology was compared; no implementation was copied or tested.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-039"></a>

## C-039: Editable data grid

Supports cell-level navigation and editing in tabular data.

Kind: component. Shared contract: [data](families.md#data).

### Variants to specify

- Cell editing
- Bulk selection
- Virtualized
- Frozen columns

### Entry-specific states and behavior

- Focus versus selection, edit mode, validation and unsaved changes
- Keyboard grid behavior needs a dedicated specification.

### Project decisions still required

- Are spreadsheet-like interactions really required?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs editable data grid. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | optional | Include when the project needs editable data grid. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [CAR](../INVENTORY-SOURCES.md#CAR), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-040"></a>

## C-040: Chart and graph

Encodes data for a specific comparison or relationship.

Kind: component. Shared contract: [data](families.md#data).

### Variants to specify

- Bar
- Line
- Scatter
- Area
- Part-to-whole

### Entry-specific states and behavior

- No data, partial data, uncertainty and selected series
- Supply readable summary and access to underlying values.

### Project decisions still required

- Which visual encoding avoids misleading conclusions?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs chart and graph. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs chart and graph. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs chart and graph. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs chart and graph. |
| [Web app](profile-web-app.md) | optional | Include when the project needs chart and graph. |
| [Website](profile-website.md) | optional | Include when the project needs chart and graph. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [CAR](../INVENTORY-SOURCES.md#CAR), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-041"></a>

## C-041: Metric and statistic

Highlights a quantitative value with its context.

Kind: component. Shared contract: [data](families.md#data).

### Variants to specify

- Single value
- Comparison
- Trend
- Threshold

### Entry-specific states and behavior

- Loading, stale, missing and out-of-range values must be distinguishable.

### Project decisions still required

- What unit, time frame and comparison make the number meaningful?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs metric and statistic. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs metric and statistic. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs metric and statistic. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs metric and statistic. |
| [Web app](profile-web-app.md) | optional | Include when the project needs metric and statistic. |
| [Website](profile-website.md) | optional | Include when the project needs metric and statistic. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [CAR](../INVENTORY-SOURCES.md#CAR), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-042"></a>

## C-042: Tree view

Navigates or selects hierarchical nodes.

Kind: component. Shared contract: [data](families.md#data).

### Variants to specify

- Navigation
- Selection
- Lazy-loaded

### Entry-specific states and behavior

- Expanded, collapsed, loading child nodes, focus and selected node.

### Project decisions still required

- Is hierarchy essential, and how deep can it become?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs tree view. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs tree view. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs tree view. |
| [Web app](profile-web-app.md) | optional | Include when the project needs tree view. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [CAR](../INVENTORY-SOURCES.md#CAR), [APG](../INVENTORY-SOURCES.md#APG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-043"></a>

## C-043: Avatar

Represents a person, account or group.

Kind: component. Shared contract: [structure](families.md#structure).

### Variants to specify

- Photo
- Initials
- Group
- Fallback

### Entry-specific states and behavior

- Missing image, privacy-restricted identity and loading fallback.

### Project decisions still required

- What identity can be shown without revealing unnecessary data?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs avatar. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs avatar. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs avatar. |
| [Web app](profile-web-app.md) | optional | Include when the project needs avatar. |
| [Website](profile-website.md) | optional | Include when the project needs avatar. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-044"></a>

## C-044: Badge, tag and chip

Shows status or a compact label, sometimes with an action.

Kind: component. Shared contract: [feedback](families.md#feedback).

### Variants to specify

- Status badge
- Count
- Category tag
- Filter chip

### Entry-specific states and behavior

- Selected/removable chips need action semantics; static tags do not.
- Interactive chip variants supplement the feedback family: focus, pressed, selected/unselected, unavailable and removed states. Static badges/tags have no focus or selection state; record that exclusion. Specify focus recovery after removal.

### Project decisions still required

- Is this information, a filter, or a command?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs badge, tag and chip. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs badge, tag and chip. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs badge, tag and chip. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs badge, tag and chip. |
| [Web app](profile-web-app.md) | optional | Include when the project needs badge, tag and chip. |
| [Website](profile-website.md) | optional | Include when the project needs badge, tag and chip. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-045"></a>

## C-045: Progress indicator

Shows progress through an operation or sequence.

Kind: component. Shared contract: [feedback](families.md#feedback).

### Variants to specify

- Determinate
- Indeterminate
- Step progress

### Entry-specific states and behavior

- Running, stalled, complete, failed and canceled
- Do not invent precise progress when it is unknown.

### Project decisions still required

- Can progress be measured and can the operation be canceled?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs progress indicator. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs progress indicator. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs progress indicator. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs progress indicator. |
| [Web app](profile-web-app.md) | optional | Include when the project needs progress indicator. |
| [Website](profile-website.md) | optional | Include when the project needs progress indicator. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-046"></a>

## C-046: Loading skeleton and placeholder

Reserves or indicates content while it loads.

Kind: component. Shared contract: [feedback](families.md#feedback).

### Variants to specify

- Skeleton
- Spinner
- Shimmer-free
- Inline

### Entry-specific states and behavior

- Initial loading, slow loading and failure need distinct outcomes
- Respect reduced motion and avoid layout jumps.

### Project decisions still required

- What should appear if loading never completes?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs loading skeleton and placeholder. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs loading skeleton and placeholder. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs loading skeleton and placeholder. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs loading skeleton and placeholder. |
| [Web app](profile-web-app.md) | optional | Include when the project needs loading skeleton and placeholder. |
| [Website](profile-website.md) | optional | Include when the project needs loading skeleton and placeholder. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-047"></a>

## C-047: Inline validation message

Explains an input problem or useful confirmation.

Kind: component. Shared contract: [feedback](families.md#feedback).

### Variants to specify

- Error
- Warning
- Success
- Instruction

### Entry-specific states and behavior

- Show at an appropriate time and keep it associated with the field.

### Project decisions still required

- What correction can the user actually make?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs inline validation message. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs inline validation message. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs inline validation message. |
| [Web app](profile-web-app.md) | optional | Include when the project needs inline validation message. |
| [Website](profile-website.md) | optional | Include when the project needs inline validation message. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-048"></a>

## C-048: Banner and inline alert

Communicates contextual or page-level status.

Kind: component. Shared contract: [feedback](families.md#feedback).

### Variants to specify

- Information
- Warning
- Error
- Success

### Entry-specific states and behavior

- Persistent versus dismissible, repeated and resolved states.

### Project decisions still required

- How urgent is the message and where should it persist?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | required | Starter dependency required by P-021; confirm the dependency when scoping. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | required | Starter dependency required by P-021; confirm the dependency when scoping. |
| [Native tablet app](profile-native-tablet.md) | required | Starter dependency required by P-021; confirm the dependency when scoping. |
| [Shared touch display](profile-touch.md) | required | Starter dependency required by P-021; confirm the dependency when scoping. |
| [Web app](profile-web-app.md) | required | Starter dependency required by P-021; confirm the dependency when scoping. |
| [Website](profile-website.md) | required | Starter dependency required by P-021; confirm the dependency when scoping. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-049"></a>

## C-049: Toast and snackbar

Provides a short nonblocking update.

Kind: component. Shared contract: [feedback](families.md#feedback).

### Variants to specify

- Transient
- Actionable
- Stacked
- Persistent alternative

### Entry-specific states and behavior

- Duration, duplicate messages and action expiry
- Critical information needs a persistent route.

### Project decisions still required

- Will users have enough time and another way to find the result?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs toast and snackbar. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs toast and snackbar. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs toast and snackbar. |
| [Web app](profile-web-app.md) | optional | Include when the project needs toast and snackbar. |
| [Website](profile-website.md) | optional | Include when the project needs toast and snackbar. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-050"></a>

## C-050: Notification item and inbox

Presents updates that users may revisit.

Kind: component. Shared contract: [feedback](families.md#feedback).

### Variants to specify

- Unread
- Read
- Grouped
- Actionable

### Entry-specific states and behavior

- Permission, unread count, stale action and empty inbox
- Do not confuse in-app updates with OS permission.
- Actionable notification variants supplement feedback: focus, pressed, unread/read, unavailable, dismissed and action-error states. A noninteractive message has no control focus state. Specify focus recovery and durable access to the message.

### Project decisions still required

- Which updates matter and how can users control frequency?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs notification item and inbox. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs notification item and inbox. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs notification item and inbox. |
| [Web app](profile-web-app.md) | optional | Include when the project needs notification item and inbox. |
| [Website](profile-website.md) | optional | Include when the project needs notification item and inbox. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-051"></a>

## C-051: Dialog

Presents a focused temporary interaction.

Kind: component. Shared contract: [overlay](families.md#overlay).

### Variants to specify

- Modal
- Nonmodal
- Confirmation
- Alert dialog

### Entry-specific states and behavior

- Open/closed, initial focus, cancel, submit and unsaved state
- Define focus containment only for modal behavior.

### Project decisions still required

- Does the task justify interrupting the current context?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs dialog. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs dialog. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs dialog. |
| [Web app](profile-web-app.md) | optional | Include when the project needs dialog. |
| [Website](profile-website.md) | optional | Include when the project needs dialog. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [MAT](../INVENTORY-SOURCES.md#MAT), [APPLE](../INVENTORY-SOURCES.md#APPLE), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-052"></a>

## C-052: Sheet and side panel

Presents secondary content in a temporary or persistent panel.

Kind: component. Shared contract: [overlay](families.md#overlay).

### Variants to specify

- Bottom sheet
- Side sheet
- Detents
- Persistent panel

### Entry-specific states and behavior

- Open, resized, dismissed and keyboard-obscured states
- A sheet is not always modal.

### Project decisions still required

- Which platform presentation and dismissal behaviors apply?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs sheet and side panel. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs sheet and side panel. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs sheet and side panel. |
| [Web app](profile-web-app.md) | optional | Include when the project needs sheet and side panel. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [MAT](../INVENTORY-SOURCES.md#MAT), [APPLE](../INVENTORY-SOURCES.md#APPLE), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-053"></a>

## C-053: Popover

Presents contextual content anchored to a trigger.

Kind: component. Shared contract: [overlay](families.md#overlay).

### Variants to specify

- Informational
- Action list
- Form

### Entry-specific states and behavior

- Open/closed, anchor repositioning and outside interaction.

### Project decisions still required

- Is the content interactive, and where should focus move?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs popover. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs popover. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs popover. |
| [Web app](profile-web-app.md) | optional | Include when the project needs popover. |
| [Website](profile-website.md) | optional | Include when the project needs popover. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [MAT](../INVENTORY-SOURCES.md#MAT), [APPLE](../INVENTORY-SOURCES.md#APPLE), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-054"></a>

## C-054: Tooltip and contextual help

Provides brief supporting explanation.

Kind: component. Shared contract: [overlay](families.md#overlay).

### Variants to specify

- Tooltip
- Help text
- Toggletip

### Entry-specific states and behavior

- Hover and focus behavior differ from tap-to-open help
- Essential information must not exist only in a tooltip.
- A tooltip contains no interactive controls; richer help uses an explicitly activated popover or other suitable container.

### Project decisions still required

- Should this explanation be permanently visible instead?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs tooltip and contextual help. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs tooltip and contextual help. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs tooltip and contextual help. |
| [Web app](profile-web-app.md) | optional | Include when the project needs tooltip and contextual help. |
| [Website](profile-website.md) | optional | Include when the project needs tooltip and contextual help. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [APG](../INVENTORY-SOURCES.md#APG), [MAT](../INVENTORY-SOURCES.md#MAT), [APPLE](../INVENTORY-SOURCES.md#APPLE), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-055"></a>

## C-055: Image and responsive picture

Displays imagery with appropriate sizing and alternatives.

Kind: component. Shared contract: [media](families.md#media).

### Variants to specify

- Responsive
- Art-directed
- Decorative
- Informative

### Entry-specific states and behavior

- Loading, broken image, crop changes and text alternatives.

### Project decisions still required

- What information would be lost without this image?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs image and responsive picture. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs image and responsive picture. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs image and responsive picture. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs image and responsive picture. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs image and responsive picture. |
| [Web app](profile-web-app.md) | optional | Include when the project needs image and responsive picture. |
| [Website](profile-website.md) | optional | Include when the project needs image and responsive picture. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [WCAG](../INVENTORY-SOURCES.md#WCAG), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-056"></a>

## C-056: Audio and video player

Presents time-based media with usable controls.

Kind: component. Shared contract: [media](families.md#media).

### Variants to specify

- Audio
- Video
- Live
- Prerecorded

### Entry-specific states and behavior

- Play, pause, seek, buffering, failure, captions and reduced-motion alternative.

### Project decisions still required

- Which captions, descriptions, controls and rights are required?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs audio and video player. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs audio and video player. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs audio and video player. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs audio and video player. |
| [Web app](profile-web-app.md) | optional | Include when the project needs audio and video player. |
| [Website](profile-website.md) | optional | Include when the project needs audio and video player. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [WCAG](../INVENTORY-SOURCES.md#WCAG), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-057"></a>

## C-057: Carousel and gallery

Presents a collection of visual items.

Kind: component. Shared contract: [media](families.md#media).

### Variants to specify

- Manual
- Paginated
- Swipe
- Lightbox gallery

### Entry-specific states and behavior

- Active slide, paused rotation and boundaries
- Provide controls beyond swipe and avoid hidden essential content.

### Project decisions still required

- Does sequential presentation help more than a visible list?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs carousel and gallery. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs carousel and gallery. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs carousel and gallery. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs carousel and gallery. |
| [Web app](profile-web-app.md) | optional | Include when the project needs carousel and gallery. |
| [Website](profile-website.md) | optional | Include when the project needs carousel and gallery. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [WCAG](../INVENTORY-SOURCES.md#WCAG), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-058"></a>

## C-058: Divider and separator

Separates content or functional regions.

Kind: primitive. Shared contract: [structure](families.md#structure).

### Variants to specify

- Horizontal
- Vertical
- Decorative
- Semantic

### Entry-specific states and behavior

- Do not add announcement noise for purely decorative lines.

### Project decisions still required

- Does the separation convey a meaningful boundary?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs divider and separator. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs divider and separator. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs divider and separator. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs divider and separator. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs divider and separator. |
| [Web app](profile-web-app.md) | optional | Include when the project needs divider and separator. |
| [Website](profile-website.md) | optional | Include when the project needs divider and separator. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-059"></a>

## C-059: Container, stack and grid

Arranges content using reusable layout structures.

Kind: primitive. Shared contract: [structure](families.md#structure).

### Variants to specify

- Stack
- Inline
- Grid
- Split pane

### Entry-specific states and behavior

- Wrap, overflow, narrow windows and reordered layouts.
- The layout container itself is noninteractive; default plus breakpoint, orientation and text-reflow layout conditions apply. Interactive descendants retain their own control states. Do not invent container focus, pressed or selected states.

### Project decisions still required

- How should reading order and priority survive rearrangement?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | optional | Include when the project needs container, stack and grid. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native tablet app](profile-native-tablet.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Website](profile-website.md) | required | Shared starter requirement for this profile; confirm in project scope. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [CAR](../INVENTORY-SOURCES.md#CAR), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="c-060"></a>

## C-060: Resizable splitter

Lets users adjust adjoining panes.

Kind: component. Shared contract: [action](families.md#action).

### Variants to specify

- Horizontal
- Vertical
- Collapsible

### Entry-specific states and behavior

- Dragging, keyboard resizing, min/max and collapsed states.
- Splitter variants supplement action: focused, resizing, minimum, maximum, collapsed and expanded where collapsible. Specify keyboard resizing, accessible current/minimum/maximum values and focus recovery; noncollapsible variants exclude collapsed/expanded.

### Project decisions still required

- Can users resize without a pointer and recover the default layout?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Passive display](profile-display.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Marketing and sales](profile-marketing-sales.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native phone app](profile-native-phone.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs resizable splitter. |
| [Shared touch display](profile-touch.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |
| [Web app](profile-web-app.md) | optional | Include when the project needs resizable splitter. |
| [Website](profile-website.md) | not-applicable | Outside this starter profile; add through an explicit scope change if needed. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [APG](../INVENTORY-SOURCES.md#APG), [MAT](../INVENTORY-SOURCES.md#MAT), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

