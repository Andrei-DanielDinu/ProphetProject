# R245 — Electronic Fuel Injection & Engine Control Unit (ECU)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R245 · ELECTRONIC FUEL INJECTION & CLOSED-LOOP ECU       ║
║  End product: 1 × Complete Automotive EFI & Engine Control Unit  ║
║  Emission control: Stoichiometric λ = 1.000 ± 0.005, Low BSFC    ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The electronic powertrain management prerequisite for:        ║
║    • Maximum thermal efficiency in internal combustion [→ R240]  ║
║    • Elimination of toxic carbon monoxide and unburnt fuel smog ║
║    • Drive-by-wire cruise control and autonomous vehicle driving ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. 32-Bit Real-Time Automotive Microcontroller: 1 [→ R130]    ║
║    2. Solenoid Electromagnetic Fuel Injectors: 4 pcs [→ R084]    ║
║       • High-speed needle valve, 12 V solenoid, 4-hole orifice   ║
║    3. Heated Zirconia Oxygen Sensor (λ sensor): 1 [→ R283]       ║
║    4. Variable Reluctance Crankshaft Position Sensor: 1 [→ R283] ║
║    5. Piezoresistive Manifold Absolute Pressure (MAP) Sensor: 1  ║
║    6. High-Pressure Electric Fuel Pump (3.5 bar): 1 [→ R284]     ║
║    7. Machined Aluminium Fuel Rail with Pressure Regulator: 1    ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: PRECISION FUEL INJECTORS & DELIVERY                    ║
║    1a. Machine injector nozzle body from hardened stainless      ║
║        steel [→ R036] on precision lathe [→ R072]. Drill four    ║
║        microscopic spray orifices (150 μm diameter).             ║
║    1b. Wind electromagnetic solenoid coil with fine enamelled    ║
║        copper wire [→ R084]. Install spring-loaded magnetic      ║
║        plunger needle valve.                                     ║
║    1c. Dynamic response: When energized with 12 V, needle valve  ║
║        lifts in 1.2 milliseconds, spraying atomized conical fuel ║
║        droplets (<50 μm SMD) directly toward intake valves.      ║
║    1d. Fuel rail: Distribute gasoline at regulated 3.5 bar       ║
║        pressure across all cylinders.                            ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: SENSOR TRANSDUCERS (ENGINE STATE RECOGNITION)          ║
║    2a. Crankshaft position: 60-minus-2 tooth steel reluctor      ║
║        wheel mounted on crankshaft generates magnetic AC pulses  ║
║        in variable reluctance sensor, providing 6° crank angle   ║
║        resolution and Top Dead Center (TDC) missing-tooth index. ║
║    2b. Zirconia oxygen sensor: Heated yttria-stabilized zirconia ║
║        thimble exposed to exhaust gas generates a Nernst voltage ║
║        step: 0.1 V for lean (excess O₂), 0.9 V for rich (excess  ║
║        fuel), switching sharply at stoichiometric 14.7:1 AFR!    ║
║    2c. MAP sensor: Piezoresistive silicon diaphragm measures     ║
║        intake manifold vacuum from 10 kPa to 105 kPa.            ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: REAL-TIME ECU ENGINE CONTROL LOOP                      ║
║    3a. Microcontroller executes main interrupt loop synchronized ║
║        to every crankshaft tooth pulse (<10 μs response).        ║
║    3b. Speed-Density Mass Air Calculation:                       ║
║        m_air = (V_cyl × MAP × VE) / (R_gas × T_air).             ║
║    3c. Base pulse width determination: Interpolate required fuel ║
║        mass from 16×16 Volumetric Efficiency (VE) ROM table.     ║
║    3d. Closed-loop PID lambda feedback: Adjust injector pulse    ║
║        width continuously to hold exhaust λ at exactly 1.000:    ║
║        Ensures three-way catalytic converter simultaneously      ║
║        oxidizes CO/HC and reduces NOx with >99% efficiency!      ║
║    3e. Direct electronic ignition firing: Compute ignition       ║
║        spark advance angle and trigger IGBT coil driver.         ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Stoichiometric precision: 14.7 ± 0.1 air-to-fuel ratio.     ║
║    • Injector flow matching: ±1.5% across all 4 cylinders.       ║
║    • Operating temperature: Withstands -40°C to +125°C under-hood║
╚══════════════════════════════════════════════════════════════════╝
```
