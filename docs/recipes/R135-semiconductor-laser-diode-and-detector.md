# R135 — Semiconductor Laser Diode & Photodetector

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R135 · SEMICONDUCTOR LASER DIODE & PIN PHOTODETECTOR    ║
║  End product: 1 × 1,550 nm Distributed Feedback (DFB) Laser Diode║
║  Optical output: 20 mW single-mode, Linewidth: <1 MHz, InGaAsP   ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The electro-optic photonics prerequisite for:                 ║
║    • Optical fiber telecommunication transmitters [→ R133]       ║
║    • LiDAR time-of-flight rangefinder lasers [→ R244]            ║
║    • Precision barcode, CD/DVD/Blu-ray optical disc pickup heads ║
║    • Laser interferometers for sub-nanometer metrology [→ R071]  ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Indium Phosphide (InP) Single-Crystal Wafers: [→ R100, R030]║
║    2. Organometallic Precursors:                                 ║
║       • Trimethylindium (TMIn): 100 g [→ R030]                   ║
║       • Triethylgallium (TEGa): 100 g [→ R034]                   ║
║       • Arsine Gas (AsH₃): 500 g, Phosphine Gas (PH₃): 500 g     ║
║    3. Gold-Zinc (p-contact) & Gold-Germanium (n-contact): [→ R000]║
║    4. Metal-Organic Chemical Vapor Deposition (MOCVD) Tool: 1    ║
║    5. Holographic Grating Interference Exposure Tool: 1 [→ R101] ║
║    6. Cleaving & Optical Facet Die Sorter: 1 [→ R072]            ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: QUANTUM WELL HETEROSTRUCTURE EPITAXY (MOCVD)          ║
║    1a. Load cleaned n-type InP substrate wafer into MOCVD reactor║
║        chamber at 650°C under pure hydrogen carrier gas.         ║
║    1b. Grow 1.0 μm n-InP cladding layer.                         ║
║    1c. Grow Multiple Quantum Well (MQW) active region:           ║
║        Deposit 5 periods of 6 nm strained InGaAsP quantum wells  ║
║        separated by 10 nm InGaAsP barrier layers:                ║
║        Bandgap is precisely tuned to emit at λ = 1,550 nm        ║
║        (the minimum attenuation window of silica fiber!).        ║
║    1d. Holographic grating fabrication: Holographically expose a ║
║        240 nm pitch Bragg diffraction grating into the upper     ║
║        waveguide layer to provide single-frequency distributed   ║
║        feedback (DFB).                                           ║
║    1e. Overgrow 1.5 μm p-type InP cladding and p⁺-InGaAs contact.║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: WAFER PROCESSING & DIE CLEAVING                        ║
║    2a. Etch wafer into narrow 2.0 μm wide optical ridge waveguides║
║        using reactive ion etching [→ R101].                      ║
║    2b. Passivate ridge sidewalls with SiO₂; sputter Au/Zn/Au     ║
║        p-contact metal on top and Au/Ge/Ni n-contact on backside.║
║    2c. Cleave wafer along natural crystal planes to produce      ║
║        mirror-like optical facets (cavity length = 300 μm).      ║
║    2d. Thin-film coating: Sputter 95% high-reflectivity (HR)     ║
║        coating on rear facet, and 5% anti-reflective (AR)        ║
║        coating on front emission facet.                          ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: CO-PACKAGED InGaAs PIN PHOTODETECTOR & MODULE          ║
║    3a. Photodetector chip: Epitaxially grow intrinsic InGaAs     ║
║        absorption layer on n-InP substrate; diffuse Zn for p⁺:   ║
║        Incoming 1,550 nm photons generate electron-hole pairs    ║
║        with 0.95 A/W responsivity and <50 picosecond rise time!  ║
║    3b. Mount laser diode chip, rear monitor photodiode, and      ║
║        Peltier thermoelectric cooler (TEC) inside hermetic gold- ║
║        plated butterfly package with sapphire optical window.    ║
║    3c. Laser weld single-mode optical fiber pigtail [→ R133]     ║
║        aligned to sub-micron accuracy for >70% optical coupling. ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Threshold current (Ith): <12 mA at 25°C.                    ║
║    • Side-Mode Suppression Ratio (SMSR): >45 dB.                 ║
║    • Modulation bandwidth: >10 GHz (10 Gbps direct modulation).  ║
╚══════════════════════════════════════════════════════════════════╝
```
