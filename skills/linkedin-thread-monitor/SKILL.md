---
name: linkedin-thread-monitor
description: Review supplied or authorized LinkedIn post threads for unanswered questions, risk, lead signals, and response opportunities. Use for thread-level triage and handoff, not general social listening.
---

# LinkedIn thread monitor

Turn a bounded set of LinkedIn comments into an auditable action queue. Read [LinkedIn conversations](../../references/linkedin-conversations.md). Use `linkedin-reply-handler` after triage when full reply drafting is requested.

## Scope

Establish the post or thread identifiers, account, monitoring window, last-reviewed point, objective, escalation policy, owners, and whether the source is pasted data, an export, or an authorized connection. State any pagination, missing replies, deleted content, or timestamp limitations.

## Workflow

1. Record coverage and normalize each item to its parent comment where the source allows.
2. Separate new activity from previously reviewed items; do not infer that an absent item was deleted.
3. Classify items and assign `low`, `medium`, `high`, or `urgent` risk with a short reason tied to the escalation policy.
4. Flag unanswered factual questions, corrections, complaints, lead signals, substantive additions, spam, and abuse.
5. Detect duplicates and threads already resolved by the author or another participant.
6. Recommend the next action, owner, and response deadline or review order. Draft only a brief holding response when explicitly requested and adequately supported.

## Output

Return:

- `Coverage` — sources, identifiers, window, item count, and limitations;
- `Priority queue` — item, context, classification, risk, recommended action, owner, and status;
- `Themes` — recurring questions or misconceptions grounded in cited items;
- `Escalations` — exact reason and required decision;
- `Next checkpoint` — what should be reviewed next, without claiming continuous monitoring.

This skill is read-only. Never claim to watch a thread after the response ends, and never send, hide, report, or delete a comment.
