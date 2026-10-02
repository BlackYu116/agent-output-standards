#!/usr/bin/env python3
"""Check this repository's local structure, not language or factual correctness."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def check(root):
    errors = []
    required = ['README.md', 'AGENTS.md', 'CONTRIBUTING.md', 'CHANGELOG.md',
                'skills/clear-output/SKILL.md', 'evals/cases.json', 'evals/README.md']
    for name in required:
        if not (root / name).is_file():
            errors.append(f'Missing required file: {name}')
    for path in root.rglob('*.md'):
        if '.git' in path.parts:
            continue
        text = path.read_text(encoding='utf-8')
        # Supports the inline links used here; not a complete Markdown parser.
        for target in re.findall(r'\]\(([^\s)]+)\)', text):
            target = target.strip('<>')
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            dest = (path.parent / unquote(parts.path)).resolve()
            if not dest.is_relative_to(root.resolve()) or not dest.exists():
                errors.append(f'{path.relative_to(root)}: invalid local link {target}')
    skill = root / 'skills/clear-output/SKILL.md'
    if skill.exists():
        text = skill.read_text(encoding='utf-8')
        match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
        if not match:
            errors.append('SKILL.md: missing frontmatter')
        else:
            fields = dict(re.findall(r'^(name|description):\s*(.+)$', match[1], re.M))
            if fields.get('name') != 'clear-output' or not fields.get('description'):
                errors.append('SKILL.md: invalid name or missing description')
    try:
        cases = json.loads((root / 'evals/cases.json').read_text(encoding='utf-8'))
        if not isinstance(cases, list) or not cases:
            raise ValueError('cases must be a nonempty list')
        ids = set()
        for i, case in enumerate(cases):
            if not isinstance(case, dict):
                errors.append(f'case {i}: must be an object')
                continue
            ident = case.get('id')
            if not isinstance(ident, str) or not ident or ident in ids:
                errors.append(f'case {i}: invalid or duplicate id')
            else:
                ids.add(ident)
            if not isinstance(case.get('prompt'), str) or not case['prompt'].strip():
                errors.append(f'case {i}: missing prompt')
            for field in ('expected', 'failure_modes'):
                values = case.get(field)
                if not isinstance(values, list) or not values or not all(isinstance(v, str) and v.strip() for v in values):
                    errors.append(f'case {i}: {field} must be a nonempty string list')
            if 'source_text' in case and not isinstance(case['source_text'], str):
                errors.append(f'case {i}: source_text must be a string')
    except (OSError, ValueError) as exc:
        errors.append(f'evals/cases.json: {exc}')
    return errors

if __name__ == '__main__':
    failures = check(ROOT)
    if failures:
        print('\n'.join(failures), file=sys.stderr)
        sys.exit(1)
    print('PASS: required files, local link targets, skill frontmatter, and evaluation case structure')
    print('Not checked: external links, link anchors, factual accuracy, language quality, or agent behavior')
