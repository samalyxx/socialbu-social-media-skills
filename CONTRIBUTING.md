# Contributing

Contributions should make one of the thirteen LinkedIn workflows more accurate, operational, or safe without expanding it into a catchall.

## Skill changes

- Keep each folder name, frontmatter `name`, and routing description aligned.
- Preserve the distinction between post writing, hook work, voice editing, repurposing, comments, owned-post replies, thread monitoring, planning, advocacy, profile work, measurement, story capture, and SocialBu execution.
- State required inputs, decisions, deliverables, evidence boundaries, and handoffs. Avoid generic advice that does not change agent behavior.
- Put shared guidance in one of the seven focused files under `references/` and link it where the agent should read it.
- Use draft mode for every workflow that does not need connected SocialBu data.

## Claims and safety

- Ground product-specific claims in public SocialBu documentation linked from `references/socialbu-capabilities.md`.
- Do not guess current plan, account, network, media, or LinkedIn limits.
- Do not add credentials, secret-shaped examples, personal data, tracking, an SDK, a client library, or a product integration.
- Do not add a path around the publisher's final preview and fresh exact-action confirmation. Each publish, schedule, or autopost mutation must be confirmed separately immediately before execution.
- Do not weaken source fidelity, disclosure, privacy, or escalation rules for stylistic convenience.

## Before submitting

Run:

```bash
./scripts/validate.sh
git diff --check
```

Review changed Markdown links and confirm no unfinished scaffold text remains. Describe the behavior changed and the validation performed in the pull request.

By contributing, you agree that your contribution is licensed under [MIT](LICENSE).
