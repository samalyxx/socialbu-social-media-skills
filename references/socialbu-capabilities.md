# SocialBu capabilities reference

Use this file for product-boundary checks, not as a promise that every account, plan, or connected network has every feature.

## Publicly documented capabilities

- SocialBu provides publishing and scheduling, AI content generation, content curation, listening, a social inbox, automation, analytics, and collaboration. Source: [SocialBu product overview](https://socialbu.com/).
- The publishing workspace can prepare posts for multiple connected accounts, customize per-network settings, publish immediately, schedule, queue, save drafts, or use approval workflows where available. Source: [Publish](https://socialbu.com/publish) and [create and schedule posts](https://help.socialbu.com/en/articles/7733804-create-and-schedule-posts-in-socialbu).
- SocialBu MCP is an OAuth-authorized bridge for compatible clients. Its documented operations include posts, schedules, analytics, teams, accounts, automations, and curated content. Source: [MCP Server](https://socialbu.com/mcp-server). Endpoint: `https://socialbu.com/mcp`.
- The API covers publishing, account management, analytics, team collaboration, media, AI content, and more. Source: [SocialBu API](https://socialbu.com/api).

## Constraints to preserve

- Connected account options vary by network, account type, media, permissions, plan, and platform API rules.
- Never infer that an account is connected or a tool is available. Inspect authorized data or ask the user.
- Never claim a current price, plan limit, or network capability without checking the applicable SocialBu page. Product information changes.
- MCP authorization permits tool access; it does not replace user confirmation for consequential actions.
