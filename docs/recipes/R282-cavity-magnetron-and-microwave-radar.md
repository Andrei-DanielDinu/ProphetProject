# R282 — Cavity Magnetron and Microwave Radar

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R282 · CAVITY MAGNETRON & S-BAND MICROWAVE RADAR         ║
║  End product: Operational 3 GHz (10 cm) Microwave Pulse Radar    ║
║  Peak RF power: 500 Kilowatts, Detection range: 60 km (Aircraft) ║
╠══════════════════════════════════════════════════════════════════╣
║  WHY CENTIMETRIC RADAR DEFEATS NIGHT AND CLOUDS                  ║
║    Early long-wave radar (1.5 m wavelength) required football-   ║
║    field wire antennas and could not detect low targets.         ║
║    The Cavity Magnetron (Randall & Boot, 1940) generates         ║
║    gigawatt-class pulses at 10 cm wavelength from a fist-sized   ║
║    copper block: allows a narrow, razor-sharp microwave pencil   ║
║    beam to be focused by a compact 1-meter parabolic dish!       ║
╠══════════════════════════════════════════════════════════════════╣
║  PHYSICS OF THE RESONANT CAVITY MAGNETRON                        ║
║                                                                  ║
║  1. ANODE BLOCK FABRICATION [→ R030 / R072]                      ║
║     • Massive cylinder of oxygen-free high-conductivity (OFHC)   ║
║       pure copper (8 cm diameter × 6 cm tall).                   ║
║     • Precision-bored central cylindrical cathode hole (16 mm).  ║
║     • 8 Cylindrical resonant cavities (10 mm dia) milled around  ║
║       the perimeter, connected to center hole by narrow slots.   ║
║     • Each cavity acts as a microscopic LC resonant tank:        ║
║       The cylindrical cavity wall is an inductor (L); the        ║
║       narrow slot faces are a capacitor (C). Resonant frequency: ║
║       f = 1 / (2π √(L C)) = 3,000,000,000 Hz (3 Gigahertz!).     ║
║                                                                  ║
║  2. CATHODE & TRANSVERSE MAGNETIC FIELD                          ║
║     • Central oxide-coated barium cathode heated to 850°C.       ║
║     • High-voltage DC pulse: 20,000 Volts applied between        ║
║       cathode (-) and copper anode block (+).                    ║
║     • Permanent Alnico magnet (0.15 Tesla) exerts magnetic field ║
║       parallel to the cathode axis (perpendicular to electric E).║
║     • Electrons emitted by cathode are bent by Lorentz force     ║
║       (F = q(E + v × B)) into a rotating hub of 4 electronic     ║
║       spokes sweeping past the cavity slot mouths.                ║
║     • Electron spokes induce surging RF alternating currents in  ║
║       the cavity walls, radiating 500 kW of microwave energy     ║
║       out through a glass coupling loop into a hollow waveguide! ║
╠══════════════════════════════════════════════════════════════════╣
║  RADAR SYSTEM ARCHITECTURE                                       ║
║    • Pulse Modulator: Discharges high-voltage pulse capacitor    ║
║      through a hydrogen thyratron tube every 1 millisecond.      ║
║    • TR Duplexer Cell: Spark-gap tube switches common antenna    ║
║      between transmitter (500 kW blast) and receiver (<1 μW echo)║
║      in 1 microsecond without blowing out sensitive diode mixer! ║
║    • Parabolic Dish Antenna: Rotates 360° at 15 RPM.             ║
║    • Plan Position Indicator (PPI): Cathode ray tube (CRT) with  ║
║      rotating electron sweep trace synchronized to dish heading: ║
║      Echoes appear as glowing green map points showing exact     ║
║      range and azimuth of approaching ships and planes!          ║
╚══════════════════════════════════════════════════════════════════╝
```
