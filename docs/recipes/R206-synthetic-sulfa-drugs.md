# R206 — Synthetic Sulfa Drugs (Sulfanilamide Synthesis)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R206 · SULFA ANTIMICROBIALS (SULFANILAMIDE SYNTHESIS)    ║
║  End product: 10 kg Pure Sulfanilamide Powder (USP Grade)        ║
║  Formula: C₆H₈N₂O₂S, Mechanism: Competitive Dihydropteroate      ║
║  Synthetase inhibitor (halts bacterial folic acid synthesis)     ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The fully synthetic antimicrobial prerequisite for:           ║
║    • Battlefield wound dusting (halts gangrene, strep, staph)    ║
║    • Treatment of bacterial meningitis, dysentery, urinary sepsis║
║    • Scalable antibiotic therapy without biological fermenters   ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Aniline Oil (C₆H₅NH₂): 6.0 kg                              ║
║       [→ Benzene R054 + Nitric acid R053 ──► Nitrobenzene + Fe/HCl]║
║    2. Acetic Anhydride / Glacial Acetic Acid: 7.0 kg [→ R054]    ║
║    3. Chlorosulfonic Acid (ClSO₃H): 30 kg                        ║
║       [→ Sulfur trioxide SO₃ + Anhydrous HCl gas, R053]          ║
║    4. Concentrated Aqueous Ammonia (NH₄OH, 28%): 25 L [→ R055]   ║
║    5. Hydrochloric Acid (HCl 37%) & Sodium Carbonate: [→ R052]   ║
║    6. Glass-Lined Enamelled Jacketed Reactor: 1 [→ R060, R036]   ║
║    7. Stainless Steel Nutsche Filter & Vacuum Drier: 1 [→ R036]  ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: ACETYLATION (PROTECTION OF THE AMINO GROUP)            ║
║    1a. Charge 6.0 kg aniline into glass-lined reactor.           ║
║    1b. Slowly add 7.0 kg glacial acetic acid with stirring:      ║
║        C₆H₅NH₂ + CH₃COOH ──► C₆H₅NHCOCH₃ (Acetanilide) + H₂O.    ║
║    1c. Heat to reflux at 105°C for 3 hours.                      ║
║    1d. Discharge into cold water: Pure white crystalline         ║
║        acetanilide precipitates. Filter and dry (8.5 kg).        ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: CHLOROSULFONATION                                      ║
║    2a. Cool reactor jacket to 10°C. Charge 30 kg chlorosulfonic  ║
║        acid (fuming corrosive liquid; handle in fume hood).      ║
║    2b. Add 8.5 kg dry powdered acetanilide in small portions,    ║
║        maintaining temperature below 20°C:                       ║
║        C₆H₅NHCOCH₃ + 2 ClSO₃H ──► p-CH₃CONH-C₆H₄-SO₂Cl           ║
║        (p-Acetamidobenzenesulfonyl chloride) + H₂SO₄ + HCl↑.     ║
║    2c. Heat mixture to 60°C for 2 hours to complete conversion.  ║
║    2d. Pour crude reaction mix onto crushed ice: The sulfonyl    ║
║        chloride precipitates as a granular white solid.          ║
║    2e. Rapidly filter cold and wash with ice-cold water.         ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: AMIDATION & DEPROTECTION                               ║
║    3a. Slurry the sulfonyl chloride cake in 25 L concentrated    ║
║        28% aqueous ammonia at 15°C:                              ║
║        p-CH₃CONH-C₆H₄-SO₂Cl + 2 NH₃ ──►                          ║
║        p-CH₃CONH-C₆H₄-SO₂NH₂ (p-Acetamidobenzenesulfonamide)     ║
║        + NH₄Cl.                                                  ║
║    3b. Heat to 70°C for 30 minutes to complete amidation.        ║
║    3c. Acid hydrolysis (deprotection): Add 10 L 6M HCl and boil  ║
║        under reflux for 45 minutes: The protecting acetyl group  ║
║        is cleaved off as acetic acid:                            ║
║        p-CH₃CONH-C₆H₄-SO₂NH₂ + H₂O + HCl ──►                     ║
║        p-NH₂-C₆H₄-SO₂NH₂·HCl (Sulfanilamide hydrochloride).      ║
║    3d. Cool to 25°C. Neutralize with saturated sodium carbonate  ║
║        (Na₂CO₃) solution until pH reaches 7.0 exactly:           ║
║        Pure free sulfanilamide precipitates as brilliant white   ║
║        glistening crystals.                                      ║
║    3e. Filter, wash with ice water, and dry at 80°C.             ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Melting point: 164.5°C to 166.5°C.                          ║
║    • Purity: >99.5% (Nitrite potentiometric titration).          ║
║    • Heavy metals: <10 ppm.                                      ║
╚══════════════════════════════════════════════════════════════════╝
```
