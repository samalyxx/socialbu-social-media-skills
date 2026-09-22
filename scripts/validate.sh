#!/bin/sh
set -eu

fail() { echo "validation failed: $*" >&2; exit 1; }

expected_skills='linkedin-comment-drafter
linkedin-content-planner
linkedin-employee-advocacy
linkedin-engager-analytics
linkedin-hook-extractor
linkedin-humanizer
linkedin-interviewer
linkedin-post-writer
linkedin-profile-optimizer
linkedin-reply-handler
linkedin-repurposer
linkedin-thread-monitor'

actual_skills=$(find skills -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort)
[ "$actual_skills" = "$expected_skills" ] || fail "expected exactly twelve LinkedIn skills"

for path in README.md SKILL.md CLAUDE.md .codex-plugin/plugin.json .claude-plugin/plugin.json .claude-plugin/marketplace.json .agents/plugins/marketplace.json assets/linkedin-skills-overview.png lib/approval.py lib/config.py lib/url_parser.py scripts/selftest.py references/socialbu-publishing.md; do
  [ -s "$path" ] || fail "missing or empty: $path"
done

for skill in $expected_skills; do
  path="skills/$skill/SKILL.md"
  [ -s "$path" ] || fail "missing: $path"
  sed -n '1,12p' "$path" | grep -Fxq "name: $skill" || fail "wrong frontmatter name: $skill"
done

python3 - <<'PY'
import json
from pathlib import Path

for path in (Path('.codex-plugin/plugin.json'),):
    data = json.loads(path.read_text())
    assert data['name'] == 'linkedin-skills', path
    assert data['interface']['displayName'] == 'LinkedIn Skills', path
    assert data['skills'] == './skills/', path

claude = json.loads(Path('.claude-plugin/plugin.json').read_text())
assert claude['name'] == 'linkedin-skills'

marketplace = json.loads(Path('.agents/plugins/marketplace.json').read_text())
assert marketplace['name'] == 'linkedin-skills'
assert marketplace['plugins'][0]['name'] == 'linkedin-skills'
PY

[ "$(od -An -tx1 -N8 assets/linkedin-skills-overview.png | tr -d ' \n')" = 89504e470d0a1a0a ] || fail "bad overview PNG"

if find skills -maxdepth 1 -type d -name '*socialbu*' | grep .; then fail "SocialBu cannot be a skill name"; fi
if grep -R -Ei 'socialbu-linkedin-skills|socialbu-linkedin-publisher' README.md SKILL.md .codex-plugin .claude-plugin skills; then fail "obsolete SocialBu product identity remains"; fi
echo "validation passed: 12 LinkedIn Skills workflows, Codex + Claude manifests, safe local helpers, and assets"
