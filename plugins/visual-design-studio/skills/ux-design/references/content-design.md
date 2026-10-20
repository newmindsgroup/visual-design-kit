# Content design

Version-Timestamp: 2026-10-20 02:04:32 UTC

Words are interface. Design them with the flow, in real context, at the reading level of the audience, and test whether people understand them. Copy that compensates for a confusing interaction is a symptom; fix the interaction first.

## Plain language defaults

| Rule | Default |
| --- | --- |
| Reading level | Grade 6-8 for consumer products; GOV.UK writes for a reading age of 9; expert tools keep precise terms but define each once |
| Sentence length | Average 15-20 words; split any sentence over 25 |
| Paragraphs on screen | 1-3 sentences |
| Voice | Active ("We sent your code"), second person ("you"), present tense |
| Words | Common words: buy (not purchase), help (not assist), start (not commence), about (not regarding), use (not utilize) |
| Order | Most important information first; front-load headings, links and list items with the key word |
| Numbers | Numerals ("3 items"), not words; thousands separators per locale |
| Jargon | Remove it or define it once, in place |

Standards and sources: ISO 24495-1:2023 (plain language governing principles), the US Plain Writing Act of 2010 and the Federal Plain Language Guidelines, GOV.UK content design guidance, Sarah Richards' *Content Design* (2017).

## Readability formulas and their limits

- **Flesch Reading Ease** (0-100, higher is easier): 60-70 reads as plain English.
- **Flesch-Kincaid Grade Level**: US school grade; aim for 6-8 for general audiences.
- **SMOG**: often preferred for health information.
- Formulas count syllables and sentence length only. Short, familiar, wrong words still score well. Use formulas to flag problems and test comprehension with people.

**Comprehension tests.** Highlighter test (popularized at GOV.UK): participants mark text that makes them confident in green and unsure in red. Cloze test: delete every fifth word; 60% or more correct replacements suggests adequate comprehension. Task-based questions: "Based on this page, can you return an opened item?"

## Voice and tone

Voice is constant; tone flexes with the moment (as in Mailchimp's public Content Style Guide).

**Voice chart.** 3-4 traits written as "this, not that", each with an example:

| Trait | Not | Sounds like |
| --- | --- | --- |
| Clear | Clever | "Your plan renews on 4 March." |
| Warm | Gushing | "Welcome back. Pick up where you left off." |
| Confident | Bossy | "We recommend the annual plan for teams of 5 or more." |

**Tone by moment:**

| Moment | Tone | Example |
| --- | --- | --- |
| Onboarding | Encouraging, brief | "Add your first project. It takes about a minute." |
| Success | Calm, specific | "Payment sent. It arrives in 1-2 business days." |
| Error the user can fix | Direct, helpful | "Enter a date in the past." |
| System failure | Accountable | "We couldn't save your changes. Your edits are kept on this device; try again in a moment." |
| Destructive action | Serious, exact | "Delete 'Q3 budget'? This also deletes its 14 files." |
| Outage or security | Plain, factual, no humor | "Some payments are delayed. We'll email you when they're processed." |

Humor belongs only in low-stakes moments, and never in errors, money, health, security or grief.

## Microcopy patterns

| Element | Rule | Good | Avoid |
| --- | --- | --- | --- |
| Button | Verb + object, sentence case, usually 1-3 words; names the result | "Save changes", "Create invoice", "Send 3 invites" | "Submit", "OK", "Yes", "Click here" |
| Link | Describes the destination (WCAG 2.4.4) | "Read the refund policy" | "Learn more" repeated 6 times |
| Label | Short noun phrase, always visible, no colon | "Email address" | Placeholder used as the label |
| Hint | Format or reason, shown before the field | "We'll only use this to send your receipt" | Hints only in tooltips |
| Placeholder | An example, never essential information | "name@example.com" | "Enter your email address" |
| Tooltip | Supplementary detail only | Definition of "APR" | Instructions needed to complete the task |
| Empty state | What this is, why it is empty, the next action | "No invoices yet. Create one, or import from a spreadsheet." | "Nothing here!" |
| Confirmation dialog | Title asks about the specific action; body states the consequence; buttons repeat the verb | "Delete 3 projects?" / "Delete projects" / "Cancel" | "Are you sure?" / "Yes" / "No" |
| Toast | Past tense, what happened, optional Undo | "Archived 3 messages. Undo" | "Success!" |
| Progress | What is happening and how far | "Uploading 3 of 12 files" | "Please wait..." |
| Permission request | Why, in the user's terms, before the system prompt | "Allow notifications to hear when your order ships." | Asking on first launch with no context |

## Error messages

Formula: **what happened + how to fix it**, plus why only when it helps. Put the message next to the field, repeat it in an error summary for long forms, keep the user's input, and never blame the user.

| Situation | Bad | Good (GOV.UK style) |
| --- | --- | --- |
| Required field empty | "Field is required" | "Enter your date of birth" |
| Wrong format | "Invalid email" | "Enter an email address in the correct format, like name@example.com" |
| Out of range | "Invalid date" | "Date of birth must be in the past" |
| Too long | "Error 413" | "Message must be 500 characters or fewer" |
| Card declined | "Transaction failed" | "Your bank declined this card. Try another card or contact your bank." |
| Lost connection, outcome unknown | "Failed. Retry?" | "We can't confirm your payment went through. Check your email for a receipt before trying again." |
| Server error | "Oops! Something went wrong" | "We couldn't load your invoices. Refresh the page; if it keeps happening, contact support with code INV-503." |

Error codes help support; show them after the human sentence, never alone. "Oops" and exclamation marks add nothing to an error.

## Dates, numbers and inclusive language

- Unambiguous dates: "4 March 2026" or "Mar 4, 2026" per locale; never 03/04/26 in international products.
- Times in the user's time zone with the zone shown when it matters ("9:00 AM ET").
- Currency with symbol and, where ambiguous, ISO code ("$120 CAD").
- Gender-neutral language; ask for gender only when needed, with self-describe and prefer-not-to-say options.
- People-first or identity-first language as the community prefers; ask if unsure.
- Name fields: one "Full name" field handles more of the world's names than first and last fields (W3C guidance on personal names).

## Localization

Leave room for expansion. A common planning table (IBM globalization guidance) for English source text:

| English length | Typical expansion |
| --- | --- |
| Up to 10 characters | 100-200% |
| 11-20 | 80-100% |
| 21-30 | 60-80% |
| 31-50 | 40-60% |
| 51-70 | 31-40% |
| Over 70 | About 30% |

- Never concatenate strings ("You have " + n + " items"); use ICU MessageFormat with plural rules.
- Avoid idioms, puns and culture-bound metaphors in UI text.
- Give translators context: screenshot, character limit, variable meanings.
- Plan for right-to-left scripts with logical CSS properties; see the `typography` and `layout` skills.

## Process

1. Write the user need first: "As a [who], I need [what] so that [why]."
2. Put real or realistic content into wireframes from the first draft; no lorem ipsum.
3. Keep a string inventory with keys, context and limits (`checkout.payment.error.declined`).
4. Maintain a glossary of preferred terms and banned synonyms.
5. Test comprehension with the target audience and fix the flow when copy keeps failing.

Deep process for client projects: [content writing](../../../library/draft-skills/design-content-writing/SKILL.md).
