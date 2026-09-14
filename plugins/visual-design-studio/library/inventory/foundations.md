# Brand foundations and tokens

Version-Timestamp: 2026-09-07 14:29:54 AST

Generated from master.json. Listed concepts and shared specification starters only. No completed component specifications, implementation or testing is supplied. Profile selections are starting recommendations, not approved project scope.

[Index](index.md) | [Specification template](../templates/system-item.md)

<a id="f-001"></a>

## F-001: Semantic color

Named roles for text, surfaces, borders, actions and status.

Kind: token. Shared contract: [tokens](families.md#tokens).

### Variants to specify

- Light
- Dark
- High contrast
- Print

### Entry-specific states and behavior

- State palettes must preserve meaning and measured contrast.

### Project decisions still required

- Which palettes, themes and status roles are actually needed?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Passive display](profile-display.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Marketing and sales](profile-marketing-sales.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native phone app](profile-native-phone.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native tablet app](profile-native-tablet.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Website](profile-website.md) | required | Shared starter requirement for this profile; confirm in project scope. |

Token roles: None required by this entry.

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-002"></a>

## F-002: Typography tokens

Named roles for font size, weight, line height and tracking.

Kind: token. Shared contract: [tokens](families.md#tokens).

### Variants to specify

- Body
- Heading
- Label
- Display
- Code

### Entry-specific states and behavior

- Check text scaling, missing glyphs and long translated strings.

### Project decisions still required

- Which scales and script coverage can the approved fonts support?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Passive display](profile-display.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Marketing and sales](profile-marketing-sales.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native phone app](profile-native-phone.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native tablet app](profile-native-tablet.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Website](profile-website.md) | required | Shared starter requirement for this profile; confirm in project scope. |

Token roles: None required by this entry.

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-003"></a>

## F-003: Spacing tokens

A named scale for gaps, padding and margins.

Kind: token. Shared contract: [tokens](families.md#tokens).

### Variants to specify

- Compact
- Comfortable
- Large-format

### Entry-specific states and behavior

- Adapt spacing without changing reading order.

### Project decisions still required

- Which units and density variants fit each medium?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Passive display](profile-display.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Marketing and sales](profile-marketing-sales.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native phone app](profile-native-phone.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native tablet app](profile-native-tablet.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Website](profile-website.md) | required | Shared starter requirement for this profile; confirm in project scope. |

Token roles: None required by this entry.

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-004"></a>

## F-004: Grid and container tokens

Named columns, gutters, margins and container widths.

Kind: token. Shared contract: [tokens](families.md#tokens).

### Variants to specify

- Fluid
- Fixed
- Multi-column
- Print grid

### Entry-specific states and behavior

- Specify narrow, wide and overflow behavior.

### Project decisions still required

- Which layout constraints depend on the target surface?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs grid and container tokens. |
| [Passive display](profile-display.md) | optional | Include when the project needs grid and container tokens. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs grid and container tokens. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs grid and container tokens. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs grid and container tokens. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs grid and container tokens. |
| [Web app](profile-web-app.md) | optional | Include when the project needs grid and container tokens. |
| [Website](profile-website.md) | optional | Include when the project needs grid and container tokens. |

Token roles: None required by this entry.

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-005"></a>

## F-005: Shape tokens

Named corner, border-width and outline roles.

Kind: token. Shared contract: [tokens](families.md#tokens).

### Variants to specify

- Square
- Rounded
- Pill
- Stroke

### Entry-specific states and behavior

- Selected and focus outlines must remain distinguishable.

### Project decisions still required

- Which shapes belong to brand identity versus platform controls?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs shape tokens. |
| [Passive display](profile-display.md) | optional | Include when the project needs shape tokens. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs shape tokens. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs shape tokens. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs shape tokens. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs shape tokens. |
| [Web app](profile-web-app.md) | optional | Include when the project needs shape tokens. |
| [Website](profile-website.md) | optional | Include when the project needs shape tokens. |

Token roles: None required by this entry.

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-006"></a>

## F-006: Layer and elevation tokens

Named stacking and depth roles for surfaces.

Kind: token. Shared contract: [tokens](families.md#tokens).

### Variants to specify

- Flat
- Raised
- Overlay
- Scrim

### Entry-specific states and behavior

- Overlay order must not hide focus or essential content.

### Project decisions still required

- What surface separation is needed without relying on shadows?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs layer and elevation tokens. |
| [Passive display](profile-display.md) | optional | Include when the project needs layer and elevation tokens. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs layer and elevation tokens. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs layer and elevation tokens. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs layer and elevation tokens. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs layer and elevation tokens. |
| [Web app](profile-web-app.md) | optional | Include when the project needs layer and elevation tokens. |
| [Website](profile-website.md) | optional | Include when the project needs layer and elevation tokens. |

Token roles: None required by this entry.

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-007"></a>

## F-007: Motion tokens

Named durations, delays, easing and transition roles.

Kind: token. Shared contract: [tokens](families.md#tokens).

### Variants to specify

- Immediate
- Standard
- Emphasis
- Reduced

### Entry-specific states and behavior

- Reduced motion is a separate behavior decision, not merely slower animation.

### Project decisions still required

- Which motion conveys state or orientation?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs motion tokens. |
| [Passive display](profile-display.md) | optional | Include when the project needs motion tokens. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs motion tokens. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs motion tokens. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs motion tokens. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs motion tokens. |
| [Web app](profile-web-app.md) | optional | Include when the project needs motion tokens. |
| [Website](profile-website.md) | optional | Include when the project needs motion tokens. |

Token roles: None required by this entry.

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-008"></a>

## F-008: Icon and control-size tokens

Named icon sizes, control dimensions and interaction areas.

Kind: token. Shared contract: [tokens](families.md#tokens).

### Variants to specify

- Small
- Standard
- Large
- Physical

### Entry-specific states and behavior

- Visual glyph size and activation area are different measurements.

### Project decisions still required

- Which platform or physical target criteria apply?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs icon and control-size tokens. |
| [Passive display](profile-display.md) | optional | Include when the project needs icon and control-size tokens. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs icon and control-size tokens. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs icon and control-size tokens. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs icon and control-size tokens. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs icon and control-size tokens. |
| [Web app](profile-web-app.md) | optional | Include when the project needs icon and control-size tokens. |
| [Website](profile-website.md) | optional | Include when the project needs icon and control-size tokens. |

Token roles: None required by this entry.

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-009"></a>

## F-009: Focus indication tokens

Named visible focus treatments and offsets.

Kind: token. Shared contract: [tokens](families.md#tokens).

### Variants to specify

- Keyboard
- High contrast
- Assistive focus

### Entry-specific states and behavior

- Do not obscure focus or depend on color change alone.

### Project decisions still required

- How will focus remain visible on every surface?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs focus indication tokens. |
| [Passive display](profile-display.md) | optional | Include when the project needs focus indication tokens. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs focus indication tokens. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs focus indication tokens. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs focus indication tokens. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs focus indication tokens. |
| [Web app](profile-web-app.md) | optional | Include when the project needs focus indication tokens. |
| [Website](profile-website.md) | optional | Include when the project needs focus indication tokens. |

Token roles: None required by this entry.

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-010"></a>

## F-010: Density tokens

Named compactness settings for repeated interface elements.

Kind: token. Shared contract: [tokens](families.md#tokens).

### Variants to specify

- Compact
- Standard
- Comfortable

### Entry-specific states and behavior

- Retain usable targets and readable text when density changes.

### Project decisions still required

- Is user-selectable density needed?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs density tokens. |
| [Passive display](profile-display.md) | optional | Include when the project needs density tokens. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs density tokens. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs density tokens. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs density tokens. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs density tokens. |
| [Web app](profile-web-app.md) | optional | Include when the project needs density tokens. |
| [Website](profile-website.md) | optional | Include when the project needs density tokens. |

Token roles: None required by this entry.

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-011"></a>

## F-011: Brand principles

Shared reasons that guide recognizable brand choices.

Kind: foundation. Shared contract: [identity](families.md#identity).

### Variants to specify

- Corporate
- Product
- Campaign

### Entry-specific states and behavior

- Record approved principles separately from proposed interpretations.

### Project decisions still required

- Which principles are fixed and which can vary?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Passive display](profile-display.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Marketing and sales](profile-marketing-sales.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native phone app](profile-native-phone.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native tablet app](profile-native-tablet.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Website](profile-website.md) | required | Shared starter requirement for this profile; confirm in project scope. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [OFL](../INVENTORY-SOURCES.md#OFL), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-012"></a>

## F-012: Logo architecture

The relationship between primary marks, variants and sub-brands.

Kind: foundation. Shared contract: [identity](families.md#identity).

### Variants to specify

- Wordmark
- Symbol
- Combination
- Endorsement

### Entry-specific states and behavior

- Keep approved geometry separate from new proposals.

### Project decisions still required

- Which marks and relationships are actually approved?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs logo architecture. |
| [Passive display](profile-display.md) | optional | Include when the project needs logo architecture. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs logo architecture. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs logo architecture. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs logo architecture. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs logo architecture. |
| [Web app](profile-web-app.md) | optional | Include when the project needs logo architecture. |
| [Website](profile-website.md) | optional | Include when the project needs logo architecture. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [OFL](../INVENTORY-SOURCES.md#OFL), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-013"></a>

## F-013: Color usage rules

Rules for applying brand and semantic colors across media.

Kind: foundation. Shared contract: [identity](families.md#identity).

### Variants to specify

- Primary
- Accent
- Background
- Monochrome

### Entry-specific states and behavior

- Brand preference does not override meaning or legibility.

### Project decisions still required

- Which colors are restricted and what are their permitted roles?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs color usage rules. |
| [Passive display](profile-display.md) | optional | Include when the project needs color usage rules. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs color usage rules. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs color usage rules. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs color usage rules. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs color usage rules. |
| [Web app](profile-web-app.md) | optional | Include when the project needs color usage rules. |
| [Website](profile-website.md) | optional | Include when the project needs color usage rules. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [OFL](../INVENTORY-SOURCES.md#OFL), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-014"></a>

## F-014: Typography usage rules

Rules for typeface choice, hierarchy and language coverage.

Kind: foundation. Shared contract: [identity](families.md#identity).

### Variants to specify

- Editorial
- Interface
- Display
- Multiscript

### Entry-specific states and behavior

- Check actual licensing and fallback behavior.

### Project decisions still required

- Which fonts are licensed for each operation and output?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs typography usage rules. |
| [Passive display](profile-display.md) | optional | Include when the project needs typography usage rules. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs typography usage rules. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs typography usage rules. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs typography usage rules. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs typography usage rules. |
| [Web app](profile-web-app.md) | optional | Include when the project needs typography usage rules. |
| [Website](profile-website.md) | optional | Include when the project needs typography usage rules. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [OFL](../INVENTORY-SOURCES.md#OFL), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-015"></a>

## F-015: Iconography style

Rules for a coherent visual symbol vocabulary.

Kind: foundation. Shared contract: [identity](families.md#identity).

### Variants to specify

- Outline
- Filled
- Pictogram
- Platform icon

### Entry-specific states and behavior

- Differentiate decorative symbols from meaningful controls.

### Project decisions still required

- When should the system use native symbols instead of custom ones?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs iconography style. |
| [Passive display](profile-display.md) | optional | Include when the project needs iconography style. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs iconography style. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs iconography style. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs iconography style. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs iconography style. |
| [Web app](profile-web-app.md) | optional | Include when the project needs iconography style. |
| [Website](profile-website.md) | optional | Include when the project needs iconography style. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [OFL](../INVENTORY-SOURCES.md#OFL), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-016"></a>

## F-016: Imagery and art direction

Rules for photography, illustration, composition and representation.

Kind: foundation. Shared contract: [identity](families.md#identity).

### Variants to specify

- Photography
- Illustration
- Product
- Diagram

### Entry-specific states and behavior

- Specify crop, factual accuracy, rights and alternative descriptions.
- Use paired suitable/unsuitable examples to explain the approved project image policy, including crop and context; no photographic style is universally correct.

### Project decisions still required

- What should imagery communicate and what must it avoid?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs imagery and art direction. |
| [Passive display](profile-display.md) | optional | Include when the project needs imagery and art direction. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs imagery and art direction. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs imagery and art direction. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs imagery and art direction. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs imagery and art direction. |
| [Web app](profile-web-app.md) | optional | Include when the project needs imagery and art direction. |
| [Website](profile-website.md) | optional | Include when the project needs imagery and art direction. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [OFL](../INVENTORY-SOURCES.md#OFL), [SCOPE](../INVENTORY-SOURCES.md#SCOPE), [SPECIMEN-SYNTH](../INVENTORY-SOURCES.md#SPECIMEN-SYNTH). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation. Original generic documentation refinement; comparison disposition is recorded in EXAMPLE-COMPARISON.md. The added specimen/composition advice is internally synthesized; SPECIMEN-SYNTH records the EX3 observation boundary, while other cited sources retain their narrower basis.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-017"></a>

## F-017: Motion and sound principles

Rules for purposeful movement and audible feedback.

Kind: foundation. Shared contract: [identity](families.md#identity).

### Variants to specify

- Transition
- Narrative
- Feedback
- Silent alternative

### Entry-specific states and behavior

- Account for reduced motion, captions and unexpected sound.

### Project decisions still required

- Which effects are useful rather than decorative?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs motion and sound principles. |
| [Passive display](profile-display.md) | optional | Include when the project needs motion and sound principles. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs motion and sound principles. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs motion and sound principles. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs motion and sound principles. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs motion and sound principles. |
| [Web app](profile-web-app.md) | optional | Include when the project needs motion and sound principles. |
| [Website](profile-website.md) | optional | Include when the project needs motion and sound principles. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: [G-010: Motion, media and sensory alternatives](governance.md#g-010)

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [OFL](../INVENTORY-SOURCES.md#OFL), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-018"></a>

## F-018: Voice and tone

Rules for how the brand speaks across situations.

Kind: foundation. Shared contract: [language](families.md#language).

### Variants to specify

- Instructional
- Support
- Marketing
- Serious error

### Entry-specific states and behavior

- Tone changes with context while intent stays clear.

### Project decisions still required

- How does the voice change during errors, risk or sensitive tasks?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Passive display](profile-display.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Marketing and sales](profile-marketing-sales.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native phone app](profile-native-phone.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native tablet app](profile-native-tablet.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Website](profile-website.md) | required | Shared starter requirement for this profile; confirm in project scope. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-019"></a>

## F-019: Terminology and naming

A consistent vocabulary for features, actions and brand language.

Kind: foundation. Shared contract: [language](families.md#language).

### Variants to specify

- Product terms
- Acronyms
- Labels
- Prohibited language

### Entry-specific states and behavior

- Keep abbreviations understandable and translations consistent.

### Project decisions still required

- Who owns the glossary and approves new terms?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Passive display](profile-display.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Marketing and sales](profile-marketing-sales.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native phone app](profile-native-phone.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native tablet app](profile-native-tablet.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Website](profile-website.md) | required | Shared starter requirement for this profile; confirm in project scope. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-020"></a>

## F-020: Localization and RTL

Rules for language, text direction and locale-dependent formats.

Kind: foundation. Shared contract: [language](families.md#language).

### Variants to specify

- RTL
- Text expansion
- Dates
- Numbers
- Currency

### Entry-specific states and behavior

- Do not blindly mirror media controls, logos or numeric content.

### Project decisions still required

- Which languages, scripts and locale conventions require testing?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Passive display](profile-display.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Marketing and sales](profile-marketing-sales.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native phone app](profile-native-phone.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Native tablet app](profile-native-tablet.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Shared touch display](profile-touch.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Web app](profile-web-app.md) | required | Shared starter requirement for this profile; confirm in project scope. |
| [Website](profile-website.md) | required | Shared starter requirement for this profile; confirm in project scope. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: [G-009: Text scaling, reflow and reading order](governance.md#g-009)

Source basis: [GOV](../INVENTORY-SOURCES.md#GOV), [WCAG](../INVENTORY-SOURCES.md#WCAG), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-021"></a>

## F-021: Responsive and adaptive rules

Rules for adapting layout to window, orientation and input.

Kind: foundation. Shared contract: [identity](families.md#identity).

### Variants to specify

- Narrow
- Expanded
- Split view
- Large text

### Entry-specific states and behavior

- A tablet is not just a scaled phone and touch is not a mouse.

### Project decisions still required

- Which content priorities and navigation change at each size?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs responsive and adaptive rules. |
| [Passive display](profile-display.md) | optional | Include when the project needs responsive and adaptive rules. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs responsive and adaptive rules. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs responsive and adaptive rules. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs responsive and adaptive rules. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs responsive and adaptive rules. |
| [Web app](profile-web-app.md) | optional | Include when the project needs responsive and adaptive rules. |
| [Website](profile-website.md) | optional | Include when the project needs responsive and adaptive rules. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [OFL](../INVENTORY-SOURCES.md#OFL), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

<a id="f-022"></a>

## F-022: Data visualization language

Shared encoding rules for charts and quantitative communication.

Kind: foundation. Shared contract: [identity](families.md#identity).

### Variants to specify

- Categorical
- Sequential
- Diverging
- Uncertainty

### Entry-specific states and behavior

- Include units, uncertainty, non-color encoding and underlying data access.

### Project decisions still required

- Which comparisons and precision are truthful for the data?

### Profile starting points

| Profile | Selection | Rationale |
| --- | --- | --- |
| [Brand guidelines](profile-brand.md) | optional | Include when the project needs data visualization language. |
| [Passive display](profile-display.md) | optional | Include when the project needs data visualization language. |
| [Marketing and sales](profile-marketing-sales.md) | optional | Include when the project needs data visualization language. |
| [Native phone app](profile-native-phone.md) | optional | Include when the project needs data visualization language. |
| [Native tablet app](profile-native-tablet.md) | optional | Include when the project needs data visualization language. |
| [Shared touch display](profile-touch.md) | optional | Include when the project needs data visualization language. |
| [Web app](profile-web-app.md) | optional | Include when the project needs data visualization language. |
| [Website](profile-website.md) | optional | Include when the project needs data visualization language. |

Token roles: [F-001: Semantic color](foundations.md#f-001), [F-002: Typography tokens](foundations.md#f-002), [F-003: Spacing tokens](foundations.md#f-003)

Dependencies: None recorded.

Related concepts: See shared family and dependencies.

Source basis: [IBM](../INVENTORY-SOURCES.md#IBM), [OFL](../INVENTORY-SOURCES.md#OFL), [SCOPE](../INVENTORY-SOURCES.md#SCOPE). Original entry and specification prompts. Sources are naming or guidance comparisons, not endorsement or an adopted implementation.

Status: inventoried; common specification template available; implementation not provided; testing not performed.

