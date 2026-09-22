# LinkedIn Skills for Claude Code and Codex

[![Release](https://img.shields.io/github/v/release/samalyxx/linkedin-skills?display_name=release&color=1D4ED8)](https://github.com/samalyxx/linkedin-skills/releases)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-7C3AED.svg)](.claude-plugin/plugin.json)
[![Codex](https://img.shields.io/badge/Codex-compatible-0A66C2.svg)](.codex-plugin/plugin.json)
[![Skills](https://img.shields.io/badge/Agent-Skills-334155.svg)](SKILL.md)
[![SocialBu MCP](https://img.shields.io/badge/SocialBu-MCP_optional-2563EB.svg)](https://socialbu.com/mcp-server)
[![License](https://img.shields.io/badge/license-MIT-22C55E.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/samalyxx/linkedin-skills?style=flat&logo=github)](https://github.com/samalyxx/linkedin-skills/stargazers)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-F59E0B.svg)](CONTRIBUTING.md)

**LinkedIn Skills** is a practical, draft-first LinkedIn marketing bundle for Claude Code and Codex. It helps you turn real source material into credible posts, comments, replies, plans, profile improvements, and reviewable experiments—without inventing results or claiming LinkedIn access.

![LinkedIn Skills workflow: write, engage, plan, review, approve, schedule](assets/linkedin-skills-overview.png)

## What you can do

Once installed, ask in plain language. The relevant skill handles the workflow.

- **Write a post:** “Turn these verified product notes into a LinkedIn post for a B2B founder.”
- **Comment thoughtfully:** “Draft a useful comment on this supplied post; add one supported point.”
- **Improve a draft:** “Humanize this copy without changing its claims.”
- **Plan content:** “Create a 7-day LinkedIn plan for a cybersecurity consultant.”
- **Review a profile:** “Audit this LinkedIn profile for positioning and credibility.”
- **Learn from results:** “Analyze this engagement export; separate findings from guesses.”

## Install

Choose the route that matches your agent. The repository is public and the skills work without an API key.

### Codex CLI

```bash
codex plugin marketplace add samalyxx/linkedin-skills
codex plugin add linkedin-skills@linkedin-skills
```

For a local checkout:

```bash
git clone https://github.com/samalyxx/linkedin-skills.git
cd linkedin-skills
codex plugin marketplace add .
codex plugin add linkedin-skills@linkedin-skills
```

### Claude Code

If your Claude Code version exposes plugin commands, add the marketplace and install the bundle:

```text
/plugin marketplace add samalyxx/linkedin-skills
/plugin install linkedin-skills@linkedin-skills
```

If plugin commands are unavailable, clone the repository into your working directory. Claude Code can read the canonical [`skills/`](skills/) instructions directly.

### Claude web or desktop

1. Open **Customize** and then **Plugins**.
2. Add a marketplace from the repository `samalyxx/linkedin-skills`.
3. Find **LinkedIn Skills** in the marketplace and install it.
4. Start a new chat and request a LinkedIn task in normal language.

### Any SKILL.md-compatible agent

```bash
npx skills add samalyxx/linkedin-skills
```

Or clone the repository where your agent discovers `SKILL.md` files.

## The 12 skills

| Skill | Outcome |
| --- | --- |
| Post writer | Evidence-led post draft with a clear audience, angle, and claim boundary. |
| Comment drafter | A substantive comment grounded in the supplied post. |
| Reply handler | Safe, owner-aware reply drafts for comments on your post. |
| Humanizer | Voice edit that retains facts and does not fabricate experience. |
| Hook extractor | Opening-angle options that connect honestly to the body. |
| Content planner | Editorial themes, briefs, owners, and measurable experiments. |
| Profile optimizer | Positioning review and ready-to-edit profile suggestions. |
| Repurposer | Source-faithful LinkedIn adaptation or post series. |
| Employee advocacy | Voluntary advocacy briefs with truthful personalization. |
| Thread monitor | Bounded thread triage, priorities, and escalation routes. |
| Engager analytics | Observations, hypotheses, and next tests from supplied data. |
| Interviewer | Structured story capture from real professional experiences. |

## Optional: schedule or publish with SocialBu

By default, **LinkedIn Skills drafts content for you to review and copy into LinkedIn**. No SocialBu account is required. If you want an MCP-compatible agent to help schedule or publish after your review, connect [SocialBu](https://socialbu.com/publish) as the optional execution layer.

### What SocialBu adds

SocialBu provides the account and publishing workspace. Through its [MCP server](https://socialbu.com/mcp-server), a connected assistant can create drafts, inspect planned posts, prepare approval-pending posts, schedule posts, or publish immediately. LinkedIn Skills remains the writing and review layer: it selects an angle, creates the draft, checks claims, and presents the action for approval.

### Set up SocialBu

1. Sign in to SocialBu, open **Accounts**, then select **Add** or **View all platforms**.
2. Choose **LinkedIn** and authorize the profile, organization, or brand you actually intend to use. Confirm that the selected account appears in SocialBu before scheduling anything.
3. In Claude, Codex, OpenClaw, or another MCP-compatible client, add the SocialBu MCP server:

   ```text
   https://socialbu.com/mcp
   ```

4. Complete SocialBu's OAuth sign-in in your own browser. Do not paste credentials into a chat, prompt, or repository.
5. Ask for a draft first, then request a schedule or publish action only when the post is final.

SocialBu also works without MCP: use the draft from this bundle in the SocialBu Publish or Calendar screens and schedule it manually. See SocialBu's official [account connection guide](https://help.socialbu.com/en/help/articles/8734070-how-to-connect-your-social-media-accounts-to-socialbu) for platform authorization details.

### Approval is required every time

Before any SocialBu action, LinkedIn Skills must present an approval card with the exact:

- LinkedIn profile, organization, or brand;
- final text, links, and media;
- action: **save draft**, **schedule**, or **publish now**; and
- scheduled date, time, and timezone when applicable.

It may execute only after a new confirmation for that unchanged preview. Editing the text, account, media, action, or time invalidates approval and requires a new confirmation. The bundle does not scrape LinkedIn, store credentials, or publish by default. See [the publishing boundary](references/socialbu-publishing.md).

## Verify a checkout

```bash
./scripts/validate.sh
python3 -m unittest discover -s tests
python3 scripts/selftest.py
```

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md), [CLAUDE.md](CLAUDE.md), and [SECURITY.md](SECURITY.md). This independent project is not affiliated with LinkedIn, Claude, Codex, or SocialBu.

## Related open-source skill bundles

Part of a family of draft-first social-media skill bundles for Claude Code and Codex. Each bundle is platform-specific, keeps publishing optional, and uses the same fresh-approval rule when SocialBu is connected.

- [**LinkedIn Skills**](https://github.com/samalyxx/linkedin-skills) — LinkedIn posts, profile work, professional engagement, and planning.
- [**X Skills**](https://github.com/samalyxx/x-skills) — concise posts, threads, replies, and conversation planning.
- [**Instagram Skills**](https://github.com/samalyxx/instagram-skills) — visual briefs, captions, carousels, Reels concepts, and community replies.
- [**YouTube Skills**](https://github.com/samalyxx/youtube-skills) — video concepts, titles, descriptions, community posts, and channel planning.
- [**Threads Skills**](https://github.com/samalyxx/threads-skills) — conversational posts, replies, series, and topic plans.
- [**TikTok Skills**](https://github.com/samalyxx/tiktok-skills) — short-form concepts, hooks, scripts, captions, and community responses.
- [**Facebook Skills**](https://github.com/samalyxx/facebook-skills) — Page posts, community management, event promotion, and content planning.
