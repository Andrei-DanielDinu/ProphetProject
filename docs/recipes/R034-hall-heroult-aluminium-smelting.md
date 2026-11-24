# R034 — Hall-Héroult Electrolytic Aluminium Smelting

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R034 · HALL-HÉROULT ELECTROLYTIC ALUMINIUM SMELTING       ║
║  End product: 100 kg Aluminium Metal Ingot (Al, 99.8% purity)     ║
║  Density: 2.70 g/cm³, Melting point: 660.3°C                     ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The structural lightweight metal prerequisite for:            ║
║    • Aircraft airframes and aerodynamic skin [→ R241]            ║
║    • High-voltage overhead AC electrical transmission wire       ║
║    • Engine cylinder blocks, pistons, and heat exchangers [→ R240]║
║    • Lightweight rocketry tanks and aerospace structures [→ R111]║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Bauxite Ore (Al₂O₃·2H₂O): 400 kg [→ R000-F, R003]          ║
║    2. Sodium Hydroxide (NaOH lye): 120 kg [→ R052]               ║
║    3. Cryolite Bath (Na₃AlF₆ flux): 30 kg [→ R000, fluorite/soda] ║
║    4. Aluminium Fluoride (AlF₃): 5 kg [→ R000]                   ║
║    5. Pre-baked Carbon Anodes & Cathode Carbon Blocks: 45 kg     ║
║       [→ R025 calcined coke + coal tar pitch binder]             ║
║    6. Direct Current Electrical Power: 1,400 kWh at 4.5 V, 15 kA ║
║       [→ R080 DC Dynamo / R170 Hydroelectric Dam]                ║
║    7. Steel Shell Cell lined with Refractory Alumina Brick: 1    ║
║       [→ R040, R023]                                             ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: BAYER PROCESS (BAUXITE TO REFINED ALUMINA Al₂O₃)       ║
║    1a. Crush 400 kg bauxite ore to <100 mesh.                    ║
║    1b. Digest in concentrated NaOH solution (30% wt) at 175°C,   ║
║        5 bar pressure in an autoclave [→ R070]:                  ║
║        Al₂O₃ + 2 NaOH + 3 H₂O ──► 2 NaAl(OH)₄ (Sodium Aluminate).║
║        Iron and silica impurities precipitate out as "red mud".  ║
║    1c. Filter out insoluble red mud residue. Cool sodium         ║
║        aluminate filtrate to 60°C and seed with 5 kg pure        ║
║        Al(OH)₃ crystals to precipitate aluminium hydroxide:      ║
║        NaAl(OH)₄ ──► Al(OH)₃↓ + NaOH (recycle lye).              ║
║    1d. Calcine precipitated Al(OH)₃ in a rotary kiln [→ R160] at ║
║        1,100°C for 2 hours to drive off all crystal water:       ║
║        2 Al(OH)₃ ──► Al₂O₃ (dry white powder, 190 kg) + 3 H₂O↑.  ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: ELECTROLYTIC REDUCTION (HALL-HÉROULT CELL)             ║
║    2a. Melt cryolite (Na₃AlF₆) eutectic flux in carbon-lined     ║
║        steel bath at 960°C. Dissolve 5 wt% refined Al₂O₃ in melt.║
║    2b. Lower pre-baked carbon anode blocks into bath from top.   ║
║        The carbon bottom lining serves as the cathode (-).       ║
║    2c. Pass DC current (4.5 V per cell, 15,000 A):              ║
║        Cathode reaction:  Al³⁺ + 3 e⁻ ──► Al (molten liquid)     ║
║        Anode reaction:    2 O²⁻ + C ──► CO₂↑ + 4 e⁻              ║
║    2d. Molten aluminium (density 2.3 g/cm³ at 960°C) settles to  ║
║        the bottom beneath the cryolite bath (density 2.1 g/cm³), ║
║        protected from atmospheric oxidation.                     ║
║    2e. Vacuum siphon molten aluminium pad every 24 hours into    ║
║        preheated refractory ladles [→ R033]. Cast into ingots.   ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Purity: >99.7% Al (Spectrographic spark assay).             ║
║    • Iron impurity: <0.18%, Silicon impurity: <0.10%.            ║
║    • Electrical conductivity: 62% IACS.                          ║
╚══════════════════════════════════════════════════════════════════╝
```
