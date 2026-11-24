# R080 — Electrical Dynamo (DC Generator)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R080 · ELECTRICAL DYNAMO — DC GENERATOR                 ║
║  End product: 1 DC generator, 100V / 5A = 500W output          ║
╠══════════════════════════════════════════════════════════════════╣
║  WHAT YOU GET                                                    ║
║    A rotating electromagnetic generator converting mechanical   ║
║    energy (from steam engine R070 or waterwheel) into direct-   ║
║    current electricity. 500W is enough to:                       ║
║    • Power 10 × 50W arc lamps (dramatic!)                       ║
║    • Run electrolysis (refining metals, making chlorine)        ║
║    • Charge lead-acid batteries (R081)                          ║
║    • Power telegraph (R082)                                      ║
║    • Eventually: electrolytic aluminium production (R083)        ║
╠══════════════════════════════════════════════════════════════════╣
║  PHYSICS (must understand before building)                       ║
║                                                                  ║
║  Faraday's Law of Induction (1831 — Prophet knows this in 2975 BCE):║
║    EMF = -N × dΦ/dt                                              ║
║    Where:                                                        ║
║      EMF = electromotive force (volts)                           ║
║      N = number of coil turns                                    ║
║      dΦ/dt = rate of change of magnetic flux through coil       ║
║                                                                  ║
║  For this generator:                                             ║
║    B (field) = 0.5 Tesla (from iron core + copper coil magnet)  ║
║    A (coil area) = 0.01 m² (10×10 cm armature)                  ║
║    N (turns) = 500                                               ║
║    ω (rotation) = 60 rad/s (≈ 600 RPM)                          ║
║    Peak EMF = N × B × A × ω = 500 × 0.5 × 0.01 × 60 = 150 V   ║
║    RMS EMF ≈ 150/√2 = 106 V. With commutator → ~100 V DC.      ║
╠══════════════════════════════════════════════════════════════════╣
║  INGREDIENTS                                                     ║
║                                                                  ║
║  A) 20 kg pure copper wire (various gauges)   [→ R084]          ║
║     For: armature coils (500 turns × 2 m/turn = 1,000 m),      ║
║     field coils (200 turns), lead wires.                         ║
║     Wire diameter: 1.5 mm (armature), 2.0 mm (field coils).    ║
║     Insulation: waxed cotton thread wrapped helically.           ║
║                                                                  ║
║  B) 50 kg soft iron (pure Fe, low carbon)     [→ R040]          ║
║     Laminated iron core: slice iron into 1 mm sheets.           ║
║     Sheets insulated with paper (later: shellac).                ║
║     Why laminated: reduces eddy current losses.                  ║
║     If not laminated: 70%+ of power lost to heat in core.       ║
║                                                                  ║
║  C) 2 kg lead + 500g tin (for commutator solder) [→ R085]      ║
║     Commutator segments: copper strips, soldered to armature.   ║
║                                                                  ║
║  D) 500g pine pitch (insulation for coil wound layers) ■ TERM.  ║
║     Heated liquid, painted between coil layers. Insulates.      ║
║                                                                  ║
║  E) Mechanical drive: shaft from steam engine or waterwheel      ║
║     [→ R070 or Manual 09]                                        ║
║     Required speed: 600 RPM. Gear up waterwheel (30 RPM) by    ║
║     20:1 gear ratio using crown wheel + lantern pinions.         ║
╠══════════════════════════════════════════════════════════════════╣
║  TOOLS                                                           ║
║    • Wire-drawing dies (iron, progressively smaller holes)       ║
║      [→ R084]                                                    ║
║    • Coil winding jig (wooden mandrel, 10×10 cm, 500 turns)      ║
║    • Precision lathe (for commutator turning)   [→ R086]        ║
║    • Soldering iron (copper tip, heated in forge)               ║
╠══════════════════════════════════════════════════════════════════╣
║  DIMENSIONS                                                      ║
║                                                                  ║
║  Overall: 60 cm × 40 cm × 50 cm. Mass: ~80 kg.                  ║
║                                                                  ║
║  Cross-section of generator:                                     ║
║                                                                  ║
║         N ──────────────────── S        ← Permanent or          ║
║         │   FIELD MAGNET POLES │          electro-magnet         ║
║         │      ┌─────────┐     │          iron core + field coil ║
║         │      │ ARMATURE│     │                                 ║
║         │      │ (rotating│    │        ← 500-turn copper coil  ║
║         │      │ iron core│    │          wound on iron drum     ║
║         │      │ + coils) │    │                                 ║
║         │      └────┬────┘     │                                 ║
║         └───────────┼──────────┘                                 ║
║                     │ SHAFT (driven by steam engine)             ║
║                     │                                            ║
║              COMMUTATOR                                          ║
║              (copper segments, insulated gaps)                   ║
║                     │                                            ║
║              BRUSHES (carbon or copper, press against commutator)║
║                     │                                            ║
║              OUTPUT TERMINALS (+/-)                              ║
╠══════════════════════════════════════════════════════════════════╣
║  PROCESS OVERVIEW (each sub-component has its own recipe)       ║
║                                                                  ║
║  STEP 1 — BUILD FIELD MAGNET                                     ║
║    1a. Option A: Electromagnet (better — adjustable field):      ║
║        Soft iron U-shape core (10 kg iron bar, forged to U).    ║
║        Wind 200 turns of 2mm copper wire around each pole.      ║
║        Connect to separate DC supply (use lead-acid battery     ║
║        or separate small generator — chicken-and-egg problem:    ║
║        see note below).                                          ║
║    1b. Option B: Permanent magnet (simpler for first build):    ║
║        Use hardened steel (R041, fully magnetised by stroke-     ║
║        magnetising: heat to 800°C, cool in Earth's magnetic     ║
║        field aligned N-S while hammering. Weak but sufficient   ║
║        for first experiment).                                    ║
║                                                                  ║
║    ⚠ BOOTSTRAP PROBLEM: To get electricity, you need a magnet.  ║
║      To make an electromagnet, you need electricity.             ║
║      SOLUTION: Use a permanent magnet (hardened steel, touch-    ║
║      magnetised) for the FIRST generator only. Use its output   ║
║      to power the electromagnets of the SECOND generator.        ║
║      The Prophet knows this — Siemens solved it in 1866 CE.     ║
║                                                                  ║
║  STEP 2 — WIND ARMATURE                                          ║
║    2a. Laminate iron core: hammer soft iron to 1 mm sheets,     ║
║        stack with paper (or pine pitch painted) between layers. ║
║        Clamp with iron bolts. Final block: 100×100×80 mm.       ║
║    2b. Machine (file/scrape to shape) 8 slots for coil windings.║
║    2c. Wind 500 turns of 1.5 mm copper wire in slots.           ║
║        Each layer: paint with hot pine pitch. Cool. Next layer. ║
║        Total wire: 500 × (100mm+100mm+100mm+100mm) = 200 m.    ║
║        Mass: 200 m × π × 0.75²mm² × 8.9 g/cm³ ≈ 3.1 kg Cu.   ║
║                                                                  ║
║  STEP 3 — MAKE COMMUTATOR                                        ║
║    3a. 16 copper segments, each 2 cm × 1 cm × 2 mm.            ║
║        Cut from copper strip. File all surfaces flat.            ║
║    3b. Arrange in ring around shaft. Insulate segments with      ║
║        thin pine pitch painted card between each.                ║
║    3c. Turn commutator on lathe [→ R086] to round, smooth.      ║
║    3d. Solder each segment to corresponding armature coil lead. ║
║                                                                  ║
║  STEP 4 — BRUSHES                                                ║
║    4a. Carbon brushes: not available early → use copper strip    ║
║        spring-loaded against commutator. Replace frequently.    ║
║    4b. Later (once charcoal bonding chemistry is known):        ║
║        pressed carbon (charcoal + pitch, fired) = carbon brush. ║
║                                                                  ║
║  STEP 5 — ASSEMBLE AND TEST                                      ║
║    5a. Mount field magnet and armature on common iron frame.    ║
║    5b. Air gap between armature and field poles: 2–3 mm.        ║
║        Smaller gap = stronger field = more output.               ║
║    5c. Connect shaft to steam engine via belt drive (leather     ║
║        belt on turned wooden pulleys).                           ║
║    5d. FIRST TEST: spin by hand. With permanent magnet: measure  ║
║        output with simple galvanometer [→ R087].                 ║
║    5e. At 600 RPM (60 rad/s): should see 80–120V on galvanometer.║
╠══════════════════════════════════════════════════════════════════╣
║  SKILLS                                                          ║
║    • Understanding of Faraday's law (must teach first)           ║
║    • Wire drawing (R084): weeks of practice                      ║
║    • Coil winding: patience, consistent tension on wire          ║
║    • Commutator machining: requires lathe (R086)                 ║
║    TRAINING TIME: 6 months from zero to first working generator. ║
╚══════════════════════════════════════════════════════════════════╝
```
