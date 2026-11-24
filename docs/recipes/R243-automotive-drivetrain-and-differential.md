# R243 — Automotive Drivetrain, Differential, and Hydraulic Brakes

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R243 · AUTOMOTIVE DRIVETRAIN & HYDRAULIC CHASSIS         ║
║  Components: 1. Bevel Gear Open Differential                     ║
║              2. 4-Speed Synchromesh Manual Transmission          ║
║              3. Pascal Hydraulic Dual-Circuit Disc Brakes        ║
╠══════════════════════════════════════════════════════════════════╣
║  PART 1: THE BEVEL GEAR OPEN DIFFERENTIAL (Onésiphore Pecqueur)  ║
║                                                                  ║
║  THE CORNERING PARADOX:                                          ║
║    When a vehicle turns a curve, the outside wheel travels a     ║
║    longer circular arc than the inside wheel:                    ║
║    v_outer = ω × (R + w/2)  vs  v_inner = ω × (R - w/2).         ║
║    If both wheels are locked to a solid axle, tires scrub and    ║
║    skid across pavement, and the steel axle snaps from torsion.  ║
║                                                                  ║
║  MECHANICAL RESOLUTION:                                          ║
║    • Crown Wheel (Ring Gear): Large hypoid spiral bevel gear     ║
║      driven by the engine driveshaft pinion (R072).              ║
║    • Differential Carrier Case: Bolted to crown wheel, houses    ║
║      two floating conical bevel pinions ("spider gears").        ║
║    • Sun Gears (Side Gears): Splined to left and right drive     ║
║      half-shafts.                                                ║
║    • Operation:                                                  ║
║      - Traveling straight: Spider gears do not rotate on pins;   ║
║        entire carrier spins as a solid block; wheels turn 1:1.   ║
║      - Turning a corner: Resistance on inside wheel causes       ║
║        spider gears to rotate on their pins, transferring exact  ║
║        excess RPM to outside wheel:                              ║
║        (ω_left + ω_right) / 2 = ω_carrier (Always conserved!).   ║
╠══════════════════════════════════════════════════════════════════╣
║  PART 2: PASCAL HYDRAULIC DUAL-CIRCUIT BRAKES                    ║
║                                                                  ║
║  PRESSURE MULTIPLICATION:                                        ║
║    By Pascal's Law, static pressure applied to an enclosed       ║
║    fluid transmits undiminished in all directions: P = F / A.    ║
║    • Master Cylinder Piston: Area A₁ = 3.0 cm². Driver exerts   ║
║      500 N pedal force: Fluid pressure P = 500 N / 3 cm² = 16.7 bar║
║    • Wheel Caliper Pistons: 4 pistons, each Area A₂ = 20.0 cm².  ║
║      Clamping force per caliper = P × A₂ = 16.7 bar × 20 cm²     ║
║      = 3,340 N (Over 6× mechanical force amplification!).        ║
║    • Cast iron ventilated rotor disks clamped by semi-metallic   ║
║      friction pads: converts 50 tonnes of kinetic energy into    ║
║      thermal heat, stopping vehicle from 100 km/h in 35 meters!  ║
╚══════════════════════════════════════════════════════════════════╝
```
