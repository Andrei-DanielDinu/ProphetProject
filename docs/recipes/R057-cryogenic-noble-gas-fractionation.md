# R057 — Cryogenic Noble Gas Fractionation (Argon, Neon, Helium)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R057 · CRYOGENIC NOBLE GAS EXTRACTION (Ar, Ne, He)       ║
║  End product: 100 m³ Ultra-Pure Argon (99.9999%) + Helium (99.99%)║
║  Operating temperatures: -186°C (Argon), -246°C (Neon), 4.2 K (He)║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The inert chemical shield and extreme cryogenics tool for:    ║
║    • Argon shielding gas for titanium Kroll process [→ R035]     ║
║    • Argon atmosphere for Czochralski silicon ingots [→ R100]    ║
║    • Helium carrier gas for chromatography and gas lasers [→ R064]║
║    • Liquid helium cooling for superconducting MRI magnets       ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Atmospheric Cryogenic Air Separation Unit: 1 [→ R110]      ║
║    2. Natural Gas / Monazite Sand (Helium source): [→ R054, R000]║
║    3. Crude Argon Side-Draw Distillation Column: 1 [→ R036]      ║
║    4. Catalytic Hydrogen Deoxygenator Reactor: 1 [→ R056]        ║
║    5. Cryogenic Molecular Sieve Synthetic Zeolite Beds: 2 [→ R060]║
║    6. Multi-Stage Helium Reciprocating Compressor (150 bar): 1   ║
║    7. Cryogenic Coldbox with Vacuum-Perlite Insulation: 1 [→ R092]║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: CRUDE ARGON COLUMN (0.93% ATMOSPHERIC ABUNDANCE)       ║
║    1a. Cryogenic air distillation column [→ R110]: Argon has a   ║
║        boiling point (-185.9°C) intermediate between nitrogen    ║
║        (-195.8°C) and oxygen (-183.0°C).                         ║
║    1b. At the 30th tray above the oxygen sump, argon reaches a   ║
║        peak local concentration of ~10% in vapor phase.          ║
║    1c. Side-draw argon stream: Tap vapor into auxiliary packed   ║
║        crude argon column (40 trays):                            ║
║        Top product is "crude argon" containing 95% Ar, 4.5% O₂,  ║
║        and 0.5% N₂.                                              ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: CATALYTIC DEOXYGENATION & PURE ARGON DISTILLATION      ║
║    2a. Deoxo reactor: Mix crude argon with stoichiometric pure   ║
║        hydrogen gas [→ R056]. Pass over palladium/alumina catalyst║
║        pellets at 400°C:                                         ║
║        $2\text{ H}_2 + \text{O}_2 ──► 2\text{ H}_2\text{O}$.     ║
║        Oxygen is completely consumed down to $<1\text{ ppm}$!    ║
║    2b. Condense and dry generated water through 4A synthetic     ║
║        zeolite molecular sieve beds [→ R060].                    ║
║    2c. Pure argon column: Feed deoxygenated argon into secondary ║
║        cryogenic column: Pure nitrogen boils off the top;        ║
║        Pure liquid Argon (99.9999% "six-nines" electronic grade) ║
║        taps from the reboiler bottom at -185.9°C!                ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: NEON & HELIUM LIQUEFACTION CASCADE                     ║
║    3a. Non-condensable gas recovery: Neon and Helium do not      ║
║        liquefy at liquid nitrogen temperatures (-196°C).         ║
║        They accumulate in the main condenser dome of the air     ║
║        separation unit as a non-condensable purge gas.           ║
║    3b. Cryogenic charcoal adsorption: Pass purge gas through     ║
║        activated coconut carbon beds [→ R042] immersed in liquid ║
║        nitrogen at -196°C: Nitrogen and oxygen adsorb completely;║
║        crude Ne-He gas passes through unhindered.                ║
║    3c. Neon separation: Cool to 27 K (-246°C) using closed-cycle ║
║        Brayton helium expander: Neon freezes into solid neon     ║
║        crystals, leaving gaseous helium in the vapor space.      ║
║    3d. Liquid Helium Collins cycle (4.2 K): Compress helium gas  ║
║        to 25 bar; precool with liquid nitrogen to 77 K; expand   ║
║        through reciprocating expansion engines to 10 K; finally  ║
║        expand through Joule-Thomson needle valve: Helium liquefies║
║        into superfluid helium liquid at 4.22 K (-268.9°C)!       ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Argon purity: $>99.9999\%$ ($<0.5\text{ ppm O}_2$,          ║
║      $<1\text{ ppm N}_2$, $<0.2\text{ ppm H}_2\text{O}$).        ║
║    • Helium temperature: 4.2 K at 1.0 atm (maintains liquid state║
║      inside vacuum-jacketed super-insulated liquid dewars).      ║
╚══════════════════════════════════════════════════════════════════╝
```
