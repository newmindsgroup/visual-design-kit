# Shared specification family contracts

Version-Timestamp: 2026-09-07 14:29:54 AST

Generated from master.json. Listed concepts and shared specification starters only. No completed component specifications, implementation or testing is supplied. Profile selections are starting recommendations, not approved project scope.

These contracts identify questions and acceptance topics. Apply them with the entry notes and record exclusions. They are not complete specifications for every family member.

<a id="access"></a>

## Accessibility and inclusive use

Common specification questions for accessibility and inclusive use, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Choose applicable criteria and test method
- Record failures, remediation and untested scope
- Include relevant users and assistive technology when authorized

### Accessibility

- Requirements are not conformance results
- Separate web, native software and physical access evidence

### Content and data

- Target platforms and access needs
- Criteria, levels and exceptions
- Test evidence and owner

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [G-007: Accessibility requirements](governance.md#g-007), [G-008: Keyboard, focus and assistive input](governance.md#g-008), [G-009: Text scaling, reflow and reading order](governance.md#g-009), [G-010: Motion, media and sensory alternatives](governance.md#g-010), [G-012: Physical installation and device acceptance](governance.md#g-012)

<a id="account"></a>

## Account and permissions flows

Common specification questions for account and permissions flows, not a completed component specification.

Interaction class: flow. State slots: default, loading, error, offline, permission-denied, success.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Separate identity verification from authorization
- Protect sessions and show recoverable failures
- Do not invent account requirements

### Accessibility

- Avoid inaccessible authentication barriers
- Explain permission consequences and alternatives

### Content and data

- Identity methods and access rules
- Expiry, recovery and retention
- System permission vocabulary

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [P-009: Onboarding and first use](patterns.md#p-009), [P-010: Sign-in and authentication](patterns.md#p-010), [P-011: Registration and verification](patterns.md#p-011), [P-012: Account recovery](patterns.md#p-012), [P-013: Account settings and profile](patterns.md#p-013), [P-014: Permission request and access denial](patterns.md#p-014), [P-015: Session expiry and sign-out](patterns.md#p-015), [P-016: Consent and privacy choices](patterns.md#p-016)

<a id="action"></a>

## Actions and links

Common specification questions for actions and links, not a completed component specification.

Interaction class: action. State slots: default, focus, pressed, unavailable.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Separate navigation from commands
- Prevent duplicate submission and show progress when asynchronous

### Accessibility

- Name the action clearly
- Keyboard and assistive input must trigger the same outcome
- Preserve visible focus; do not make hover essential

### Content and data

- Action label and destination
- Busy and unavailable explanation

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [C-001: Button](ui.md#c-001), [C-002: Link](ui.md#c-002), [C-003: Button group and split button](ui.md#c-003), [C-004: Floating action button](ui.md#c-004), [C-032: Toolbar and command menu](ui.md#c-032), [C-060: Resizable splitter](ui.md#c-060)

<a id="app-screen"></a>

## Application screen templates

Common specification questions for application screen templates, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Assemble tasks with navigation and system states
- Support smaller and expanded windows without losing context

### Accessibility

- Check focus, reading order, input methods and text scaling
- Test the real target platform

### Content and data

- Route, task and data model
- Permission boundary
- Empty, error and offline specimens

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [T-010: Application shell](templates.md#t-010), [T-011: Dashboard and overview screen](templates.md#t-011), [T-012: Collection and management screen](templates.md#t-012), [T-013: Record detail and workspace](templates.md#t-013), [T-014: Create and edit screen](templates.md#t-014), [T-015: Authentication and recovery screen](templates.md#t-015), [T-016: Account and settings screen](templates.md#t-016), [T-017: Onboarding and setup screen](templates.md#t-017), [T-018: Mobile detail and drill-down screen](templates.md#t-018), [T-019: Tablet list-detail workspace](templates.md#t-019), [T-020: Notification center screen](templates.md#t-020), [T-023: Optional commerce screen set](templates.md#t-023)

<a id="brand-asset"></a>

## Brand master deliverables

Common specification questions for brand master deliverables, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Maintain editable masters and approved variants
- Separate brand asset rights from template reuse

### Accessibility

- Check intended sizes, backgrounds and accessible alternatives
- Preserve readable identity at each medium

### Content and data

- Owner, source and usage rights
- Master and export versions
- Production dimensions

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [A-001: Logo master and lockups](assets.md#a-001), [A-002: Logo usage and clear-space guide](assets.md#a-002), [A-003: Brand guideline document](assets.md#a-003), [A-004: Icon and illustration asset set](assets.md#a-004), [A-005: Image library and usage notes](assets.md#a-005), [A-006: App icon and launch artwork](assets.md#a-006), [A-007: Favicon and site identity assets](assets.md#a-007)

<a id="campaign"></a>

## Campaign and marketing deliverables

Common specification questions for campaign and marketing deliverables, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Adapt a shared message to each channel
- Specify dimensions, safe zones and destination
- Keep variants linked to their approved baseline

### Accessibility

- Readable content, captions and alternatives
- Respect user choice and platform access constraints

### Content and data

- Audience, offer, copy and claims evidence
- Licensed assets
- Channel specifications and expiry

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [A-008: Campaign creative brief](assets.md#a-008), [A-009: Campaign visual template set](assets.md#a-009), [A-010: Social profile and cover artwork](assets.md#a-010), [A-011: Social post and carousel templates](assets.md#a-011), [A-012: Email campaign and newsletter template](assets.md#a-012), [A-013: Transactional email template](assets.md#a-013), [A-014: Digital advertising template](assets.md#a-014), [A-015: Campaign landing content kit](assets.md#a-015), [A-016: Video and motion branding kit](assets.md#a-016), [A-017: Event and webinar kit](assets.md#a-017), [A-018: Press and media kit](assets.md#a-018), [A-033: Digital signage content kit](assets.md#a-033)

<a id="content-flow"></a>

## Content and communication patterns

Common specification questions for content and communication patterns, not a completed component specification.

Interaction class: flow. State slots: default, loading, error, offline, permission-denied, success.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Make content hierarchy and intent clear
- Separate editorial claims from evidence and permissions

### Accessibility

- Plain language, correct reading order and alternatives
- Avoid manipulative or misleading choices

### Content and data

- Audience and message
- Supporting evidence and approvals
- Distribution and retention context

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [P-026: Help and support](patterns.md#p-026), [P-027: Editorial storytelling and evidence](patterns.md#p-027), [P-035: Share, print and deep link](patterns.md#p-035)

<a id="data"></a>

## Data display and visualization

Common specification questions for data display and visualization, not a completed component specification.

Interaction class: data. State slots: default, loading, empty, partial, error.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Specify empty, partial and stale data
- Distinguish a static table from an editable interactive grid

### Accessibility

- Provide semantic relationships and text alternatives
- Offer non-color encodings and accessible data access

### Content and data

- Dataset schema, units and labels
- Sorting, precision, missing values and freshness

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [C-036: List and list item](ui.md#c-036), [C-038: Data table](ui.md#c-038), [C-039: Editable data grid](ui.md#c-039), [C-040: Chart and graph](ui.md#c-040), [C-041: Metric and statistic](ui.md#c-041), [C-042: Tree view](ui.md#c-042)

<a id="disclosure"></a>

## Disclosure and organized panels

Common specification questions for disclosure and organized panels, not a completed component specification.

Interaction class: disclosure. State slots: default, focus, expanded, collapsed.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Keep expanded state explicit
- Define one or many open panels and lazy content behavior

### Accessibility

- Associate trigger and panel
- Keyboard operation must fit the specific pattern
- Do not hide essential task instructions

### Content and data

- Panel labels and headings
- State persistence
- Deep-link behavior

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [C-033: Tabs](ui.md#c-033), [C-034: Accordion and disclosure](ui.md#c-034)

<a id="discovery"></a>

## Finding and organizing information

Common specification questions for finding and organizing information, not a completed component specification.

Interaction class: flow. State slots: default, loading, error, offline, permission-denied, success.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Preserve query, filters, ordering and position
- Explain no results and partial availability

### Accessibility

- Expose search and filter state
- Keyboard and assistive users need equivalent paths

### Content and data

- Index or data source
- Facets, sorting keys and localization
- Query limits and performance

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [P-005: Search results and no results](patterns.md#p-005), [P-006: Filter, facet and sort](patterns.md#p-006), [P-007: Load more and virtual scrolling](patterns.md#p-007), [P-008: Bulk selection and actions](patterns.md#p-008), [P-029: Map and location workflow](patterns.md#p-029)

<a id="display-layout"></a>

## Display layout templates

Common specification questions for display layout templates, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Assemble readable content for the actual screen or installation
- Define fallback and content refresh behavior

### Accessibility

- Check real viewing distance, light and access
- No untested hardware claims

### Content and data

- Screen geometry and orientation
- Source media and schedule
- Site and operation constraints

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [T-021: Display message layout](templates.md#t-021), [T-022: Touch welcome and task screen](templates.md#t-022)

<a id="feedback"></a>

## Feedback and status

Common specification questions for feedback and status, not a completed component specification.

Interaction class: data. State slots: default, loading, empty, partial, error.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Match urgency to interruption
- Keep important information available long enough to act

### Accessibility

- Announce changes appropriately without excessive interruption
- Pair color with text or symbols

### Content and data

- Message, cause and recovery action
- Severity, duration and duplicate suppression

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [C-044: Badge, tag and chip](ui.md#c-044), [C-045: Progress indicator](ui.md#c-045), [C-046: Loading skeleton and placeholder](ui.md#c-046), [C-047: Inline validation message](ui.md#c-047), [C-048: Banner and inline alert](ui.md#c-048), [C-049: Toast and snackbar](ui.md#c-049), [C-050: Notification item and inbox](ui.md#c-050)

<a id="form-flow"></a>

## Form and editing flows

Common specification questions for form and editing flows, not a completed component specification.

Interaction class: flow. State slots: default, loading, error, offline, permission-denied, success.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Keep progress and entered data when safe
- Validate at appropriate times and recover from server errors
- Prevent duplicate completion

### Accessibility

- Error summary and field errors must work together
- Support keyboard, assistive input and plain-language instructions

### Content and data

- Field schema
- Business constraints and validation messages
- Retention and submission outcome

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [P-001: Form validation and recovery](patterns.md#p-001), [P-002: Multi-step form and task list](patterns.md#p-002), [P-003: Review, confirm and receipt](patterns.md#p-003), [P-004: Inline editing and autosave](patterns.md#p-004), [P-028: Scheduling and calendar workflow](patterns.md#p-028)

<a id="governance"></a>

## System ownership and maintenance

Common specification questions for system ownership and maintenance, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Assign owners and a change process
- Preserve versions, baseline approvals and migration notes

### Accessibility

- Track accessibility requirements as maintenance work
- Do not infer acceptance from a completed checklist

### Content and data

- Decision IDs, owner and evidence
- Contribution and deprecation records
- Dependencies and rights

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [G-001: System scope and ownership](governance.md#g-001), [G-002: Component and asset specification](governance.md#g-002), [G-003: Token source and versioning](governance.md#g-003), [G-004: Contribution and review process](governance.md#g-004), [G-005: Release, deprecation and migration](governance.md#g-005), [G-006: Documentation and examples](governance.md#g-006), [G-019: Measurement and feedback plan](governance.md#g-019), [G-020: Extensions and exceptions register](governance.md#g-020)

<a id="identity"></a>

## Identity and visual direction

Shared identity, visual language and adaptation rules, including responsive composition and data encoding.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Express one recognizable identity across appropriate variants
- Preserve exact supplied marks until separately approved

### Accessibility

- Legibility and contrast need actual-size evidence
- Do not rely on color alone for meaning

### Content and data

- Approved mark and asset sources
- Intended media, audiences and languages

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [F-011: Brand principles](foundations.md#f-011), [F-012: Logo architecture](foundations.md#f-012), [F-013: Color usage rules](foundations.md#f-013), [F-014: Typography usage rules](foundations.md#f-014), [F-015: Iconography style](foundations.md#f-015), [F-016: Imagery and art direction](foundations.md#f-016), [F-017: Motion and sound principles](foundations.md#f-017), [F-021: Responsive and adaptive rules](foundations.md#f-021), [F-022: Data visualization language](foundations.md#f-022)

<a id="input"></a>

## Text and structured inputs

Common specification questions for text and structured inputs, not a completed component specification.

Interaction class: input. State slots: default, focus, filled, invalid, read-only, unavailable.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Keep label, help and errors associated
- Preserve user entry on recoverable errors
- Define parsing, format, limits and validation timing

### Accessibility

- Do not use a placeholder as the only label
- Support keyboard, autofill and input-method editors
- Explain errors without relying on color

### Content and data

- Label, help, constraints
- Valid and invalid sample data
- Privacy and retention

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [C-005: Text field](ui.md#c-005), [C-006: Text area](ui.md#c-006), [C-007: Number input and stepper](ui.md#c-007), [C-008: Search field](ui.md#c-008), [C-015: Combobox and autocomplete](ui.md#c-015), [C-019: Date and date-range picker](ui.md#c-019), [C-020: Time picker](ui.md#c-020), [C-021: File upload control](ui.md#c-021), [C-022: Rich-text editor](ui.md#c-022)

<a id="language"></a>

## Voice and localization

Common specification questions for voice and localization, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Use consistent vocabulary and intent
- Adapt language, formats and text direction without losing meaning

### Accessibility

- Plain language and useful labels
- Confirm reading order and alternative text in each locale

### Content and data

- Glossary
- Locale, language and writing system
- Translator and content owner

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [F-018: Voice and tone](foundations.md#f-018), [F-019: Terminology and naming](foundations.md#f-019), [F-020: Localization and RTL](foundations.md#f-020)

<a id="media"></a>

## Media presentation and controls

Common specification questions for media presentation and controls, not a completed component specification.

Interaction class: media. State slots: default, loading, error, paused, reduced-motion.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Define play/pause, loading and failure
- Avoid unexpected audio and unnecessary motion
- Provide a static or reduced-motion alternative

### Accessibility

- Captions, descriptions and useful alternatives where relevant
- Media controls need names, focus and keyboard access

### Content and data

- Licensed source, poster, crop and aspect ratio
- Captions and transcript
- Duration and delivery budget

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [C-055: Image and responsive picture](ui.md#c-055), [C-056: Audio and video player](ui.md#c-056), [C-057: Carousel and gallery](ui.md#c-057)

<a id="navigation"></a>

## Navigation and location

Common specification questions for navigation and location, not a completed component specification.

Interaction class: action. State slots: default, focus, pressed, unavailable.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Preserve location and navigation state
- Distinguish top-level destination from in-page tabs and actions

### Accessibility

- Expose current location
- Avoid hiding essential navigation behind hover
- Preserve predictable focus on route change

### Content and data

- Destination tree
- Current and previous location
- Long labels and overflow

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.
- Use native back/navigation conventions; an iPad tab bar is not a mandatory bottom bar.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [C-023: Header and application bar](ui.md#c-023), [C-025: Primary navigation](ui.md#c-025), [C-026: Sidebar, drawer and navigation rail](ui.md#c-026), [C-027: Native tab bar](ui.md#c-027), [C-028: Breadcrumb](ui.md#c-028), [C-029: Back and close control](ui.md#c-029), [C-030: Skip link and landmark navigation](ui.md#c-030), [C-031: Pagination](ui.md#c-031)

<a id="operations"></a>

## Production, security and delivery

Common specification questions for production, security and delivery, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Define operational and permission boundaries
- Reuse existing manifest and handoff contracts
- Record recoverability and maintenance responsibilities

### Accessibility

- Maintain access through failure/recovery
- Protect shared-session privacy and user control

### Content and data

- Artifact, runtime and release evidence
- Privacy and security constraints
- Rollback and ownership

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [G-011: Native system integration requirements](governance.md#g-011), [G-013: Privacy, consent and shared-session rules](governance.md#g-013), [G-014: Security and permission boundaries](governance.md#g-014), [G-015: Performance and resilience budget](governance.md#g-015), [G-016: Content and asset rights register](governance.md#g-016), [G-017: Quality evidence and acceptance record](governance.md#g-017), [G-018: Production manifest and handoff](governance.md#g-018)

<a id="overlay"></a>

## Dialogs and temporary surfaces

Common specification questions for dialogs and temporary surfaces, not a completed component specification.

Interaction class: overlay. State slots: default, focus, open, closed.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Define modal versus nonmodal behavior
- Return focus when dismissed and protect unsaved work

### Accessibility

- Name the surface
- Modal focus must stay within it while open; provide a reachable dismissal
- Do not treat a tooltip as a form

### Content and data

- Title and content
- Trigger and return-focus target
- Dismissal and cancel behavior

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [C-051: Dialog](ui.md#c-051), [C-052: Sheet and side panel](ui.md#c-052), [C-053: Popover](ui.md#c-053), [C-054: Tooltip and contextual help](ui.md#c-054)

<a id="physical-flow"></a>

## Physical display and shared sessions

Common specification questions for physical display and shared sessions, not a completed component specification.

Interaction class: physical. State slots: default, idle, offline, error, reset.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Define attract, active, idle-warning and reset modes
- Clear personal data between users
- Recover from lost connectivity and interrupted power

### Accessibility

- Test approach, reach, seated/standing viewing and alternative access
- Never require hover; provide accessible session extension where applicable

### Content and data

- Site constraints and device capabilities
- Dwell time and content schedule
- Privacy, reset and operations owner

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [P-031: Display scheduling and attract loop](patterns.md#p-031), [P-032: Shared touch session and idle reset](patterns.md#p-032), [P-033: Physical access and assisted alternative](patterns.md#p-033), [P-034: Kiosk recovery and operator escape](patterns.md#p-034)

<a id="print"></a>

## Print and environmental deliverables

Common specification questions for print and environmental deliverables, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Specify physical dimensions, substrate and production constraints
- Proof at actual scale before release

### Accessibility

- Check reading distance, contrast, tactile needs and placement as applicable
- Do not apply web pixels as physical measurements

### Content and data

- Print process, color profile and finishing
- Installation context
- Supplier and proof evidence

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [A-027: Business stationery](assets.md#a-027), [A-028: Brochure, flyer and poster](assets.md#a-028), [A-029: Packaging and label artwork](assets.md#a-029), [A-030: Environmental signage and wayfinding](assets.md#a-030), [A-031: Event booth and exhibition graphics](assets.md#a-031), [A-032: Merchandise and apparel artwork](assets.md#a-032)

<a id="sales"></a>

## Sales enablement deliverables

Common specification questions for sales enablement deliverables, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Build a clear argument for a specific audience
- Keep pricing, claims and approvals versioned
- Separate reusable layout from deal-specific facts

### Accessibility

- Readable slides/documents with meaningful order
- Accessible exports and text alternatives

### Content and data

- Problem, evidence and offer
- Pricing or scope owner
- Confidentiality and intended recipient

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [A-019: Sales presentation deck](assets.md#a-019), [A-020: Proposal and statement-of-work layout](assets.md#a-020), [A-021: Sales one-pager](assets.md#a-021), [A-022: Case study template](assets.md#a-022), [A-023: Product and service datasheet](assets.md#a-023), [A-024: Sales playbook and battlecard](assets.md#a-024), [A-025: Quote and pricing sheet](assets.md#a-025), [A-026: Demo and handoff script](assets.md#a-026)

<a id="selection"></a>

## Choice controls

Common specification questions for choice controls, not a completed component specification.

Interaction class: selection. State slots: default, focus, selected, unavailable.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Distinguish immediate change from submitted selection
- Specify single or multiple selection and defaults

### Accessibility

- Group related options with a clear label
- Announce selection and allow keyboard/assistive operation

### Content and data

- Option IDs and labels
- Disabled-option reasons
- Minimum and maximum selection

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [C-011: Checkbox](ui.md#c-011), [C-012: Radio group](ui.md#c-012), [C-013: Switch](ui.md#c-013), [C-014: Select and picker](ui.md#c-014), [C-016: Multiselect](ui.md#c-016), [C-017: Segmented control](ui.md#c-017), [C-018: Slider and range slider](ui.md#c-018)

<a id="structure"></a>

## Layout and content primitives

Common specification questions for layout and content primitives, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Preserve reading order when rearranging visual layout
- Separate decorative structure from interactive behavior

### Accessibility

- Use real heading/list/landmark semantics where relevant
- Reflow and long content need checks

### Content and data

- Text hierarchy
- Content grouping and overflow rules

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [C-009: Field label, help and counter](ui.md#c-009), [C-010: Fieldset and form group](ui.md#c-010), [C-024: Footer](ui.md#c-024), [C-035: Card and tile](ui.md#c-035), [C-037: Description and key-value list](ui.md#c-037), [C-043: Avatar](ui.md#c-043), [C-058: Divider and separator](ui.md#c-058), [C-059: Container, stack and grid](ui.md#c-059)

<a id="system-flow"></a>

## System states and task continuity

Common specification questions for system states and task continuity, not a completed component specification.

Interaction class: flow. State slots: default, loading, error, offline, permission-denied, success.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Distinguish loading, empty, partial, stale, offline and denied access
- Provide explicit recovery and cancellation
- Keep destructive actions proportionate

### Accessibility

- Communicate status and recovery without trapping focus
- Preserve useful access when network or permissions fail

### Content and data

- State source and retry policy
- Last-updated time
- Recovery owner and help path

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [P-021: Loading, empty and partial content](patterns.md#p-021), [P-022: Error, offline and retry](patterns.md#p-022), [P-023: Destructive action and undo](patterns.md#p-023), [P-024: Notifications and preferences](patterns.md#p-024), [P-025: File management and export](patterns.md#p-025), [P-030: Collaboration and activity history](patterns.md#p-030)

<a id="tokens"></a>

## Semantic tokens

Common specification questions for semantic tokens, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Separate global, semantic and component roles
- Preserve approved baseline values; no arbitrary substitutions

### Accessibility

- Check all intended themes and text scales; a token name is not a contrast test

### Content and data

- Role names
- Source authority and change owner
- Mapping across outputs

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.
- Which values are shared, and which vary by platform, density, theme or print process?

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003), [F-004: Grid and container tokens](foundations.md#f-004), [F-005: Shape tokens](foundations.md#f-005), [F-006: Layer and elevation tokens](foundations.md#f-006), [F-007: Motion tokens](foundations.md#f-007), [F-008: Icon and control-size tokens](foundations.md#f-008), [F-009: Focus indication tokens](foundations.md#f-009), [F-010: Density tokens](foundations.md#f-010)

<a id="transaction"></a>

## Optional commerce and payment

Common specification questions for optional commerce and payment, not a completed component specification.

Interaction class: flow. State slots: default, loading, error, offline, permission-denied, success.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Show totals and commitments before confirmation
- Prevent duplicate transactions and support failure recovery

### Accessibility

- Make corrections and cancellation understandable
- Do not rely on visual-only price or status cues

### Content and data

- Currency, taxes and fees
- Inventory and fulfillment
- Provider, legal and security requirements

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.
- Is commerce present at all? This is conditional, not a required module for every system.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [P-017: Product discovery and comparison](patterns.md#p-017), [P-018: Cart and checkout](patterns.md#p-018), [P-019: Payment and refund](patterns.md#p-019), [P-020: Subscription and billing](patterns.md#p-020)

<a id="web-page"></a>

## Website page templates

Common specification questions for website page templates, not a completed component specification.

Interaction class: none. State slots: default.

A slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.

### Behavior

- Assemble patterns and components for a page purpose
- Preserve responsive hierarchy and navigation

### Accessibility

- Check document structure, reflow and keyboard route
- Include meaningful title, headings and landmarks

### Content and data

- Page goal and content model
- SEO and metadata
- Long content and localization

### Decisions

- Choose actual anatomy, limits, variants and acceptance criteria for the project.
- State which inherited states apply and give reasons for exclusions.

### Platform adaptations

- android: Use Android system interaction, Back behavior, TalkBack and text scaling; adapt navigation to window size. Confirm platform/version guidance.
- display: No touch assumed. Test legibility at distance, dwell time, captions, loops, offline fallback and panel conditions.
- ios: Use iOS/iPadOS semantics, navigation and system controls; consider Dynamic Type, VoiceOver, safe areas and system keyboard. Do not translate ARIA roles into native APIs.
- print: No hover or interactive state. Specify trim, bleed, substrate, color process, viewing distance and proofing where applicable.
- touch: No hover-only action. Include seated/standing reach, assistive input/focus, on-screen keyboard, timeout warning, reset and privacy between users.
- web: Use semantic HTML and appropriate keyboard/focus behavior; ARIA only when needed. Responsive layout and browser history require verification.

Members: [T-001: Content page](templates.md#t-001), [T-002: Home and landing page](templates.md#t-002), [T-003: Listing and search page](templates.md#t-003), [T-004: Detail page](templates.md#t-004), [T-005: Contact and lead form page](templates.md#t-005), [T-006: Pricing and comparison page](templates.md#t-006), [T-007: Help and support page](templates.md#t-007), [T-008: Confirmation and receipt page](templates.md#t-008), [T-009: Not-found and service-error page](templates.md#t-009)

