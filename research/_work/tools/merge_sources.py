#!/usr/bin/env python3
"""Merge research/_work/sources_WS*.csv (+ verification fragment) into research/sources.csv and validate."""
import csv, glob, os, re, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
WORK = os.path.join(ROOT, '_work')
HEADER = ['id','claim','url','publisher','date_published','date_accessed','quote',
          'primary_secondary','label','method','search_language','country','workstream']
ALLOWED = {
    'primary_secondary': {'primary','secondary'},
    'label': {'VERIFIED','LEAD'},
    'method': {'search-extract','fetched','api-query','derived'},
    'search_language': {'EN','ET','LV','LT','RU'},
    'country': {'EE','LV','LT','Baltic','EU','other'},
}

def norm(v):
    return (v or '').strip()

def main():
    files = sorted(glob.glob(os.path.join(WORK, 'sources_*.csv')))
    rows, problems = [], []
    ids = collections.Counter()
    for f in files:
        with open(f, newline='', encoding='utf-8') as fh:
            r = csv.DictReader(fh)
            hdr = [h.strip() for h in (r.fieldnames or [])]
            missing = [h for h in HEADER if h not in hdr]
            if missing:
                problems.append(f'{os.path.basename(f)}: missing columns {missing}')
            for i, row in enumerate(r, start=2):
                row = {k.strip(): norm(v) for k, v in row.items() if k}
                out = {h: row.get(h, '') for h in HEADER}
                if not out['id']:
                    problems.append(f'{os.path.basename(f)}:{i}: empty id'); continue
                ids[out['id']] += 1
                for col, allowed in ALLOWED.items():
                    v = out[col]
                    if v and v not in allowed:
                        # tolerate case differences
                        match = [a for a in allowed if a.lower() == v.lower()]
                        if match: out[col] = match[0]
                        else: problems.append(f"{out['id']}: {col}='{v}' not in {sorted(allowed)}")
                q = out['quote'].lstrip('~').strip()
                nwords = len(q.split())
                if nwords > 25:
                    problems.append(f"{out['id']}: quote has {nwords} words (>25)")
                if out['label'] == 'VERIFIED' and not out['url'].startswith('http'):
                    problems.append(f"{out['id']}: VERIFIED without http URL")
                rows.append(out)
    dups = [k for k, c in ids.items() if c > 1]
    if dups:
        problems.append(f'duplicate ids: {dups[:30]}')
    rows.sort(key=lambda r: (r['workstream'] or r['id'].split('-')[0], r['id']))
    with open(os.path.join(ROOT, 'sources.csv'), 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=HEADER, quoting=csv.QUOTE_ALL)
        w.writeheader(); w.writerows(rows)
    # stats
    def domain(u):
        m = re.match(r'https?://([^/]+)/?(.*)', u)
        return m.group(1).lower().removeprefix('www.') if m else ''
    urls = {r['url'].rstrip('/').lower() for r in rows if r['url'].startswith('http')}
    url_primary = {}
    for r in rows:
        u = r['url'].rstrip('/').lower()
        if not u.startswith('http'): continue
        url_primary[u] = url_primary.get(u, False) or r['primary_secondary'] == 'primary'
    ver = [r for r in rows if r['label'] == 'VERIFIED']
    print(f'fragments: {[os.path.basename(f) for f in files]}')
    print(f'rows: {len(rows)} | VERIFIED: {len(ver)} | LEAD: {sum(r["label"]=="LEAD" for r in rows)}')
    print(f'distinct URLs: {len(urls)} | distinct primary URLs: {sum(url_primary.values())} | distinct domains: {len({domain(u) for u in urls})}')
    print('rows by workstream:', dict(collections.Counter(r['workstream'] for r in rows)))
    print('primary/secondary:', dict(collections.Counter(r['primary_secondary'] for r in rows)))
    print('country:', dict(collections.Counter(r['country'] for r in rows)))
    print('search_language:', dict(collections.Counter(r['search_language'] for r in rows)))
    print('method:', dict(collections.Counter(r['method'] for r in rows)))
    print(f'problems ({len(problems)}):')
    for p in problems[:200]: print('  -', p)

if __name__ == '__main__':
    main()
