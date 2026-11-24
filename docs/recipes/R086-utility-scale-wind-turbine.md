# R086 — Utility-Scale Three-Blade Wind Turbine

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R086 · 2.5 MEGAWATT THREE-BLADE UTILITY WIND TURBINE     ║
║  End product: 1 × 2.5 MW Grid-Connected Wind Turbine Generator   ║
║  Rotor diameter: 110 meters, Hub height: 90 m, Capacity: 2.5 MW  ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The massive renewable kinetic energy prerequisite for:        ║
║    • Baseload zero-carbon industrial electricity generation      ║
║    • Powering regional seawater desalination and hydrogen plants ║
║    • Supplying continental AC transmission networks [→ R082]     ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Structural Steel Plate (S355 for tower): 180 tonnes [→ R040]║
║    2. E-Glass Fiber & Epoxy Resin (Blades): 35 tonnes [→ R060]   ║
║    3. Carbon Fiber Spar Cap Spars: 4 tonnes [→ R167]             ║
║    4. Planetary Step-Up Gearbox (1:100 ratio): 1 pc [→ R072]     ║
║    5. Doubly-Fed Induction Generator (DFIG, 2.5 MW): 1 [→ R284]  ║
║    6. Four-Point Contact Slewing Bearings: 4 pcs [→ R041, R072]  ║
║    7. Hydraulic Pitch & Yaw Actuator System: 1 [→ R284]          ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: COMPOSITE ROTOR BLADE FABRICATION (54 METERS EACH)     ║
║    1a. Precision machine matched female mold halves from steel   ║
║        and tooling composite [→ R072, R163].                     ║
║    1b. Lay down multi-axial E-glass fiber fabric in aerodynamic  ║
║        shell shape (DU91-W2-250 thick airfoil at root, NACA-63   ║
║        thin high-lift airfoil at tip).                           ║
║    1c. Insert main structural spar: Fabricate hollow box girder  ║
║        spar using high-modulus unidirectional carbon fiber caps  ║
║        [→ R167] to withstand massive flapwise bending moments.   ║
║    1d. Vacuum-Assisted Resin Transfer Molding (VARTM): Seal mold ║
║        in airtight vacuum bag; pull -0.95 bar vacuum. Infuse     ║
║        degassed epoxy resin; cure at 75°C for 8 hours.           ║
║    1e. Bond shell halves together along leading/trailing edges   ║
║        with high-strength methacrylate structural adhesive.      ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: DRIVE TRAIN & NACELLE INTEGRATION                      ║
║    2a. Cast ductile iron hub with three pitch bearing rings.     ║
║    2b. Forge forged alloy steel main low-speed shaft (450 mm dia)║
║        supported by spherical roller main bearings.              ║
║    2c. Install planetary gearbox: Two planetary stages + one     ║
║        helical parallel stage stepped up 1:105 (converts 14 RPM  ║
║        rotor rotation to 1,500 RPM high-speed generator shaft).  ║
║    2d. Mount 2.5 MW Doubly-Fed Induction Generator (DFIG)        ║
║        [→ R284]: Stator connects directly to 690 V grid; wound   ║
║        rotor connects through back-to-back IGBT power converter  ║
║        [→ R130], allowing variable-speed operation (±30% synch). ║
║    2e. Install high-speed aerodynamic disc brake on generator shaft║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: TUBULAR STEEL TOWER & ERECTION                         ║
║    3a. Roll 25 mm structural steel plates into conical cylinder  ║
║        sections (4.5 m base diameter, 3.0 m top diameter).       ║
║    3b. Submerged-arc weld internal and external seams [→ R040];  ║
║        weld heavy forged connection flanges. Assemble 3 sections.║
║    3c. Bolt base flange to reinforced concrete gravity foundation║
║        (700 m³ concrete [→ R160] + 50 tonnes rebar) with 140     ║
║        high-tensile prestressed anchor bolts.                    ║
║    3d. Hoist nacelle and complete 3-blade rotor using heavy      ║
║        crawler crane [→ R070].                                   ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 4: ACTIVE PITCH & YAW CONTROL LOOP                        ║
║    4a. Wind vane & anemometer continuously report wind vector.   ║
║    4b. Four electric yaw gear motors rotate entire 100-tonne     ║
║        nacelle into wind within ±2°.                             ║
║    4c. Individual Pitch Control (IPC): Independent electric      ║
║        servos [→ R284] twist each blade along its axis in real   ║
║        time: Feather blades at cut-out wind speed (>25 m/s) to   ║
║        stop rotation aerodynamically and protect machine.        ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Power curve: Cut-in speed 3.0 m/s; Rated 2.5 MW @ 11.5 m/s. ║
║    • Blade static test: Blade tip deflects 8 meters under 100%   ║
║      ultimate design load without structural fracture.           ║
║    • Design operating lifetime: 20 years continuous service.     ║
╚══════════════════════════════════════════════════════════════════╝
```
