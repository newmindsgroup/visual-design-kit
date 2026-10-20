# Spacing

Version-Timestamp: 2026-10-20 02:07:10 UTC

Space is the main grouping tool. Use one scale, make space between groups clearly larger than space inside them, and let the parent layout own the gaps between components.

## The scale

The token contract uses a 4px base (`--space-n` = n x 0.25rem). Use 8px steps for most layout and 4px steps inside components.

| Token | px | Typical use |
| --- | --- | --- |
| `--space-0` | 0 | Reset |
| `--space-1` | 4 | Icon-to-text gap in tight UI, label to helper text, chip vertical padding |
| `--space-2` | 8 | Label to input, icon to text in buttons, items in a tight stack |
| `--space-3` | 12 | Button vertical padding, list item gaps, card title to body |
| `--space-4` | 16 | Card padding on phones, field to field, paragraph spacing, phone margins |
| `--space-5` | 20 | Medium card padding, comfortable list rows |
| `--space-6` | 24 | Card padding on desktop, form groups, desktop gutters |
| `--space-8` | 32 | Between groups inside a section, heading top spacing |
| `--space-10` | 40 | Between sub-sections |
| `--space-12` | 48 | Section padding on phones, between card rows |
| `--space-16` | 64 | Section spacing on tablets |
| `--space-20` | 80 | Section spacing on desktop |
| `--space-24` | 96 | Major section breaks, hero padding |

Larger values compose from tokens: `calc(var(--space-16) * 2)` is 128px; `calc(var(--space-20) * 2)` is 160px. Never introduce off-scale values (13px, 22px, 37px) except a documented optical correction.

## Proximity rules

Gestalt proximity: things that are close are read as related. Make the relationship visible with ratios.

| Relationship | Inside | Between | Ratio |
| --- | --- | --- | --- |
| Label, input, helper text | 4-8px | 16-24px to the next field | 3x |
| Form fields, fieldsets | 16-24px between fields | 32-48px between fieldsets | 2x |
| Heading and its content | 8-16px below the heading | 32-64px above the heading | 2-4x |
| Card contents, cards | 12-16px inside | 24-32px between cards | 2x |
| Items in a section, sections | 24-48px | 80-160px between sections | 2-3x |

The most common spacing bug is a heading equidistant from the section above and the paragraph below, so it floats between them. Space above a heading should be at least twice the space below it.

## Internal vs external spacing

- **Internal** spacing is a component's padding and the gaps between its own parts. The component owns it.
- **External** spacing is the gap between components. The parent layout owns it, with `gap` or a stack rule. Components do not set outer margins.
- External spacing is always at least as large as the internal spacing of the components it separates; otherwise cards look glued together.

```css
.stack { display: flex; flex-direction: column; gap: var(--stack-gap, var(--space-4)); }
.cluster { display: flex; flex-wrap: wrap; gap: var(--space-2) var(--space-3); align-items: center; }
.section { padding-block: clamp(var(--space-12), 8vw, calc(var(--space-20) * 2)); }   /* 48px to 160px */
```

## Component spacing defaults

| Component | Size | Internal spacing |
| --- | --- | --- |
| Button | Heights 32 / 40 / 48px (sm / md / lg) | Inline padding 12 / 16 / 24px; icon gap 8px |
| Text input, select | Height 40px (44-48px on touch-first) | Inline padding 12px; label above at 8px |
| Checkbox and radio rows | Row 32-44px | Control to label 8px; hit area at least `--size-target-min` 24px, ideally `--size-target-comfortable` 44px |
| Card | | Padding 16px phones, 24px desktop, 32px for feature cards |
| Dialog | Width 400-640px | Padding 24-32px; actions separated by 24px |
| Table cell | Row 32 / 40 / 48px by density | 8-12px vertical, 12-16px horizontal |
| List item | | 12-16px vertical |
| Chip, tag | Height 24-32px | 4-6px vertical, 8-12px horizontal |
| Top navigation (web) | Height 56-72px | Items 24-32px apart |
| Toast | | 12-16px padding; 16-24px from the viewport edge |

## Section spacing by context

| Context | Phones | Desktop |
| --- | --- | --- |
| Product UI regions (panels, toolbars, page sections) | 16-24px | 24-48px |
| Documentation and articles (between h2 sections) | 40-48px | 48-64px |
| Marketing sections | 48-80px | 80-160px |
| Luxury, editorial and quiet-minimal | 64-96px | 120-200px |
| Dense dashboards (between widget rows) | 12-16px | 16-24px |

## Density modes

Offer density when users spend hours in the product (tables, admin, email, trading).

| Mode | Row height | Cell padding | Body size | Use |
| --- | --- | --- | --- | --- |
| Compact | 32px | 4-8px vertical | 13-14px | Experts, large data sets, desktop only |
| Default | 40px | 8-12px vertical | 14-16px | Most products |
| Comfortable | 48-56px | 12-16px vertical | 16px | Touch, occasional users, older adults |

- Material Design expresses density as steps that each remove 4dp of height; the same idea works with these tokens.
- Implement with an attribute that swaps component tokens: `[data-density="compact"] { --row-height: 2rem; --cell-pad-block: var(--space-1); }`.
- Never let compact mode shrink touch targets below 24x24px or text below 12px.

## Optical spacing

Measured equality is not perceived equality.

- Text boxes include half-leading above and below; a heading at line-height 1.1 looks closer to an image than body text at 1.5 with the same gap. Compensate by 2-4px or trim with `text-box`.
- Icons drawn with internal padding look farther from text than the box suggests; tighten the gap by 2px.
- Round and pointed shapes look smaller than squares; give them slightly less surrounding space or slightly more size (see [composition](composition.md)).
- All-caps labels sit visually higher than mixed case; center them by eye, not by box.
- Buttons with a leading icon look unbalanced with equal padding; reduce padding on the icon side by 2-4px.

## Spacing checklist

- Every gap maps to a `--space-*` token (or a documented composite).
- Between-group space is at least twice within-group space.
- Headings sit closer to their content than to the previous section.
- Components have no outer margins; layouts use `gap`.
- Density modes keep targets and minimum text sizes.
