# R120 — Natural Uranium Graphite Reactor (CP-1 Critical Pile)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R120 · NATURAL URANIUM GRAPHITE CRITICAL REACTOR (CP-1)  ║
║  End product: Operational Nuclear Fission Reactor (200 kW)       ║
║  Criticality condition: k_effective >= 1.000                     ║
╠══════════════════════════════════════════════════════════════════╣
║  WHY THIS DOES NOT REQUIRE ENRICHMENT                            ║
║    Uranium ore contains only 0.72% fissile U-235; 99.28% is      ║
║    U-238 (which absorbs fast neutrons without fissioning).       ║
║    Isotope enrichment (centrifuges) takes decades to build.      ║
║    HOWEVER: Enrico Fermi proved in 1942 that with ULTRA-PURE     ║
║    GRAPHITE as a moderator, fast fission neutrons (2 MeV) slow   ║
║    down to thermal velocities (0.025 eV) where the fission cross-║
║    section of U-235 is 580 barns (huge!).                        ║
║    Natural uranium CAN achieve self-sustaining criticality       ║
║    WITHOUT ENRICHMENT if boron impurities in graphite are < 1 ppm!║
╠══════════════════════════════════════════════════════════════════╣
║  INGREDIENTS                                                     ║
║  A) 40 tonnes Ultra-Pure Nuclear-Grade Graphite Blocks           ║
║     [→ R000-C/R025: Petroleum coke baked at 2,800°C graphitization║
║     furnace; chlorine gas purged to remove all boron/cadmium].   ║
║  B) 6 tonnes Natural Uranium Metal Cylinders (3 cm dia × 10 cm)  ║
║     [→ Leached pitchblende ore extracted with TBP solvent,       ║
║     reduced to UF₄, then reduced with magnesium metal at 900°C]. ║
║  C) 30 tonnes Natural Uranium Oxide (UO₂) Pellets                ║
║  D) 6 × Cadmium or Boron-steel control safety rods [→ R040]      ║
╠══════════════════════════════════════════════════════════════════╣
║  CONSTRUCTION: LATTICE GEOMETRY                                  ║
║    1. Lay layer of graphite bricks to form a 7-meter octagonal   ║
║       circular base.                                             ║
║    2. Every second layer: drill 8 cm holes on a 21 cm square     ║
║        lattice spacing. Insert uranium metal/oxide cylinders.    ║
║    3. The geometric spacing is critical: fast neutrons emitted   ║
║       by a uranium lump escape into the surrounding graphite,    ║
║       make ~110 elastic collisions with carbon nuclei, lose      ║
║       speed without being captured by U-238, and drift back into ║
║       the next uranium lump as thermal neutrons to trigger U-235!║
║    4. Insert cadmium control rods deep into vertical channels:   ║
║       Cadmium is a massive thermal neutron sponge (σ = 2,500 b), ║
║       keeping k_eff < 0.95 (subcritical shutdown).               ║
╠══════════════════════════════════════════════════════════════════╣
║  STARTUP & CRITICALITY PROTOCOL                                  ║
║    1. Install BF₃ proportional neutron counter chamber.          ║
║    2. Slowly withdraw cadmium control rod #1 by 10 cm increments.║
║    3. Plot neutron count vs 1/(1-k): as k approaches 1.000,      ║
║       neutron count rate diverges toward infinity!               ║
║    4. At 3.2 m withdrawal: k_effective reaches 1.002.            ║
║       The pile becomes CRITICAL. Self-sustaining chain reaction  ║
║       releases steady megawatt heat and high-flux neutron beams. ║
╚══════════════════════════════════════════════════════════════════╝
```
