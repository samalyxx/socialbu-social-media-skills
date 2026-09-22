#!/bin/sh
set -eu

fail() {
  echo "validation failed: $*" >&2
  exit 1
}

expected_skills='linkedin-comment-drafter
linkedin-content-planner
linkedin-employee-advocacy
linkedin-engagement-review
linkedin-hook-lab
linkedin-humanizer
linkedin-post-writer
linkedin-profile-optimizer
linkedin-reply-handler
linkedin-repurposer
linkedin-story-bank
linkedin-thread-monitor
socialbu-linkedin-publisher'

expected_references='linkedin-content-planning.md
linkedin-conversations.md
linkedin-hooks.md
linkedin-measurement.md
linkedin-profile.md
linkedin-writing.md
socialbu-capabilities.md'

required_paths='README.md
PLAN.md
AGENTS.md
SKILL.md
SECURITY.md
CONTRIBUTING.md
LICENSE
assets/socialbu-linkedin-skills-hero.png
.codex-plugin/plugin.json
.codex-marketplace/socialbu-linkedin-skills/.codex-plugin/plugin.json
references/linkedin-content-planning.md
references/linkedin-conversations.md
references/linkedin-hooks.md
references/linkedin-measurement.md
references/linkedin-profile.md
references/linkedin-writing.md
references/socialbu-capabilities.md'

for path in $required_paths; do
  [ -f "$path" ] || fail "missing required file: $path"
  [ -s "$path" ] || fail "empty required file: $path"
done

[ -L .codex-marketplace/socialbu-linkedin-skills/skills ] || fail "marketplace skills entry must be a symlink"
[ "$(readlink .codex-marketplace/socialbu-linkedin-skills/skills)" = '../../skills' ] || fail "marketplace skills symlink has the wrong target"
[ -f .codex-marketplace/socialbu-linkedin-skills/skills/linkedin-post-writer/SKILL.md ] || fail "marketplace skills symlink is broken"
[ ! -e .codex-marketplace/socialbu-social-media-skills ] || fail "superseded marketplace package remains"
[ ! -e assets/socialbu-skills-hero.png ] || fail "superseded hero asset remains"

actual_skills=$(
  for path in skills/*; do
    [ -d "$path" ] || continue
    basename "$path"
  done | sort
)
[ "$actual_skills" = "$expected_skills" ] || {
  echo "expected skills:" >&2
  echo "$expected_skills" >&2
  echo "actual skills:" >&2
  echo "$actual_skills" >&2
  fail "skills directory must contain exactly the thirteen LinkedIn skills"
}

skill_file_count=$(find skills -mindepth 2 -maxdepth 2 -type f -name SKILL.md | wc -l | tr -d ' ')
[ "$skill_file_count" = 13 ] || fail "expected 13 skill files, found $skill_file_count"

actual_references=$(
  for path in references/*.md; do
    [ -f "$path" ] || continue
    basename "$path"
  done | sort
)
[ "$actual_references" = "$expected_references" ] || {
  echo "expected references:" >&2
  echo "$expected_references" >&2
  echo "actual references:" >&2
  echo "$actual_references" >&2
  fail "references directory must contain exactly the seven v2 references"
}

check_frontmatter() {
  path=$1
  expected_name=$2
  [ "$(sed -n '1p' "$path")" = '---' ] || fail "missing opening frontmatter delimiter: $path"
  closing_line=$(awk 'NR > 1 && $0 == "---" { print NR; exit }' "$path")
  [ -n "$closing_line" ] || fail "missing closing frontmatter delimiter: $path"
  actual_name=$(sed -n "2,$((closing_line - 1))p" "$path" | sed -n 's/^name:[[:space:]]*//p')
  [ "$actual_name" = "$expected_name" ] || fail "frontmatter name mismatch in $path"
  sed -n "2,$((closing_line - 1))p" "$path" | grep -Eq '^description:[[:space:]]*[^[:space:]].*$' || fail "missing frontmatter description: $path"
}

check_frontmatter SKILL.md socialbu-linkedin-skills
for skill in $expected_skills; do
  path="skills/$skill/SKILL.md"
  [ -f "$path" ] || fail "missing skill entrypoint: $path"
  check_frontmatter "$path" "$skill"
  grep -Fq "$skill" README.md || fail "README does not list $skill"
  grep -Fq "skills/$skill/SKILL.md" SKILL.md || fail "root router does not route $skill"
done

python3 - <<'PY'
import json
import pathlib
import re
import urllib.parse

root = pathlib.Path('.')
manifest_paths = [
    root / '.codex-plugin/plugin.json',
    root / '.codex-marketplace/socialbu-linkedin-skills/.codex-plugin/plugin.json',
]
for path in manifest_paths:
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f'validation failed: invalid manifest {path}: {exc}')
    allowed = {
        'id', 'name', 'version', 'description', 'skills', 'apps', 'mcpServers',
        'interface', 'author', 'homepage', 'repository', 'license', 'keywords',
    }
    unknown = sorted(set(data) - allowed)
    if unknown:
        raise SystemExit(f'validation failed: unsupported fields in {path}: {unknown}')
    if data.get('name') != 'socialbu-linkedin-skills':
        raise SystemExit(f'validation failed: wrong plugin name in {path}')
    if data.get('version') != '2.0.0':
        raise SystemExit(f'validation failed: wrong plugin version in {path}')
    if not isinstance(data.get('description'), str) or not data['description'].strip():
        raise SystemExit(f'validation failed: missing description in {path}')
    if not isinstance(data.get('author'), dict) or not str(data['author'].get('name', '')).strip():
        raise SystemExit(f'validation failed: missing author.name in {path}')
    if data.get('skills') != './skills/':
        raise SystemExit(f'validation failed: wrong skills path in {path}')
    interface = data.get('interface')
    if not isinstance(interface, dict):
        raise SystemExit(f'validation failed: missing interface object in {path}')
    for field in ('displayName', 'shortDescription', 'longDescription', 'developerName', 'category'):
        if not isinstance(interface.get(field), str) or not interface[field].strip():
            raise SystemExit(f'validation failed: missing interface.{field} in {path}')
    capabilities = interface.get('capabilities')
    if not isinstance(capabilities, list) or not capabilities or not all(isinstance(item, str) and item.strip() for item in capabilities):
        raise SystemExit(f'validation failed: invalid interface.capabilities in {path}')
    prompts = interface.get('defaultPrompt')
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3 or not all(isinstance(item, str) and 0 < len(item) <= 128 for item in prompts):
        raise SystemExit(f'validation failed: invalid interface.defaultPrompt in {path}')
    website = interface.get('websiteURL')
    parsed = urllib.parse.urlparse(website) if isinstance(website, str) else None
    if parsed is None or parsed.scheme != 'https' or not parsed.netloc:
        raise SystemExit(f'validation failed: invalid interface.websiteURL in {path}')
    if not re.fullmatch(r'#[0-9A-Fa-f]{6}', str(interface.get('brandColor', ''))):
        raise SystemExit(f'validation failed: invalid interface.brandColor in {path}')

link_pattern = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
for path in sorted(root.rglob('*.md')):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8')
    for raw_target in link_pattern.findall(text):
        target = raw_target.strip().strip('<>')
        if not target or target.startswith('#') or '://' in target or target.startswith('mailto:'):
            continue
        local = target.split('#', 1)[0]
        resolved = (path.parent / local).resolve()
        if not resolved.exists():
            raise SystemExit(f'validation failed: broken local link in {path}: {raw_target}')
PY

text_files="README.md PLAN.md AGENTS.md SKILL.md SECURITY.md CONTRIBUTING.md $(find skills references .codex-plugin .codex-marketplace/socialbu-linkedin-skills/.codex-plugin -type f \( -name '*.md' -o -name '*.json' \) -print)"
if grep -Eni 'TODO|TBD|FIXME|CHANGEME|YOUR[_ -]?(API[_ -]?KEY|TOKEN|SECRET)|\{\{[^}]+\}\}|sk-[A-Za-z0-9_-]{20,}|Bearer[[:space:]]+[A-Za-z0-9._-]{16,}' $text_files; then
  fail "unfinished marker or secret-shaped content found"
fi

secret_path=$(find . -path './.git' -prune -o -type f \( -name '.env' -o -name '.env.*' -o -name '*.pem' -o -name '*.key' -o -iname '*credentials*' \) -print -quit)
[ -z "$secret_path" ] || fail "secret-like file found: $secret_path"

publisher=skills/socialbu-linkedin-publisher/SKILL.md
grep -Fq 'https://socialbu.com/mcp' "$publisher" || fail "publisher is missing the exact SocialBu MCP endpoint"
grep -Fq 'Immediately before every state-changing call' "$publisher" || fail "publisher is missing the immediate confirmation gate"
grep -Fq 'separate confirmation for each post, account, schedule, or autopost mutation' "$publisher" || fail "publisher is missing per-action confirmation"
grep -Fq 'fresh confirmation before any retry' "$publisher" || fail "publisher is missing safe retry handling"

if grep -Eri 'publish(es|ed|ing)? automatically|auto[- ]publish|without (user )?confirmation' README.md SKILL.md AGENTS.md SECURITY.md CONTRIBUTING.md skills references; then
  fail "unsafe automatic publishing language found"
fi

png_signature=$(od -An -tx1 -N8 assets/socialbu-linkedin-skills-hero.png | tr -d ' \n')
[ "$png_signature" = '89504e470d0a1a0a' ] || fail "hero asset is not a valid PNG"

echo "validation passed: 13 skills, 7 references, manifests, links, safety rules, and assets"
