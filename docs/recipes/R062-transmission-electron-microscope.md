# R062 — Transmission Electron Microscope (TEM)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R062 · TRANSMISSION ELECTRON MICROSCOPE (TEM)           ║
║  End product: 1 × 200 kV High-Resolution Electron Microscope     ║
║  Point resolution: 0.19 nm (Direct imaging of atomic lattices)   ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The sub-atomic materials characterization prerequisite for:   ║
║    • Imaging crystal lattice defects in semiconductor wafers [→ R100]║
║    • Visualizing virus structures and molecular biology [→ R150] ║
║    • Verifying nanoscale gate oxides and carbon nanotubes [→ R167]║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Tungsten Hairpin / LaB₆ Single-Crystal Cathode: 1 [→ R091] ║
║    2. High-Voltage Cockcroft-Walton Accelerator (200 kV): 1      ║
║       [→ R082, R101 high-voltage diodes]                         ║
║    3. Soft Magnetic Iron Pole Pieces (Pure Armco Iron): 12 pcs   ║
║       [→ Ultra-low carbon wrought iron, R040]                    ║
║    4. Precision Enamelled Copper Magnetic Lens Coils: [→ R084]   ║
║    5. Ultra-High Vacuum Turbomolecular & Ion Getter Pump: 1      ║
║       (Vacuum <10⁻⁷ Pa) [→ R092]                                 ║
║    6. Phosphor Viewing Screen & YAG-CCD Camera: 1 [→ R060, R130] ║
║    7. Precision Goniometer Specimen Stage: 1 [→ R071, R072]      ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: ELECTRON GUN & HIGH-VOLTAGE ACCELERATION COLUMN        ║
║    1a. Mount hairpin tungsten filament (diameter 100 μm [→ R091])║
║        inside Wehnelt cylinder aperture.                         ║
║    1b. Pass direct current to heat filament to 2,700 K: Emits    ║
║        electrons by thermionic emission.                         ║
║    1c. 200 kV accelerating anode: Multi-stage accelerator column ║
║        with high-stability voltage divider accelerates electrons ║
║        to 70% of the speed of light ($v = 0.695 c$):             ║
║        De Broglie wavelength of 200 keV electrons:               ║
║        $\lambda = \frac{h}{\sqrt{2 m_0 e V (1 + \frac{e V}{2 m_0 c^2})}} = 0.00251\text{ nm}$ (2.5 picometers!).║
║        Over 200,000 times shorter than visible light!            ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: ELECTROMAGNETIC LENSES & COLUMN OPTICS                 ║
║    2a. Machine rotationally symmetric lens pole pieces from pure ║
║        low-hysteresis iron [→ R040] with sub-micron concentricity║
║        on precision lathe [→ R072].                              ║
║    2b. Wind water-cooled coils with thousands of turns of fine   ║
║        copper wire [→ R084]. Current stability $\Delta I/I < 10^{-6}$.║
║    2c. Magnetic lens action: Strong inhomogeneous magnetic field ║
║        in pole piece gap ($B \approx 2.0\text{ T}$) exerts Lorentz║
║        force ($F = -e \vec{v} \times \vec{B}$), focusing the     ║
║        spiraling electron beam to a parallel 10 nm spot.         ║
║    2d. Column arrangement:                                       ║
║        • Dual condenser lenses: Collimates incident electron beam║
║        • Objective lens: Primary image formation (mag: 50×)      ║
║        • Diffraction aperture: Selects selected area diffraction ║
║        • Intermediate & Projector lenses: Magnifies final image  ║
║          up to 1,000,000× onto viewing screen.                   ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: SPECIMEN PREPARATION & VACUUM IMAGING                  ║
║    3a. Specimen must be electron-transparent (thickness <50 nm). ║
║        Polish sample mechanically, then dimple and thin to       ║
║        perforation with argon ion milling beam [→ R057].         ║
║    3b. Insert 3 mm copper grid into side-entry goniometer stage; ║
║        air-lock pumps down to <10⁻⁵ Pa in 60 seconds.            ║
║    3c. Transmitted electrons undergo phase contrast and          ║
║        diffraction contrast as they pass through atomic columns. ║
║    3d. Project magnified electron wave onto P20 phosphor screen  ║
║        or fiber-optically coupled CCD detector [→ R130, R133].   ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Lattice resolution: Clear atomic column fringe spacing of   ║
║      gold <200> planes ($d = 0.204\text{ nm}$).                  ║
║    • High-voltage ripple: <1 ppm peak-to-peak at 200 kV.         ║
║    • Astigmatism: Correctable to <5 nm using 8-pole stigmator.   ║
╚══════════════════════════════════════════════════════════════════╝
```
