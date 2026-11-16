# Methodology: Capability Dependency Model

> "You cannot invent the steam engine without cylinder boring; you cannot bore cylinders without the slide-rest lathe; you cannot build lathes without flat surface plates; you cannot scrape surface plates without hardened steel chisels."

---

## 1. Graph Theoretical Foundations

The Prophet Project models technological civilization as a **Directed Acyclic Graph (DAG)** of capabilities:

$$G = (V, E)$$

Where:
- $V$ is the set of capabilities (technologies, institutional practices, metrology standards).
- $E$ is the set of directed dependency edges $(u, v)$ indicating that capability $u$ is a strict prerequisite for capability $v$.

```
[ Root Node: Flint Knapping ] ---------> [ Fiber Hafting ] ---------> [ Standard Metrology ]
                                                                                |
                                                                                v
[ Root Node: Friction Fire ] ----------> [ Earthenware Pottery ] ----> [ Copper Smelting ]
```

### AND / OR Prerequisite Logic
- **AND Prerequisites (`prerequisites_all`)**: All listed capabilities must reach minimum maturity before the dependent capability can be developed.
- **OR Prerequisites (`prerequisites_any`)**: Alternative technological or material pathways (e.g., either alluvial tin from trade OR arsenical copper as a temporary substitute; either coal-coke OR hydroelectric power).
- **Acyclicity Constraint**: The graph must contain **zero directed cycles** ($\forall v, v \not\to^* v$). Circular dependencies represent logical impossibilities in physical reality.

---

## 2. Technology Capability Levels (T-Levels)

To avoid confusing a laboratory demonstration with an operating industry, every node is assigned a capability readiness tier:

| Level | Designation | Operational Definition |
|---|---|---|
| **T0** | Principle Understood | Theoretical or physical mechanism is known conceptually. |
| **T1** | Demonstrated | A proof-of-concept prototype functions under controlled conditions. |
| **T2** | Repeatable Prototype | Multiple independent teams can build working replicas. |
| **T3** | Pilot Process | A small production facility operates with measured inputs and outputs. |
| **T4** | Scaled Capability | Production reliably supplies multiple regional workshops or cities. |
| **T5** | Maintainable Industry | The society independently sources inputs, trains staff, and repairs tools. |
| **T6** | Resilient Infrastructure | The capability survives regional wars, epidemics, or supply cuts via redundancy. |

---

## 3. The Critical Path Principle

The **Critical Path** through the civilizational dependency graph is the longest sequence of dependent nodes from primitive tools to modern technology. 
Accelerating civilizational development requires identifying which nodes lie on this critical path and investing engineering and educational resources to clear bottlenecks before dependent industries are held back.
