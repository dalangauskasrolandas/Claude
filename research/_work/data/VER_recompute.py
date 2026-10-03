#!/usr/bin/env python3
"""Independent verifier recomputation (stdlib only) - "Baltic Revenue Engine", 2026-10-03.

Re-run:  python3 research/_work/data/VER_recompute.py
Does NOT import WS5_models.py: tax, unit economics, price floors and capacity are re-implemented
here from the stated formulas (A-WS5-01, A-WS5-13..38) and compared with WS5_models.csv.
Also recomputes the <=50-staff G1 funnel from db_coverage.csv, the G2 chamber sum, event weekdays,
and the scenario grids used by the red team (A-WS8-xx).
"""
import csv, os, datetime, itertools

HERE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ 1. tax + unit economics
S, IT = 0.33, 0.22
def net_fie(p):  # P = profit after deductible costs
    soc = S * p / (1 + S); inc = IT * (p - soc); return p - soc - inc
NET_SHARE = net_fie(1.0)
def net_naive(p):
    soc = S * p; return p - soc - IT * (p - soc)
print(f"net share official {NET_SHARE:.4f} | literal reading {net_naive(1.0):.4f} | gap {NET_SHARE - net_naive(1.0):.4f}")

CRM = dict(prices=[1200, 2500, 5000], deliver=25, sales=12, admin=2, support=3, direct=0)
AUT = dict(prices=[450, 1200, 3000], deliver=15, sales=8, admin=1.5, support=3, direct=10)
def unit(m, price, deliver=None, sales=None):
    d = m['deliver'] if deliver is None else deliver
    s = m['sales'] if sales is None else sales
    h = d + s + m['admin'] + m['support']
    return net_fie(price - m['direct']) / h, h
def retainer(price, churn=0.15, tools=150, deliver=20, sales=15, onboarding=15, admin=1):
    L = 1 / churn
    rev, cost = price * L, tools * L
    h = deliver * L + onboarding + sales + admin * L
    return net_fie(rev - cost) / h, h, L

out = {}
for name, m in (("CRM", CRM), ("AUT", AUT)):
    out[name] = [round(unit(m, p)[0], 1) for p in m['prices']]
out["LEAD"] = [round(retainer(p)[0], 1) for p in (1000, 1800, 2850)]
print("net EUR/h low/mid/high:", out)

def floor_project(m, target):
    h = m['deliver'] + m['sales'] + m['admin'] + m['support']
    return target * h / NET_SHARE + m['direct']
def floor_retainer(target, churn=0.15, tools=150):
    L = 1 / churn; h = 20 * L + 15 + 15 + 1 * L
    return target * h / (NET_SHARE * L) + tools
for t in (15, 25, 40):
    print(f"price needed for net EUR {t}/h: CRM {floor_project(CRM, t):,.0f} | AUT {floor_project(AUT, t):,.0f} | LEAD/month {floor_retainer(t):,.0f}")

# capacity (A-WS5-38): projects/yr = (H*46 - 72)/unit hours
OVER = 363.0 + 0  # placeholder replaced below
FX, VAT = 0.86, 0.24
overhead_base = 240 * FX * (1 + VAT) + 350
def cap_project(m, price, H):
    ah = H * 46; n = (ah - 72) / (m['deliver'] + m['sales'] + m['admin'] + m['support'])
    prof = n * (price - m['direct']) - overhead_base
    return n, net_fie(prof), net_fie(prof) / ah
def cap_retainer(price, H):
    ah = H * 46; avail = (ah - 72) / 12
    per = 20 + 1 + 0.15 * (15 + 15); n = avail / per
    prof = n * 12 * price - n * 12 * 150 - overhead_base
    return n, net_fie(prof), net_fie(prof) / ah
print(f"overhead base {overhead_base:.0f} EUR/yr")
for H in (10, 15, 20):
    a = cap_project(CRM, 2500, H); b = cap_project(AUT, 1200, H); c = cap_retainer(1800, H)
    print(f"H={H}: CRM {a[0]:.1f}/yr net {a[1]:,.0f} ({a[2]:.1f}/h) | AUT {b[0]:.1f}/yr net {b[1]:,.0f} ({b[2]:.1f}/h) | LEAD conc {c[0]:.1f} net {c[1]:,.0f} ({c[2]:.1f}/h)")

# compare with WS5_models.csv
ref = {}
with open(os.path.join(HERE, 'WS5_models.csv'), newline='', encoding='utf-8') as fh:
    for r in csv.DictReader(fh):
        ref[(r['section'], r['model'], r['scenario'], r['metric'])] = float(r['value']) if r['value'].replace('.', '', 1).replace('-', '', 1).isdigit() else None
chk = []
for name, m, label in (("CRM", CRM, "CRM setup"), ("AUT", AUT, "Automation project")):
    for p in m['prices']:
        k = ("price_sensitivity", label, f"price={p}", "net_per_h")
        chk.append(abs(unit(m, p)[0] - ref[k]))
for p in (1000, 1800, 2850):
    k = ("price_sensitivity", "Lead-gen retainer", f"price={p}", "net_per_h")
    chk.append(abs(retainer(p)[0] - ref[k]))
for H in (10, 15, 20):
    k = ("capacity", "CRM setup", f"H={H};price=2500", "net"); chk.append(abs(cap_project(CRM, 2500, H)[1] - ref[k]) / 1000)
    k = ("capacity", "Lead-gen retainer", f"H={H};price=1800", "net"); chk.append(abs(cap_retainer(1800, H)[1] - ref[k]) / 1000)
print(f"independent vs WS5_models.csv: {len(chk)} values compared, max abs diff {max(chk):.4f} (net EUR/h; capacity diffs scaled /1000)")

# ------------------------------------------------------------------ 2. <=50-staff funnel (Hunter 1-10 + 11-50)
rows = list(csv.DictReader(open(os.path.join(HERE, 'db_coverage.csv'), newline='', encoding='utf-8')))
R = {r['query_id']: r for r in rows}
def n(q): return float(R[q]['results_total'])
def mar(q): return float(R[q]['maritime_rows_in_sample']) / float(R[q]['sample_n'])
STAT_1049 = {"EE": 6284, "LV": 6457, "LT": 12815}
IND = {"LOG": "LOG", "WHS": "WHS", "MFG": "MFG", "PRO": "PRO", "ADM": "ADM"}
# email multipliers: (a) WS1 pooled over all 22 exact segments; (b) only exact segments that are inside the <=50 buckets
def pooled(filter_fn):
    t = a = p = 0.0
    for r in rows:
        rt = float(r['results_total'] or 0); sn = float(r['sample_n'] or 0)
        if rt and rt <= 100 and sn == rt and r['technology_filter_applied'].startswith('none') and filter_fn(r):
            t += rt; a += rt * float(r['pct_any_email']) / 100; p += rt * float(r['pct_personal_email']) / 100
    return t, a / t, p / t
all22 = pooled(lambda r: True)
le50 = pooled(lambda r: r['headcount'] in ('1-10', '11-50'))
print(f"pooled exact segments: all22 n={all22[0]:.0f} any {all22[1]:.3f} personal {all22[2]:.3f} | <=50 only n={le50[0]:.0f} any {le50[1]:.3f} personal {le50[2]:.3f}")
res = {}
for c in ("EE", "LV", "LT"):
    allrec = n(f"{c}-ALL-1-10") + n(f"{c}-ALL-11-50")
    log_ex = sum(n(f"{c}-LOG-{b}") * (1 - mar(f"{c}-LOG-{b}")) for b in ("1-10", "11-50"))
    other = {k: n(f"{c}-{k}-1-10") + n(f"{c}-{k}-11-50") for k in ("WHS", "MFG", "PRO", "ADM")}
    low = log_ex + other['WHS'] + other['MFG'] + other['ADM'] + other['PRO'] * 2 / 3
    high = log_ex + other['WHS'] + other['MFG'] + other['ADM'] + other['PRO']
    # 11-50 only
    l50 = n(f"{c}-LOG-11-50") * (1 - mar(f"{c}-LOG-11-50"))
    low50 = l50 + n(f"{c}-WHS-11-50") + n(f"{c}-MFG-11-50") + n(f"{c}-ADM-11-50") + n(f"{c}-PRO-11-50") * 2 / 3
    high50 = l50 + n(f"{c}-WHS-11-50") + n(f"{c}-MFG-11-50") + n(f"{c}-ADM-11-50") + n(f"{c}-PRO-11-50")
    res[c] = dict(all=allrec, log_ex=log_ex, low=low, high=high, low50=low50, high50=high50)
    print(f"{c}: all-industry records {allrec:,.0f}; logistics ex-maritime {log_ex:,.0f}; target records {low:,.0f}-{high:,.0f}; "
          f"11-50 only {low50:,.0f}-{high50:,.0f}; coverage 11-50/stat 10-49 {n(f'{c}-ALL-11-50')/STAT_1049[c]:.1%}")
    for tag, (_, ea, ep) in (("WS1 pooled-22", all22), ("<=50-only pooled", le50)):
        print(f"   {tag}: any-email {low*ea:,.0f}-{high*ea:,.0f} (11-50: {low50*ea:,.0f}-{high50*ea:,.0f}) | personal {low*ep:,.0f}-{high*ep:,.0f} (11-50: {low50*ep:,.0f}-{high50*ep:,.0f})")


# ------------------------------------------------------------------ 2b. corrected personal-email bracket (A-WS9-01/02)
print("\nBracket used in 01_market_size.md 'Scope <=50 staff' table (low = low target x <=50-only rate; high = high target x WS1 pooled rate):")
for c in ("EE", "LV", "LT"):
    r = res[c]
    anyl, anyh = r['low'] * all22[1], r['high'] * all22[1]
    pl, ph = r['low'] * le50[2], r['high'] * all22[2]
    pl50, ph50 = r['low50'] * le50[2], r['high50'] * all22[2]
    any50l, any50h = r['low50'] * all22[1], r['high50'] * all22[1]
    print(f"  {c}: any-email {anyl:,.0f}-{anyh:,.0f} | 11-50 any {any50l:,.0f}-{any50h:,.0f} | personal {pl:,.0f}-{ph:,.0f} | 11-50 personal {pl50:,.0f}-{ph50:,.0f}")
print(f"  rates: all22 any {all22[1]:.4f} personal {all22[2]:.4f}; <=50-only any {le50[1]:.4f} personal {le50[2]:.4f} (n={le50[0]:.0f}; accounting {sum(float(R[q]['results_total']) for q in R if '-ACC-' in q and ('-1-10' in q or '-11-50' in q)):.0f} + consulting 88)")

# ------------------------------------------------------------------ 3. G2 chamber sum
print("G2 network route:", 470 + 130 + 100 + 100 + 100, "memberships (not de-duplicated, all sizes)")

# ------------------------------------------------------------------ 4. event weekdays (WS6)
ev = {"EE-1": "2026-10-07", "EE-2": "2026-10-14", "EE-3": "2026-10-15", "EE-4": "2026-11-03", "EE-5": "2026-11-11",
      "EE-6": "2026-11-12", "EE-7": "2026-11-17", "EE-8": "2026-11-18", "EE-9a": "2026-11-25", "EE-9b": "2026-11-26",
      "EE-10": "2026-12-01", "EE-11": "2026-12-09", "EE-12": "2026-12-10", "EE-13a": "2027-01-27", "EE-13c": "2027-01-29",
      "LV-1a": "2026-10-08", "LV-1b": "2026-10-09", "LV-2side": "2027-03-17", "LV-2a": "2027-03-18", "LV-2b": "2027-03-19",
      "LT-1a": "2026-10-14", "LT-1b": "2026-10-15", "LT-2": "2026-10-15", "LT-3": "2026-11-19", "LT-4a": "2026-11-26", "LT-4b": "2026-11-27"}
print("weekday check:", {k: datetime.date.fromisoformat(v).strftime('%a') for k, v in ev.items()})
print("weekend days among events:", [k for k, v in ev.items() if datetime.date.fromisoformat(v).weekday() >= 5])
print("tickets: RUP 239 + sTARTUp 109 + TechChill 359 =", 239 + 109 + 359, "| with visitor/regular tickets 349+129+359 =", 349 + 129 + 359)
print("interview acceptance needed: ELEA 65:", f"{15/65:.1%}-{20/65:.1%}", "| ELEA 68:", f"{15/68:.1%}-{20/68:.1%}",
      "| LINEKA 42:", f"{15/42:.1%}-{20/42:.1%}", "| LINEKA 60:", f"{15/60:.1%}-{20/60:.1%}")

# ------------------------------------------------------------------ 5. red-team scenario grids (A-WS8-xx)
print("\nCRM mid price net EUR/h vs sales hours per won client (delivery 25 h):")
for sh in (6, 12, 25, 40, 60):
    print(f"  sales {sh:>2} h: low {unit(CRM, 1200, sales=sh)[0]:.1f} | mid {unit(CRM, 2500, sales=sh)[0]:.1f} | high {unit(CRM, 5000, sales=sh)[0]:.1f}")
print("break-even sales hours per win for net EUR 15/h (CRM, delivery 25 h):")
for p in (1200, 2500, 5000):
    h_total = net_fie(p) / 15
    print(f"  price {p}: total hours allowed {h_total:.1f} -> sales hours {h_total - 25 - 2 - 3:.1f}")
print("\ncontacts needed per won client = 1 / (reply x meeting-per-reply x win-per-meeting)  [scenario grid, inputs are placeholders]")
grid = []
for reply, mtg, win in itertools.product((0.03, 0.05), (0.25, 0.5), (0.2, 0.3)):
    grid.append((reply, mtg, win, 1 / (reply * mtg * win)))
for g in grid: print(f"  reply {g[0]:.0%} x meeting/reply {g[1]:.0%} x win/meeting {g[2]:.0%} -> {g[3]:.0f} contacts per win")
lo, hi = min(g[3] for g in grid), max(g[3] for g in grid)
print(f"  range {lo:.0f}-{hi:.0f} contacts per win")
for c in ("EE", "LV", "LT"):
    r = res[c]
    plo, phi = r['low50'] * le50[2], r['high50'] * all22[2]      # corrected named-e-mail pool, 11-50 bucket (A-WS9-02)
    print(f"  {c}: named-email pool, 11-50 bucket {plo:,.0f}-{phi:,.0f} -> wins if every firm is contacted once: {plo/hi:.1f}-{phi/lo:.1f}")
print("\nwins per quarter (13 weeks) if half of the weekly hours go to selling (A-WS8-06):")
for S in (12, 25, 40, 60):
    print(f"  {S:>2} sales h per win: " + " | ".join(f"{H} h/wk -> {13*H*0.5/S:.1f}" for H in (10, 15, 20)))
print("entry-price ratios (A-WS8-05):", f"floor net15 {floor_project(AUT,15):,.0f}/300 = {floor_project(AUT,15)/300:.1f}x; net25 {floor_project(AUT,25):,.0f}/300 = {floor_project(AUT,25)/300:.1f}x; vs EUR 100: {floor_project(AUT,15)/100:.1f}x-{floor_project(AUT,25)/100:.1f}x")
