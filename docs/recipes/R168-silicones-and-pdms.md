# R168 — Silicones & Polydimethylsiloxane (PDMS)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R168 · SILICONE ELASTOMERS & OILS (PDMS)                 ║
║  End product: 50 kg Polydimethylsiloxane Silicone Gum & Fluid    ║
║  Thermal range: -60°C to +250°C, Hydrophobic, Dielectric oil     ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The heat-resistant, dielectric, bio-compatible polymer for:   ║
║    • High-temperature electrical motor insulation varnishes [→ R284]║
║    • Vacuum pump diffusion fluids and vacuum seal grease [→ R092]║
║    • Soft-lithography microfluidic diagnostic chips [→ R150]     ║
║    • Gaskets, flexible tubing, and medical-grade implants [→ R208]║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Silicon Metal Powder (98.5% MGS): 30 kg [→ R100]           ║
║    2. Chloromethane Gas (CH₃Cl): 100 kg                          ║
║       [→ Methanol R054 + HCl gas R053 at 300°C over Al₂O₃]       ║
║    3. Copper Catalyst Powder (elemental Cu, <10 μm): 3.0 kg [→ R030]║
║    4. Deionized Water: 100 L [→ R060]                            ║
║    5. Fumed Silica Filler Powder: 15 kg [→ R100 flame pyrolysis] ║
║    6. Fluidized Bed Reactor (Müller-Rochow Direct Process): 1    ║
║    7. Fractional Distillation Column (50 theoretical trays): 1   ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: MÜLLER-ROCHOW DIRECT SYNTHESIS                         ║
║    1a. Grind silicon metal with copper catalyst to fine powder   ║
║        contact mass (90% Si, 10% Cu).                            ║
║    1b. Fluidize contact mass in vertical reactor with gaseous    ║
║        chloromethane at 300°C and 3 bar:                         ║
║        Si + 2 CH₃Cl ──► (CH₃)₂SiCl₂ (Dimethyldichlorosilane, 80%) ║
║        Side products: CH₃SiCl₃, (CH₃)₃SiCl, and SiCl₄.           ║
║    1c. Condense liquid organochlorosilane crude mixture.         ║
║    1d. Fractional distillation through 50-tray column [→ R070]:  ║
║        Separate pure dimethyldichlorosilane (boiling pt 70.1°C)  ║
║        from methyltrichlorosilane (b.p. 65.7°C, 4.4°C gap!).     ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: HYDROLYSIS & CYCLIC SILOXANE FORMATION                ║
║    2a. Feed pure (CH₃)₂SiCl₂ continuously into excess water with ║
║        vigorous mechanical stirring at 30°C:                     ║
║        n (CH₃)₂SiCl₂ + n H₂O ──► [─Si(CH₃)₂─O─]ₙ + 2n HCl↑.     ║
║    2b. Scrub and recycle aqueous hydrochloric acid.              ║
║    2c. The hydrolyzate consists of linear silanol fluids and     ║
║        cyclic oligomers (mainly octamethylcyclotetrasiloxane D₄).║
║    2d. Separate organic siloxane oil layer from water layer.     ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: RING-OPENING POLYMERIZATION & CROSSLINKING             ║
║    3a. Polymerize D₄ cyclic siloxanes at 150°C using potassium   ║
║        hydroxide (KOH, 50 ppm) or sulfuric acid catalyst [→ R053]║
║        to yield high-molecular-weight linear PDMS gum:           ║
║        ...─O─Si(CH₃)₂─O─Si(CH₃)₂─O─... (MW ~500,000).            ║
║    3b. End-cap with hexamethyldisiloxane to control viscosity    ║
║        (from 10 cSt thin oil to 1,000,000 cSt gum).              ║
║    3c. Elastomer compounding: Blend PDMS gum with 30 wt% fumed   ║
║        silica reinforcement and 1 wt% benzoyl peroxide curative. ║
║    3d. Heat mold at 170°C for 10 min: Free-radical methyl-methyl ║
║        crosslinking produces high-elasticity silicone rubber.    ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Thermal degradation onset: >350°C in air.                   ║
║    • Dielectric breakdown strength: 20 kV/mm.                    ║
║    • Biocompatibility: Zero cytotoxicity, zero tissue reaction.  ║
╚══════════════════════════════════════════════════════════════════╝
```
