# R037 — Sintered Tungsten Carbide (Hardmetal Tooling)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R037 · SINTERED TUNGSTEN CARBIDE CUTTING INSERTS          ║
║  End product: 100 × CNC/Lathe Cutting Inserts (WC-6Co, Grade K10)║
║  Hardness: 92 HRA / 1,600 HV (second only to diamond)            ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The wear-resistant machining material required for:           ║
║    • High-speed metal cutting lathes and milling machines [→ R072]║
║    • Deep rock drilling roller-cone bits for petroleum [→ R054]  ║
║    • Precision wire drawing dies for micro-wires [→ R084, R091]  ║
║    • Armor-piercing penetrators and high-pressure extrusion dies ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Tungsten Trioxide Powder (WO₃, >99.9%): 15 kg [→ R091]     ║
║    2. Ultra-fine Carbon Black: 1.0 kg [→ R025 lampblack pyrolysis]║
║    3. Cobalt Metal Powder (Co, <2 μm particle size): 1.0 kg      ║
║       [→ R000-F cobaltite ore reduction]                         ║
║    4. Paraffin Wax (temporary pressing binder): 200 g [→ R054]   ║
║    5. Hydrogen Gas Furnace (H₂ dry, -60°C dew point): [→ R052]   ║
║    6. Carbide-lined Planetary Ball Mill: 1 [→ R040, R036]        ║
║    7. Hydraulic Compacting Press (200 MPa): 1 [→ R070]           ║
║    8. High-Vacuum Sintering Furnace (1,450°C, <1 Pa): 1 [→ R092] ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: CARBURIZATION (TUNGSTEN METAL TO TUNGSTEN CARBIDE WC)  ║
║    1a. Reduce WO₃ powder in dry H₂ tube furnace at 850°C to pure ║
║        fine tungsten metal powder (particle size ~1.5 μm):       ║
║        WO₃ + 3 H₂ ──► W + 3 H₂O↑.                                ║
║    1b. Intimately blend 11.9 kg W powder with 0.776 kg carbon    ║
║        black (stoichiometric 6.13% C by weight).                 ║
║    1c. Charge powder into high-purity graphite crucibles [→ R025].║
║    1d. Heat in hydrogen resistance furnace to 1,450°C for 3 hrs: ║
║        W + C ──► WC (Mono-tungsten carbide).                     ║
║    1e. Sieve synthesized WC through 325-mesh screen.             ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: MILLING, SPRAY-DRYING & COMPACTION                     ║
║    2a. Charge 94 wt% WC powder + 6 wt% Cobalt powder + 2 wt%    ║
║        paraffin wax + ethanol into carbide-lined ball mill.      ║
║    2b. Mill for 72 hours with WC balls to smear ductile cobalt   ║
║        uniformly over every microscopic WC crystal grain.        ║
║    2c. Vacuum dry milled slurry to evaporate ethanol. Granulate  ║
║        free-flowing spherical granules (<100 μm).                ║
║    2d. Compact granules in hardened tool steel dies [→ R047] at  ║
║        200 MPa hydraulic pressure into indexable insert blanks   ║
║        (12 mm × 12 mm × 4 mm triangles and squares).             ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: LIQUID-PHASE VACUUM SINTERING                          ║
║    3a. Load green compacts on graphite trays dusted with Al₂O₃.  ║
║    3b. Dewaxing stage: Heat in vacuum furnace to 450°C under     ║
║        flowing H₂ sweep to vaporize paraffin wax completely.     ║
║    3c. Vacuum ramping: Pump down to 0.1 Pa vacuum. Ramp to       ║
║        1,420°C (above the Co-WC eutectic melting point 1,320°C). ║
║    3d. Liquid-phase sintering: Molten cobalt wets WC grains by   ║
║        capillary action. WC dissolves and reprecipitates; compact║
║        undergoes 18% linear shrinkage, eliminating all porosity! ║
║    3e. Hold for 60 min, then cool under 50 bar argon gas quench. ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Density: 14.95 ± 0.05 g/cm³ (Archimedes method).            ║
║    • Hardness: 92.5 HRA (Rockwell A scale).                      ║
║    • Transverse Rupture Strength (TRS): >2,200 MPa.              ║
║    • Machining test: Turn hardened 4140 steel (45 HRC) at        ║
║      surface speed of 180 m/min for 30 minutes with zero chipping.║
╚══════════════════════════════════════════════════════════════════╝
```
