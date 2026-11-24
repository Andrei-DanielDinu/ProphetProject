# R167 — Carbon Fiber Precursor & High-Modulus Pyrolysis

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R167 · HIGH-STRENGTH CARBON FIBER (T700 GRADE)           ║
║  End product: 10 kg Continuous Carbon Fiber Tow (12,000 filaments)║
║  Tensile Strength: 4,900 MPa, Tensile Modulus: 230 GPa           ║
║  Density: 1.80 g/cm³, Diameter per filament: 7.0 μm              ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The ultimate structural composite reinforcement for:          ║
║    • Lightweight aerospace airframes, helicopter rotor blades [→ R241]║
║    • Rocket motor cases and high-pressure composite tanks [→ R111]║
║    • High-speed centrifuge rotors for isotope enrichment [→ R120]║
║    • Industrial robot arms, race car monocoques, wind turbine blades║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Acrylonitrile Monomer (CH₂=CH-CN): 25 kg                   ║
║       [→ Propylene R054 + Ammonia R055 + O₂ ammoxidation]        ║
║    2. Dimethyl Sulfoxide Solvent (DMSO): 100 L [→ R053]          ║
║    3. Azobisisobutyronitrile Initiator (AIBN): 50 g              ║
║    4. Wet Spinning Line with Precision Spinneret: 1 [→ R072]     ║
║    5. Multi-Zone Oxidative Stabilization Oven (200-300°C): 1     ║
║    6. High-Temperature Nitrogen Carbonization Furnace (1,400°C): 1║
║       [→ R080, R110 nitrogen gas sweep]                         ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: POLYACRYLONITRILE (PAN) PRECURSOR SPINNING             ║
║    1a. Solution polymerize acrylonitrile (98 wt%) and methyl     ║
║        acrylate (2 wt% comonomer) in DMSO at 60°C with AIBN.     ║
║    1b. Degas viscous polymer dope (viscosity 50 Pa·s).           ║
║    1c. Pump dope through tantalum spinneret containing 12,000    ║
║        micro-orifices (50 μm diameter) into aqueous DMSO bath.   ║
║    1d. Coagulate filaments; stretch 800% in boiling water to     ║
║        orient PAN polymer chains parallel to the fiber axis.     ║
║    1e. Dry and take up white PAN precursor fiber tow on spools.  ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: OXIDATIVE STABILIZATION (CYCLIZATION)                  ║
║    2a. Pass PAN tow continuously through 4-stage hot air ovens   ║
║        ramped from 200°C to 280°C over 60 minutes under tension. ║
║    2b. Intramolecular cyclization: Nitrile (C≡N) groups cross-   ║
║        link into ladder polymer pyridine structures:             ║
║        Adjacent nitrile groups cyclize, rendering fiber non-     ║
║        flammable and thermoset.                                  ║
║    2c. Fiber turns from white to golden to pitch black.          ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: HIGH-TEMPERATURE CARBONIZATION & SIZING                ║
║    3a. Pass stabilized tow through low-temperature furnace       ║
║        (300–800°C) under high-purity nitrogen atmosphere [→ R110]║
║        to evolve H₂O, NH₃, and HCN.                              ║
║    3b. Pass directly into high-temperature furnace (1,400°C)     ║
║        under argon/nitrogen sweep: non-carbon elements (H, N, O) ║
║        are completely expelled. Turbostratic hexagonal carbon    ║
║        graphitic basal planes align perfectly along fiber axis.  ║
║    3c. Surface treatment: Pass through dilute ammonium carbonate ║
║        electrolytic bath to oxidize surface for resin bonding.   ║
║    3d. Apply 1 wt% epoxy sizing; wind finished tow onto spools.  ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Carbon content: >93% wt.                                    ║
║    • Filament diameter: 7.0 ± 0.3 μm.                            ║
║    • Single-filament tensile test: >4,800 MPa.                   ║
╚══════════════════════════════════════════════════════════════════╝
```
