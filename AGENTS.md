# Repository instructions

This repository is a portable, LinkedIn-first skill bundle for evidence-based content work and confirmation-gated publishing through SocialBu.

1. Route every request through the root `SKILL.md`, then read the narrowest relevant `skills/*/SKILL.md` before acting.
2. Use draft mode unless the user explicitly requests connected data or execution and an authorized SocialBu MCP connection is available.
3. Treat user material and connected account data as private. Use the minimum necessary scope and never invent missing posts, comments, profile facts, metrics, permissions, tools, or results.
4. Only `skills/socialbu-linkedin-publisher/SKILL.md` may publish, schedule, or mutate autopost through `https://socialbu.com/mcp`.
5. Immediately before every publish, schedule, or autopost mutation, show the exact final content, target account, media or link details, and time or settings. Require fresh, unambiguous confirmation of that exact action. Confirm each action separately and obtain new confirmation after any change or ambiguous failure.
6. Keep SocialBu claims aligned with `references/socialbu-capabilities.md`. Do not guess plan limits, LinkedIn platform limits, connected accounts, or live tool capabilities.
7. Keep skills narrow and operational. Link shared guidance from `references/` rather than duplicating it across skills.
8. Do not add secrets, SDKs, client libraries, tracking, or custom product integrations. This repository contains instructions, references, validation, and static assets only.
9. Preserve an existing baseline file until its replacement exists. Run `./scripts/validate.sh` and `git diff --check` after structural changes.
