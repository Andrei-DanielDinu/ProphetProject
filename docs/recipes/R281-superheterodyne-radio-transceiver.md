# R281 — Superheterodyne Radio Transceiver

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R281 · SUPERHETERODYNE AM/FM RADIO TRANSCEIVER           ║
║  End product: Operational Wireless Voice Transmitter & Receiver  ║
║  Frequency: 540–1,600 kHz (Medium Wave AM) / 88–108 MHz (VHF FM) ║
╠══════════════════════════════════════════════════════════════════╣
║  EDWIN ARMSTRONG'S SUPERHETERODYNE BREAKTHROUGH (1918)           ║
║    Tuned Radio Frequency (TRF) receivers required adjusting 4   ║
║    separate tuned stages simultaneously; selectivity changed at  ║
║    every frequency across the dial.                              ║
║    Armstrong's Superheterodyne shifts ANY incoming radio carrier ║
║    frequency down to a SINGLE, FIXED Intermediate Frequency (IF, ║
║    standardized at 455 kHz) where razor-sharp multistage tuned   ║
║    filters can amplify the signal with extreme gain and zero     ║
║    instability!                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  MATHEMATICAL HETERODYNE MIXING                                  ║
║    Multiplying two sinusoidal frequencies generates sum and      ║
║    difference products via trigonometric identity:               ║
║    sin(ω_RF · t) × sin(ω_LO · t) =                               ║
║    ½ [ cos((ω_RF - ω_LO)·t) - cos((ω_RF + ω_LO)·t) ]             ║
║    By tuning the Local Oscillator (LO) to track always:          ║
║    f_LO = f_RF + 455 kHz                                         ║
║    The difference frequency is ALWAYS exactly 455 kHz (the IF)!  ║
╠══════════════════════════════════════════════════════════════════╣
║  RECEIVER CIRCUIT TOPOLOGY                                       ║
║                                                                  ║
║  1. ANTENNA & RF TUNED PRESELECTOR                               ║
║     • Ferrite rod inductor coil + ganged variable air tuning     ║
║       capacitor (C_var 10–365 pF): selects target station.       ║
║                                                                  ║
║  2. MIXER / LOCAL OSCILLATOR STAGE [→ R090 triode / R101]        ║
║     • Pentagrid converter tube or dual-gate MOSFET: mixes        ║
║       incoming weak RF signal with local oscillator sine wave.   ║
║                                                                  ║
║  3. 455 kHz IF AMPLIFIER STAGE                                   ║
║     • Two cascaded IF transformer cans (shielded LC tank tuned   ║
║       precisely to 455.0 kHz with adjustable ferrite slugs).     ║
║     • Provides 80 dB of clean, un-distorted voltage gain!        ║
║                                                                  ║
║  4. DEMODULATOR (DETECTOR) & AUTOMATIC GAIN CONTROL (AGC)        ║
║     • Point-contact germanium diode (R101): strips high-frequency║
║       455 kHz carrier, leaving the envelope audio speech wave.   ║
║     • Negative DC average voltage fed back to IF amplifier grid: ║
║       automatically turns down gain on strong stations and       ║
║       boosts weak stations to maintain uniform speaker volume!   ║
║                                                                  ║
║  5. AUDIO POWER AMPLIFIER & LOUDSPEAKER [→ R280]                 ║
║     • Class-A/B audio amplifier delivers 2 Watts audio to 8-Ohm  ║
║       permanent magnet moving-coil loudspeaker: crystal-clear    ║
║       voice and music broadcast received from 500 km away!       ║
╚══════════════════════════════════════════════════════════════════╝
```
