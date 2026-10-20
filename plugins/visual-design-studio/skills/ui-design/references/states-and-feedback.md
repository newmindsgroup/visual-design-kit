# States and feedback

Version-Timestamp: 2026-10-20 02:04:32 UTC

Most of an interface's life is spent in states other than the ideal one: loading, empty, partly loaded, failed, offline, waiting for permission. Design each one on purpose, and give people feedback proportional to the wait and to the stakes.

## Response-time limits

Jakob Nielsen's three limits (*Usability Engineering*, 1993, building on Robert Miller, 1968, and Card, Robertson and Mackinlay, 1991):

| Response time | Perception | What to show |
| --- | --- | --- |
| Up to 0.1 s | Instant; the user caused it | The result itself; pressed state on the control |
| 0.1-1 s | Noticeable delay, flow kept | Pressed or busy state on the control; no spinner. If waits are often near 1 s, delay any indicator by about 300ms and, once shown, keep it at least 500ms so it does not flash (convention) |
| 1-10 s | Attention holds, but people want to know it is working | Skeleton for content areas; inline spinner with text for actions ("Saving..."); add what is happening after 2-3 s ("Checking availability") |
| Over 10 s | Attention breaks; people switch tasks | Determinate progress (percent or "Step 2 of 5"), a time estimate, Cancel, and the option to continue in the background with a notification when done |

The Doherty threshold adds a practical target: aim for system responses under 400ms to keep people productive.

## Skeletons, spinners, progress and optimistic UI

| Pattern | Use for | Rules |
| --- | --- | --- |
| Skeleton | Page or section loads where the layout is known | Match the final layout so nothing shifts (CLS); neutral blocks in `--color-bg-sunken`; gentle pulse of about 1.5-2 s, static under reduced motion; set `aria-busy="true"` on the region |
| Inline spinner | Actions inside a control (button, row, field) | 16-20px, next to or replacing the icon, with the label kept; lock the control's width |
| Page spinner | Rarely; unknown layout and short waits | Centered with text; prefer a skeleton |
| Determinate progress bar | Uploads, exports, imports, multi-step jobs | Percent or count, estimate, Cancel; `role="progressbar"` with `aria-valuenow` |
| Indeterminate bar | Background refresh of existing content | Thin bar at the top of the region; content stays usable |
| Optimistic update | Low-risk, high-success actions (like, star, reorder, toggle, mark read) | Show the result immediately; on failure revert and explain inline with Retry |

## Empty states

| Type | When | Content |
| --- | --- | --- |
| First use | Nothing created yet | What this area is for, one primary action, an optional secondary (import, template, sample data). A small illustration is optional |
| User cleared | Inbox zero, all tasks done | Brief acknowledgment; what happens next. No confetti for routine work |
| No results | Search or filters return nothing | The query and active filters, suggestions (check spelling, remove a filter), one-click "Clear filters" |
| No permission | User cannot see content | What is restricted, who can grant access, a "Request access" action |
| Error | Content failed to load | See errors below; not an empty state with a sad face |

Anatomy: heading (what), one sentence (why it is empty or what it will hold), primary action, optional link. Keep it inside the content area at the size of the content it replaces, not as a full-screen illustration.

## Errors by level

| Level | Example | Pattern |
| --- | --- | --- |
| Field | Invalid email | Inline message under the field; see [forms](forms.md) |
| Form | Several fields wrong on submit | Error summary at top with links; focus moved there |
| Section | One widget or panel failed | Inline error in that region with Retry; the rest of the page keeps working |
| Page | Page cannot load (404, 403, 500) | Full error page: plain explanation, search, links home and to help; correct HTTP status |
| System | Offline, outage, maintenance, degraded service | Persistent banner at the top of the app with status and what still works |
| Transaction with unknown outcome | Connection lost after paying | Say the outcome is unknown, show how to check (order history, email), block blind retry until status is confirmed |

Rules: keep user input; retry automatically with backoff for transient network errors before showing an error; give support a reference code after the human sentence; never show stack traces. Error copy follows `ux-design` [content design](../../ux-design/references/content-design.md).

**Offline:** banner "You're offline. Changes will sync when you reconnect." Queue edits locally where possible, mark unsynced items, and confirm when sync completes.

## Success

- Small actions: the result is the feedback (item appears, state changes), plus a toast when the effect is off-screen.
- Completed transactions (order, payment, booking, submission): a dedicated confirmation page or panel with a heading, reference number, what happens next and when, and a confirmation email.
- Milestones (first project shipped, course completed): a moment of celebration is fine; keep it short and respect `prefers-reduced-motion`. The ending shapes memory (peak-end rule).

## Choosing the feedback surface

| Surface | Use for | Do not use for | Persistence | Semantics |
| --- | --- | --- | --- | --- |
| Inline message | Field errors, section status, confirmations next to the action | Global events | Until resolved | Linked with `aria-describedby`; status text in a live region if it appears later |
| Toast (snackbar) | Brief confirmation of the user's own action, with at most one action such as Undo | Errors needing action, critical info, anything the user must read | Auto-dismiss after about 5-10 s (Material's snackbar guidance uses 4-10 s); pause on hover and focus; dismiss button | `role="status"` (polite); `--z-toast` |
| Banner | Persistent page or system status: trial ending, offline, maintenance, missing setup | Confirmations of routine actions | Until dismissed or resolved; critical ones not dismissible | Static text, or `role="status"` if inserted later; reserve space or overlay to avoid layout shift |
| Dialog | A decision the user must make before continuing (destructive confirm, unsaved changes) | Success messages, tips, marketing | Until the user decides | `role="dialog"` or `alertdialog` for urgent confirmations; focus trapped |
| Notification center | Events that happened while the user was elsewhere | Immediate feedback | Until read or cleared | Badge with accessible count |
| Badge | Counts or status on navigation | Explanations | Until resolved | Text alternative ("3 unread") |
| Push, email, SMS | Time-sensitive or out-of-app events the user opted into | Anything trivial | External | Respect preferences and quiet hours |

Toast rules: one line where possible, two at most; place bottom-center on phones (above any tab bar) and bottom-left or bottom-right on desktop; stack no more than 3; never the only path to an action, because a disappearing control fails people who need more time (WCAG 2.2.1); offer the same action elsewhere (Undo also in the item's menu, for example).

Use `role="alert"` (assertive) only for urgent, important messages: submission errors, session-expiry warnings, failed payments.

## Destructive and irreversible actions

1. **Prefer undo** for reversible deletes: act immediately, show "Deleted 'Q3 plan'. Undo" for 5-10 s, keep items in trash for a period (30 days is common).
2. **Confirm** irreversible actions in a dialog that names the object and the consequence: "Delete 'Q3 plan' permanently? Its 14 files will also be deleted." Buttons: "Delete permanently" (danger, primary) and "Cancel"; initial focus on Cancel for high-impact actions.
3. **Type to confirm** for the highest-impact actions (delete a workspace, a repository, all data): ask the user to type the name.
4. **Grace periods** for account and workspace deletion; see [flows](flows.md).

## Notifications

**Tier every notification:**

| Tier | Examples | Channels | Can user turn it off? |
| --- | --- | --- | --- |
| Critical / security | New sign-in, password change, payment failure | In-app, email (push, SMS optional) | No, but they can choose channels |
| Transactional | Order shipped, invoice paid, booking confirmed | Email, in-app, push if opted in | Rarely |
| Actionable | Mention, assignment, approval request, reply | In-app, push, email digest | Yes, per category |
| Informational | Status changes, weekly summary | In-app, digest | Yes |
| Promotional | Offers, product news | Email or push with explicit marketing consent | Yes, one click |

**Preferences:** a matrix of category by channel, digests (daily or weekly), quiet hours, per-thread mute, and "pause all" for a set period.

**In-app center:** bell with a count badge (cap "99+"), list grouped by Today, Earlier; each item says who did what to which object, with a deep link; mark read on open; "Mark all as read"; filters for mentions and assignments.

**Push permission:** never on first launch. Ask in context, after the person has seen value, with a pre-permission screen explaining the benefit ("Get notified when your order ships"), then trigger the OS prompt. Android 13 and later require a runtime notification permission; iOS shows its prompt once, so a declined prompt can only be reversed in Settings.

**Email:** marketing email needs a working unsubscribe; Gmail and Yahoo's bulk-sender rules (in force since 2024) require one-click unsubscribe for bulk senders. Confirm current requirements with each provider and counsel (CAN-SPAM in the US, GDPR and ePrivacy rules in the EU and UK).

**Content:** specific, actionable, no clickbait: "Dana assigned you 'Homepage copy', due Friday."

## Session timeouts

- Warn before expiry with at least 20 seconds to respond and a "Stay signed in" action (WCAG 2.2.1); a 2-minute warning is a common choice.
- Announce the warning with `role="alertdialog"`.
- After expiry, re-authenticate without losing entered data where possible, and return to the same place.
