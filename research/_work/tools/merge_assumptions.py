#!/usr/bin/env python3
"""Concatenate research/_work/assumptions_WS*.md (+ verification) into research/assumptions.md."""
import glob, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
WORK = os.path.join(ROOT, '_work')
files = sorted(glob.glob(os.path.join(WORK, 'assumptions_*.md')))
parts = ["# Assumptions register (every ESTIMATE input with its basis)\n",
         "Merged from workstream fragments in `_work/`. IDs `A-WSn-xx` are referenced in the workstream files as `[E:A-WSn-xx]`. "
         "Each entry gives value, formula, inputs (VERIFIED source IDs from `sources.csv` or other assumptions), rationale, confidence, and where it is used.\n"]
count = 0
for f in files:
    txt = open(f, encoding='utf-8').read().strip()
    ws = re.search(r'assumptions_(\w+)\.md', f).group(1)
    n = len(re.findall(r'^###\s+A-', txt, flags=re.M))
    count += n
    # demote any top-level heading in fragments
    txt = re.sub(r'^#\s', '## ', txt, flags=re.M) if txt.startswith('# ') else txt
    parts.append(f"\n---\n\n## {ws} ({n} entries)\n\n{txt}\n")
open(os.path.join(ROOT, 'assumptions.md'), 'w', encoding='utf-8').write('\n'.join(parts))
print(f'merged {len(files)} files, {count} assumption entries')
