# Product flows

Version-Timestamp: 2026-10-20 02:04:32 UTC

Patterns for the flows every product needs. Each section gives defaults and a checklist; map them onto the project's flow IDs from `ux-design` [journeys and flows](../../ux-design/references/journeys-and-flows.md). Regulatory notes shape design; confirm requirements with counsel for the specific product and jurisdiction.

## Onboarding

**Goal:** time to first value, not a tour of features.

- Ask only questions whose answers change the first screen (role, use case, team size). 1-3 questions, each skippable, with a visible "Skip".
- Get people to a real result in the first session: a template, sample data, an import, or a guided first task.
- Prefer contextual hints at the moment of need over up-front carousels and product tours; tours of 5+ steps are mostly skipped.
- A setup checklist of 3-6 items shows progress; count account creation as the first completed item (goal-gradient effect). Let people dismiss it.
- Empty states double as onboarding: each explains the area and offers the first action.
- Defer email verification, profile photos and invitations until they add value, unless security requires them first.
- Measure: activation rate (the event that predicts retention), time to first value, checklist completion, day-7 retention.

## Authentication

**Sign-in defaults (as of 2026):**

| Method | Default treatment |
| --- | --- |
| Passkeys (WebAuthn / FIDO2) | Offer first for consumer and SaaS products. Enable autofill on the username field (`autocomplete="username webauthn"`) so saved passkeys appear in the browser's suggestion list; offer "Create a passkey" right after sign-up or a successful password sign-in, explaining the benefit in one line ("Sign in with your fingerprint, face or screen lock") |
| Email + password | Keep as fallback. Identifier first ("Email address", then Continue) lets you route to passkey, SSO or password |
| Magic link or email code | Good for low-frequency consumer products; codes work better than links when people open email on another device |
| Social sign-in (Google, Apple, others) | Use the providers' official button guidelines; apps on iOS that offer third-party sign-in generally must also offer Sign in with Apple or an equivalent privacy-focused option (check current App Store Review Guidelines) |
| Enterprise SSO (SAML, OIDC) | Detect the work email domain on the identifier step and redirect; also offer "Sign in with SSO" explicitly |

**Passwords (NIST SP 800-63B-4, 2025):** at least 15 characters when the password is the only factor, at least 8 when it is part of multi-factor authentication; accept at least 64 characters, spaces and Unicode; no composition rules (no "one uppercase, one symbol"); no forced periodic changes; check new passwords against lists of breached and common passwords; allow paste and password managers. Show requirements up front and a show/hide toggle.

**Multi-factor authentication:**

- Order of preference to offer: passkey or security key (phishing-resistant), authenticator app (TOTP), push approval with number matching, then SMS or voice codes as a fallback; NIST classes SMS and voice as restricted authenticators.
- Code entry: one field, `autocomplete="one-time-code"`, `inputmode="numeric"`, paste allowed, auto-submit on the last digit optional.
- Recovery codes at setup (8-10 single-use codes), with download and copy, and a confirmation that the user saved them.
- "Remember this device for 30 days" (or the security policy's period) reduces friction.
- Step-up authentication only for sensitive actions (change payout account, export data), with a clear reason.

**WCAG 3.3.8 Accessible Authentication (Minimum):** no cognitive function test (remembering a password, solving a puzzle, transcribing characters) unless there is an alternative, a mechanism to help (password manager autofill, paste), or the test is object recognition or identifying personal content. Passkeys, email links and allowing paste all satisfy it.

**Copy and errors:**

- Do not reveal whether an account exists on password reset: "If an account exists for that email, we've sent a reset link."
- Sign-in error: "Email or password is incorrect" plus a reset link; after repeated failures, explain the lockout or delay and when it ends.
- Sign-up: minimal fields (email, then password or passkey); name and other details later.
- Session timeout warnings follow [states and feedback](states-and-feedback.md).

## Pricing pages

- 3-4 plans side by side on desktop (stacked or swipeable on mobile), plus "Enterprise: contact sales" when relevant.
- Each plan card: name, who it is for in one line, price with billing period and currency, primary CTA, the 4-6 features that differ (not everything), and limits (seats, usage).
- Highlight the recommended plan with a label ("Most popular" only if true) and a border or background, not color alone.
- Monthly/annual toggle near the top; show annual savings as a real figure ("2 months free" or "Save 17%") and the billed amount ("$190 billed yearly").
- Full comparison table below with a sticky header row of plan names and CTAs; group features; use check marks with text alternatives.
- FAQ for billing, trials, cancellation, refunds, taxes and data on downgrade.
- Show prices in local currency where you sell; in the EU and UK consumer prices must include VAT, and the UK's DMCC Act (consumer rules in force since April 2025) requires mandatory fees in the headline price. US FTC rules restrict hidden "junk fees" in specific sectors (live events, short-term lodging).
- Usage-based pricing: a calculator with sensible defaults and an example bill.
- Free trial terms in plain words next to the CTA: length, whether a card is needed, what happens at the end, how to cancel.

Page-level structure and persuasion rules are in `web-design` [page architecture](../../web-design/references/page-architecture.md) and [conversion](../../web-design/references/conversion.md).

## Checkout

Baymard Institute puts the average documented cart abandonment rate around 70% (70.22% as of September 2025); its surveys repeatedly rank unexpected extra costs, forced account creation and long or complicated checkouts among the top fixable reasons. Verify current figures at baymard.com before citing them.

- **Guest checkout** is the default, shown as prominently as sign-in. Offer account creation after purchase ("Save your details for next time").
- **Total cost early:** shipping, taxes and fees visible in the cart, not first revealed at payment. Estimate shipping from postcode or location.
- **Express wallets** (Apple Pay, Google Pay, PayPal, Shop Pay, regional methods) at the top of the cart and checkout.
- **Steps:** contact, delivery, payment, review, or a single page with clear sections. Show progress and keep an order summary visible (sidebar on desktop, collapsible at top on mobile).
- **Address:** autocomplete lookup with a manual option; "Billing same as delivery" checked by default.
- **Delivery options** with dates ("Arrives Thu 12 March"), not only speeds.
- **Payment:** card number with automatic spacing and card type detection; expiry as MM/YY in one field; hosted fields from the payment provider; handle 3-D Secure and Strong Customer Authentication (EU/UK PSD2) as an in-flow step with a clear return.
- **Promo code** field collapsed behind a link, so it does not send people off to search for codes.
- **Final button** states the commitment: "Pay $84.20" or "Place order"; EU consumer law requires wording that makes the obligation to pay clear (such as "order with obligation to pay").
- **Errors** keep every entered value; declined cards suggest another method.
- **Confirmation page:** order number, summary, delivery estimate, email sent, next steps, account creation offer.
- **No pre-ticked add-ons** (insurance, donations, subscriptions): banned for consumers in the EU and a dark pattern everywhere.

## Search and filter

- **Search field:** visible in the header on content and commerce sites, wide enough for about 27 characters on desktop; placeholder as an example ("Search products, e.g. 'linen shirt'").
- **Autocomplete:** suggestions after 1-2 characters with matched text highlighted, about 8-10 items on desktop and fewer on mobile, grouped (queries, categories, products); keyboard navigable (ARIA combobox).
- **Tolerance:** typos, plurals, synonyms and the site's own vocabulary; zero-result queries reviewed monthly.
- **Results page:** query echoed with the count ("84 results for 'linen shirt'"), sort options (relevance first), facets with counts, applied filters as removable chips with "Clear all".
- **Facets:** most used first, 5-10 values visible with "Show more", search inside long facets, disabled or hidden values with zero results.
- **Desktop applies filters instantly; mobile collects them in a sheet with a "Show 42 results" button.**
- **No results:** keep the query visible, suggest corrections, show popular categories or relaxed matches, and offer contact or help.
- **State in the URL** so results can be shared and Back restores them.

## Settings

- Group by the user's mental model (Account, Notifications, Privacy, Billing, Team, Integrations), not by internal service.
- Add search once there are more than about 20-30 settings.
- Switches apply immediately with a brief "Saved" confirmation; forms of related fields use an explicit Save with unsaved-changes protection.
- Show scope when it matters: "Applies to you" versus "Applies to everyone in Acme workspace".
- Explain consequences under each setting in one line; link to help for complex ones.
- Dangerous actions (transfer ownership, delete workspace) at the bottom in a clearly separated "Danger zone" with confirmation.
- Respect system settings by default (theme, reduced motion, language) with an override.

## Account deletion and cancellation

- **Findable:** in account settings under a plain label ("Delete account"), not hidden behind support email. Apple's App Store guidelines require in-app account deletion for apps that support account creation (since June 2022), and Google Play requires an in-app path and a web link.
- **Explain consequences:** what is deleted, what is kept and why (invoices for tax law), what happens to shared content and team ownership.
- **Offer alternatives without obstruction:** pause, downgrade or export data, presented once, with the delete path still one click away.
- **Re-authenticate** before deletion; then confirm by typing "DELETE" or the account email for high-impact accounts.
- **Grace period** of 14-30 days with a clear restore path, then permanent deletion, and a confirmation email.
- **Data export** before deletion (machine-readable format) supports GDPR rights of access and portability; deletion supports the right to erasure (GDPR Art. 17) and US state deletion rights (CCPA/CPRA and others).
- **Subscriptions:** cancel online, through the same channel and with no more steps than sign-up. In the US the FTC's 2024 click-to-cancel rule was vacated by the Eighth Circuit in July 2025, but ROSCA, the FTC Act and state automatic-renewal laws (such as California's, amended effective July 2025) still apply. In the EU, an online withdrawal function for distance contracts applies from 19 June 2026 (Directive (EU) 2023/2673). Confirm requirements with counsel for each market.
- Never use guilt ("No, I don't want to save money") or a maze of retention screens. These are listed dark patterns in `web-design` [conversion](../../web-design/references/conversion.md).
