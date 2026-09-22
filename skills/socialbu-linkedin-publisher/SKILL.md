---
name: socialbu-linkedin-publisher
description: Inspect authorized LinkedIn publishing state and, only after a final preview plus fresh exact-action confirmation, publish, schedule, or configure autopost through SocialBu MCP. Use only for explicit connected execution requests.
---

# SocialBu LinkedIn publisher

Use SocialBu MCP at exactly `https://socialbu.com/mcp` for authorized LinkedIn publishing operations. Read [SocialBu capability and execution boundary](../../references/socialbu-capabilities.md) before any tool use. This skill is the only skill in this bundle allowed to publish, schedule, or change autopost state.

## Preconditions

- The user explicitly requested a connected SocialBu operation.
- A compatible client has an authorized SocialBu MCP connection.
- The live tool schema exposes the needed operation.
- The target resolves to an authorized LinkedIn account. Never select an account from display name alone when an identifier is available.

If any precondition fails, remain in draft mode and explain what is missing. Never ask the user to paste a token, cookie, API key, or OAuth secret.

## Reads

Read-only inspection of authorized accounts, drafts, schedules, posts, or tool capabilities does not require confirmation when it is necessary for the user's request. State the read scope and retrieve the minimum data needed. A read must not trigger creation, mutation, or publication.

## Prepare the exact action

Resolve and display a final preview with:

- action: `publish now`, `schedule`, or the exact autopost create, update, enable, or disable operation;
- target LinkedIn account name and stable identifier;
- full final post text;
- media, document, link, mention, and accessibility details supplied to the tool;
- for scheduling, the exact date, time, timezone, and resulting timestamp;
- for autopost, the source, trigger, filters, transformation, target, cadence, start state, and failure behavior;
- any tool limitation, ambiguity, or missing optional setting.

Do not abbreviate the content in the confirmation preview or substitute an earlier draft.

## Confirmation gate

Immediately before every state-changing call, ask one direct question that names the exact action and target shown in the final preview. Execute only after the user gives an unambiguous affirmative response to that preview in the same conversational context.

The following never count as confirmation: connecting MCP, asking for a draft, asking to prepare an action, approving a content plan, a general instruction to manage publishing, or approval of a version whose content, account, media, timing, or settings later changed.

Confirmation is single-use and action-specific. Obtain separate confirmation for each post, account, schedule, or autopost mutation. Never infer blanket approval, and never enable autopost by default.

## Execute and report

1. Recheck that the preview still matches the pending tool arguments.
2. Make one state-changing call.
3. Report the returned status, target, effective time and timezone, and identifier.
4. If the call fails or the result is ambiguous, stop. Inspect read-only state when available, show the user what is known, and obtain fresh confirmation before any retry that could duplicate or alter content.

Do not silently change copy, time, account, media, or autopost settings to satisfy a tool error. Do not claim success unless the tool response establishes it.
