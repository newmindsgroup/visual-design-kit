# AI interfaces: chat, assistants and agents

Version-Timestamp: 2026-10-20 02:04:32 UTC

A good AI interface makes three things obvious at all times: what the system is doing, what it based its answer on, and what it will do next with the user's permission. Speed, control and honesty about uncertainty matter more than a clever persona.

Public guidance worth reading alongside this file: Microsoft's 18 Guidelines for Human-AI Interaction (Amershi and colleagues, CHI 2019, HAX Toolkit), Google PAIR's *People + AI Guidebook*, Apple's Human Interface Guidelines on machine learning and generative AI, IBM Carbon for AI (the AI label pattern), and Emily Campbell's *Shape of AI* pattern catalog. Query `industry.ai-products` in the atlas for category conventions and clichés.

## Layout defaults

| Element | Default |
| --- | --- |
| Conversation column | Assistant text at `--measure-body` (66ch) max; full-width blocks for code, tables and media |
| User messages | Visually distinct (aligned end or tinted `--color-bg-sunken`), with Edit on hover and focus |
| Assistant messages | Plain prose on the canvas (no bubble), rendered Markdown: headings, lists, tables, code blocks with language label and Copy |
| Composer | Pinned to the bottom, multi-line, grows to about 40% of the viewport then scrolls; attachments, model or mode picker and Send in one row |
| Send key | Enter sends and Shift+Enter adds a line on desktop; on touch keyboards, Return adds a line and the Send button sends; make it configurable |
| Side panel | Artifacts, canvas, sources or agent progress open in a resizable panel on desktop (40-60% width) and full screen on mobile |
| Message actions | Copy, Regenerate (last response), Edit (user turn), feedback, Share; visible on hover and focus, always on touch |

## Streaming

- Show the first output fast. If the first token takes more than about 1 s, show a working state immediately ("Thinking", "Searching") so the request feels received.
- Stream into a stable layout: no jumping when Markdown blocks close. Render an unfinished code fence as a code block and complete it when it closes.
- Auto-scroll only while the user is at the bottom. If they scroll up, stop following and show a "Jump to latest" button.
- **Stop** replaces Send during generation, in the same position, reachable by keyboard (Esc in the composer is a common shortcut). After stopping, keep the partial answer and mark it "Stopped".
- Do not fake typing with character-by-character animation beyond the real stream; under `prefers-reduced-motion`, render in larger chunks.
- Screen readers: do not announce every token. Mark the message container `aria-busy="true"` while streaming and announce once when complete ("Response complete"), or by paragraph; keep focus in the composer.

## Regenerate, edit and branches

- **Regenerate** produces a new version of the last answer; show versions as "2 / 3" with previous and next controls rather than discarding the old one.
- **Edit** a user message to fork the conversation from that point; keep the original branch reachable.
- **Retry** after an error resends the same prompt; the user's text is never lost.
- Offer quick modifiers where they help ("Shorter", "More formal", "Explain simply"), as chips under the answer.

## Citations and sources

- Cite at the claim, not only at the end: numbered inline markers ([1]) or underlined phrases that link to sources.
- A sources list or panel shows title, publisher or domain, date, and a favicon; hovering or focusing a citation previews the quoted passage.
- Distinguish where content came from: retrieved documents, the user's files, web search, tool output, or the model's own knowledge. Label uncited claims as unsourced when sourcing is expected.
- Show search activity briefly ("Searched 6 sites") and let people expand it.
- Never fabricate citations; if retrieval failed, say so.

## Uncertainty and limits

- Express uncertainty in words tied to the reason ("I couldn't find this in the contract; the closest clause is 7.2") rather than a numeric confidence score users cannot interpret.
- Flag high-stakes domains (medical, legal, financial, safety) with a short, specific note and a route to a qualified human, not boilerplate on every answer.
- State capability limits in the empty state and when a request falls outside them.
- Avoid anthropomorphic claims ("I feel", "I understand you") that overstate what the system is.

## Tool calls and progress

- Each tool step appears as a compact status line with an icon and a verb in progress: "Searching the web", "Reading 5 pages", "Running code", "Querying sales_2026". Completed steps collapse to a summary; details (inputs, outputs, logs) expand on demand.
- Long-running agent tasks show a plan (numbered steps), the current step, elapsed time, and controls to pause, stop or redirect.
- Background work: let people leave and come back; notify on completion or when input is needed; show a task list of running and finished jobs.
- Errors in a step say which step failed and what the agent will do (retry, skip, ask).

## Approvals for agent actions

Classify every action the agent can take:

| Class | Examples | Default |
| --- | --- | --- |
| Read-only, internal | Search the user's documents, read a page, run analysis in a sandbox | Run without asking; log it |
| Reversible write | Draft an email, create a document, edit a file with version history | Run or ask per user setting; show the result with Undo |
| External or irreversible | Send email or messages, publish, purchase, pay, delete, change permissions, submit forms, run commands outside a sandbox | Always ask before running |
| Sensitive data use | Share personal data with a third-party tool | Ask, naming the data and the recipient |

**Approval card anatomy:** what will happen in plain words ("Send this email to 14 recipients"), the exact target and parameters (recipients, amount, file paths), a preview or diff of the change, the cost if any, and buttons: **Approve**, **Edit**, **Deny** (with optional feedback). "Always allow this kind of action" is an explicit, separate choice, never pre-selected, and revocable in settings.

Keep an activity log of everything the agent did, with timestamps, inputs and outcomes, and undo or rollback where the system allows it. Dry-run previews beat after-the-fact apologies.

## Artifacts and canvas

- Persistent outputs (documents, code, designs, data tables, app previews) open in a side panel or canvas, separate from the chat stream.
- The artifact has its own title, version history (v1, v2 with diff), copy, download and share actions.
- Users can edit directly and ask for changes to a selected part ("Rewrite this paragraph"); the assistant's edits show as tracked changes or a diff.
- Live previews of generated code run in a sandbox and say so.

## Feedback

- Thumbs up and down on each response; a down vote opens optional reasons (inaccurate, unhelpful, unsafe, other) and a comment field. Never block the conversation.
- Say what happens to feedback and whether the conversation is shared with reviewers.
- Close the loop where possible: "Thanks; we'll use this to improve answers about billing."

## Suggestions and empty state

- Empty state: one line on what the assistant can do here, 3-4 starter prompts specific to the product and the user's context (their recent files, their role), and a short note on limits and data use.
- Follow-up suggestions after an answer: 2-3 chips that continue the task, not generic prompts.
- Avoid the generic AI look: a sparkle icon, a purple gradient and "How can I help you today?" say nothing about the product. Name the concrete jobs instead ("Summarize this week's support tickets").

## Errors, limits and outages

| Situation | Message pattern |
| --- | --- |
| Network drop mid-stream | Keep the partial answer; "Connection lost. Retry" resumes or regenerates |
| Rate or usage limit | Say which limit, when it resets in local time, and what remains available ("You've reached the limit for this model. You can send more messages at 3:40 PM, or switch to the standard model now.") |
| Model fallback | Tell the user when a different model answered |
| Context too long | Explain plainly and offer to start a new conversation with a summary |
| Request declined | Say briefly what cannot be done and offer what can, without lecturing |
| Tool or integration failure | Name the integration and the fix ("Reconnect Google Drive") |

Never lose the user's prompt or attachments on any error.

## Memory and privacy disclosure

- Show when memory is used ("Using what you told me about your team") and when it is saved ("Memory updated"), with a link to view, edit or delete memories.
- A memory management page lists what is remembered, with delete per item and "Delete all".
- Offer temporary or incognito chats that are not saved to history or memory, and state the retention period for normal chats.
- State whether conversations are used to train models and provide the opt-out in settings, not only in a policy.
- Show which connected sources (email, files, calendars) a conversation can access, and let users limit them per conversation.
- **Disclosure that it is AI:** the EU AI Act's Article 50 transparency obligations (applying from 2 August 2026) require that people are told they are interacting with an AI system unless that is obvious, and that AI-generated or manipulated content is marked; details for marking synthetic content may phase in later. Label AI-generated content in the UI and in exported files. Confirm requirements with counsel for the specific product and jurisdiction.

## Human handoff

- Offer "Talk to a person" whenever the user asks, when the assistant cannot resolve the issue after 2-3 attempts, or when the topic needs a human (complaints, account security, bereavement, safety).
- Transfer the conversation context so the user does not repeat themselves (WCAG 3.3.7 applies in spirit).
- Show the expected wait or the hours when humans are available, and the channel (chat, callback, email).
- Never present a bot as a human; label agent and human messages distinctly.

## Input and attachments

- Drag-and-drop and a paperclip button; files appear as chips with name, type, size, upload progress and remove.
- State accepted types and limits before upload.
- Voice input with a visible recording state and a transcript the user can edit before sending.
- Show a character or token counter only near the limit.

## Accessibility checklist for chat

- Conversation history uses a list or `role="log"` region with headings or labels per message ("You said", "Assistant said").
- Streaming announcement as above; Stop button reachable and labeled.
- All message actions keyboard reachable; focus order composer, then messages from newest.
- Code blocks are real `pre` and `code` elements; Copy announces "Copied".
- Contrast and target sizes follow [accessibility](accessibility.md).
