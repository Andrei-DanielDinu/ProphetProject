# R070 — Steam Engine (Reciprocating Piston Engine)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R070 · STEAM ENGINE — SINGLE-CYLINDER BEAM ENGINE       ║
║  End product: 1 operational steam engine, ~5 kW shaft output    ║
╠══════════════════════════════════════════════════════════════════╣
║  WHAT YOU GET                                                    ║
║    A Watt-type single-acting beam engine. Output: 5 kW at       ║
║    shaft = 50 kg lifted 10 m/s = powers 1 water pump, or        ║
║    1 large bellows set, or 1 small mill.                         ║
║                                                                  ║
║    WHY THIS IS THE INFLECTION POINT:                             ║
║    Before steam: human muscle and waterwheel are the only        ║
║    reliable mechanical energy sources.                           ║
║    After steam: energy is available anywhere, any time,          ║
║    scalable by adding more boilers, in any quantity needed.      ║
║    Steam enables: mine drainage, iron production scale-up,       ║
║    textile mills, railroad (eventual), electrical generators.    ║
╠══════════════════════════════════════════════════════════════════╣
║  PREREQUISITES — MUST BE COMPLETE BEFORE ATTEMPTING             ║
║    ✓ Iron production established (R040) — 500+ kg iron stockpile ║
║    ✓ Steel tool production (R041) — precision boring possible   ║
║    ✓ Copper sheet rolling (from R030) — boiler plates           ║
║    ✓ Lead/hemp packing material for piston seals                 ║
║    ✓ Cast iron (R071) — requires iron poured into sand molds    ║
║      (different from wrought iron — just pour liquid iron from  ║
║      a hotter furnace at 1,250°C+ directly into sand mold)     ║
╠══════════════════════════════════════════════════════════════════╣
║  COMPONENTS AND THEIR RECIPES                                    ║
║                                                                  ║
║  COMPONENT 1: BOILER                           [→ R072]         ║
║    Material: wrought iron sheet, 5 mm thick. Riveted.           ║
║    Size: 1.2 m diameter × 2.0 m long (cylindrical).            ║
║    Working pressure: 2 bar (200 kPa, ~2 atm gauge).            ║
║    Safety valve: lead disk held by weight, lifts at 2.2 bar.   ║
║    Steam output: 500 kg/hour at 2 bar / 134°C.                  ║
║                                                                  ║
║  COMPONENT 2: CYLINDER AND PISTON              [→ R073]         ║
║    Cylinder: cast iron, bored to ±0.5 mm tolerance.            ║
║    Bore: 25 cm diameter. Stroke: 60 cm.                         ║
║    Swept volume: π × 0.125² × 0.6 = 0.029 m³ per stroke.       ║
║    At 2 bar, single-acting: average pressure 1.0 bar (since      ║
║    exhaust at 0 bar gauge). Force: 1.0 × 10⁵ Pa × 0.049 m² = 4,900 N ║
║    Work per stroke: 4,900 N × 0.6 m = 2,940 J.                 ║
║    At 30 strokes/min: Power = 2,940 × 30/60 = 1,470 W × 3     ║
║    (efficiency factor: 30%) → ~5 kW gross.                      ║
║    Piston: cast iron, rings: lead-hemp rope (pre-metal era)      ║
║    or later: cast iron piston rings.                            ║
║                                                                  ║
║  COMPONENT 3: BEAM (WALKING BEAM)              [→ R074]         ║
║    Oak timber beam, 4 m long, 20 × 25 cm cross-section.         ║
║    Pivots on iron bearing at centre point.                       ║
║    One end: connects to piston rod via iron chain.               ║
║    Other end: connects to output crank or pump rod.             ║
║                                                                  ║
║  COMPONENT 4: VALVE GEAR                       [→ R075]         ║
║    4-way steam distribution valve (slide valve):                 ║
║    Cast iron block with machined valve face (flat, hand-scraped).║
║    Controls: steam in → cylinder → exhaust timing.              ║
║                                                                  ║
║  COMPONENT 5: GOVERNOR                         [→ R076]         ║
║    Watt centrifugal governor: 2 × 500g cast iron balls on       ║
║    hinged arms attached to output shaft. When RPM rises:         ║
║    balls fly outward, raise collar, partially close steam valve.║
║    Keeps engine at constant speed despite load variation.        ║
╠══════════════════════════════════════════════════════════════════╣
║  DIMENSIONS AND LAYOUT DIAGRAM                                   ║
║                                                                  ║
║  Side view of complete Watt beam engine:                         ║
║                                                                  ║
║                    WALKING BEAM (4 m oak)                        ║
║            PISTON ◄──────●──────────────────────► OUTPUT        ║
║            ROD    │      │ PIVOT on                │  SHAFT/     ║
║                   │      │ iron post               │  PUMP ROD  ║
║                 CYLINDER │                         │            ║
║                 (25 cm   │                        CRANK or      ║
║                  bore)   │                        FLYWHEEL      ║
║                   │      │                         │            ║
║               BOILER (below cylinder)              │            ║
║               1.2m × 2.0m                         │            ║
║               rivet-assembled                      ▼            ║
║               wrought iron                     SHAFT OUTPUT     ║
║                                                (drives: pump,   ║
║                                                 bellows, mill)  ║
╠══════════════════════════════════════════════════════════════════╣
║  CRITICAL SPECIFICATIONS                                         ║
║                                                                  ║
║  BOILER SAFETY (non-optional):                                   ║
║    • Wall thickness: 5 mm wrought iron minimum at 2 bar.        ║
║      Safety factor 4: burst pressure ~8 bar.                    ║
║    • Safety valve: MUST be installed before EVERY firing.        ║
║      Valve: 5 cm dia lead disk + 2 kg weight. Lifts at 2.5 bar.║
║    • Water level gauge: copper tube, 20 cm, bottom sealed to    ║
║      boiler below waterline, top to steam space above. Glass    ║
║      tube preferred once available. ALWAYS check before firing. ║
║    • Never heat boiler dry. Minimum 60% water fill.             ║
║    ⚠ BOILER EXPLOSION at 5 bar: lethal within 50 m radius.      ║
║      Do not exceed rated pressure. Train fireman continuously.  ║
║                                                                  ║
║  CYLINDER BORING TOLERANCE:                                      ║
║    • ±0.5 mm bore tolerance achievable with iron boring bar.    ║
║    • Method: horizontal boring bar (iron rod, 2 m long,         ║
║      supported at both ends on timber bearings). Single-point   ║
║      hardened iron cutting tool clamped to bar. Rotate bar      ║
║      slowly (1 rpm) while advancing axially through cylinder.   ║
║    • Surface roughness: smooth by dragging iron-hemp hone.      ║
╠══════════════════════════════════════════════════════════════════╣
║  SKILLS REQUIRED                                                 ║
║    • Boilermaking: riveting hot iron (R072)                      ║
║    • Cylinder boring: horizontal boring mill operation (R073)    ║
║    • Valve face hand-scraping (requires hardened steel scraper)  ║
║    • Steam pressure management (the fireman's skill)             ║
║    PREREQUISITE SKILLS: Advanced blacksmithing (R040-R045),     ║
║    Cast iron pouring (R071), Precision measurement with gauges.  ║
║    TOTAL BUILD TIME: 6 months (once all materials available).   ║
║    TRAINING TIME for operator: 1 month.                          ║
╚══════════════════════════════════════════════════════════════════╝
```

## Ingredient Decomposition Tree for R070

```
Steam Engine (R070)
├── Boiler (R072) →
│   ├── Wrought iron sheet, 5mm (R040 → hammered flat)
│   ├── Rivets (R040 → hammered into shape)
│   └── Flux (R027) + forge (R021) for rivet heating
├── Cylinder + Piston (R073) →
│   ├── Cast iron (R071) →
│   │   ├── Pig iron from hot bloomery at 1,250°C (R040 extended)
│   │   └── Sand molds (R000-F + clay binder)
│   └── Boring bar (steel, R041)
├── Walking Beam (R074) →
│   ├── Oak timber, 4m × 20×25cm (R000-I) ■ TERM.
│   └── Iron pivot pin and bearings (R040)
├── Slide Valve (R075) →
│   ├── Cast iron block (R071)
│   └── Hand scraping tools (R041 steel)
└── Governor (R076) →
    ├── Cast iron balls × 2, 500g each (R071)
    ├── Iron rod arms (R040)
    └── Iron linkage (R040)
```
