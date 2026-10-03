#!/usr/bin/env python3
"""Evidence scorecard generator for 00_research_summary.md (lead analyst synthesis).

Scores 1-5, 5 = most favourable to the operator. Every score is built from a BASIS code
(country x component base value taken from the workstream synthesis inputs) plus explicit,
evidence-referenced modifiers. Bundles use stated combination rules. This is analyst
JUDGMENT built on labelled evidence; codes are defined in the basis tables printed below.

Run: python3 scorecard.py  -> writes _work/data/scorecard.csv and _work/data/scorecard.md
"""
import csv, os, itertools, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, '..', 'data')

COUNTRIES = ['EE', 'LV', 'LT']
COMPONENTS = ['A', 'B', 'C']
BUNDLES = {'A+B': ['A', 'B'], 'A+B+C': ['A', 'B', 'C']}
GROUPS = ['G1-Logistics', 'G1-Wholesale', 'G1-Manufacturing', 'G1-ProfServices', 'G1-Accounting', 'G2-Foreign']

# ---- Base values: (score, code, evidence) per dimension, country, component -------------
# D = demand evidence (WS2 §12; 'gap' = not researched / no evidence, not a negative finding)
D = {
 ('EE','A'): (2, 'D-EE-A', '[V:WS2-007][V:WS2-010]'),
 ('EE','B'): (4, 'D-EE-B', '[V:WS2-001][V:WS2-003][V:WS2-049][V:WS2-050]'),
 ('EE','C'): (1, 'D-EE-C', 'gap; [V:WS2-016]'),
 ('LV','A'): (4, 'D-LV-A', '[V:WS2-069][V:WS2-070][E:A-WS2-08][V:WS3-017]'),
 ('LV','B'): (2, 'D-LV-B', '[V:WS2-060][V:WS2-062][V:WS2-054]'),
 ('LV','C'): (1, 'D-LV-C', 'gap'),
 ('LT','A'): (2, 'D-LT-A', '[V:WS2-059][V:WS2-042][V:WS2-043]'),
 ('LT','B'): (3, 'D-LT-B', '[V:WS2-057][V:WS2-054][V:WS2-067]'),
 ('LT','C'): (1, 'D-LT-C', 'gap'),
}
# W = willingness-to-pay evidence (WS5 §12)
W = {
 ('EE','A'): (3, 'W-EE-A', '[V:WS3-005][E:A-WS2-05][V:WS2-007][V:WS2-009]'),
 ('EE','B'): (2, 'W-EE-B', '[V:WS3-005]'),
 ('EE','C'): (2, 'W-EE-C', '[V:WS3-004][V:WS3-003]'),
 ('LV','A'): (4, 'W-LV-A', '[V:WS3-017][V:WS3-018][V:WS3-019][V:WS2-020]'),
 ('LV','B'): (2, 'W-LV-B', '[V:WS2-022][V:WS3-046]'),
 ('LV','C'): (2, 'W-LV-C', '[V:WS3-009]'),
 ('LT','A'): (2, 'W-LT-A', '[V:WS3-025]'),
 ('LT','B'): (3, 'W-LT-B', '[V:WS3-024][E:A-WS5-19]'),
 ('LT','C'): (3, 'W-LT-C', '[V:WS3-008]'),
}
# C = competition intensity, 5 = least competition (WS3 §12; 'p' = provisional, under-searched)
C = {
 ('EE','A'): (2, 'C-EE-A', '[V:WS3-026][V:WS3-012][V:WS3-016][V:WS3-021][V:WS3-005][V:WS3-013]'),
 ('EE','B'): (3, 'C-EE-B(p)', '[V:WS3-021][V:WS3-005]'),
 ('EE','C'): (2, 'C-EE-C', '[V:WS3-001][V:WS3-009]'),
 ('LV','A'): (2, 'C-LV-A', '[V:WS3-013][V:WS3-017][V:WS3-022][E:A-WS3-03]'),
 ('LV','B'): (3, 'C-LV-B(p)', '[V:WS3-013][E:A-WS3-03]'),
 ('LV','C'): (2, 'C-LV-C', '[V:WS3-002][V:WS3-009]'),
 ('LT','A'): (2, 'C-LT-A', '[V:WS3-014][V:WS3-023][V:WS3-025][V:WS3-013]'),
 ('LT','B'): (2, 'C-LT-B', '[V:WS3-024][V:WS3-034][V:WS3-035]'),
 ('LT','C'): (2, 'C-LT-C', '[V:WS3-007][V:WS3-008][V:WS3-002]'),
}
# L = legal risk, 5 = lowest risk (WS4 §8.1; applies to legal-person targets — see note on sole traders)
L = {
 ('EE','A'): (4, 'L-A', '[E:A-WS4-01]'), ('LV','A'): (4, 'L-A', '[E:A-WS4-01]'), ('LT','A'): (4, 'L-A', '[E:A-WS4-01]'),
 ('EE','B'): (3, 'L-B', '[E:A-WS4-01]'), ('LV','B'): (3, 'L-B', '[E:A-WS4-01]'), ('LT','B'): (3, 'L-B', '[E:A-WS4-01]'),
 ('EE','C'): (3, 'L-EE-C', '[V:WS4-001][V:WS4-004][V:WS4-005]'),
 ('LV','C'): (3, 'L-LV-C', '[V:WS4-016][V:WS4-019][V:WS4-011]'),
 ('LT','C'): (4, 'L-LT-C(p)', '[V:WS4-031][V:WS4-034][V:WS4-036]'),
}
# A = async/evening fit, 5 = fully async (WS6 §8.2 rubric reconciled with WS5 §7 daytime shares)
ASYNC = {
 'A': (3, 'A-A', '[E:A-WS6-05][E:A-WS5-33] (25% of hours need business hours)'),
 'B': (4, 'A-B', '[E:A-WS6-05][E:A-WS5-33] (10%)'),
 'C': (3, 'A-C', '[E:A-WS5-33] (30%: same-day replies, booking, client calls); WS6 rated 4 — lower value kept'),
}
# G = language advantage real? (WS1 §3.5/§8, WS3 §5, WS6 §8.3)
G = {
 'EE': (2, 'G-EE', '[V:WS1-099][V:WS1-100][V:WS6-012][V:WS3-002][V:WS3-013]'),
 'LV': (2, 'G-LV', '[V:WS1-101][V:WS1-104][V:WS3-009][V:WS3-013]'),
 'LT': (3, 'G-LT', '[V:WS1-105][V:WS1-106][V:WS6-025][V:WS6-027][V:WS3-007]'),
}
G_C_MOD = ('Gm-C', '-1 for C in EE/LV: outbound copy in ET/LV the operator cannot write or proof-read; competitors are native [V:WS3-002][V:WS3-009]; LLM quality evidence is benchmark-only [V:WS0-005][V:WS0-006]')

# ---- Group modifiers (only where evidence exists) ---------------------------------------
def group_mod(dim, group, country, comp):
    """Return (delta, code) for single components."""
    if dim == 'D':
        if group == 'G1-Accounting' and comp == 'B' and country == 'EE':
            return 1, 'Dm-acct-EE (+1: buyers may demand e-invoices since 1 Jul 2025 [V:WS2-073])'
        if group == 'G2-Foreign' and comp == 'C':
            return None, 'D-G2-C'   # absolute override below
        if group == 'G2-Foreign' and comp in ('A', 'B'):
            return None, 'D-G2-AB'
    if dim == 'W' and group == 'G2-Foreign':
        return None, 'W-G2'
    if dim == 'C' and group == 'G2-Foreign':
        return None, 'C-G2'
    return 0, ''

G2_ABS = {
 ('D','C'): (2, 'D-G2-C', 'agencies already sell Baltic market-entry outbound to foreign firms [V:WS3-053][V:WS3-049]'),
 ('D','A'): (1, 'D-G2-AB', 'gap: no evidence of foreign firms buying Baltic CRM/automation set-up'),
 ('D','B'): (1, 'D-G2-AB', 'gap'),
 ('W','C'): (3, 'W-G2-C', '[V:WS3-053][V:WS3-008]'),
 ('W','A'): (1, 'W-G2-AB', 'gap'),
 ('W','B'): (1, 'W-G2-AB', 'gap'),
 ('C','A'): (2, 'C-G2', '[V:WS3-053][V:WS3-049][V:WS3-031]'),
 ('C','B'): (2, 'C-G2', '[V:WS3-053][V:WS3-049][V:WS3-031]'),
 ('C','C'): (2, 'C-G2', '[V:WS3-053][V:WS3-049][V:WS3-031]'),
}

def clip(x):
    return max(1, min(5, x))

def single(dim, country, comp, group):
    if group == 'G2-Foreign' and (dim, comp) in G2_ABS:
        s, code, _ = G2_ABS[(dim, comp)]
        return s, code
    if dim == 'D': s, code, _ = D[(country, comp)]
    elif dim == 'W': s, code, _ = W[(country, comp)]
    elif dim == 'C': s, code, _ = C[(country, comp)]
    elif dim == 'L': s, code, _ = L[(country, comp)]
    elif dim == 'A': s, code, _ = ASYNC[comp]
    elif dim == 'G':
        s, code, _ = G[country]
        if comp == 'C' and country in ('EE', 'LV'):
            s, code = s - 1, code + '+' + G_C_MOD[0]
    d, mcode = group_mod(dim, group, country, comp)
    if d:
        s, code = s + d, code + '+' + mcode.split(' ')[0]
    return clip(s), code

def bundle(dim, country, comps, group):
    vals = [single(dim, country, c, group) for c in comps]
    scores = [v[0] for v in vals]
    if dim == 'C':   # competition: A+B faces CRM partners that already automate; A+B+C: no single provider found (weak)
        if comps == ['A', 'B']:
            return min(scores), 'Cb-AB [V:WS3-013][V:WS3-024]'
        return 3, 'Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]'
    # demand, WTP, legal, async, language: weakest link (no evidence of joint demand or joint WTP)
    i = scores.index(min(scores))
    return min(scores), 'min(' + vals[i][1] + ')'

def main():
    rows = []
    for country, group, comp in itertools.product(COUNTRIES, GROUPS, COMPONENTS + list(BUNDLES)):
        rec = {'country': country, 'group': group, 'component': comp}
        codes = []
        for dim in ['D', 'W', 'C', 'L', 'A', 'G']:
            if comp in BUNDLES:
                s, code = bundle(dim, country, BUNDLES[comp], group)
            else:
                s, code = single(dim, country, comp, group)
            rec[dim] = s
            codes.append(f'{dim}:{code}')
        rec['mean'] = round(statistics.mean(rec[d] for d in 'DWCLAG'), 2)
        rec['min'] = min(rec[d] for d in 'DWCLAG')
        rec['basis'] = '; '.join(codes)
        rows.append(rec)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, 'scorecard.csv'), 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), quoting=csv.QUOTE_ALL)
        w.writeheader(); w.writerows(rows)
    # markdown: one table per country
    md = []
    for country in COUNTRIES:
        md.append(f'\n#### {country}\n')
        md.append('| Group | Comp. | Demand | WTP | Competition | Legal | Async | Language | Mean | Basis codes |')
        md.append('|---|---|---|---|---|---|---|---|---|---|')
        for r in rows:
            if r['country'] != country: continue
            md.append(f"| {r['group']} | {r['component']} | {r['D']} | {r['W']} | {r['C']} | {r['L']} | {r['A']} | {r['G']} | {r['mean']} [E:A-WS0-01] | {r['basis']} |")
    open(os.path.join(OUT_DIR, 'scorecard.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    ranked = sorted(rows, key=lambda r: (-r['mean'], -r['D'], -r['W']))
    print('TOP 10'); [print(r['country'], r['group'], r['component'], r['mean'], 'DWCLAG', [r[d] for d in 'DWCLAG']) for r in ranked[:10]]
    print('BOTTOM 10'); [print(r['country'], r['group'], r['component'], r['mean'], 'DWCLAG', [r[d] for d in 'DWCLAG']) for r in ranked[-10:]]
    print('rows', len(rows))

if __name__ == '__main__':
    main()
