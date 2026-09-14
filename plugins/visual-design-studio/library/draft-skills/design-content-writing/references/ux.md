# UX writing

Version-Timestamp: 2026-09-08 15:36:02 AST

Begin with the actual task and state model; use UXD-22 for message records. Inventory only applicable labels, navigation, hints, validation, empty/loading/success/error states, confirmations, permission/access restrictions, onboarding, search/no-results, notifications, cancellation, deletion, privacy, timeout/session reset, offline and recovery.

For every message record its trigger, conditions, message key, visible copy, accessible wording, variables with types/examples, action and expected next state. Success requires the system's actual confirmation. A timeout may mean outcome unknown, not failed. Preserve data and avoid implying retry is safe when a duplicate action is possible. Keep sensitive data out of public/shared-screen messages.

Keep labels specific and consistent with actions. Explain recoverable mistakes without blame; do not use persuasion or jokes where they obscure consequences. Separate user-input fixes from service failure or eligibility. Consent and destructive actions must communicate real consequences and available choices; specialist review applies where needed.

Specify pluralization, dates/numbers, locale, translation context, variable escaping ownership and expansion constraints; never concatenate fragments that break meaning in translation. Reuse approved terminology. Check accessible names against visible labels and inspect actual focus/status announcements in implementation. No copy-only accessibility certification.

Handoff: stable message keys and state/requirement IDs to component specifications, localization and implementation tests. A changed trigger or action invalidates affected strings and checks.
