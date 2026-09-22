# SocialBu capability and execution boundary

Use this file before making a SocialBu-specific claim or using SocialBu MCP. It records public product boundaries, not a promise that a particular workspace, plan, LinkedIn account, or tool exposes every capability.

## Documented product surface

- SocialBu publicly describes publishing and scheduling, content creation and curation, a social inbox, monitoring, analytics, collaboration, and automations. Source: [SocialBu](https://socialbu.com/).
- Publishing options can include immediate publishing, scheduling, queues, drafts, network-specific settings, and approval workflows where available. Sources: [Publish](https://socialbu.com/publish) and [create and schedule posts](https://help.socialbu.com/en/articles/7733804-create-and-schedule-posts-in-socialbu).
- SocialBu MCP is an OAuth-authorized bridge for compatible clients. The connection endpoint for this bundle is exactly `https://socialbu.com/mcp`. Public documentation: [SocialBu MCP](https://socialbu.com/mcp-server).

Product behavior can vary by plan, workspace role, connected network and account type, media, permissions, platform APIs, and the MCP tools currently exposed. Inspect the live tool schema and authorized workspace before relying on a capability. Do not guess prices, limits, support, account access, identifiers, or current platform constraints.

## Operating modes

**Draft mode:** Use user-provided briefs, text, exports, screenshots, or metrics. Return drafts and recommendations without claiming account access.

**Connected read mode:** With an authorized MCP connection, perform only the minimum read needed for the request. Reads can include listing or inspecting available accounts, posts, schedules, threads, and analytics when exposed by the live schema. Treat returned data as private.

**Connected action mode:** Publishing, scheduling, or enabling an autopost behavior is an external state change. Authorization to connect or read is not authorization to mutate.

## Exact-action confirmation protocol

Immediately before every publish, schedule, or autopost action:

1. Inspect the current tool schema and resolve the exact target account; never infer either.
2. Present a final preview containing the full content, media or link details, target LinkedIn account, action type, and exact scheduled date, time, and timezone when relevant.
3. State any unresolved limitation or ambiguity.
4. Ask the user to confirm that exact action. Confirmation must be an unambiguous affirmative response after the preview and in the same conversational context.
5. Execute once, then report the returned status and identifier without exposing credentials.

A request to draft, a general instruction such as “handle publishing,” approval of an earlier version, or a confirmation given before content, account, action, or timing changed is not valid execution confirmation. Each distinct action needs its own confirmation; never use blanket confirmation for a batch. If a call fails or its outcome is unclear, do not retry a state change without showing the current state and obtaining fresh confirmation.

Do not request, store, log, or expose OAuth tokens, session cookies, API keys, or other credentials. This repository contains instructions only and must not add a SocialBu client library or custom product integration.
