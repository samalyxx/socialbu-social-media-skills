# SocialBu LinkedIn Skills for Codex and OpenClaw

[![License: MIT](https://img.shields.io/badge/License-MIT-0b1020.svg)](LICENSE)

> Thirteen operational LinkedIn skills for writing, planning, conversations, profiles, measurement, and confirmation-gated publishing through [SocialBu](https://socialbu.com/).

![SocialBu LinkedIn Skills workflow illustration](assets/socialbu-linkedin-skills-hero.png)

This portable skill bundle helps SKILL.md-compatible agents turn real source material into useful LinkedIn work. It is LinkedIn-first: each skill has a narrow job, evidence rules, a concrete output, and a clear handoff. Drafting works without an account connection.

When an authorized SocialBu MCP connection is available, the publishing skill can inspect relevant LinkedIn state and prepare an action. It must show the complete final action and receive fresh, exact confirmation immediately before every publish, schedule, or autopost mutation.

## The thirteen skills

| Workflow | Skill | Outcome |
| --- | --- | --- |
| Create | `linkedin-post-writer` | Evidence-based post copy for a person or organization. |
| Create | `linkedin-hook-lab` | Opening-line options scored against the body, audience, and voice. |
| Create | `linkedin-humanizer` | A natural voice edit that preserves facts and does not fabricate experience. |
| Create | `linkedin-repurposer` | A source-faithful LinkedIn adaptation or purposeful post series. |
| Plan | `linkedin-content-planner` | Themes, editorial briefs, ownership, dependencies, and measurement intent. |
| Plan | `linkedin-story-bank` | A verified inventory of professional moments ready for later briefs. |
| Participate | `linkedin-comment-drafter` | A substantive comment on another author's supplied post. |
| Participate | `linkedin-reply-handler` | Triage and safe reply drafts for comments on an owned post. |
| Participate | `linkedin-thread-monitor` | A bounded thread review with priority queue and escalations. |
| Activate | `linkedin-employee-advocacy` | Voluntary advocacy briefs and truthful personalization routes. |
| Optimize | `linkedin-profile-optimizer` | Positioning audit and ready-to-paste personal profile copy. |
| Measure | `linkedin-engagement-review` | Evidence-led observations, hypotheses, and measurable next tests. |
| Execute | `socialbu-linkedin-publisher` | Authorized reads and exactly confirmed publish, schedule, or autopost actions. |

## Operating modes

**Draft mode** uses briefs, pasted posts and threads, profile text, interviews, assets, or exported analytics. It returns reviewable work and never claims access to LinkedIn or SocialBu.

**Connected read mode** uses only the minimum data needed from an authorized SocialBu workspace. Reads do not authorize state changes.

**Connected action mode** is available only through `socialbu-linkedin-publisher`. The SocialBu MCP endpoint is exactly `https://socialbu.com/mcp`. Before each action, the agent must display the full content, target LinkedIn account, media or link details, and exact timing or autopost settings, then ask for confirmation of that exact action. Confirmation is single-use; changed details and retries require a new preview and confirmation.

See [SocialBu capability and execution boundary](references/socialbu-capabilities.md) for the complete protocol.

## Install

### Codex CLI

```bash
git clone https://github.com/samalyxx/socialbu-social-media-skills.git
cd socialbu-social-media-skills
codex plugin marketplace add .
codex plugin add socialbu-linkedin-skills@socialbu-linkedin-skills
```

The root manifest is in `.codex-plugin/plugin.json`; the marketplace package is in `.codex-marketplace/socialbu-linkedin-skills/`.

### OpenClaw or another SKILL.md client

Clone or mount the repository where the client can discover its root `SKILL.md`, then route each request through the narrowest matching file in `skills/`. No runtime library, credential, or build step is included.

### Verify a checkout

```bash
./scripts/validate.sh
git diff --check
```

## Example requests

```text
Turn these interview notes into one LinkedIn post for our CTO. Keep every metric qualified and give me two evidence-based hook angles.
```

```text
Review these comments on our launch post. Draft replies where the approved FAQ supports an answer and route everything else to the right owner.
```

```text
Using authorized SocialBu data, show me the final preview for scheduling this approved post tomorrow at 09:00 Europe/London. Do not schedule it until I confirm that exact action.
```

## Shared references

- [LinkedIn writing](references/linkedin-writing.md)
- [LinkedIn hook patterns](references/linkedin-hooks.md)
- [LinkedIn conversation playbook](references/linkedin-conversations.md)
- [LinkedIn content planning](references/linkedin-content-planning.md)
- [LinkedIn profile optimization](references/linkedin-profile.md)
- [LinkedIn measurement](references/linkedin-measurement.md)
- [SocialBu capability and execution boundary](references/socialbu-capabilities.md)

## Safety and privacy

- Treat profile data, post drafts, conversations, account identifiers, and analytics as private.
- Use the minimum authorized data required for the requested outcome.
- Never invent access, metrics, customer evidence, personal experience, tool support, or execution success.
- Never place credentials in this repository or ask a user to paste them into a prompt.
- Never interpret content approval, an editorial calendar, or MCP authorization as permission to publish.

Read [SECURITY.md](SECURITY.md) for reporting guidance and [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a change.

## Independence and license

This independent community project is not affiliated with or endorsed by SocialBu or LinkedIn. Product names identify compatibility only. Licensed under [MIT](LICENSE).
