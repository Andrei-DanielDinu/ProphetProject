# R171 — Municipal Water Treatment & Pressurized Distribution Network

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R171 · MUNICIPAL DRINKING WATER PURIFICATION PLANT       ║
║  Capacity: 50,000 m³/day (Supplies clean water for 250,000 people)║
║  Purity: Zero coliform bacteria, Turbidity <0.1 NTU, Residual Cl  ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The primary public health prerequisite for:                   ║
║    • Eradication of cholera, typhoid fever, dysentery, schistosoma║
║    • Reliable industrial boiler feed and chemical process water  ║
║    • Pressurized urban fire protection and high-rise living [→ R161]║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Raw River / Canal Water (Nile intake): 52,000 m³/day [→ R000]║
║    2. Aluminium Sulfate Coagulant (Alum, Al₂(SO₄)₃·14H₂O): 1.5 t ║
║       [→ Bauxite R034 + Sulfuric acid R053]                      ║
║    3. Hydrated Lime (Ca(OH)₂ pH adjustment): 500 kg [→ R027]    ║
║    4. Graded Quartz Sand Filter Bed (0.45–0.55 mm): 200 tonnes   ║
║       [→ Crushed quartz pebbles, R000]                           ║
║    5. Chlorine Gas (Cl₂ liquefied in steel cylinders): 150 kg    ║
║       [→ Chlor-alkali electrolysis, R052/R056]                   ║
║    6. Centrifugal High-Lift Water Pumps (500 kW each): 4 pcs     ║
║       [→ R070/R284 electric motor driven]                       ║
║    7. Ductile Cast Iron Water Mains (Class K9, cement lined):    ║
║       50 km [→ R040, R160]                                       ║
║    8. Elevated Reinforced Concrete Water Tower (50 m head): 1    ║
║       [→ R160, R161]                                             ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: COAGULATION & MECHANICAL FLOCCULATION                  ║
║    1a. Coarse screening: Pass raw river water through mechanical ║
║        bar screens (25 mm gap) to remove reeds, fish, and debris.║
║    1b. Rapid flash mixing: Dose 30 mg/L aluminium sulfate (alum) ║
║        and hydrated lime into turbulent mixing chamber (velocity ║
║        gradient G > 700 s⁻¹) for 60 seconds:                     ║
║        Al³⁺ ions neutralize negative zeta potential on suspended ║
║        microscopic clay silt and bacterial cell walls:           ║
║        Al₂(SO₄)₃ + 3 Ca(OH)₂ ──► 2 Al(OH)₃↓ (Gelatinous sticky   ║
║        micro-floc precipitate) + 3 CaSO₄.                        ║
║    1c. Slow flocculation: Water flows through 3-stage paddle     ║
║        flocculation basins with gentle stirring (G = 50 to 20 s⁻¹)║
║        over 30 minutes: Micro-flocs collide and agglomerate into ║
║        heavy, visible snowflake-like "feather flocs".            ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: LAMELLA SEDIMENTATION & RAPID SAND FILTRATION          ║
║    2a. Lamella tube settlers: Flocculated water flows upward     ║
║        through inclined PVC plate packs (60° angle [→ R165]):    ║
║        Flocs settle out onto plates within 1.5 meters settling   ║
║        distance; slide down into hopper bottom; turbidity drops  ║
║        from 100 NTU down to <3 NTU.                              ║
║    2b. Rapid sand filter beds: Gravity flow through 1.2 meters   ║
║        of dual-media:                                            ║
║        • Upper layer: 0.5 m crushed anthracite coal (1.0 mm size)║
║        • Lower layer: 0.7 m graded quartz silica sand (0.5 mm)   ║
║        • Underdrain: Porous porcelain nozzles on concrete slab.  ║
║    2c. Filtration rate: 10 m/hour. Entraps remaining parasites,  ║
║        amoebic cysts, and bacteria; effluent turbidity <0.1 NTU. ║
║    2d. Automated backwashing: Every 24 hours, reverse flow with  ║
║        compressed air and clean treated water to fluidize sand   ║
║        and flush trapped silt into sludge lagoons.               ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: DISINFECTION & GRAVITY HEAD DISTRIBUTION               ║
║    3a. Gas chlorination: Inject gaseous Cl₂ through vacuum       ║
║        chlorinator ejector at 2.5 mg/L into clean-well contact   ║
║        chamber with 45 minutes contact time:                     ║
║        Cl₂ + H₂O ──► HOCl (Hypochlorous acid) + H⁺ + Cl⁻.        ║
║        HOCl penetrates bacterial cell walls, denatures essential ║
║        respiratory enzymes, and destroys virus capsids.          ║
║    3b. Ensure free residual chlorine of 0.5 mg/L at municipal tap║
║        endpoints to prevent pathogen regrowth inside distribution║
║        pipelines.                                                ║
║    3c. Pump treated water via centrifugal pumps [→ R284] into    ║
║        elevated concrete water towers (50 meters height):        ║
║        Provides 5.0 bar constant hydrostatic head across the     ║
║        municipal grid by gravity, eliminating pressure drops.    ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Biological safety: 0 colony-forming units (CFU) *E. coli*   ║
║      per 100 mL sample (100% sterile microbial assay).           ║
║    • Turbidity: <0.1 NTU (Nephelometric Turbidity Units).        ║
║    • Residual chlorine: 0.2 to 0.8 mg/L at farthest urban tap.   ║
╚══════════════════════════════════════════════════════════════════╝
```
