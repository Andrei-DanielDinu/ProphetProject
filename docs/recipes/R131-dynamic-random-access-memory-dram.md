# R131 — Dynamic Random-Access Memory (DRAM 1T1C Cell)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R131 · DYNAMIC RANDOM-ACCESS MEMORY (DRAM 1T1C)          ║
║  End product: 1 × 1 Gigabit High-Speed Synchronous DRAM Die      ║
║  Access time: <15 ns, Architecture: 1-Transistor 1-Capacitor     ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The volatile working system memory prerequisite for:          ║
║    • Storing operating system kernel and runtime code [→ R130]   ║
║    • LLM systolic matrix multiplier buffer memory [→ R140]       ║
║    • Radar signal processing arrays and video framebuffers       ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. P-type Monocrystalline Silicon Wafers: 25 pcs [→ R100]     ║
║    2. Zirconium Oxide / Hafnium Oxide High-k Dielectric: 50 g    ║
║       [→ ALD precursor Zr(NMe₂)₄, R101]                          ║
║    3. Titanium Nitride (TiN electrode metal): 100 g [→ R035]     ║
║    4. Copper Interconnect Target (99.999% Cu): 500 g [→ R030]    ║
║    5. Deep UV Stepper Photolithography Tool (193 nm): 1 [→ R101] ║
║    6. High-Aspect-Ratio Reactive Ion Etcher (RIE): 1 [→ R101]    ║
║    7. Atomic Layer Deposition (ALD) Reactor: 1 [→ R101]          ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: PASS TRANSISTOR FABRICATION                            ║
║    1a. Prepare 200 mm p-type silicon wafer with 10¹⁵ B/cm³.      ║
║    1b. Grow 4 nm thermal silicon dioxide gate oxide at 950°C.    ║
║    1c. Deposit n⁺ polysilicon wordline gate; etch into parallel  ║
║        wordlines spaced at 100 nm pitch.                         ║
║    1d. Self-aligned arsenic ion implantation at 30 keV:          ║
║        Forms n⁺ drain (connected to bitline) and source          ║
║        (connected to storage capacitor node).                    ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: HIGH-ASPECT-RATIO TRENCH / CYLINDER CAPACITOR          ║
║    2a. Deposit 2.0 μm thick borophosphosilicate glass (BPSG)     ║
║        dielectric layer over the access transistors.             ║
║    2b. Photolithographically pattern capacitor contact holes     ║
║        directly over every transistor source node.               ║
║    2c. High-aspect-ratio reactive ion etch (RIE): Etch 30:1      ║
║        aspect ratio cylindrical holes (70 nm dia × 2.0 μm deep)  ║
║        into the BPSG layer down to the silicon source plug.      ║
║    2d. ALD Bottom Electrode: Deposit 10 nm conformal TiN layer   ║
║        lining the internal walls of the cylinders.               ║
║    2e. High-k Dielectric Deposition: Deposit 6 nm ZrO₂-Al₂O₃-    ║
║        ZrO₂ (ZAZ) nanolaminate film by Atomic Layer Deposition   ║
║        at 280°C. Dielectric constant k ≈ 35.                     ║
║    2f. Top Electrode & Plate: Deposit TiN and tungsten top plate ║
║        connected to Vdd/2 (reference plate voltage).             ║
║    2g. Result: Each microscopic cell provides 25 femtofarads     ║
║        (fF) capacitance in a microscopic 0.05 μm² footprint!     ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: BITLINES, SENSE AMPLIFIERS & REFRESH TIMING            ║
║    3a. Deposit copper dual-damascene bitlines running orthogonal ║
║        to polysilicon wordlines.                                 ║
║    3b. Fabricate cross-coupled CMOS inverter differential Sense  ║
║        Amplifiers between bitline pairs (BL and /BL):            ║
║        When a wordline pulses high, the tiny 25 fF cell charge   ║
║        dumps into the 200 fF bitline capacitance, shifting line  ║
║        voltage by a minute ±100 mV.                              ║
║    3c. Sense amplifier fires: Latches the ±100 mV delta into full║
║        rail 0 V or 1.2 V CMOS logic levels and automatically     ║
║        restores full charge back into the storage capacitor!     ║
║    3d. Implement automated on-chip counter refresh circuit:      ║
║        Every memory cell row is cycled every 64 ms to prevent    ║
║        charge leakage through sub-threshold junctions.           ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Retention time: >99.999% cells retain data for >128 ms at   ║
║      85°C without refresh.                                       ║
║    • Row cycle time (tRC): <45 ns; Access time (tAA): <14 ns.    ║
║    • Zero single-bit stuck faults across 1,073,741,824 bits.     ║
╚══════════════════════════════════════════════════════════════════╝
```
