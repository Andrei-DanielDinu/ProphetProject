#!/usr/bin/env python3
"""
Validates the technology dependency network using graph theory (NetworkX).
Checks for:
1. Directed Acyclic Graph (DAG) integrity - no cycles.
2. Unresolved prerequisites (dangling references).
3. Critical path calculation from primordial tools to modern frontiers.
"""
import json
import sys
from pathlib import Path
import networkx as nx

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

def load_technologies():
    tech_file = DATA_DIR / "technologies.json"
    with open(tech_file, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_dependencies():
    technologies = load_technologies()
    tech_ids = {t["id"] for t in technologies}
    tech_map = {t["id"]: t for t in technologies}

    G = nx.DiGraph()

    for t in technologies:
        G.add_node(t["id"], name=t["name"], phase=t["phase_window"])

    missing_refs = []
    for t in technologies:
        for prereq in t.get("prerequisites_all", []):
            if prereq not in tech_ids:
                missing_refs.append((t["id"], prereq))
            else:
                # Directed edge from prerequisite to dependent technology
                G.add_edge(prereq, t["id"])

    print("=" * 60)
    print("PROPHET PROJECT: DEPENDENCY GRAPH ANALYSIS")
    print("=" * 60)
    print(f"Total Technologies: {G.number_of_nodes()}")
    print(f"Total Dependency Edges: {G.number_of_edges()}")

    if missing_refs:
        print("\n[!] MISSING PREREQUISITES FOUND:")
        for child, missing in missing_refs:
            print(f"    Technology '{child}' requires non-existent '{missing}'")
        return False

    # Check for cycles
    if not nx.is_directed_acyclic_graph(G):
        print("\n[!] CYCLES DETECTED IN DEPENDENCY GRAPH:")
        cycles = list(nx.simple_cycles(G))
        for c in cycles:
            print(f"    Cycle: {' -> '.join(c)}")
        return False
    else:
        print("\n[+] Dependency Graph is a valid Directed Acyclic Graph (DAG) - 0 cycles.")

    # Roots and Leaves
    roots = [n for n in G.nodes() if G.in_degree(n) == 0]
    leaves = [n for n in G.nodes() if G.out_degree(n) == 0]

    print(f"\nRoot Capabilities (Sticks & Stones / Zero prerequisites): {len(roots)}")
    for r in roots:
        print(f"  * {r} ({tech_map[r]['name']})")

    print(f"\nFrontier Capabilities (Terminal Nodes): {len(leaves)}")
    for l in leaves:
        print(f"  * {l} ({tech_map[l]['name']})")

    # Longest path (Critical Path)
    longest_path = nx.dag_longest_path(G)
    print(f"\nCivilizational Critical Path Depth: {len(longest_path)} tiers")
    print("Step-by-step Critical Path:")
    for idx, node in enumerate(longest_path, 1):
        print(f"  {idx:2d}. [{tech_map[node]['capability_level']}] {tech_map[node]['name']} ({node})")

    return True

if __name__ == "__main__":
    success = validate_dependencies()
    sys.exit(0 if success else 1)
