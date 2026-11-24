# R081 — Lead-Acid Secondary Storage Battery (Planté Cell)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R081 · LEAD-ACID SECONDARY STORAGE ACCUMULATOR           ║
║  End product: 1 × 12V 60Ah Rechargeable Battery (6-cell series)  ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    Provides buffer storage and portable electrical power for:    ║
║    • Self-excitation bootstrapping of dynamos [→ R080]           ║
║    • Telegraph & telephone relay stations                        ║
║    • Mobile vehicular starters and field radio gear              ║
║    • Steady DC bias for early triode plate circuits [→ R090]     ║
╠══════════════════════════════════════════════════════════════════╣
║  ELECTROCHEMICAL MECHANISM                                       ║
║    Discharge reaction:                                           ║
║    PbO₂ (pos) + Pb (neg) + 2 H₂SO₄ ──► 2 PbSO₄ + 2 H₂O  (E° = 2.05V)║
║    Charge reaction:                                              ║
║    2 PbSO₄ + 2 H₂O + Electric Current ──► PbO₂ + Pb + 2 H₂SO₄    ║
╠══════════════════════════════════════════════════════════════════╣
║  INGREDIENTS (per 2V cell × 6 cells = 12V bank)                  ║
║  A) 12 kg Pure rolled chemical lead sheet (2 mm thick)           ║
║     [→ R000-Mine: Galena (PbS) smelted in low-temp furnace 800°C]║
║  B) 4 L Sulfuric acid (H₂SO₄), 30% concentration, SG 1.25       ║
║     [→ R053: Lead chamber process]                               ║
║  C) 6 × Glass or glazed vitrified stoneware battery jars (2 L)   ║
║     [→ R020 / R060]                                              ║
║  D) Thin grooved cedar or porous ceramic plate separators        ║
║  E) Melted petroleum bitumen for sealing cell tops [→ R000-Oil]  ║
╠══════════════════════════════════════════════════════════════════╣
║  PROCESS                                                         ║
║                                                                  ║
║  STEP 1 — PLATE FORMING (Gaston Planté Method)                   ║
║    1a. Cut lead sheets into 15 × 20 cm plates with integral top  ║
║        connection lugs. Score faces with knife to increase area. ║
║    1b. Suspend alternating plates (positive and negative) in     ║
║        jar with porous cedar separators. Connect in parallel.    ║
║                                                                  ║
║  STEP 2 — ELECTROLYTE FILLING                                    ║
║    2a. Pour 30% H₂SO₄ into cells until plates submerged 2 cm.    ║
║    2b. ⚠ ALWAYS POUR ACID INTO WATER, NEVER WATER INTO ACID!    ║
║                                                                  ║
║  STEP 3 — FORMATION CYCLING (Building the Active Mass)           ║
║    3a. Connect to DC dynamo (R080): Charge at 3 Amperes for 12h. ║
║        Positive plate turns dark chocolate-brown (PbO₂).         ║
║        Negative plate turns slate-grey spongy lead (Pb).         ║
║    3b. Discharge completely through resistor.                    ║
║    3c. Reverse polarity and recharge (breaks up lead surface).   ║
║    3d. Repeat formation cycle 6 times: capacity expands from     ║
║        2 Ah to 60 Ah as deep spongy active layers develop.       ║
╠══════════════════════════════════════════════════════════════════╣
║  PERFORMANCE: Nominal cell voltage: 2.1V. Total bank: 12.6V.     ║
║  Internal resistance: <0.02 Ω. Max burst discharge: 150 Amperes.║
╚══════════════════════════════════════════════════════════════════╝
```
