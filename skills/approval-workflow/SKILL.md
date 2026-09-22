---
name: approval-workflow
description: Define a practical social content review and approval workflow.
---

# Approval workflow

## Inputs
Get roles, content types, regulated or sensitive topics, lead time, required reviewers, escalation path, and publishing cadence.

## Workflow
1. Map only the roles needed to author, review, approve, and publish.
2. Specify a clear entry criterion, approval decision, revision loop, and deadline.
3. Make exceptions visible instead of silently bypassing review.
4. Recommend a light audit trail: owner, status, date, and decision rationale.

## Output
Return `Workflow`, `Roles`, `Approval criteria`, `Escalations`, and `Operating checklist`. This skill designs process only. It must not approve or reject SocialBu posts unless the user uses the MCP operator and confirms the exact action.
