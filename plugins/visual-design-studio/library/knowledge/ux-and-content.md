# Design the task and the words together

Version-Timestamp: 2026-09-27 14:20:29 AST

Use when a page or flow is attractive but its purpose, next action or recovery is unclear. Inputs: actor/task/context evidence, service constraints, actual content, state behavior, current flow and allowed changes. This is original authored guidance; the miniature is fictional and not a usability study.

## Make the decision

1. Frame a task with a start condition and an observable completion condition. “Choose a pickup time and receive a confirmed reservation” is testable. “Feel engaged” needs further definition. Reuse the audience record selected under the existing contract. Do not invent personas, interviews, emotions or demographic preferences to make an empty record look complete.
2. Separate what is known about the task from what is known about the interface. A support log can reveal recurring questions but not prove which layout will fix them. Choose research or evaluation that can change the decision: observation for task obstacles, content testing for interpretation, or prototype tasks for competing flows. Record recruitment/sampling limits; a model walkthrough is an expert inspection, not a participant session.
3. Organize information around decisions the person must make. Place required terms before commitment, supporting detail where it answers a likely question, and advanced options where they do not hide the main task. Progressive disclosure saves attention only when the hidden information is not needed for the current decision. Keep navigation labels distinct and tied to actual destinations.
4. Define states and transitions before final copy. Include entry, incomplete input, loading, success, unavailable, error, cancellation and recovery where possible. Identify the real service effect of each action. When an external operation's outcome is unknown, the interface cannot safely turn uncertainty into “failed” and encourage an unverified retry.
5. Write message/action pairs. Say what happened, what remains possible and what the action will do. Match success copy to actual confirmation. Keep essential conditions visible rather than hiding them in reassurance. Use approved terminology, preserve variables and give translation enough context. Copy is part of behavior: changing an action label without changing the destination can make the flow less truthful.
6. Test realistic end-to-end tasks with relevant difficult content and states. Observe whether people can predict actions, understand errors and recover. Inspect keyboard/focus, announcements, narrow layouts and enlargement in implementation. Update the task model when behavior contradicts the assumption; do not only polish the sentence that exposed the problem.

## Worked miniature

Fictional community studio “Open Room” lets people reserve equipment. A prototype says “You're all set!” immediately after sending the request. The service contract actually returns a reservation only after confirmation. The proposed states become “Sending request,” “Reservation confirmed,” and “We could not confirm the result.” The final state presents only the safe recovery action supported by the real service contract; it does not invent a retry mechanism.

A test task asks a participant to reserve a tool and explain whether a reservation exists at each state. If access to participants or the service is unavailable, mark the candidate as an authored flow with untested comprehension and recovery, not as validated UX.

## Failure and repair

If navigation mirrors the company's departments but people cannot find tasks, compare a task-based hierarchy using the same content. If microcopy repeatedly compensates for confusing behavior, repair the state or action first. If every audience assertion is inferred, narrow the current use to the authorized exploration or hold the dependent decision under the audience contract.

## Handoff and limits

Use `ux` for task/state ownership and `content` for wording. Record selected UXD contracts, source-linked requirements and state transitions in the existing [UX deliverable](../templates/ux-deliverable.md); store exact message keys, variables and action destinations in [content work](../templates/content-work.md). Reuse [UX writing](../draft-skills/design-content-writing/references/ux.md).

Check reachable completion, relevant failure/recovery branches, copy/state consistency, content authority and actual evaluation evidence. A complete flow table does not prove safe service behavior, real-user comprehension, accessibility or production acceptance.
