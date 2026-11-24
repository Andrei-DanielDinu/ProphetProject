# R085 — Photovoltaic Monocrystalline Silicon Solar Cell

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R085 · PHOTOVOLTAIC MONOCRYSTALLINE SOLAR CELL (PERC)    ║
║  End product: 1 × 60-Cell Solar Photovoltaic Module (320 W)      ║
║  Cell efficiency: 22.5%, Cell format: 156 mm × 156 mm M2 wafer   ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The clean, silent, distributed electricity prerequisite for:  ║
║    • Remote off-grid communication relays and weather stations   ║
║    • Daytime industrial chemical electrolysis plants [→ R052]    ║
║    • Spacecraft and satellite solar array power wings [→ R111]   ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. P-type Monocrystalline Silicon Wafers (180 μm): 60 pcs     ║
║       (Boron doped, 1–3 Ω·cm resistivity) [→ R100]               ║
║    2. Potassium Hydroxide (KOH texturing): 2 kg [→ R052]         ║
║    3. Phosphorus Oxychloride (POCl₃ dopant): 500 mL [→ R053]     ║
║    4. Silane (SiH₄) & Ammonia (NH₃) gases: [→ R100, R055]        ║
║    5. Screen-Printing Conductive Silver Paste: 100 g [→ R000]    ║
║    6. Screen-Printing Aluminium Backside Paste: 300 g [→ R034]   ║
║    7. Quartz Tube Diffusion Furnace (900°C): 1 [→ R060]          ║
║    8. Automated Screen Printer & Belt Sintering Furnace: 1       ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: ALKALINE TEXTURING (RANDOM PYRAMID LIGHT TRAPPING)     ║
║    1a. Etch saw damage off sliced monocrystalline <100> silicon  ║
║        wafers using hot 20% NaOH solution [→ R052] at 75°C.      ║
║    1b. Anisotropic alkaline texturing: Immerse in 2% KOH +       ║
║        isopropanol solution at 80°C for 25 minutes:              ║
║        The KOH preferentially attacks the <100> silicon planes   ║
║        over <111> planes, creating billions of microscopic 3 μm  ║
║        four-sided square pyramids across the entire surface!     ║
║    1c. Light striking a pyramid reflects into an adjacent        ║
║        pyramid rather than back into the sky: Reflectance drops  ║
║        from 35% down to under 11%.                               ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: N-EMITTER DIFFUSION & DIELECTRIC PASSIVATION           ║
║    2a. Load textured p-type wafers into quartz tube furnace.     ║
║    2b. Bubble nitrogen carrier gas through liquid POCl₃ at 850°C:║
║        4 POCl₃ + 3 O₂ ──► 2 P₂O₅ + 6 Cl₂↑.                       ║
║        P₂O₅ deposits as phosphosilicate glass on the surface.    ║
║    2c. Thermal drive-in: Phosphorus atoms diffuse 0.4 μm into the║
║        p-type bulk, forming a shallow, highly conductive n⁺      ║
║        emitter layer (Sheet resistance R_sheet = 85 Ω/sq).       ║
║    2d. Remove phosphosilicate glass in dilute 10% HF [→ R166].   ║
║    2e. PECVD Antireflective Coating: Deposit 75 nm Silicon       ║
║        Nitride (SiNₓ:H) thin film at 400°C from SiH₄ + NH₃:      ║
║        Acts as quarter-wave optical anti-reflective layer (cells ║
║        turn deep cobalt blue) and passivates dangling silicon    ║
║        bonds with atomic hydrogen, increasing carrier lifetime!  ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: METALLIZATION & CONTACT SINTERING                      ║
║    3a. Screen-print rear Aluminium paste over backside; screen-  ║
║        print front silver grid with 5 busbars and 100 ultra-fine ║
║        silver fingers (width 35 μm).                             ║
║    3b. Fast-firing belt furnace: Pass wafer through 820°C zone   ║
║        for 3 seconds:                                            ║
║        • Glass frit in silver paste dissolves through the SiNₓ   ║
║          coating, establishing ohmic contact to n⁺ emitter.      ║
║        • Backside aluminium alloys with silicon, forming a       ║
║          heavily doped p⁺ Back Surface Field (BSF) that repels   ║
║          minority electrons away from rear recombination centers!║
║    3c. Module assembly: Solder 60 cells in series with copper    ║
║        ribbon; laminate between EVA polymer films, tempered glass║
║        front sheet, and backsheet inside an aluminium frame.     ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Open-circuit voltage (Voc): >680 mV per cell.               ║
║    • Short-circuit current density (Jsc): >40.5 mA/cm².          ║
║    • Fill Factor (FF): >80.5%. Cell efficiency: >22.2%.          ║
╚══════════════════════════════════════════════════════════════════╝
```
