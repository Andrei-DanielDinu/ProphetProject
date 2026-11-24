# R208 — Hemodialysis Artificial Kidney & Extracorporeal Circuit

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R208 · HEMODIALYSIS ARTIFICIAL KIDNEY SYSTEM             ║
║  End product: 1 × Clinical Hemodialysis Machine & Hollow Dialyzer║
║  Clearance: Urea clearance >250 mL/min, Ultrafiltration control  ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The life-sustaining organ-replacement prerequisite for:       ║
║    • Immediate survival of acute kidney injury & renal failure   ║
║    • Blood purification from toxins, metabolic acidosis, uremia  ║
║    • Extracorporeal membrane oxygenation (ECMO) circuit platform ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Hollow-Fiber Semi-Permeable Dialyzer Membrane: 1.8 m²      ║
║       • Polysulfone / Polyethersulfone hollow fibers: 10,000 pcs ║
║         (Internal diameter: 200 μm, Wall thickness: 40 μm)       ║
║         [→ Wet-spinning from polysulfone R163/R167]              ║
║       • Polycarbonate cylindrical housing & polyurethane potting ║
║    2. Peristaltic Roller Blood Pump: 1 [→ R284 stepper motor]    ║
║    3. Precision Proportioning Dialysate Fluid Mixing Unit: 1     ║
║       • Sodium bicarbonate concentrate (NaHCO₃): [→ R052]        ║
║       • Acidified electrolyte salts (NaCl, KCl, CaCl₂, MgCl₂):   ║
║         [→ R000-F, R052]                                         ║
║       • Reverse Osmosis (RO) ultra-pure water: 150 L/hr [→ R165] ║
║    4. Medical-Grade Silicone / PVC Blood Tubing Set: 1 [→ R168]  ║
║    5. Ultrasonic Air Bubble Detector & Optical Blood Leak Sensor:║
║       1 [→ R283, R135]                                           ║
║    6. Heparin Anticoagulant Injection Syringe Pump: 1 [→ R207]   ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: HOLLOW-FIBER DIALYZER FABRICATION                      ║
║    1a. Bundle 10,000 asymmetric polysulfone semi-permeable       ║
║        hollow fibers into cylindrical polycarbonate housing.     ║
║    1b. Centrifugally pot fiber ends in medical-grade polyurethane║
║        elastomer to seal the dialysate chamber from blood ports. ║
║    1c. Slice potted ends with surgical guillotine blade to open  ║
║        the lumen of all 10,000 hollow fibers.                    ║
║    1d. The membrane has a molecular weight cut-off (MWCO) of     ║
║        30,000 Da: Permeable to small molecules (urea 60 Da,      ║
║        creatinine 113 Da, K⁺, water) while 100% impermeable to   ║
║        serum albumin (66,000 Da) and blood cells.                ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: PROPORTIONING DIALYSATE HYDRAULIC CIRCUIT              ║
║    2a. Feed treated reverse-osmosis water at 37°C into dual-     ║
║        cylinder ceramic metering pumps [→ R072].                 ║
║    2b. Proportionally mix: 34 parts RO water + 1 part acid       ║
║        concentrate + 1.83 parts bicarbonate concentrate.         ║
║    2c. Continuous conductivity feedback [→ R283] regulates final ║
║        sodium concentration strictly at 138 mmol/L and pH at     ║
║        7.30 ± 0.05.                                              ║
║    2d. Vacuum deaeration chamber removes dissolved gases from    ║
║        dialysate fluid before it enters dialyzer.                ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: EXTRACORPOREAL BLOOD FLOW & SAFETY CONTROLS            ║
║    3a. Arterial line draws blood from patient vascular access at ║
║        300 to 400 mL/min using twin-roller peristaltic pump.     ║
║    3b. Continuous infusion of heparin (500 IU/hr) prevents       ║
║        clotting inside dialyzer fibers.                          ║
║    3c. Counter-current flow geometry: Blood flows down inside the║
║        hollow fiber lumens; dialysate flows upward outside the   ║
║        fibers at 500 mL/min, maximizing concentration gradient.  ║
║    3d. Transmembrane Pressure (TMP) regulation: Dialysate side   ║
║        is placed under controlled negative pressure (-50 to      ║
║        -300 mmHg) to draw excess patient water (ultrafiltration) ║
║        at exact volumetric rates (e.g. 800 mL/hr).               ║
║    3e. Safety fail-safes:                                        ║
║        • Optical sensor detects any red blood cell leak into     ║
║          dialysate effluent (<0.5 mL/min trigger).               ║
║        • Ultrasonic clamp detector clamps venous line instantly  ║
║          if an air microbubble (>20 μL) is detected.             ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Urea clearance (Kd): 260 mL/min at Qb=300 mL/min.           ║
║    • Albumin sieving coefficient: <0.001 (zero albumin loss).    ║
║    • Ultrafiltration accuracy: ±30 mL/hr over 4-hour treatment.  ║
╚══════════════════════════════════════════════════════════════════╝
```
