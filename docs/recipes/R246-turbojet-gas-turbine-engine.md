# R246 — Turbojet & Turbofan Gas Turbine Engine

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R246 · AXIAL-FLOW GAS TURBINE ENGINE (TURBOJET)          ║
║  End product: 1 × Axial Gas Turbine Engine (50 kN Static Thrust) ║
║  Turbine inlet temp: 1,350°C, Pressure ratio: 16:1, SFC: 0.70    ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The high-speed, high-altitude propulsion prerequisite for:    ║
║    • Supersonic and long-range commercial/military aircraft [→ R241]║
║    • High-speed cruise missiles and unmanned aerial vehicles     ║
║    • Combined-cycle natural gas industrial power generation [→ R082]║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Titanium Alloy Compressor Discs & Blades: 120 kg [→ R035]  ║
║    2. Single-Crystal Nickel Superalloy (Inconel 718 / CMSX-4):   ║
║       80 kg [→ R036, R000]                                       ║
║    3. Hastelloy X Combustion Chamber Sheet: 40 kg [→ R036]       ║
║    4. Precision Balance Dynamic Balancing Machine: 1 [→ R072]    ║
║    5. 5-Axis CNC Milling Machine for Airfoils: 1 [→ R072, R322]  ║
║    6. High-Temperature Vacuum Investment Casting Furnace: 1     ║
║       [→ R033, R092]                                             ║
║    7. Electronic FADEC Full-Authority Engine Control: 1 [→ R245] ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: MULTI-STAGE AXIAL COMPRESSOR                           ║
║    1a. Mill 8 stages of compressor discs and aerodynamic rotor   ║
║        blades from forged Ti-6Al-4V titanium alloy [→ R035].     ║
║    1b. Fit blades into fir-tree root broached slots on discs.    ║
║    1c. Compressor stages progressively compress incoming intake  ║
║        air from 1.0 bar to 16.0 bar through convergent annulus;  ║
║        stator vanes convert kinetic velocity into static pressure.║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: ANNULAR COMBUSTION CHAMBER                             ║
║    2a. Fabricate annular flame tube from perforated Hastelloy-X  ║
║        nickel-chromium sheet metal.                              ║
║    2b. Install 16 dual-orifice fuel swirl nozzles: Inject high-  ║
║        pressure aviation kerosene (jet fuel [→ R054]).           ║
║    2c. Primary zone combustion: 25% of compressed air burns with ║
║        fuel at stoichiometric flame temperature (~2,000°C).      ║
║    2d. Secondary & dilution zone: Remaining 75% of air flows     ║
║        around liner for convective cooling, then enters through  ║
║        dilution holes to mix and cool gases to 1,350°C before    ║
║        impinging on turbine blades.                              ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: SINGLE-CRYSTAL TURBINE & FILM COOLING                  ║
║    3a. Investment cast high-pressure turbine blades from nickel- ║
║        based superalloy using spiral grain selector:             ║
║        Solidifies as a single continuous crystal with zero grain ║
║        boundaries, eliminating high-temperature creep failure!   ║
║    3b. Internal serpentine cooling channels: Cast blades with    ║
║        internal ceramic cores; leach cores out with caustic soda ║
║        to form hollow cooling passages.                          ║
║    3c. Laser drill hundreds of 0.3 mm film-cooling holes across  ║
║        blade leading edge [→ R135]: High-pressure bleed air      ║
║        creates a protective insulating cool boundary layer over  ║
║        the metal surface, allowing gases at 1,350°C to pass over ║
║        metal whose melting point is only 1,320°C!                ║
║    3d. Turbine extracts mechanical power to spin compressor shaft║
║        at 12,000 RPM. Exhaust gas accelerates through convergent ║
║        nozzle to produce 50 kN net thrust.                       ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Dynamic balance: Residual unbalance <0.5 g·mm on main rotor.║
║    • Creep rupture: >1,000 hours at 980°C and 200 MPa stress.    ║
║    • Full power test run: 50 kN thrust sustained for 2 hours.    ║
╚══════════════════════════════════════════════════════════════════╝
```
