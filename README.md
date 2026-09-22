# LinkedIn Skills

An installable, LinkedIn-first skill bundle for Codex and Claude. It turns verified source material into posts, comments, replies, plans, profile improvements, and measurement reviews—without pretending to have LinkedIn access.

![LinkedIn Skills hero](assets/linkedin-skills-hero.png)

## What it includes

Twelve narrow workflows: post writer, comment drafter, reply handler, humanizer, hook extractor, content planner, profile optimizer, repurposer, employee advocacy, thread monitor, engager analytics, and interviewer. Each skill defines the information it needs, an operating sequence, quality gates, and a reviewable output.

![Draft-to-approval workflow](assets/linkedin-skills-workflow.png)

## Draft-first workflow

1. Choose the narrowest skill in [SKILL.md](SKILL.md).
2. Supply source notes, the intended audience, objective, and any approved claims.
3. Review the structured draft and quality checks.
4. Copy it to LinkedIn, or use the optional SocialBu MCP connection after a fresh action-specific confirmation.

The bundle always works in draft mode. It does not scrape LinkedIn, store accounts, or include credentials.

## Install

### Codex

```bash
git clone https://github.com/samalyxx/socialbu-social-media-skills.git
cd socialbu-social-media-skills
codex plugin marketplace add .
codex plugin add linkedin-skills@linkedin-skills
```

The Codex manifest is [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json). The repository marketplace package is in [`.codex-marketplace/linkedin-skills`](.codex-marketplace/linkedin-skills).

### Claude Code

Clone this repository, then add it as a local Claude plugin using [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json). Claude discovers the same canonical skill source in [`skills/`](skills/); the compatibility index is [`.claude/skills/README.md`](.claude/skills/README.md).

## Optional SocialBu publishing

SocialBu is an optional execution layer, not part of this product's name or skill taxonomy. Connect a compatible client to `https://socialbu.com/mcp` only if you want to schedule or publish LinkedIn content.

Before a state-changing call, show the exact final post, LinkedIn account, media/link details, and scheduled time. Execute only after a fresh affirmative confirmation for that exact preview. A draft approval, a prior confirmation, or a changed schedule never counts. See [the publishing boundary](references/socialbu-publishing.md).

## Verify a checkout

```bash
./scripts/validate.sh
python3 -m unittest discover -s tests
python3 scripts/selftest.py
```

## Contributing and security

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). This independent project is not affiliated with LinkedIn or SocialBu.
