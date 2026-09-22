# SocialBu Social Media Skills for Codex and OpenClaw

[![License: MIT](https://img.shields.io/badge/License-MIT-0b1020.svg)](LICENSE)

> A practical, safety-first collection of AI agent skills for social media planning, content creation, scheduling, engagement, reporting, and automation with [SocialBu](https://socialbu.com/).

![Abstract illustration of a connected social media workflow](assets/socialbu-skills-hero.png)

SocialBu Social Media Skills helps Codex, OpenClaw, and other SKILL.md-compatible agents turn a social media brief into useful drafts, calendars, inbox triage, analytics reviews, and automation plans. When [SocialBu MCP](https://socialbu.com/mcp-server) is connected, the agent can also work with authorized SocialBu data and tools. Nothing publishes, schedules, edits, deletes, approves, or changes an automation without the user's explicit confirmation.

## Contents

- [What this is](#what-this-is)
- [Skills](#skills)
- [Install](#install)
- [How it works](#how-it-works)
- [Safety and privacy](#safety-and-privacy)
- [FAQ](#faq)
- [Contributing](#contributing)

## What this is

This is an open-source **social media management skill bundle**, not a SocialBu replacement or an unofficial API client. It adds structured agent instructions around real marketing work: writing social posts, planning a content calendar, repurposing source material, replying to conversations, monitoring topics, reviewing social media analytics, and designing repeatable social media automation.

It works in two modes:

1. **Draft mode** — provide your brief, exported data, or copied conversations. The skills return reviewable output without connecting to an account.
2. **Connected mode** — authorize [SocialBu MCP](https://socialbu.com/mcp-server) in a compatible client. The agent can inspect authorized SocialBu resources and prepare actions; state-changing actions remain confirmation-gated.

## Skills

| Skill | Use it for |
| --- | --- |
| `social-post-writer` | Platform-aware post and caption drafts from a clear brief. |
| `content-calendar` | A realistic content calendar with themes, objectives, and production notes. |
| `post-repurposer` | Rework approved source content for another social channel. |
| `engagement-inbox` | Triage messages and comments, then draft helpful replies. |
| `social-listening` | Turn a keyword or mention brief into a listening review. |
| `analytics-review` | Explain post and account metrics, patterns, and next tests. |
| `workflow-automation` | Design reviewable SocialBu workflow automation ideas. |
| `approval-workflow` | Build an editorial review and approval process for a team. |
| `socialbu-mcp-operator` | Safely inspect or operate SocialBu MCP tools after authorization. |

## Install

### Codex CLI

```bash
git clone https://github.com/samalyxx/socialbu-social-media-skills.git
cd socialbu-social-media-skills
codex plugin marketplace add .
codex plugin add socialbu-social-media-skills@socialbu-social-media-skills
```

For a local checkout, use the same commands from the repository root. The plugin metadata is in `.codex-plugin/plugin.json`; the marketplace copy is included for distribution compatibility.

### OpenClaw

Clone or mount this repository in an OpenClaw workspace. Add an instruction such as:

```text
For SocialBu work, read the relevant socialbu-social-media-skills/skills/*/SKILL.md first.
Use SocialBu MCP only after the user has authorized it. Require explicit confirmation before every state-changing action.
```

To connect an MCP-compatible client, use the SocialBu MCP endpoint: `https://socialbu.com/mcp`. Review the [SocialBu MCP guide](https://socialbu.com/mcp-server) for current connection steps.

### Verify a checkout

```bash
./scripts/validate.sh
```

No runtime dependencies, API keys, or build step are required.

## How it works

Start with an outcome and source material. For example:

```text
Create a two-week LinkedIn and Instagram content calendar for our product launch.
Audience: independent retail owners. Goal: qualified demo requests.
Use our brand voice: direct, practical, no hype.
```

Or, with connected SocialBu MCP:

```text
Review our next seven days of scheduled posts. Identify coverage gaps and draft replacements. Do not schedule anything yet.
```

The skills prefer evidence over generic advice. They name missing inputs, distinguish a draft from an executed action, and tailor output to the requested social platform. See [SocialBu capabilities](references/socialbu-capabilities.md) and [content quality guidance](references/content-quality.md).

## Safety and privacy

- Treat account data, conversations, and analytics as private.
- Use the minimum authorized data needed for the requested task.
- Present a preview and request explicit confirmation before publishing, scheduling, editing, deleting, approving, rejecting, changing accounts, or toggling automations.
- Never invent metrics, platform support, account access, or results.
- Draft mode works without credentials; do not place secrets in this repository.

## FAQ

### Does this publish posts automatically?

No. It can draft a publishing plan. With authorized SocialBu MCP, it can prepare an action, but the operator skill requires a clear confirmation immediately before any state change.

### Do I need a SocialBu account?

No for draft mode. You need a SocialBu account and an MCP-compatible client only to access connected SocialBu workspaces. Product availability and plan limits can change; consult [SocialBu](https://socialbu.com/) and the [Help Center](https://help.socialbu.com/).

### Which platforms does it support?

The writing and planning skills can draft for any named channel. Connected functionality depends on the accounts and capabilities available in the user's SocialBu workspace; see the [capabilities reference](references/socialbu-capabilities.md).

### Is this affiliated with SocialBu?

No. This is an independent community project. “SocialBu” is used only to describe interoperability with the SocialBu product.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md), keep instructions concrete, and run `./scripts/validate.sh` before opening a pull request.

## License and attribution

Licensed under [MIT](LICENSE). This project is independently authored and was informed by SocialBu's public product and documentation pages, linked in [references/socialbu-capabilities.md](references/socialbu-capabilities.md).
