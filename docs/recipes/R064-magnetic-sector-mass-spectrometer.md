# R064 — Magnetic Sector Mass Spectrometer

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R064 · DOUBLE-FOCUSING MAGNETIC SECTOR MASS SPECTROMETER ║
║  End product: 1 × High-Resolution Isotope Ratio Mass Spectrometer║
║  Mass resolution: $M/\Delta M > 10,000$, Range: 1 to 1,000 amu   ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The fundamental chemical and isotopic analyzer for:           ║
║    • Uranium-235 vs Uranium-238 isotopic ratio assays [→ R120]   ║
║    • Radiometric geochronology dating (U-Pb, K-Ar, C-14)         ║
║    • Residual gas analysis in vacuum chambers and leak detection ║
║    • Identifying complex organic molecular synthesis products    ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Precision Electromagnet with Homogeneous Pole Faces: 1     ║
║       (Field: 0.05 to 1.5 Tesla, 60° deflection) [→ R040, R084]  ║
║    2. Cylindrical Electrostatic Energy Sector (ESA): 1 [→ R036]  ║
║    3. Electron Ionization (EI) Ion Source with Rhenium Wire: 1   ║
║       [→ R091]                                                   ║
║    4. Discrete-Dynode Electron Multiplier Detector: 1 [→ R090]   ║
║    5. High-Vacuum Stainless Chamber (<10⁻⁶ Pa): 1 [→ R036, R092] ║
║    6. Ultra-Stable Dual High-Voltage Power Supply (10 kV): 1     ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: ELECTRON IMPACT ION SOURCE & ACCELERATION              ║
║    1a. Introduce volatile sample gas through molecular leak      ║
║        pinhole orifice into ion chamber at $10^{-4}\text{ Pa}$.  ║
║    1b. Thermionic rhenium/tungsten filament [→ R091] emits 70 eV ║
║        electrons across the ionization chamber:                  ║
║        $M + e^- (70\text{ eV}) ──► M^{+\bullet} + 2 e^-$.        ║
║        70 eV matches the de Broglie wavelength of valence bonds, ║
║        producing both molecular ions and diagnostic fragment ions║
║    1c. Electrostatic repeller and extraction slit pull positive  ║
║        ions out of ionization chamber.                           ║
║    1d. Accelerate ions through multi-plate electrostatic lens at ║
║        $V = 5,000\text{ V}$: All ions acquire identical kinetic  ║
║        energy: $E_k = q V = \frac{1}{2} m v^2$.                  ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: DOUBLE-FOCUSING GEOMETRY (ESA + MAGNETIC SECTOR)       ║
║    2a. Electrostatic Analyzer (ESA): Ions pass through a 63.5°   ║
║        curved electrostatic sector between two concentric metal  ║
║        plates: Filters ions by kinetic energy alone, focusing    ║
║        all ions of identical energy to an intermediate slit,     ║
║        eliminating thermal energy dispersion!                    ║
║    2b. Magnetic Sector Analyzer: Ions enter 60° homogeneous      ║
║        magnetic field $B$ orthogonal to ion flight path.         ║
║    2c. Lorentz force bends ions into circular trajectories:      ║
║        $q v B = \frac{m v^2}{r} \implies r = \frac{m v}{q B}$.   ║
║        Substituting velocity $v = \sqrt{\frac{2 q V}{m}}$:       ║
║        $\frac{m}{q} = \frac{B^2 r^2}{2 V}$.                      ║
║    2d. Mass separation: Lighter ions bend sharply along small    ║
║        radii; heavier ions bend gradually along large radii!     ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: DETECTION & ION COUNTING                               ║
║    3a. Exit slit: Precision micrometer adjustable slit selects   ║
║        ions of exact single $m/z$ ratio.                         ║
║    3b. Faraday Cup detector: Ions strike grounded carbon-coated  ║
║        metal cup; ion current flows to ground through a $10^{11} ║
║        \Omega$ resistor; electrometer measures femtoamp currents ║
║        ($1\text{ fA} = 6,240\text{ ions/sec}$).                  ║
║    3c. Electron Multiplier: For trace analysis, ions strike      ║
║        beryllium-copper conversion dynode, emitting secondary    ║
║        electrons; cascade through 16 dynodes amplifies signal    ║
║        $10^6$-fold into measurable microsecond pulses!           ║
║    3d. Magnetic field scan: Ramp magnetic field $B$ continuously ║
║        from 0.05 T to 1.2 T; sweep entire mass spectrum from     ║
║        1 to 500 amu onto detector in 30 seconds.                 ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Mass resolution ($10\%\text{ valley}$): $>10,000$ (resolves ║
║      $C_2H_4^+$ at 28.0313 Da from $N_2^+$ at 28.0061 Da!).      ║
║    • Isotope ratio precision: $\pm 0.01\%$ on ²³⁵U/²³⁸U ratios.  ║
║    • Dynamic range: $10^8$ linear response range.                ║
╚══════════════════════════════════════════════════════════════════╝
```
