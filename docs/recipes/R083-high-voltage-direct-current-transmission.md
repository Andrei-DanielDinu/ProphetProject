# R083 — High-Voltage Direct Current (HVDC) Transmission

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R083 · HIGH-VOLTAGE DIRECT CURRENT (HVDC) CONVERTER      ║
║  End product: 1 × 500 kV, 1,000 MW Bipolar HVDC Converter Station║
║  Transmission loss: <3% per 1,000 km (zero reactive AC losses)   ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The bulk long-distance power transmission prerequisite for:   ║
║    • Transmitting thousands of MW from remote hydro dams [→ R170]║
║    • Long-distance underwater sea cables (impossible via AC)     ║
║    • Asynchronous interconnection of regional electric grids     ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. High-Power Silicon Thyristor Discs (8.5 kV, 4 kA): 400 pcs ║
║       [→ R100 125 mm monocrystalline silicon wafer, R101]        ║
║    2. Converter Transformers (Three-Phase, Star/Delta): 2 pcs    ║
║       [→ Grain-oriented electrical steel sheet R041, copper R084]║
║    3. Air-Core Smoothing Reactors (50 mH, 500 kV): 2 pcs         ║
║    4. Deionized Water Cooling Heat Exchanger Skids: 2 [→ R036]   ║
║    5. AC Harmonic Filter Shunt Capacitor Banks: 6 banks [→ R165] ║
║    6. High-Speed Optical Triggering Fiber Links: 800 pcs [→ R133]║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: HIGH-POWER THYRISTOR VALVE TOWERS                      ║
║    1a. High-power phase-control thyristors: Fabricate 125 mm     ║
║        diameter four-layer p-n-p-n silicon wafer discs [→ R100]. ║
║        Package in ceramic press-pack housings under 50 kN clamp  ║
║        force with double-sided deionized water cooling blocks.   ║
║    1b. Connect thyristors in series string (60 thyristors per    ║
║        valve arm) with parallel RC snubber circuits and grading  ║
║        resistors to ensure equal voltage sharing across string.  ║
║    1c. Assemble twelve valve arms into a 12-Pulse Bridge         ║
║        suspended inside climate-controlled valve hall from       ║
║        seismic-proof ceiling insulators.                         ║
║    1d. Optical gate firing: Trigger each thyristor gate via      ║
║        direct laser pulse through flexible optical fiber cables  ║
║        [→ R133, R135], providing 500 kV dielectric isolation.   ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: 12-PULSE CONVERTER OPERATION                          ║
║    2a. Feed AC power into dual three-phase converter transformers║
║        (one secondary winding connected in Star Y-Y, the second  ║
║        in Delta Y-Δ): Introduces a 30° electrical phase shift    ║
║        between transformer secondaries.                          ║
║    2b. 12-pulse rectification: The two 6-pulse bridges in series ║
║        eliminate the 5th and 7th harmonics automatically,        ║
║        leaving only low-amplitude 12n ± 1 harmonics.             ║
║    2c. Phase control firing angle α: Adjusting thyristor firing  ║
║        delay angle controls power flow direction and magnitude:  ║
║        • α < 90°: Rectifier mode (converts AC to +500 kV DC).    ║
║        • α > 90°: Inverter mode (converts DC back to AC grid).   ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: DC SMOOTHING & TRANSMISSION LINE                       ║
║    3a. Pass converted DC through large 50 mH oil-insulated       ║
║        smoothing reactor to suppress current ripple.             ║
║    3b. Bipolar line configuration: +500 kV positive pole and     ║
║        -500 kV negative pole conductors strung on steel towers   ║
║        with composite silicone insulators [→ R168].              ║
║    3c. Ground electrode return provides emergency monopolar      ║
║        operation if one pole suffers a line fault.               ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Valve breakdown withstand: 1,200 kV BIL lightning impulse.  ║
║    • Converter efficiency: >99.1% full load conversion.          ║
║    • Total harmonic distortion (THD) on AC grid side: <1.5%.     ║
╚══════════════════════════════════════════════════════════════════╝
```
