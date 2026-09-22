# LinkedIn-first v2 implementation plan

1. Reframe the bundle around LinkedIn outcomes: replace the project documentation, root router, repository guidance, security policy, contribution guide, and plugin metadata while preserving draft-first behavior and the supplied `assets/socialbu-linkedin-skills-hero.png` artwork.
2. Add the thirteen focused LinkedIn skills and seven shared references before removing any superseded generic skill or marketplace package, so every baseline file keeps a working replacement throughout the migration.
3. Make each workflow operational: define inputs, decision points, outputs, handoffs, evidence boundaries, and LinkedIn-specific quality checks for writing, conversations, planning, profiles, repurposing, advocacy, monitoring, review, stories, and publishing.
4. Restrict connected execution to the SocialBu MCP endpoint at `https://socialbu.com/mcp`; require a preview and fresh confirmation of the exact action, target account, content, and timing immediately before every publish, schedule, or autopost mutation.
5. Upgrade validation for exactly thirteen named skills, seven required references, valid manifests and local links, the LinkedIn hero, removal of generic skill folders, and absence of placeholders, secrets, or unsafe publishing language; finish with `./scripts/validate.sh` and `git diff --check`.
