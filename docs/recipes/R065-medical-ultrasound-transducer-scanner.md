# R065 — Medical Diagnostic Ultrasound Transducer & B-Mode Scanner

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R065 · MEDICAL ULTRASOUND TRANSDUCER & B-MODE SCANNER    ║
║  End product: 1 × 128-Element Phased Array Ultrasound Probe & DSP║
║  Frequency: 3.5 to 7.5 MHz, Axial resolution: <0.5 mm, Non-ionizing║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The non-invasive real-time medical imaging tool for:          ║
║    • Obstetrics, prenatal fetal monitoring, pregnancy safety     ║
║    • Cardiology echocardiography, heart valve defect diagnosis   ║
║    • Abdominal trauma, gallbladder stones, deep vein thrombosis  ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Lead Zirconate Titanate Piezoelectric Ceramic (PZT-5H):    ║
║       1 block (Coupling factor $k_{33} > 0.75$) [→ R000, R021]   ║
║    2. Tungsten-Powder Loaded Epoxy Backing Block: 1 [→ R091, R163]║
║    3. Quarter-Wave Acoustic Matching Layer (Araldite/Alumina): 1 ║
║    4. Flexible Polyimide Printed Circuit Interconnect: 1 [→ R163]║
║    5. Precision Diamond Dicing Wire Saw (50 μm kerf): 1 [→ R072] ║
║    6. Multi-Channel High-Voltage Pulser & Low-Noise Preamp ICs: 1║
║       [→ R101, R130]                                             ║
║    7. Digital Beamformer FPGA / DSP Scan Converter: 1 [→ R130]   ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: PIEZOELECTRIC ARRAY DICING & COMPOSITE                 ║
║    1a. Synthesize high-density Lead Zirconate Titanate ($Pb[Zr_x ║
║        Ti_{1-x}]O_3$) ceramic by solid-state calcination at      ║
║        1,250°C [→ R021]. Sputter gold electrodes on both faces.  ║
║    1b. High-voltage poling: Heat PZT to 130°C in silicone oil    ║
║        [→ R168]; apply 2.5 kV/mm electric field to permanently   ║
║        align all internal ferroelectric domains; cool under bias.║
║    1c. Sub-element dicing: Using diamond dicing saw [→ R072],    ║
║        dice PZT slab into a linear array of 128 micro-elements   ║
║        (element width = 0.20 mm, kerf gap = 0.05 mm, pitch =     ║
║        $\lambda/2 \approx 0.25\text{ mm}$ for 3.5 MHz ultrasound)║
║    1d. Fill kerf gaps with low-durometer polyurethane elastomer  ║
║        to prevent acoustic cross-talk between adjacent elements. ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: ACOUSTIC MATCHING & DAMPING BACKING                    ║
║    2a. Acoustic impedance mismatch challenge: PZT acoustic      ║
║        impedance ($Z = 30\text{ MRayls}$) is 20× higher than     ║
║        human soft tissue ($Z = 1.5\text{ MRayls}$); unmitigated, ║
║        80% of sound energy would reflect off skin surface!       ║
║    2b. Quarter-wave matching layers: Cast dual composite matching║
║        layers with intermediate impedance ($Z_1 = 6\text{ MRayls}║
║        Z_2 = 2.5\text{ MRayls}$) and thickness $t = \lambda/4$: ║
║        Destructive interference eliminates reflections and       ║
║        maximizes acoustic transmission into patient body!        ║
║    2c. Heavy tungsten-epoxy backing block: Absorbs backward-     ║
║        traveling acoustic waves, damping element ringing to      ║
║        produce short 1.5-cycle pulses for high axial resolution. ║
║    2d. Cast curved acoustic silicone lens [→ R168] over probe    ║
║        face to provide elevation geometric focusing.             ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: PHASED-ARRAY ELECTRONIC BEAMFORMING & B-MODE           ║
║    3a. Phased-array electronic steering: Fire individual pulser  ║
║        channels with nanosecond differential time delays:        ║
║        Wavefronts constructively interfere to steer acoustic beam║
║        across a 90° sector fan without moving the probe!         ║
║    3b. Dynamic receive focusing: Returning echoes from organ     ║
║        boundaries hit the 128 elements at slightly different     ║
║        times. Digital delay lines in FPGA [→ R130] dynamically   ║
║        re-align and sum signals, tracking the focal spot deeper  ║
║        into tissue in real time.                                 ║
║    3c. Time-Gain Compensation (TGC): Exponential amplifier       ║
║        boosts late returning echoes to compensate for tissue     ║
║        acoustic attenuation ($0.5\text{ dB/cm/MHz}$).            ║
║    3d. Digital Scan Converter (B-Mode / Brightness Mode): Maps   ║
║        echo amplitudes into 256 grayscale levels; interpolates   ║
║        acoustic polar coordinates $(r, \theta)$ into Cartesian   ║
║        video display at 30 frames per second!                    ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Axial resolution: <0.45 mm at 5.0 MHz.                      ║
║    • Lateral resolution: <1.2 mm at 60 mm focal depth.           ║
║    • Acoustic safety: Mechanical Index (MI) <1.0, Thermal Index  ║
║      (TI) <0.5 (completely safe for obstetric pregnancy scans). ║
╚══════════════════════════════════════════════════════════════════╝
```
