# R244 — LiDAR Time-of-Flight Pulsed Laser Scanner

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R244 · PULSED 3D TIME-OF-FLIGHT LiDAR SCANNER            ║
║  End product: 1 × 32-Beam 360° Automotive 3D LiDAR Sensor Unit   ║
║  Range: 200 meters, Accuracy: ±2 cm, Point rate: 600,000 pts/sec ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The 3D spatial vision perception prerequisite for:            ║
║    • Fully autonomous self-driving vehicles and robots [→ R322]  ║
║    • Drone terrain-following and collision avoidance             ║
║    • Precision topographic mapping and architectural surveying   ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Pulsed Laser Diode Array (905 nm, 75 W peak): 32 pcs [→ R135]║
║    2. Silicon Avalanche Photodiode (APD) Array: 32 pcs [→ R135]  ║
║    3. Aspheric Optical Glass Collimating Lenses: 2 [→ R061]      ║
║    4. Brushless DC Direct-Drive Motor with Encoder: 1 [→ R284]   ║
║    5. Time-to-Digital Converter (TDC) ASIC (ps resolution): 1    ║
║       [→ R130 CMOS fabrication]                                  ║
║    6. High-Speed FPGA / DSP Point Cloud Processor: 1 [→ R130]    ║
║    7. CNC Precision Aluminium Housing: 1 [→ R034, R072]          ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: PULSED TRANSMITTER & OPTICAL BEAM FORMING              ║
║    1a. Mount 32 pulsed semiconductor laser diodes [→ R135] in a  ║
║        vertical linear stack spanning a 30° vertical field of    ║
║        view (FOV).                                               ║
║    1b. Nanosecond GaN FET pulser circuit: Drive each laser diode ║
║        with 5-nanosecond, 25-ampere current pulses. Each laser   ║
║        emits a sharp 75 W peak optical pulse at λ = 905 nm.      ║
║    1c. Collimating optics: Align precision coated optical lenses ║
║        [→ R061] to collimate each beam into a low-divergence     ║
║        pencil beam (0.1° divergence).                            ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: AVALANCHE RECEIVER & TIME-TO-DIGITAL CONVERSION        ║
║    2a. Position matched 32-channel Silicon Avalanche Photodiode  ║
║        (APD) array at the focal plane of the collection optics.  ║
║    2b. Apply 150 V reverse bias to APDs: Incoming reflected      ║
║        photons create internal impact ionization with an internal║
║        avalanche gain of M = 100.                                ║
║    2c. Optical Bandpass Filter: Mount 905 nm narrow bandpass     ║
║        dielectric filter (10 nm FWHM) in front of APD array to   ║
║        block 99.9% of ambient solar illumination.                ║
║    2d. Time-to-Digital Converter (TDC): On-chip vernier delay    ║
║        line registers pulse emission and return with 50 ps       ║
║        time resolution. Range is calculated via speed of light:  ║
║        Distance d = (c × Δt) / 2.                                ║
║        A 50 ps time resolution yields ±7.5 mm ranging precision! ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: ROTARY SCANNING & POINT CLOUD SYNCHRONIZATION          ║
║    3a. Mount the entire optical pod on a balanced rotary spindle ║
║        driven by a brushless DC motor [→ R284] at 600–1,200 RPM  ║
║        (10–20 Hz full 360° rotational scan rate).                ║
║    3b. Optical rotary encoder provides 0.01° azimuth angular     ║
║        position feedback.                                        ║
║    3c. Point Cloud Engine: Coordinate transform polar coords     ║
║        (r, θ, φ) into Cartesian 3D coordinates (X, Y, Z) and     ║
║        stream raw point cloud data over Gigabit Ethernet [→ R134]║
║        to the autonomous driving computer.                       ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Range: 200 meters to 10% reflectivity targets.              ║
║    • Range accuracy: ±2 cm across full operating range.          ║
║    • Ingress protection: IP67 hermetic seal against dust & water.║
╚══════════════════════════════════════════════════════════════════╝
```
