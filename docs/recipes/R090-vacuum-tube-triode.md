# R090 — Vacuum Tube Triode (Pre-Transistor Electronics)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R090 · VACUUM TUBE TRIODE                               ║
║  End product: 1 working triode vacuum tube, amplification ≥ 10× ║
╠══════════════════════════════════════════════════════════════════╣
║  WHAT YOU GET                                                    ║
║    A thermionic triode (like Lee de Forest's Audion, 1906).     ║
║    Three elements inside evacuated glass envelope:               ║
║    — CATHODE: heated wire, emits electrons by thermionic emission║
║    — GRID: wire mesh, controls electron flow by voltage          ║
║    — ANODE (PLATE): collects electrons, generates output signal  ║
║                                                                  ║
║    This device enables: radio reception, signal amplification,  ║
║    logic circuits (NAND/NOR gates), analog computing,            ║
║    oscillators (radio transmission), early digital computers.    ║
║    It is the GATEWAY to all electronic technology.              ║
╠══════════════════════════════════════════════════════════════════╣
║  PREREQUISITES                                                   ║
║    ✓ Glass blowing capability (R060, R063): airtight envelope   ║
║    ✓ Tungsten wire capability (R091): cathode filament           ║
║    ✓ Vacuum pump (R092): achieve <10⁻⁴ mbar                     ║
║    ✓ Copper wire (R084): grid and lead wires                    ║
║    ✓ Nickel or carbon anode (R093)                              ║
║    ✓ Electrical supply: 6V DC (cathode), 100V DC (anode) [R080] ║
╠══════════════════════════════════════════════════════════════════╣
║  INGREDIENTS                                                     ║
║                                                                  ║
║  A) 1 glass envelope, sealed with leads   [→ R063 + R060]      ║
║     Dimensions: 60 mm diameter × 90 mm tall borosilicate-type  ║
║     glass (need a glass that handles 400°C without cracking —  ║
║     add boron source: borax/tincal mineral, Na₂B₄O₇, found in  ║
║     Siwa Oasis area [29°N 25°E] or traded from Anatolia).       ║
║     The envelope must be absolutely leak-free — any air leaks  ║
║     → cathode oxidises and dies instantly.                       ║
║                                                                  ║
║  B) 1 tungsten wire cathode filament       [→ R091]             ║
║     Diameter: 0.1 mm. Length: 30 mm (forms a U or W shape).    ║
║     Resistance at operating temp: ~5 Ω.                         ║
║     Operating current: 1.2 A at 6V. Temperature: ~2,000°C.     ║
║     (Tungsten melting point: 3,422°C — only metal that can      ║
║     survive this. No other material works.)                      ║
║                                                                  ║
║  C) 1 grid: fine copper wire helix         [→ R084]             ║
║     Wire: 0.2 mm diameter copper. Wound 10 turns, 5 mm dia      ║
║     helix, surrounding cathode at 3 mm separation.              ║
║                                                                  ║
║  D) 1 anode (plate): nickel or graphite sheet  [→ R093]         ║
║     Dimensions: 20 × 10 mm × 0.3 mm thick. Cylindrical,        ║
║     surrounding grid + cathode assembly. Collector of electrons. ║
║                                                                  ║
║  E) 4 lead-in wires (kovar or iron-glass seals) [→ R094]        ║
║     Iron wires sealed into glass base — 2 for cathode (heat),  ║
║     1 for grid, 1 for anode.                                    ║
╠══════════════════════════════════════════════════════════════════╣
║  TOOLS                                                           ║
║    • Glass lathe (or skilled free-hand glassblower) [→ R063]   ║
║    • Vacuum pump                                   [→ R092]    ║
║    • Gas torch (hydrogen + air, or oil + air)      [→ R095]    ║
║    • Electrical meter (galvanometer)               [→ R087]    ║
╠══════════════════════════════════════════════════════════════════╣
║  PROCESS                                                         ║
║                                                                  ║
║  STEP 1 — MAKE INTERNAL ASSEMBLY (outside glass)                 ║
║    1a. Cathode: take 30 mm tungsten wire (0.1 mm dia). Bend    ║
║        into W-shape (increases surface area, allows even heating).║
║        Spot-weld (or clamp) ends to two 1.5 mm iron lead-in    ║
║        wires.                                                    ║
║    1b. Grid: wind 0.2 mm copper wire, 10 turns, 5 mm dia       ║
║        helix around thin ceramic (fired clay) support rod.      ║
║        Attach 1 × 1.5 mm copper lead-in wire.                   ║
║    1c. Anode: cut nickel or graphite plate 20×10 mm. Bend to   ║
║        cylinder, 10 mm dia, surrounding both cathode + grid.    ║
║        Attach 1 lead-in wire.                                   ║
║    1d. Mount all three on a glass or ceramic spider/base mount  ║
║        with the spacing: cathode at centre, grid 3 mm out,      ║
║        anode 5 mm out from centre. Rigid, no contact between.   ║
║                                                                  ║
║  STEP 2 — GLASS ENVELOPE                                         ║
║    2a. Using glassblowing, form a cylindrical glass tube:       ║
║        60 mm dia × 90 mm tall. Closed at top.                   ║
║    2b. At the bottom: seal lead-in wires through glass (glass-  ║
║        to-metal seal). Heat small section of glass tube to soft,║
║        press iron wire through, re-seal around it. The challenge:║
║        iron and glass expand at different rates. Use fine iron  ║
║        wire (0.5–1.0 mm) pre-oxidised (surface FeO layer helps  ║
║        bonding). This is the hardest step — practice many times.║
║    2c. Final: glass tube sealed at top, 4 leads exiting bottom,║
║        and a small evacuation stem tube (5 mm dia, 30 mm long)  ║
║        also at bottom.                                           ║
║                                                                  ║
║  STEP 3 — INSERT ASSEMBLY AND SEAL (PARTIAL)                     ║
║    3a. Insert the internal assembly (from Step 1) through the   ║
║        open bottom of the envelope, wire leads through the      ║
║        glass seals you made in Step 2.                          ║
║    3b. Seal bottom of envelope around the leads using hot glass  ║
║        from torch — leave evacuation stem tube open.            ║
║                                                                  ║
║  STEP 4 — EVACUATE                                               ║
║    4a. Connect vacuum pump (R092) to evacuation stem tube.      ║
║    4b. Begin pumping. Target: <10⁻³ mbar (high vacuum needed).  ║
║        A piston pump (R092) achieves 10⁻²–10⁻³ mbar.           ║
║    4c. While pumping: heat the envelope to 300°C with torch for ║
║        20 min (drives off outgassed water and CO₂ from surfaces —║
║        this is "baking" the tube).                               ║
║    4d. At maximum vacuum: heat tungsten cathode (apply 6V)      ║
║        briefly — this "getters" remaining gas (tungsten surface  ║
║        absorbs residual oxygen/nitrogen molecules).              ║
║    4e. Seal off evacuation stem: heat stem with torch until it  ║
║        melts and closes. Tube is now hermetically sealed.        ║
║                                                                  ║
║  STEP 5 — TEST                                                   ║
║    5a. Connect cathode heater: 6V DC across heater leads.       ║
║        Filament should glow orange at 2,000°C.                  ║
║    5b. Connect anode to +100V DC (from dynamo, R080).           ║
║    5c. Grid at 0V initially. Measure anode current with         ║
║        galvanometer (R087): should read 5–20 mA.                 ║
║    5d. GRID CONTROL TEST: apply -1V to grid. Anode current      ║
║        should drop significantly. Apply +1V: current rises.     ║
║        If current responds to grid voltage: IT WORKS.           ║
║    5e. AMPLIFICATION TEST: apply 0.1V signal to grid.           ║
║        Measure output voltage across 5 kΩ anode resistor.       ║
║        Output should be 1–10V = gain of 10–100×.               ║
╠══════════════════════════════════════════════════════════════════╣
║  SKILLS                                                          ║
║    • Glass-to-metal seals: the hardest step. 50+ practice pieces║
║      before reliable results.                                    ║
║    • Vacuum pump operation: keeping connections leak-free.       ║
║    • Tungsten wire handling: very brittle at <500°C. Handle ONLY ║
║      when hot (glowing dull red = ductile).                      ║
║    TRAINING TIME: 1 year for consistent, working triodes.        ║
║    SUCCESS RATE first year: ~20% per tube.                       ║
╠══════════════════════════════════════════════════════════════════╣
║  PROPHET'S NOTE ON SEQUENCING                                    ║
║    The vacuum tube requires MANY advanced prerequisites.         ║
║    Realistic timeline with the Prophet's knowledge:              ║
║    Year 0:    Fire, pottery, copper (this month)                 ║
║    Year 1:    Bronze, iron, steel                                ║
║    Year 5:    Glass, optics, soap, basic chemistry               ║
║    Year 20:   Steam engine, precision machining, dynamo          ║
║    Year 30:   Vacuum pump, tungsten wire, borosilicate glass     ║
║    Year 40:   First working vacuum tubes                         ║
║    Year 60:   First vacuum tube radio (AM)                       ║
║    Year 80:   Vacuum tube computer (ENIAC-equivalent)            ║
║    Year 150:  Transistors (requires silicon purification R095)   ║
║    Year 200:  Integrated circuits                                ║
║    Year 300:  LLMs (with sufficient manufacturing scale)         ║
╚══════════════════════════════════════════════════════════════════╝
```
