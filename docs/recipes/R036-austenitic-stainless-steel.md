# R036 — Austenitic Stainless Steel (18/8 AISI 304)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R036 · AUSTENITIC STAINLESS STEEL (AISI 304 / 18-8)      ║
║  End product: 500 kg High-Purity Stainless Steel Billet          ║
║  Composition: 18% Cr, 8% Ni, <0.08% C, balance Fe                ║
║  Corrosion-proof, non-magnetic, heat-resistant up to 870°C       ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The non-corrosive, sanitary, high-temperature alloy for:      ║
║    • Chemical reactors, nitric/sulfuric acid vessels [→ R053]    ║
║    • Antibiotic fermentation tanks & sterile piping [→ R200]     ║
║    • Rocket engine injector domes and cryogenic plumbing [→ R111]║
║    • Surgical instruments, food canning equipment [→ R029]       ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Low-Carbon Steel Scrap / Direct Reduced Iron: 365 kg [→ R040]║
║    2. Ferrochrome (High Carbon FeCr, 65% Cr): 140 kg [→ R000-F]  ║
║    3. Electrolytic Nickel Pellets (Ni, 99.8%): 42 kg [→ R000]    ║
║    4. Ferromanganese (80% Mn): 10 kg [→ R000-F pyrolusite]       ║
║    5. Ferrosilicon (75% Si): 5 kg [→ R100 MGS]                   ║
║    6. Calcined Quicklime (CaO flux): 25 kg [→ R027]              ║
║    7. Electric Arc Furnace (EAF) with Graphite Electrodes: 1     ║
║       [→ R080, R025 graphite]                                   ║
║    8. Argon-Oxygen Decarburization (AOD) Converter: 1 [→ R110]   ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: PRIMARY MELTING IN ELECTRIC ARC FURNACE (EAF)          ║
║    1a. Charge 365 kg steel scrap, 140 kg ferrochrome, and 42 kg  ║
║        nickel into basic magnesite-lined EAF [→ R023].           ║
║    1b. Strike electric arcs from 3 graphite electrodes powered by║
║        three-phase AC transformer [→ R082]. Input 250 kWh.       ║
║    1c. Melt charge at 1,580°C. Add CaO lime to form basic slag;  ║
║        dephosphorize melt. Melt carbon content is ~1.5%.         ║
║    1d. Tap molten crude high-carbon stainless melt into AOD ladle.║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: ARGON-OXYGEN DECARBURIZATION (AOD REFINING)            ║
║    2a. Transfer molten bath to refractory AOD converter vessel.  ║
║    2b. Inject high-pressure mixture of Oxygen and Argon gas      ║
║        through submerged side tuyeres [→ R110]:                  ║
║        Phase I (Blow 3:1 O₂:Ar): Rapid decarburization from      ║
║        1.5% C down to 0.40% C without oxidizing chromium:        ║
║        C + ½ O₂ ──► CO↑ (Argon lowers CO partial pressure,      ║
║        thermodynamically favoring C oxidation over Cr oxidation).║
║        Phase II (Blow 1:1 O₂:Ar): Decarburize 0.40% down to 0.10%C.║
║        Phase III (Blow 1:3 O₂:Ar): Decarburize down to <0.04% C. ║
║    2c. Reduction step: Add 5 kg ferrosilicon and 15 kg CaO flux. ║
║        Silicon reduces any oxidized chromium in slag back into   ║
║        molten steel: 2 Cr₂O₃ + 3 Si ──► 4 Cr + 3 SiO₂.           ║
║    2d. Desulfurization: Stir with pure argon bubbling for 10 min.║
║        Sulfur drops below 0.015%.                                ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: CONTINUOUS CASTING & SOLUTION ANNEALING                ║
║    3a. Tap steel at 1,520°C into preheated bottom-pour tundish.  ║
║    3b. Cast into rectangular billets.                            ║
║    3c. Heat billets in annealing furnace to 1,065°C for 1 hour to║
║        dissolve all chromium carbides into austenitic FCC solid  ║
║        solution.                                                 ║
║    3d. Water quench rapidly to <400°C in under 3 minutes to      ║
║        prevent chromium carbide grain boundary sensitization.    ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Chemical composition: Cr: 18.2%, Ni: 8.3%, C: 0.035%.       ║
║    • Microstructure: 100% single-phase austenite (non-magnetic). ║
║    • Corrosion test: 100 hr immersion in boiling 65% HNO₃ yields ║
║      corrosion rate <0.2 mm/year.                                ║
╚══════════════════════════════════════════════════════════════════╝
```
