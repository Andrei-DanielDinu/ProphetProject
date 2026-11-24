# R101 — Planar Silicon Transistor and Photolithography

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R101 · PLANAR SILICON TRANSISTOR (NMOS FET)              ║
║  End product: Operational MOSFET Switches on Silicon Wafer       ║
║  Switching speed: > 10 MHz, Gate length: 5 μm (early planar)     ║
╠══════════════════════════════════════════════════════════════════╣
║  WHY THE PLANAR PROCESS CHANGED THE WORLD                        ║
║    Invented by Jean Hoerni and Robert Noyce (1959).              ║
║    Before planar: transistors were handmade three-dimensional    ║
║    blobs (point-contact / alloy junction).                       ║
║    Planar technology builds transistors flat on the surface      ║
║    using photographic printing (photolithography) and thermal    ║
║    diffusion through oxide windows.                              ║
║    It allows printing 1,000 or 1,000,000,000 transistors at once!║
╠══════════════════════════════════════════════════════════════════╣
║  INGREDIENTS                                                     ║
║  A) Polished P-type Silicon Wafer (150 mm) [→ R100]              ║
║  B) High-purity Oxygen gas and dry steam [→ R070 / R111]         ║
║  C) Photoresist polymer (polyvinyl cinnamate in xylene solvent)   ║
║  D) Gaseous dopants: Phosphorus oxychloride (POCl₃, N-type)      ║
║  E) Pure aluminum wire for vacuum metallization [→ R084/R092]    ║
╠══════════════════════════════════════════════════════════════════╣
║  FOUR-MASK PLANAR FABRICATION PROTOCOL                           ║
║                                                                  ║
║  STEP 1 — THERMAL OXIDATION (Growing the Shield)                 ║
║    Place wafer in quartz tube furnace at 1,050°C in pure steam:  ║
║    Si + 2 H₂O ──► SiO₂ + 2 H₂.                                   ║
║    Grows 500 nm of glass-like Silicon Dioxide across wafer.      ║
║    SiO₂ is an impermeable barrier to diffusion dopants!          ║
║                                                                  ║
║  STEP 2 — MASK 1: SOURCE AND DRAIN DIFFUSION                     ║
║    2a. Spin-coat 1 μm liquid photoresist onto wafer at 3,000 RPM.║
║    2b. Align photomask 1 (glass plate with chrome patterns).     ║
║    2c. Expose to mercury-arc ultraviolet light (365 nm UV).      ║
║        Exposed resist crosslinks; unexposed washes away in solvent║
║    2d. Hydrofluoric acid (HF) etch: dissolves exposed SiO₂       ║
║        windows down to bare silicon. Strip remaining resist.     ║
║    2e. Thermal diffusion: Pass POCl₃ vapor at 950°C for 25 min.  ║
║        Phosphorus atoms diffuse into exposed silicon, converting ║
║        P-type silicon into two deep N+ wells (Source & Drain).   ║
║                                                                  ║
║  STEP 3 — MASK 2: GATE DIELECTRIC OXIDE                          ║
║    Strip thin oxide over channel. Regrow ultra-pure, ultra-thin  ║
║    dry thermal gate oxide: 20 nm thick at 1,000°C in dry O₂.     ║
║                                                                  ║
║  STEP 4 — MASK 3: CONTACT VIAS                                   ║
║    Etch contact holes through oxide down to Source and Drain.    ║
║                                                                  ║
║  STEP 5 — MASK 4: METALLIZATION & INTERCONNECT                   ║
║    5a. Place wafer in high-vacuum chamber (<10⁻⁵ mbar, R092).    ║
║    5b. Evaporate pure aluminum via tungsten filament heater:     ║
║        aluminum condenses as a 1 μm mirror layer across wafer.   ║
║    5c. Apply photoresist, expose Mask 4, and etch away unwanted  ║
║        aluminum with phosphoric acid: leaves separate metal      ║
║        wiring for Source, Gate, and Drain terminals!             ║
╠══════════════════════════════════════════════════════════════════╣
║  VERIFICATION TEST: Connect curve tracer. Apply +3V to Gate.     ║
║  Channel inverts: current surges between Source and Drain with   ║
║  on/off switching ratio > 100,000 : 1!                           ║
╚══════════════════════════════════════════════════════════════════╝
```
