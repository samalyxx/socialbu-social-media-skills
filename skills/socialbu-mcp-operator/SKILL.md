---
name: socialbu-mcp-operator
description: Safely inspect and operate an authorized SocialBu MCP workspace with confirmation-gated state changes.
---

# SocialBu MCP operator

## Scope
Use only after the user has authorized a compatible MCP client to access SocialBu. Consult `references/socialbu-capabilities.md` and the available tool schema. Never claim a tool, account, or permission exists before inspection.

## Read operations
For listing accounts, posts, schedules, analytics, teams, curated items, or automation details: state the scope, perform the minimum read, summarize the result, and distinguish facts from recommendations. No confirmation is needed for a read that matches the user's request.

## State-changing operations
State changes include creating, editing, scheduling, publishing, deleting, approving, rejecting, connecting/removing/updating accounts, and enabling/disabling or modifying automations.

Before every state change:
1. Show the exact target, content or settings, accounts, timezone/time, and intended outcome.
2. Ask one direct confirmation question naming that exact action.
3. Execute only after an unambiguous affirmative response in the same conversational context.
4. Report the result and any returned identifier. If execution fails or is ambiguous, stop and explain.

Never treat an earlier generic request such as “schedule this” as confirmation after the proposed details change. Never bulk-act on unspecified items. Never expose tokens or OAuth data.
