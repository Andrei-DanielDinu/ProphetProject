# R283 — Industrial Sensors and Transducers

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R283 · INDUSTRIAL SENSORS & PHYSICAL TRANSDUCERS         ║
║  Products: 1. Piezoelectric Quartz Pressure Sensor               ║
║            2. Type-K Thermocouple Temperature Sensor (1,250°C)   ║
║            3. Silicon PIN Photodiode Light Sensor                ║
║            4. Capacitive Differential Accelerometer (G-Sensor)   ║
╠══════════════════════════════════════════════════════════════════╣
║  TRANSDUCTION: THE SENSES OF THE MACHINE                         ║
║    Computers and automated governors cannot act on the world     ║
║    without transducers that convert physical state variables     ║
║    (pressure, temperature, light, acceleration) into calibrated  ║
║    analog electrical voltage or charge.                          ║
╠══════════════════════════════════════════════════════════════════╣
║  SENSOR 1: PIEZOELECTRIC QUARTZ TRANSDUCER [→ R000-F / R072]     ║
║    • Physical Principle: Curie brothers (1880). Direct piezo-    ║
║      electric effect in non-centrosymmetric crystals (α-quartz). ║
║    • Crystal Orientation: Slice quartz crystal perpendicular to  ║
║      crystallographic X-axis (X-cut, 10 mm dia × 1 mm thick).    ║
║    • Sputter gold/aluminum electrodes on both flat faces.        ║
║    • Operation: Dynamic mechanical force/pressure compresses the ║
║      crystal lattice, displacing positive silicon and negative   ║
║      oxygen ions: generates a surface electrostatic charge       ║
║      (q = d₁₁ × F, where d₁₁ = 2.31 pC/N).                       ║
║    • High-impedance FET amplifier converts charge to 0–10V.      ║
║    • Measures: engine cylinder pressure, explosive shock waves.  ║
╠══════════════════════════════════════════════════════════════════╣
║  SENSOR 2: CHROMEL-ALUMEL TYPE-K THERMOCOUPLE [→ R040 / R084]    ║
║    • Physical Principle: Thomas Seebeck (1821). Thermoelectric   ║
║      effect: temperature gradient along two dissimilar metal     ║
║      wires produces a proportional open-circuit voltage EMF!     ║
║    • Leg 1 (Chromel): 90% Nickel + 10% Chromium alloy wire.      ║
║    • Leg 2 (Alumel): 95% Nickel + 2% Aluminum + 2% Manganese.    ║
║    • Hot junction: Fuse tips together in oxygen-torch flame.     ║
║    • Sensitivity: 41.2 microvolts per °C (μV/°C).                ║
║    • Range: -200°C to +1,250°C (withstands blast furnaces,      ║
║      kilns, and jet exhaust; zero melting or degradation!).      ║
╠══════════════════════════════════════════════════════════════════╣
║  SENSOR 3: SILICON PIN PHOTODIODE [→ R100 / R101]                ║
║    • Structure: Planar P-type / Intrinsic / N-type silicon wafer.║
║    • Wide intrinsic (I) layer between P and N regions.           ║
║    • Photons with energy > 1.12 eV (silicon bandgap) penetrate   ║
║      silicon, striking valence electrons into conduction band:   ║
║      generates electron-hole pairs collected by reverse bias.    ║
║    • Photocurrent is 100% linear across 6 orders of magnitude    ║
║      of light intensity! Used in optical pyrometers & encoders.  ║
╠══════════════════════════════════════════════════════════════════╣
║  SENSOR 4: CAPACITIVE MEMS ACCELEROMETER                         ║
║    • Micro-machined silicon comb finger structure:               ║
║      A central seismic proof mass (m) is suspended by flexible   ║
║      silicon micro-springs between fixed capacitor plates.       ║
║    • Acceleration causes mass to displace (F = m × a), altering  ║
║      the capacitive gap between interdigitated comb teeth:       ║
║      ΔC = ε₀ × A / Δd.                                           ║
║    • On-chip CMOS circuit converts ΔC into analog G-force        ║
║      voltage: guidance for rockets, aircraft, and robot arms!    ║
╚══════════════════════════════════════════════════════════════════╝
```
