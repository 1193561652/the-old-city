"""Deterministic economy/production projection; not a navigation or combat test.
Run from any directory: python3 tools/balance_projection.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "config/balance_v0_1.json").read_text())
SCALE = 10000  # 0.0001 fund units; avoid tax rounding drift.


def simulate(spec):
    c = CFG
    funds = c["economy"]["initial_funds"] * SCALE
    reserve = spec["reserve"] * SCALE
    cost = c["training"]["cost_per_soldier"] * SCALE
    population = c["population"]["initial_total"]
    eligible = c["population"]["initial_levy_eligible"]
    tax_rate = round(c["economy"]["tax_per_civilian_per_second"] * SCALE)
    projects = [{"requested": t, "kind": k, "started": False, "done": None}
                for t, k in spec["projects"]]
    barracks, soldiers, tax_pending, tax_paid, spent, snapshots = [], 0, 0, 0, 0, []
    minimum = funds
    for t in range(901):
        for b in barracks:
            if b["done"] == t:
                soldiers += 1
                b["done"] = None
        for p in projects:
            if p["started"] and p["done"] == t and p["kind"] == "barracks":
                barracks.append({"done": None})
        for p in projects:
            if p["started"] or p["requested"] > t:
                continue
            v = c["construction"][p["kind"]]
            workers = sum(c["construction"][q["kind"]]["max_workers"]
                          for q in projects if q["started"] and q["done"] > t)
            trainees = sum(b["done"] is not None for b in barracks)
            if funds >= v["cost"] * SCALE and eligible - soldiers - trainees - workers >= v["max_workers"]:
                funds -= v["cost"] * SCALE
                spent += v["cost"] * SCALE
                p["started"] = True
                p["actual_start"] = t
                p["done"] = t + v["work_person_seconds"] // v["max_workers"]
        workers = sum(c["construction"][p["kind"]]["max_workers"]
                      for p in projects if p["started"] and p["done"] > t)
        if t < 900:
            for b in barracks:
                trainees = sum(x["done"] is not None for x in barracks)
                if b["done"] is None and funds - cost >= reserve and eligible - workers - soldiers - trainees > 0:
                    funds -= cost
                    spent += cost
                    b["done"] = t + c["training"]["seconds_per_soldier_per_barracks"]
        trainees = sum(b["done"] is not None for b in barracks)
        assert population - workers - soldiers - trainees >= 0
        assert soldiers + workers + trainees <= eligible
        assert funds >= 0
        minimum = min(minimum, funds)
        # Snapshots are at t, before accruing the next second's tax.
        if t in (180, 420, 600, 780, 900):
            snapshots.append({"seconds": t, "soldiers_trained": soldiers,
                              "trainees": trainees, "funds": round(funds / SCALE, 2),
                              "tax_per_minute": round((population - soldiers - workers - trainees) * tax_rate * 60 / SCALE, 2)})
        if t == 900:
            break
        tax_pending += (population - workers - soldiers - trainees) * tax_rate
        if (t + 1) % c["economy"]["tax_payout_seconds"] == 0:
            funds += tax_pending
            tax_paid += tax_pending
            tax_pending = 0
    assert funds + spent == c["economy"]["initial_funds"] * SCALE + tax_paid
    assert all(p["started"] and p["done"] <= 900 for p in projects)
    return {"snapshots": snapshots, "total_tax": round(tax_paid / SCALE, 2),
            "total_spent": spent / SCALE, "minimum_funds": minimum / SCALE,
            "project_timings": [{"kind": p["kind"], "requested": p["requested"],
                                 "start": p["actual_start"], "complete": p["done"]} for p in projects]}


if __name__ == "__main__":
    result = {"limitations": "No combat, deaths, repairs, retirement, blocked paths or capacity delays. Completed troops assumed promptly deployed; reserve is held, not spent. Trained totals are NOT surviving troops or victory predictions.",
              "scenarios": {name: simulate(spec) for name, spec in CFG["projection_scenarios"].items()}}
    print(json.dumps(result, ensure_ascii=False, indent=2))
