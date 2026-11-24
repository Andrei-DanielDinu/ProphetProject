# R056 — Chlor-Alkali Membrane Cell Electrolysis

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R056 · MEMBRANE CHLOR-ALKALI ELECTROLYSIS PLANT          ║
║  End product: 10 tonnes Chlorine Gas + 11.3 tonnes Pure NaOH     ║
║  Current efficiency: >96%, Energy: 2,100 kWh/tonne Cl₂, Mercury-0║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The dual cornerstone of inorganic industrial chemistry:      ║
║    • Pure chlorine gas for PVC plastics, titanium, and water [→ R171]║
║    • Pure sodium hydroxide for alumina Bayer process [→ R034]    ║
║    • Byproduct pure hydrogen gas for Haber-Bosch ammonia [→ R055]║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Saturated Raw Brine (NaCl solution, 310 g/L): 30 m³ [→ R000]║
║    2. Perfluorosulfonic Acid Cation-Exchange Membrane: 25 m²     ║
║       (Nafion type, PTFE backbone with -SO₃⁻ groups) [→ R166]    ║
║    3. Dimensionally Stable Anodes (DSA Titanium + RuO₂): 20 pcs  ║
║       [→ R035 titanium plate coated with ruthenium oxide]        ║
║    4. Nickel Expanded Mesh Cathodes with Ni-S Coating: 20 pcs    ║
║       [→ Electrolytic nickel, R000, R036]                        ║
║    5. Chelating Ion-Exchange Resin Bed: 500 L [→ R163]           ║
║    6. High-Current DC Rectifier System (3.2 V/cell, 50 kA): 1    ║
║       [→ R083 thyristor rectifier]                               ║
║    7. Titanium Plate Heat Exchangers & Compressors: 1 set [→ R035]║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: PRIMARY & SECONDARY BRINE ULTRA-PURIFICATION          ║
║    1a. Dissolve mined rock salt or solar halite [→ R000] in water║
║        to form saturated 310 g/L NaCl solution.                  ║
║    1b. Primary chemical precipitation: Add $Na_2CO_3$ [→ R052] to║
║        precipitate $Ca^{2+}$ as $CaCO_3\downarrow$; add $NaOH$ to║
║        precipitate $Mg^{2+}$ as $Mg(OH)_2\downarrow$. Filter.    ║
║    1c. Secondary chelating ion-exchange polishing: Pass brine    ║
║        through aminophosphonic chelating resin columns:          ║
║        Reduces multivalent hardness cations ($Ca^{2+}, Mg^{2+},  ║
║        Sr^{2+}$) to $<20\text{ parts per billion (ppb)}$!        ║
║        This is critical: trace calcium would permanently clog the║
║        perfluorosulfonate membrane pores within hours.           ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: MEMBRANE CELL ELECTROCHEMICAL CASCADE                  ║
║    2a. Cell structure: Filter-press assembly clamping multiple   ║
║        electrolyzer frames separated by Nafion membranes [→ R166]║
║    2b. Anode compartment (DSA Titanium coated with RuO₂/TiO₂):   ║
║        Feed pure saturated 300 g/L NaCl brine.                   ║
║        Oxidation reaction:                                       ║
║        $2\text{ Cl}^- ──► \text{Cl}_2\uparrow + 2 e^-$           ║
║        ($E^0 = +1.36\text{ V}$). Greenish-yellow chlorine gas    ║
║        evolves vigorously at the anode mesh.                     ║
║    2c. Selective Membrane Transport: Cation-exchange membrane    ║
║        carries fixed negative sulfonate ($-SO_3^-$) groups:      ║
║        Passes positive $Na^+$ ions freely through to cathode,    ║
║        while completely repelling negative $Cl^-$ and $OH^-$ ions!║
║    2d. Cathode compartment (Activated Nickel mesh):              ║
║        Feed pure deionized water.                                ║
║        Reduction reaction:                                       ║
║        $2\text{ H}_2\text{O} + 2 e^- ──► \text{H}_2\uparrow +    ║
║        2\text{ OH}^-$ ($E^0 = -0.83\text{ V}$).                  ║
║        Pure hydrogen gas evolves at cathode; remaining $OH^-$    ║
║        combines with migrated $Na^+$ to produce ultra-pure,      ║
║        salt-free 32 wt% Sodium Hydroxide ($NaOH$) solution!      ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: DRYING, LIQUEFACTION & CAUSTIC EVAPORATION             ║
║    3a. Chlorine treatment: Hot wet $Cl_2$ gas is cooled to 15°C, ║
║        scrubbed of moisture in concentrated sulfuric acid towers ║
║        [→ R053] (dew point drops to -40°C), and compressed to    ║
║        8 bar in liquid-ring compressors into liquid chlorine.    ║
║    3b. Hydrogen treatment: Cooled, compressed to 200 bar, and    ║
║        piped directly to Haber-Bosch ammonia synthesis [→ R055]. ║
║    3c. Caustic concentration: Triple-effect falling-film nickel  ║
║        evaporators [→ R036] concentrate 32% NaOH to commercial   ║
║        50% lye or solid anhydrous caustic flakes.                ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • NaOH purity: Rayon grade ($<10\text{ ppm NaCl}$ salt).      ║
║    • Chlorine purity: $>99.8\%\text{ Cl}_2$ (<0.1% O₂ byproduct).║
║    • Membrane operating lifetime: $>3\text{ years}$ continuous.  ║
╚══════════════════════════════════════════════════════════════════╝
```
