#!/usr/bin/env python3
"""
WS5 unit-economics models - "Baltic Revenue Engine" research (EE / LV / LT), 2026-10-03.

Re-run:   python3 research/_work/data/WS5_models.py
Writes:   research/_work/data/WS5_models.csv  (long format: one row per scenario x metric)
Prints:   the markdown tables used in research/05_pricing_unit_economics.md (sections 3, 6, 7)

Every input cites an assumption id (A-WS5-xx -> research/_work/assumptions_WS5.md) or a
source id (WS5-xxx / WS2-xxx / WS3-xxx -> research/_work/sources_WS*.csv).
Unverified cost items are explicit allowances (ESTIMATE, low confidence); a verifier can
replace any parameter below and re-run. Standard library only.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_CSV = os.path.join(HERE, "WS5_models.csv")

# ----------------------------------------------------------------------------------------
# 1. Tax and VAT - Estonia 2026, FIE (sole trader) employed elsewhere
# ----------------------------------------------------------------------------------------
SOCIAL_TAX = 0.33                # WS5-001, WS5-002
INCOME_TAX = 0.22                # WS5-006 (2026 rate), WS5-007
SOCIAL_TAX_CAP_2026 = 36867.60   # WS5-002; A-WS5-05 (not binding at modelled scale)
II_PILLAR = 0.02                 # WS5-010; A-WS5-04 (default rate; 4%/6% optional)
ENTRE_ACCOUNT_RATE = 0.20        # WS5-018; A-WS5-06 (+0.02 with II pillar)
ENTRE_ACCOUNT_CEILING = 40000.0  # WS5-018
VAT = 0.24                       # WS5-011; A-WS5-07 (tool costs carry non-deductible VAT)


def tax_fie(profit, ii_pillar=False, ii_deductible=True):
    """Official FIE mechanism (A-WS5-01):
       S  = 0.33 * P / 1.33   (social tax deducted from its own base; capped)
       F  = 0.02 * P / 1.33   (II pillar, optional variant, A-WS5-04)
       IT = 0.22 * (P - S [- F])
       net = P - S - F - IT   (F is the operator's own pension saving)"""
    if profit <= 0:
        return {"social": 0.0, "ii": 0.0, "income": 0.0, "net": profit}
    social = min(SOCIAL_TAX * profit / (1 + SOCIAL_TAX), SOCIAL_TAX_CAP_2026)
    ii = II_PILLAR * profit / (1 + SOCIAL_TAX) if ii_pillar else 0.0
    income = INCOME_TAX * (profit - social - (ii if ii_deductible else 0.0))
    return {"social": social, "ii": ii, "income": income, "net": profit - social - ii - income}


def tax_naive(profit):
    """Literal reading of the brief (shown only to flag the gap, A-WS5-01):
       S = 0.33 * P ; IT = 0.22 * (P - S)."""
    if profit <= 0:
        return {"social": 0.0, "ii": 0.0, "income": 0.0, "net": profit}
    social = SOCIAL_TAX * profit
    income = INCOME_TAX * (profit - social)
    return {"social": social, "ii": 0.0, "income": income, "net": profit - social - income}


def tax_entre_account(receipts, costs, ii_pillar=False):
    """Entrepreneur account (A-WS5-06): flat tax on gross receipts, no cost deduction.
       Only conceivable for non-Estonian legal-person clients; eligibility UNKNOWN."""
    rate = ENTRE_ACCOUNT_RATE + (0.02 if ii_pillar else 0.0)
    tax = rate * receipts
    return {"social": 0.0, "ii": 0.0, "income": tax, "net": receipts - costs - tax}


NET_SHARE = tax_fie(100.0)["net"] / 100.0  # 0.5865 (A-WS5-01)

# ----------------------------------------------------------------------------------------
# 2. Capacity and overhead
# ----------------------------------------------------------------------------------------
WEEKS_PER_YEAR = 46           # A-WS5-08
WEEKLY_HOURS = [10, 15, 20]   # A-WS5-09 (BRIEF section 2)
FIXED_ADMIN_H = 72            # A-WS5-10 (hours per year)
FX_EUR_PER_USD = 0.86         # A-WS5-12 (working rate, immaterial)
OVERHEAD = {                  # A-WS5-11: Claude subscription (WS5-020) + allowance (UNKNOWN items)
    "low": {"claude_usd": 200, "other_eur": 150},    # Claude Pro, annual billing
    "base": {"claude_usd": 240, "other_eur": 350},   # Claude Pro, monthly billing (12 x $20)
    "high": {"claude_usd": 1200, "other_eur": 700},  # Claude Max 'from $100/month'
}


def overhead_eur(level="base"):
    o = OVERHEAD[level]
    return o["claude_usd"] * FX_EUR_PER_USD * (1 + VAT) + o["other_eur"]


# ----------------------------------------------------------------------------------------
# 3. Model parameters
# ----------------------------------------------------------------------------------------
PROJECTS = {
    "CRM setup": {
        "prices": [1200, 2500, 5000],              # A-WS5-13 (WS3-005, WS3-017, WS2-007/009, WS3-019, WS2-020)
        "delivery_h": 25, "delivery_range": (15, 40),   # A-WS5-14 (WS3-018, WS3-057)
        "sales_h": 12, "sales_range": (6, 25),          # A-WS5-15
        "admin_h": 2.0,                                 # A-WS5-16
        "support_h": 3.0,                               # A-WS5-17
        "direct_cost": 0.0, "direct_range": (0, 100),   # A-WS5-18
        "elapsed_weeks": 6,                             # A-WS5-34 (WS3-057)
        "daytime_share": 0.25,                          # A-WS5-33
    },
    "Automation project": {
        "prices": [450, 1200, 3000],               # A-WS5-19 (WS3-024)
        "delivery_h": 15, "delivery_range": (8, 30),    # A-WS5-20
        "sales_h": 8, "sales_range": (4, 16),           # A-WS5-21
        "admin_h": 1.5,                                 # A-WS5-22
        "support_h": 3.0,                               # A-WS5-22
        "direct_cost": 10.0, "direct_range": (0, 50),   # A-WS5-23 (WS5-020)
        "elapsed_weeks": 3,                             # A-WS5-34
        "daytime_share": 0.10,                          # A-WS5-33
    },
}
RETAINER = {
    "name": "Lead-gen retainer",
    "prices": [1000, 1800, 2850],                  # A-WS5-25 (WS3-008)
    "delivery_h_month": 20, "delivery_range": (14, 30),  # A-WS5-26
    "onboarding_h": 15,                                  # A-WS5-27
    "sales_h": 15, "sales_range": (8, 30),               # A-WS5-28
    "churn": 0.15, "churn_range": (0.08, 0.25),          # A-WS5-29 (WS3-008 month-to-month)
    "tools_month": 150, "tools_range": (80, 300),        # A-WS5-30 (allowance incl. VAT)
    "admin_h_month": 1.0,                                # A-WS5-31
    "setup_fee": 0, "setup_fee_alt": 900,                # A-WS5-32 (WS3-008: 3,750 - 2,850)
    "daytime_share": 0.30,                               # A-WS5-33
}
TARGETS_NET_PER_H = [15, 25, 40]   # A-WS5-36 (scenario targets, not benchmarks)

# ----------------------------------------------------------------------------------------
# 4. Unit economics
# ----------------------------------------------------------------------------------------


def apply_tax(regime, revenue, cost):
    profit = revenue - cost
    if regime == "fie":
        return tax_fie(profit)
    if regime == "fie_ii":
        return tax_fie(profit, ii_pillar=True)
    if regime == "naive":
        return tax_naive(profit)
    if regime == "entre":
        return tax_entre_account(revenue, cost)
    raise ValueError(regime)


def project_unit(p, price, delivery_h=None, sales_h=None, direct=None, regime="fie"):
    d = p["delivery_h"] if delivery_h is None else delivery_h
    s = p["sales_h"] if sales_h is None else sales_h
    c = p["direct_cost"] if direct is None else direct
    hours = d + s + p["admin_h"] + p["support_h"]
    t = apply_tax(regime, price, c)
    profit = price - c
    return {
        "revenue": price, "cost": c, "hours": hours, "profit": profit,
        "social": t["social"], "ii": t["ii"], "income_tax": t["income"], "net": t["net"],
        "gross_per_h": profit / hours, "net_per_h": t["net"] / hours,
        "billed_rate": price / d,
    }


def retainer_unit(r, price, churn=None, tools=None, delivery_h=None, sales_h=None,
                  setup_fee=None, regime="fie"):
    ch = r["churn"] if churn is None else churn
    L = 1.0 / ch                                    # expected lifetime in months (A-WS5-29)
    tl = r["tools_month"] if tools is None else tools
    d = r["delivery_h_month"] if delivery_h is None else delivery_h
    s = r["sales_h"] if sales_h is None else sales_h
    sf = r["setup_fee"] if setup_fee is None else setup_fee
    revenue = price * L + sf
    cost = tl * L
    hours = d * L + r["onboarding_h"] + s + r["admin_h_month"] * L
    t = apply_tax(regime, revenue, cost)
    profit = revenue - cost
    return {
        "lifetime_months": L, "revenue": revenue, "cost": cost, "hours": hours, "profit": profit,
        "social": t["social"], "ii": t["ii"], "income_tax": t["income"], "net": t["net"],
        "gross_per_h": profit / hours, "net_per_h": t["net"] / hours,
        "billed_rate": price / d,
    }


def required_price_project(p, target):
    hours = p["delivery_h"] + p["sales_h"] + p["admin_h"] + p["support_h"]
    return target * hours / NET_SHARE + p["direct_cost"]


def required_price_retainer(r, target):
    L = 1.0 / r["churn"]
    hours = r["delivery_h_month"] * L + r["onboarding_h"] + r["sales_h"] + r["admin_h_month"] * L
    return target * hours / (NET_SHARE * L) + r["tools_month"]

# ----------------------------------------------------------------------------------------
# 5. Annual capacity (supply-side ceiling, A-WS5-38)
# ----------------------------------------------------------------------------------------


def annual_project(p, price, H, overhead_level="base"):
    annual_h = H * WEEKS_PER_YEAR
    avail = annual_h - FIXED_ADMIN_H
    unit_h = p["delivery_h"] + p["sales_h"] + p["admin_h"] + p["support_h"]
    n = avail / unit_h
    revenue = n * price
    profit = n * (price - p["direct_cost"]) - overhead_eur(overhead_level)
    t = tax_fie(profit)
    return {
        "units_per_year": n, "concurrent": n * p["elapsed_weeks"] / WEEKS_PER_YEAR,
        "revenue": revenue, "profit": profit, "net": t["net"],
        "net_per_h": t["net"] / annual_h, "annual_h": annual_h,
        "daytime_h_week": H * p["daytime_share"],
    }


def annual_retainer(r, price, H, overhead_level="base"):
    annual_h = H * WEEKS_PER_YEAR
    avail_month = (annual_h - FIXED_ADMIN_H) / 12.0
    per_client_month_h = (r["delivery_h_month"] + r["admin_h_month"]
                          + r["churn"] * (r["onboarding_h"] + r["sales_h"]))
    n = avail_month / per_client_month_h
    revenue = n * 12 * (price + r["churn"] * r["setup_fee"])
    profit = revenue - n * 12 * r["tools_month"] - overhead_eur(overhead_level)
    t = tax_fie(profit)
    return {
        "units_per_year": n * 12 * r["churn"],     # new clients needed per year (replacement)
        "concurrent": n, "revenue": revenue, "profit": profit, "net": t["net"],
        "net_per_h": t["net"] / annual_h, "annual_h": annual_h,
        "daytime_h_week": H * r["daytime_share"],
    }

# ----------------------------------------------------------------------------------------
# 6. Run all scenarios, write CSV, print markdown
# ----------------------------------------------------------------------------------------


def eur(x, d=0):
    return f"€{x:,.{d}f}"


def main():
    rows = []

    def rec(section, model, scenario, metrics):
        for k, v in metrics.items():
            rows.append({"section": section, "model": model, "scenario": scenario,
                         "metric": k, "value": round(v, 4) if isinstance(v, float) else v})

    # --- 6.0 tax regimes on EUR 1,000 profit
    print("\n### T1 Tax on EUR 1,000 of FIE profit (2026)\n")
    print("| Regime | Social tax | II pillar | Income tax | Net | Net share |")
    print("|---|---|---|---|---|---|")
    for name, t in [("Official FIE formula (A-WS5-01)", tax_fie(1000)),
                    ("Official + II pillar 2% (A-WS5-04)", tax_fie(1000, True)),
                    ("Literal brief reading (S=0.33P)", tax_naive(1000)),
                    ("Entrepreneur account, zero costs (A-WS5-06)", tax_entre_account(1000, 0))]:
        print(f"| {name} | {eur(t['social'],2)} | {eur(t['ii'],2)} | {eur(t['income'],2)} | "
              f"{eur(t['net'],2)} | {t['net']/1000:.2%} |")
        rec("tax", "all", name, {k: v for k, v in t.items()})

    # --- 6.1 price sensitivity (base hours/churn/tools)
    print("\n### T2 Unit economics at three price levels (base inputs, FIE official tax)\n")
    print("| Model | Price (excl. VAT) | Hours per unit | Billed rate per delivery h | "
          "Pre-tax profit per unit | Net after tax per unit | Gross €/h | **Net €/h** |")
    print("|---|---|---|---|---|---|---|---|")
    for name, p in PROJECTS.items():
        for price in p["prices"]:
            u = project_unit(p, price)
            rec("price_sensitivity", name, f"price={price}", u)
            print(f"| {name} | {eur(price)} | {u['hours']:.1f} | {eur(u['billed_rate'])} | "
                  f"{eur(u['profit'])} | {eur(u['net'])} | {eur(u['gross_per_h'],1)} | "
                  f"**{eur(u['net_per_h'],1)}** |")
    for price in RETAINER["prices"]:
        u = retainer_unit(RETAINER, price)
        rec("price_sensitivity", RETAINER["name"], f"price={price}", u)
        print(f"| {RETAINER['name']} (per client lifetime {u['lifetime_months']:.1f} mo) | "
              f"{eur(price)}/mo | {u['hours']:.1f} | {eur(u['billed_rate'])} | {eur(u['profit'])} | "
              f"{eur(u['net'])} | {eur(u['gross_per_h'],1)} | **{eur(u['net_per_h'],1)}** |")

    # --- 6.2 delivery-hours sensitivity
    print("\n### T3 Net €/h - delivery hours (low / base / high) x price\n")
    print("| Model | Delivery hours | " + " | ".join(["Low price", "Mid price", "High price"]) + " |")
    print("|---|---|---|---|---|")
    for name, p in PROJECTS.items():
        for dh in [p["delivery_range"][0], p["delivery_h"], p["delivery_range"][1]]:
            vals = []
            for price in p["prices"]:
                u = project_unit(p, price, delivery_h=dh)
                rec("delivery_hours", name, f"delivery_h={dh};price={price}", {"net_per_h": u["net_per_h"]})
                vals.append(eur(u["net_per_h"], 1))
            print(f"| {name} | {dh} | " + " | ".join(vals) + " |")
    r = RETAINER
    for dh in [r["delivery_range"][0], r["delivery_h_month"], r["delivery_range"][1]]:
        vals = []
        for price in r["prices"]:
            u = retainer_unit(r, price, delivery_h=dh)
            rec("delivery_hours", r["name"], f"delivery_h_month={dh};price={price}", {"net_per_h": u["net_per_h"]})
            vals.append(eur(u["net_per_h"], 1))
        print(f"| {r['name']} | {dh}/month | " + " | ".join(vals) + " |")

    # --- 6.3 sales-hours sensitivity
    print("\n### T4 Net €/h - sales hours per won client (low / base / high) x price\n")
    print("| Model | Sales h per win | Low price | Mid price | High price |")
    print("|---|---|---|---|---|")
    for name, p in PROJECTS.items():
        for sh in [p["sales_range"][0], p["sales_h"], p["sales_range"][1]]:
            vals = []
            for price in p["prices"]:
                u = project_unit(p, price, sales_h=sh)
                rec("sales_hours", name, f"sales_h={sh};price={price}", {"net_per_h": u["net_per_h"]})
                vals.append(eur(u["net_per_h"], 1))
            print(f"| {name} | {sh} | " + " | ".join(vals) + " |")
    for sh in [r["sales_range"][0], r["sales_h"], r["sales_range"][1]]:
        vals = []
        for price in r["prices"]:
            u = retainer_unit(r, price, sales_h=sh)
            rec("sales_hours", r["name"], f"sales_h={sh};price={price}", {"net_per_h": u["net_per_h"]})
            vals.append(eur(u["net_per_h"], 1))
        print(f"| {r['name']} | {sh} | " + " | ".join(vals) + " |")

    # --- 6.4 lead-gen churn, tools, setup fee
    print("\n### T5 Lead-gen retainer - churn x price (net €/h; lifetime in months)\n")
    print("| Monthly churn | Lifetime (months) | €1,000/mo | €1,800/mo | €2,850/mo |")
    print("|---|---|---|---|---|")
    for ch in [r["churn_range"][0], r["churn"], r["churn_range"][1]]:
        vals = []
        for price in r["prices"]:
            u = retainer_unit(r, price, churn=ch)
            rec("churn", r["name"], f"churn={ch};price={price}", {"net_per_h": u["net_per_h"]})
            vals.append(eur(u["net_per_h"], 1))
        print(f"| {ch:.0%} | {1/ch:.1f} | " + " | ".join(vals) + " |")
    print("\n### T6 Lead-gen retainer - tools & data allowance and setup fee x price (net €/h)\n")
    print("| Variant | €1,000/mo | €1,800/mo | €2,850/mo |")
    print("|---|---|---|---|")
    for tl in [r["tools_range"][0], r["tools_month"], r["tools_range"][1]]:
        vals = []
        for price in r["prices"]:
            u = retainer_unit(r, price, tools=tl)
            rec("tools", r["name"], f"tools_month={tl};price={price}", {"net_per_h": u["net_per_h"]})
            vals.append(eur(u["net_per_h"], 1))
        print(f"| Tools {eur(tl)}/client-month | " + " | ".join(vals) + " |")
    vals = []
    for price in r["prices"]:
        u = retainer_unit(r, price, setup_fee=r["setup_fee_alt"])
        rec("setup_fee", r["name"], f"setup_fee={r['setup_fee_alt']};price={price}", {"net_per_h": u["net_per_h"]})
        vals.append(eur(u["net_per_h"], 1))
    print(f"| Base tools + {eur(r['setup_fee_alt'])} setup fee | " + " | ".join(vals) + " |")

    # --- 6.5 tax-regime comparison at mid price
    print("\n### T7 Tax regime comparison at the mid price (net €/h)\n")
    print("| Model (mid price) | Official FIE | FIE + II pillar 2% | Literal brief reading | "
          "Entrepreneur account (foreign clients; eligibility UNKNOWN) |")
    print("|---|---|---|---|---|")
    for name, p in PROJECTS.items():
        price = p["prices"][1]
        vals = []
        for reg in ["fie", "fie_ii", "naive", "entre"]:
            u = project_unit(p, price, regime=reg)
            rec("tax_regime", name, f"regime={reg};price={price}", {"net_per_h": u["net_per_h"]})
            vals.append(eur(u["net_per_h"], 1))
        print(f"| {name} ({eur(price)}) | " + " | ".join(vals) + " |")
    price = r["prices"][1]
    vals = []
    for reg in ["fie", "fie_ii", "naive", "entre"]:
        u = retainer_unit(r, price, regime=reg)
        rec("tax_regime", r["name"], f"regime={reg};price={price}", {"net_per_h": u["net_per_h"]})
        vals.append(eur(u["net_per_h"], 1))
    print(f"| {r['name']} ({eur(price)}/mo) | " + " | ".join(vals) + " |")

    # --- 6.6 required price for target net EUR/h
    print("\n### T8 Price required to reach a target net €/h (base inputs)\n")
    print("| Model | Net €15/h | Net €25/h | Net €40/h |")
    print("|---|---|---|---|")
    for name, p in PROJECTS.items():
        vals = []
        for tg in TARGETS_NET_PER_H:
            pr = required_price_project(p, tg)
            rec("required_price", name, f"target={tg}", {"price": pr})
            vals.append(eur(pr))
        print(f"| {name} (per project) | " + " | ".join(vals) + " |")
    vals = []
    for tg in TARGETS_NET_PER_H:
        pr = required_price_retainer(r, tg)
        rec("required_price", r["name"], f"target={tg}", {"price": pr})
        vals.append(eur(pr) + "/mo")
    print(f"| {r['name']} (per month) | " + " | ".join(vals) + " |")

    # --- 6.7 capacity
    print("\n### T9 Capacity at 10 / 15 / 20 h per week (mid price, base overhead "
          f"{eur(overhead_eur('base'))}/yr, supply-side ceiling)\n")
    print("| Model | h/week | Annual hours | Units per year (projects) or new clients per year (retainer) | "
          "Concurrent | Revenue/yr (excl. VAT) | Pre-tax profit/yr | Net/yr | Net €/h all-in | "
          "Daytime h/week needed |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for name, p in PROJECTS.items():
        price = p["prices"][1]
        for H in WEEKLY_HOURS:
            a = annual_project(p, price, H)
            rec("capacity", name, f"H={H};price={price}", a)
            print(f"| {name} | {H} | {a['annual_h']:.0f} | {a['units_per_year']:.1f} | {a['concurrent']:.1f} | "
                  f"{eur(a['revenue'])} | {eur(a['profit'])} | {eur(a['net'])} | {eur(a['net_per_h'],1)} | "
                  f"{a['daytime_h_week']:.1f} |")
    price = r["prices"][1]
    for H in WEEKLY_HOURS:
        a = annual_retainer(r, price, H)
        rec("capacity", r["name"], f"H={H};price={price}", a)
        print(f"| {r['name']} | {H} | {a['annual_h']:.0f} | {a['units_per_year']:.1f} | {a['concurrent']:.1f} | "
              f"{eur(a['revenue'])} | {eur(a['profit'])} | {eur(a['net'])} | {eur(a['net_per_h'],1)} | "
              f"{a['daytime_h_week']:.1f} |")

    # --- 6.8 capacity across all three price levels (net per hour all-in, 15 h/week)
    print("\n### T10 All-in net €/h at capacity (incl. fixed admin hours and base overhead) "
          "- 10 / 15 / 20 h per week x price\n")
    print("| Model | Price | 10 h/wk | 15 h/wk | 20 h/wk |")
    print("|---|---|---|---|---|")
    for name, p in PROJECTS.items():
        for price in p["prices"]:
            vals = []
            for H in WEEKLY_HOURS:
                a = annual_project(p, price, H)
                rec("capacity_allin", name, f"H={H};price={price}", {"net_per_h": a["net_per_h"], "net": a["net"]})
                vals.append(f"{eur(a['net_per_h'],1)} ({eur(a['net'])}/yr)")
            print(f"| {name} | {eur(price)} | " + " | ".join(vals) + " |")
    for price in r["prices"]:
        vals = []
        for H in WEEKLY_HOURS:
            a = annual_retainer(r, price, H)
            rec("capacity_allin", r["name"], f"H={H};price={price}", {"net_per_h": a["net_per_h"], "net": a["net"]})
            vals.append(f"{eur(a['net_per_h'],1)} ({eur(a['net'])}/yr)")
        print(f"| {r['name']} | {eur(price)}/mo | " + " | ".join(vals) + " |")

    # --- 6.9 LLM run-cost example (A-WS5-24)
    print("\n### T11 Client LLM run-cost example: 300 inquiries/month x (3,000 in + 800 out tokens)\n")
    print("| Model | USD in/out per MTok (WS5-020) | USD per month |")
    print("|---|---|---|")
    for m, pin, pout in [("Haiku 4.5", 1, 5), ("Sonnet 5.5", 2, 10), ("Opus 5.5", 4, 20)]:
        usd = 300 * (3000 * pin + 800 * pout) / 1_000_000
        rec("llm_cost", m, "300 inquiries/month", {"usd_per_month": usd})
        print(f"| {m} | {pin} / {pout} | ${usd:.2f} |")

    print(f"\nOverhead scenarios (EUR/yr): low {overhead_eur('low'):.0f}, base {overhead_eur('base'):.0f}, "
          f"high {overhead_eur('high'):.0f}; FIE net share of profit = {NET_SHARE:.4f}")

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["section", "model", "scenario", "metric", "value"],
                           quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    print(f"\nwrote {len(rows)} rows -> {OUT_CSV}")


if __name__ == "__main__":
    main()
