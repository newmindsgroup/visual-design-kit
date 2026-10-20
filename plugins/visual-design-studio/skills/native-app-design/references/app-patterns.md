# App patterns within platform rules

Version-Timestamp: 2026-10-20 02:08:24 UTC

Patterns that decide retention and App Review outcomes. Store-policy references are to Apple's App Review Guidelines (last updated 16 October 2026, checked on 2026-10-20) and the Apple HIG. Google Play Help pages could not be fetched from this environment; Play items are from Google's published policy as last known and marked "verify". Policies change; confirm the current text, and confirm regulatory points with counsel for the specific product and jurisdiction.

## Onboarding

| Decision | Default | Change when |
| --- | --- | --- |
| Screens before value | Zero: open on useful content or a sample | A device pairing, health or finance setup legally or technically requires steps first |
| If a flow is needed | 1-3 screens, skippable, interactive (do the task, not read about it) | Complex pro tools: replace the tour with contextual tips |
| Account | Let people use the app without an account unless the core feature is account-based (App Review 5.1.1(v)) | Banking, messaging, multiplayer |
| Sign-in options | Passkeys plus email; if you offer Google, Facebook or similar social login for the primary account, also offer an equivalent private option such as Sign in with Apple (App Review 4.8) | Enterprise or education accounts only (exempt under 4.8) |
| Setup | Postpone customization; ship sensible defaults | Personalization is the product (music, news): ask 1 question, show results immediately |
| Splash | Only the system launch screen; no logo animation over 1 second | Never block on large downloads; bundle first-run content |

Avoid tutorials that explain the OS (how to scroll), licensing walls inside onboarding, and asking for ratings or purchases before people have used the app.

## Permission priming

- Ask **in context**, at the moment the feature needs it (camera when they tap Scan), never all at launch.
- iOS pre-alert screen (HIG privacy): optional; **one button only**, which opens the system alert; do not label it "Allow"; no close or cancel route that skips the alert; no incentives, fake alerts or images of the alert. Write the purpose string as a specific benefit ("Scan receipts to fill in expenses automatically").
- Android: request with the runtime dialog; if `shouldShowRequestPermissionRationale` is true, show a rationale first. After repeated denial the system stops showing the dialog, so offer a button that opens app settings.
- Prefer permission-free alternatives: the system photo picker instead of full library access, location button or approximate location, manual address entry when location is declined (App Review 5.1.1(iv)).
- Paid features must not depend on granting data access (5.1.1(ii)).

## Notifications

- iOS: request authorization after showing value, or use **provisional authorization** to deliver quietly to Notification Center first. Assign an honest interruption level:

| Level | Breaks through Focus | Use |
| --- | --- | --- |
| Passive | No | Recommendations, digests |
| Active (default) | No | Replies, updates people asked for |
| Time Sensitive | Yes | Security alerts, a delivery arriving within the hour |
| Critical | Yes, and overrides silent mode | Health and safety only; needs an Apple entitlement |

- Android 13+: notifications need the `POST_NOTIFICATIONS` runtime permission. Define notification **channels** by type (messages, order updates, promotions) so people can mute one without losing all.
- Marketing pushes need explicit opt-in with clear consent language and an in-app opt-out (App Review 4.5.4). Never send marketing as Time Sensitive.
- Notifications must not be required for the app to work. Put actions in the notification (Reply, Mark done) and deep-link to the exact item.

## Offline, sync and loading states

| State | What to show | Rule |
| --- | --- | --- |
| Loading, under 1s | Nothing or a subtle indicator | Avoid flashes of spinners |
| Loading, 1-5s | Skeletons matching the final layout, or the M3 loading indicator | Keep the shell interactive |
| Loading, over 5s | Determinate progress with a cancel | Explain what is happening |
| Fresh | Content | Pull-to-refresh available |
| Stale | Content plus "Updated 10 min ago" | Show freshness when it changes a decision (prices, balances, departures) |
| Offline | Cached content plus a non-blocking banner | Distinguish "offline" from "no results" |
| Pending changes | Item marked "Waiting to sync" | Queue only idempotent actions; never queue payments silently |
| Conflict | Both versions with a clear choice | Never overwrite silently |
| Failed | What failed, why if known, Retry | Keep the user's input |

Classify each feature as local, cached or network-required before designing. The draft skill `design-touch-offline` has the connectivity matrix method.

## Paywalls and subscriptions

Content every paywall shows before purchase (App Review 3.1.2(c) and Apple's Schedule 2; Google Play subscription policy, verify):

- What people get, in concrete terms (how many, how much storage, which features).
- Price and billing period in the local currency, with the per-period price as the primary number; any per-week or per-month breakdown must not be bigger than the real charge.
- Trial length, the date or moment the first charge happens, and the renewal price.
- How to cancel (Apple subscriptions are managed in system Settings), Restore Purchases, and links to terms and privacy policy.
- A visible close or "Not now" control from the first frame.

Store rules that shape the design:

- **Apple**: digital content and features unlock through In-App Purchase (3.1.1). Reader apps (magazines, books, music, video) may link to an external account page with an entitlement (3.1.3(a)). Physical goods and services consumed outside the app must not use IAP (3.1.3(e)). In the United States storefront, apps may include buttons and external links to other purchase methods without the entitlement (3.1.1(a), 3.1.3). Auto-renewing subscriptions last at least 7 days.
- **Google Play**: digital goods use Google Play Billing, with region-specific alternative and user-choice billing programs; US rules changed after the Epic v. Google remedies in 2025 (verify the current Payments policy for each market).
- Patterns to avoid: hidden or delayed close buttons, preselected plans with misleading savings badges, fake countdowns, guilt copy on the decline button, and a trial toggle that silently changes the plan. Subscription and auto-renewal laws vary by jurisdiction; confirm with counsel.

## Account deletion (required)

- Apple: if the app supports account creation, it must offer **account deletion inside the app** (App Review 5.1.1(v)); the privacy policy must explain retention and deletion (5.1.1(i)). Apps using Sign in with Apple should revoke the user's tokens on deletion (verify current developer guidance).
- Google Play: apps with account creation must provide an in-app path to delete the account and its data **and** a web link where people can request deletion without reinstalling, declared in the Data safety form (verify).
- Design: Settings > Account > Delete account, reachable in 3 taps or fewer. Explain what is deleted and what is retained for legal reasons, offer data export first, remind people that store subscriptions are cancelled separately, confirm once (type-to-confirm only for high-stakes accounts), then show completion. Do not route people to email support as the only path.

## Rating and review prompts

- Use the system prompts only: StoreKit's review request (Apple disallows custom review prompts, 5.6.1) and Google's In-App Review API. Apple shows the prompt at most 3 times in 365 days; Google applies an undisclosed quota. Neither guarantees display, so never attach a button that "opens the prompt".
- Trigger after a success moment (task completed, third order delivered), not at launch, not mid-task, at least 1-2 weeks apart (HIG).
- Do not gate the prompt with "Do you like the app?" to send only happy users to the store; it misrepresents ratings and risks policy action. A separate, always-available Feedback item in Settings is fine.
- Do not offer rewards for ratings.

## Gestures and discoverability

| Gesture | iOS meaning | Android meaning | Visible alternative |
| --- | --- | --- | --- |
| Swipe from left edge | Back | Back (either edge with gesture navigation) | Back button |
| Swipe up from bottom | Home or app switcher (system) | Home or recents (system) | None needed; never override |
| Swipe on list row | Reveal actions (delete, archive) | Same (less common; Material uses swipe for dismiss) | Context menu or Edit mode |
| Long press | Context menu with preview | Context menu or selection mode | More (ellipsis) button |
| Pull down | Refresh | Refresh | Refresh in menu or automatic |
| Pinch | Zoom | Zoom | Zoom buttons or double tap |
| Drag | Reorder, drag and drop | Same | Edit mode with handles |

- Every gesture-only action needs a visible control or menu item; gestures are accelerators.
- Never claim system edge gestures. Keep horizontal carousels and drawing canvases clear of edges or provide an explicit mode.
- Teach a gesture once in context (a hint the first time a list appears), then stop.
- Provide accessibility actions (VoiceOver custom actions, TalkBack custom actions) for every swipe action.

## Forms on mobile

- Correct keyboard per field (email, number pad, phone, URL), return key labeled with the next action, and content types for autofill (name, address, one-time code, new password) so passkeys and password managers work.
- One column, labels above fields, inline validation after the field loses focus, errors stated as fixes. Keep the primary button visible above the keyboard.
- Use native pickers for dates, times and short choice lists; avoid custom wheels.
