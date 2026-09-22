#!/bin/sh
set -eu

required='README.md AGENTS.md SKILL.md SECURITY.md CONTRIBUTING.md LICENSE .codex-plugin/plugin.json .codex-marketplace/socialbu-social-media-skills/.codex-plugin/plugin.json references/socialbu-capabilities.md references/content-quality.md'
for path in $required; do
  test -f "$path" || { echo "missing: $path" >&2; exit 1; }
done

test -d .codex-marketplace/socialbu-social-media-skills/skills || {
  echo "missing or broken marketplace skills link" >&2
  exit 1
}

count=$(find skills -mindepth 2 -maxdepth 2 -name SKILL.md -type f | wc -l | tr -d ' ')
test "$count" = 9 || { echo "expected 9 skill files, found $count" >&2; exit 1; }

for path in SKILL.md skills/*/SKILL.md; do
  first=$(sed -n '1p' "$path")
  test "$first" = '---' || { echo "missing frontmatter: $path" >&2; exit 1; }
done

echo "validation passed"
