# R284 — AC Induction Motor and Closed-Loop Servomotors

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R284 · THREE-PHASE INDUCTION MOTOR & DIGITAL SERVOS      ║
║  Products: 1. 10 kW Squirrel-Cage AC Induction Motor (1,450 RPM) ║
║            2. Precision Closed-Loop DC Brushless Servomotor      ║
╠══════════════════════════════════════════════════════════════════╣
║  PART 1: NIKOLA TESLA SQUIRREL-CAGE INDUCTION MOTOR (1888)       ║
║                                                                  ║
║  WHY THIS IS THE WORKHORSE OF ALL FACTORIES                      ║
║    DC motors have carbon brushes and commutators that spark,     ║
║    wear out, and require constant maintenance.                   ║
║    Tesla's induction motor has ZERO electrical connections to    ║
║    the rotor! It is brushless, maintenance-free, explosion-      ║
║    proof, and runs continuously for decades.                     ║
║                                                                  ║
║  PHYSICAL MECHANISM:                                             ║
║    1. Three-phase AC current (R082) fed into stator coils        ║
║       spaced 120° apart creates a ROTATING MAGNETIC FIELD        ║
║       spinning at synchronous speed N_s = (120 × f) / P = 1500 RPM║
║    2. The rotating field sweeps through the rotor bars, cutting  ║
║       them with magnetic flux.                                   ║
║    3. By Faraday's Law, massive currents are induced in the      ║
║       short-circuited copper rotor bars.                         ║
║    4. By Lorentz Force (F = I × L × B), the induced rotor        ║
║       currents interact with the stator field, exerting rotary   ║
║       torque that drags the rotor into spin!                     ║
║                                                                  ║
║  MANUFACTURING:                                                  ║
║  A) Stator Core: 0.5 mm laminated silicon steel punchings (R040) ║
║     with 36 slots. Wound with enameled copper wire (R084).       ║
║  B) Squirrel-Cage Rotor: Cylindrical iron lamination pack.       ║
║     Heavy copper or aluminum bars die-cast into perimeter slots,║
║     welded to solid short-circuiting end-rings at both faces.    ║
║  C) Shaft & Bearings: Forged steel shaft on deep-groove ball     ║
║     bearings running in cast iron end-bells.                     ║
╠══════════════════════════════════════════════════════════════════╣
║  PART 2: CLOSED-LOOP DIGITAL BRUSHLESS SERVOMOTOR                ║
║                                                                  ║
║  WHY SERVOS ENABLE ROBOTICS & AUTOMATION                         ║
║    An induction motor spins continuously. A servomotor must      ║
║    move to an EXACT angular coordinate (e.g. 47.35°), lock with  ║
║    zero play, and resist external deflecting loads.              ║
║                                                                  ║
║  COMPONENTS:                                                     ║
║    • Rotor: High-energy Neodymium-Iron-Boron (NdFeB) or Samarium-║
║      Cobalt permanent magnet rotor drum.                         ║
║    • Stator: 3-phase slotless winding driven by PWM H-bridge.    ║
║    • Optical Rotary Shaft Encoder (R283): Glass disc etched with ║
║      4,096 radial chromium chrome lines. Dual photodiode sensors ║
║      read quadrature pulses: detects 0.087° position increments! ║
║    • Microcontroller PID Servo Loop (R130):                      ║
║      Samples optical position 10,000 times per second. Compares  ║
║      actual position to target: calculates Proportional,         ║
║      Integral, and Derivative corrective currents, driving error ║
║      to ABSOLUTE ZERO within 5 milliseconds!                     ║
╚══════════════════════════════════════════════════════════════════╝
```
