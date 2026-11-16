#!/usr/bin/env python3
"""
Calculates labor allocation, specialized workforce growth, and caloric food surplus requirements
across the technological phases.
"""
import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

DAILY_CALORIC_REQUIREMENT_KCAL = 2500
WHEAT_CALORIC_DENSITY_KCAL_PER_KG = 3400
KG_WHEAT_PER_PERSON_YEAR = (DAILY_CALORIC_REQUIREMENT_KCAL * 365) / WHEAT_CALORIC_DENSITY_KCAL_PER_KG  # ~268 kg/person/yr

def load_data():
    with open(DATA_DIR / "phases.json", "r", encoding="utf-8") as f:
        phases = json.load(f)
    with open(DATA_DIR / "technologies.json", "r", encoding="utf-8") as f:
        technologies = json.load(f)
    with open(DATA_DIR / "workforce.json", "r", encoding="utf-8") as f:
        skills = json.load(f)
    return phases, technologies, skills

def calculate_workforce_balances():
    phases, technologies, skills = load_data()

    print("=" * 65)
    print("PROPHET PROJECT: WORKFORCE & CALORIC SURPLUS BALANCE MODEL")
    print("=" * 65)

    # Estimate required specialist workforce by phase
    phase_tech_counts = {p["phase"]: 0 for p in phases}
    phase_labor_days = {p["phase"]: 0.0 for p in phases}

    for t in technologies:
        start_p, end_p = t["phase_window"]
        phase_tech_counts[start_p] += 1
        for inp in t.get("inputs", []):
            if inp.get("unit") == "person_days" and inp.get("quantity"):
                phase_labor_days[start_p] += inp["quantity"]

    print("\nPhase Technology & Labor Demands:")
    for p in phases:
        p_idx = p["phase"]
        count = phase_tech_counts.get(p_idx, 0)
        p_days = phase_labor_days.get(p_idx, 0)
        print(f"  Phase {p_idx} ({p['name']}): {count:2d} technologies | {p_days:8.1f} initial pilot person-days")

    # Agricultural labor surplus model
    # Baseline: 1 ancient farmer produces surplus for 0.1 to 0.2 non-farmers.
    # Industrial: 1 modern farmer produces surplus for 50-100 non-farmers.
    surplus_ratios = {
        0: 0.10,  # 10% surplus
        1: 0.15,
        2: 0.20,
        3: 0.35,  # Water power & iron plowshares
        4: 0.80,  # Steam threshing & rotation
        5: 3.50,  # Haber-Bosch & early mechanization
        6: 25.0,  # Modern combine harvesters & green revolution
        7: 60.0   # Automated robotics & precision agriculture
    }

    print("\nAgricultural Caloric Multiplier & Feasibility:")
    all_feasible = True
    for p in phases:
        p_idx = p["phase"]
        ratio = surplus_ratios.get(p_idx, 1.0)
        farmers_needed_per_100_specialists = int(100.0 / ratio)
        wheat_reserve_needed_tons_per_1000_specialists = (1000 * KG_WHEAT_PER_PERSON_YEAR) / 1000.0

        print(f"  Phase {p_idx}: Each farmer supports {ratio:.2f} non-farmers "
              f"({farmers_needed_per_100_specialists} farmers per 100 specialists) | "
              f"Grain reserve requirement: {wheat_reserve_needed_tons_per_1000_specialists:.1f} metric tons/yr")

    print("\n[+] Workforce & Food Security Model successfully computed.")
    return True

if __name__ == "__main__":
    success = calculate_workforce_balances()
    sys.exit(0 if success else 1)
