---
name: linkedin-reply-handler
description: Triage comments on a person's or organization's LinkedIn post and draft safe, context-aware author replies. Use for owned-post conversations; use linkedin-comment-drafter for commenting on another author's post.
---

# LinkedIn reply handler

Help an author continue useful conversations while routing risk to the right human. Read [LinkedIn conversations](../../references/linkedin-conversations.md).

## Intake

Use the original post, the full available comment thread, the replying identity, approved facts, voice guidance, response objective, escalation rules, and ownership for product, support, legal, security, people, or crisis questions. Preserve identifiers so drafts stay attached to the correct comment.

## Workflow

1. Classify every in-scope comment using the conversation playbook.
2. Mark response need as `reply`, `react only`, `no response`, `hide/report recommendation`, or `escalate`.
3. Identify facts needed and whether a public response is appropriate.
4. Draft only what the approved context supports. Avoid turning praise or disagreement into a sales pitch.
5. Check the parent-child relationship so a reply does not answer the wrong person or repeat an earlier answer.
6. Assign an owner and priority to every escalation.

## Output

For each item, return `Comment ID`, `Author`, `Classification`, `Risk`, `Recommended action`, `Draft reply`, `Fact check`, and `Owner`. Then summarize `Open escalations` and `Coverage` so the user knows which comments were not included.

Do not reveal personal data, confirm private account information, accept liability, promise a refund or resolution, or imitate a named employee without their supplied voice and authorization. Drafting is not sending; this skill performs no external action.
