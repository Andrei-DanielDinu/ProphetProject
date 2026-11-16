# Modern Technology: Orbital Space Stations (ISS) and Life Support

> "An orbital space station is a permanent outpost suspended at the boundary between Earth and the cosmos. To keep fragile biological humans alive in hard vacuum, extreme ionizing radiation, and microgravity requires closing the chemical cycles of air, water, and heat inside a self-contained ecological machine."

---

## 1. Orbital Architecture and Hull Engineering

The International Space Station (ISS) orbits at an average altitude of $400\text{ km}$ with an orbital inclination of $51.6^\circ$, traveling at $7.66\text{ km/s}$ ($27,600\text{ km/h}$) and completing one orbit every 92 minutes.

```
                    [ External Ammonia Heat Radiators ]
                                    |
   +-------------+       +----------+----------+       +-------------+
   | Solar Array |       |    Truss Backbone   |       | Solar Array |
   | Wing (GaAs) | ===== |   (P1/S1 Radiators) | ===== | Wing (GaAs) |
   +-------------+       +----------+----------+       +-------------+
                                    |
             +----------------------+----------------------+
             |                      |                      |
             v                      v                      v
      [ Columbus Lab ]       [ Destiny Lab ]        [ Kibo Module ]
             |                      |                      |
             +-------------[ Node 2 (Harmony) ]------------+
                                    |
                          [ Crew Airlock (Quest) ]
                                    |
                         [ Docking Port / Dragon ]
```

### Pressure Hull Fabrication
Modules are built from **Aluminum-Lithium alloys (Al-Li 2195)**, offering $30\%$ higher stiffness-to-weight ratio than standard structural aluminum.
- The hull is pocket-milled into an internal **isogrid pattern** (triangular stiffener ribs machined directly out of thick plate).
- Cylindrical sections are joined using **Friction Stir Welding (FSW)**, a solid-state joining process that eliminates melting, porosity, and heat-affected cracking, ensuring hermetic containment at $101.3\text{ kPa}$ internal air pressure against zero external atmospheric pressure.

### The Whipple Shield (Micrometeoroid & Orbital Debris Protection)
Objects in Low Earth Orbit collide at relative velocities of $7\text{ to } 15\text{ km/s}$—where a $1\text{ cm}$ aluminum bolt carries the kinetic energy of an anti-tank grenade.

A solid metal plate thick enough to stop such impacts would be too heavy to launch. Instead, the ISS uses **Whipple Standoff Shields**:

```
Hypervelocity Debris (v ~ 10 km/s) ===> | Bumper | =======> (Dispersed Molten Cloud) =======> | Module Hull |
                                      (Thin Al)            (Standoff Space: 10 cm)        (Kevlar/Nextel)
```

1. **Outer Bumper Sheet**: Thin ($1.5\text{--}2.5\text{ mm}$) high-strength aluminum plate mounted $10\text{ cm}$ outside the hull.
2. **Shock Vaporization**: On impact, the shockwave pressure exceeds the material strength of the particle, shattering and vaporizing it into an expanding cloud of microscopic molten droplets and gas.
3. **Internal Catch Layers**: Layers of flexible Nextel ceramic fabric and Kevlar backing absorb the momentum of the dispersed cloud without puncturing the inner pressure vessel wall.

---

## 2. Environmental Control and Life Support Systems (ECLSS)

Human metabolic consumption per astronaut per day:
- **Oxygen**: $0.84\text{ kg}$
- **Food (dry solids)**: $0.62\text{ kg}$
- **Water (drinking & food preparation)**: $2.8\text{ kg}$
- **Metabolic Carbon Dioxide produced**: $1.0\text{ kg}$
- **Metabolic Waste Water (urine, sweat, respiration)**: $3.5\text{ kg}$

Without closed-loop recycling, a six-person crew would require over 18 metric tons of resupply cargo annually just for air and water.

### Water Recovery System (WRS)
The ISS recycles over $93\text{--}98\%$ of all crew wastewater:
1. **Urine Processor Assembly (UPA)**: Raw urine is treated with chromic/sulfuric acid oxidizers to halt bacterial ammonia generation. It enters a low-pressure **Vapor Compression Distillation (VCD)** rotating centrifuge drum. Centrifugal force pushes the liquid film against heated drum walls; low pressure boils water at $35^\circ\text{C}$, separating pure water vapor from brine.
2. **Water Processor Assembly (WPA)**: Distillate and cabin humidity condensate are filtered through particulate beds, passed through multi-filtration beds of activated carbon and ion-exchange resins, and heated to $130^\circ\text{C}$ in a catalytic reactor with gaseous oxygen to oxidize volatile organics. Trace iodine is added as a biocidal residual before drinking.

### Oxygen Generation Assembly (OGA)
- Purified recycled water undergoes PEM (Proton Exchange Membrane) **water electrolysis**:
$$2\text{H}_2\text{O} \to 2\text{H}_2 \uparrow + \text{O}_2 \uparrow$$
- Pure oxygen is vented directly into the station cabin to maintain $21\%$ atmospheric concentration.
- Byproduct hydrogen gas is routed to the Sabatier reactor.

### The Sabatier Carbon Dioxide Reduction Reactor
Carbon dioxide exhaled by the crew is scrubbed using regenerative zeolite molecular sieves (CDRA). Instead of venting $CO_2$ into space (which would represent permanent loss of oxygen mass), $CO_2$ is reacted with hydrogen from the OGA:

$$\text{CO}_2 + 4\text{H}_2 \xrightarrow[\text{400}^\circ\text{C}]{\text{Ruthenium Catalyst}} \text{CH}_4 \uparrow + 2\text{H}_2\text{O}$$

The recovered water is fed directly back into the electrolysis unit, reclaiming over $50\%$ of the oxygen that would otherwise be discarded as carbon dioxide! The byproduct methane ($\text{CH}_4$) is vented overboard.

---

## 3. Active Thermal Control Systems (ATCS)

Vacuum is an exceptional thermal insulator: in space, conduction and convection do not exist. An orbital station faces severe thermal imbalances:
- The sunlit side reaches $+121^\circ\text{C}$ while the shadow side plunges to $-157^\circ\text{C}$.
- Internal avionics, computers, experiment racks, and crew metabolism generate $70\text{ to } 120\text{ kW}$ of continuous waste heat that must be rejected to prevent the station from becoming an oven.

```
[ Internal Avionics & Crew Cabins ]  --> Heat collected by Internal Water Loop (Safe)
                 |
                 v (Titanium Plate-Fin Heat Exchangers)
[ External Active Thermal Loop ]     --> Ammonia liquid pumped at 3.5 bar (Hazardous)
                 |
                 v
[ Deployable Radiator Panels ]       --> Honeycomb Al panels coated with silverized Teflon
                 |
                 v
[ Thermal Infrared Radiation into Deep Space: Q = epsilon * sigma * A * T^4 ]
```

- **Two-Loop Separation**: Water is used inside the cabin because it is non-toxic. Liquid anhydrous **ammonia ($\text{NH}_3$)** is used in external radiator loops because water would freeze solid in shadow passes (ammonia freezes at $-77^\circ\text{C}$).
- **Heat Radiators**: Giant deployable panels ($24\text{ m} \times 3.6\text{ m}$) coated with white zinc-oxide or silverized Teflon film. They face edge-on to the Sun and broadside to dark deep space ($3\text{ K}$ cold sink), radiating waste thermal heat in the far infrared spectrum.

---

## 4. Extravehicular Activity (EVA) Spacesuits

An EVA spacesuit (e.g., NASA EMU) is a miniature, anthropomorphic one-person spacecraft:
1. **Atmospheric Regulation**: Operates on $100\%$ pure oxygen at $29.6\text{ kPa}$ ($4.3\text{ psi}$). The reduced pressure prevents the suit from ballooning into a rigid, unbendable structure, while pure oxygen provides adequate alveolar partial pressure ($P_{\text{AO}_2}$) to prevent hypoxia.
2. **Liquid Cooling and Ventilation Garment (LCVG)**: A knitted spandex undergarment woven with 90 meters of flexible plastic capillary tubing. Chilled water pumped through the tubes directly absorbs conductive heat from the astronaut's skin, preventing heat exhaustion.
3. **Multi-Layer Insulation (MLI)**: 14 distinct layers:
   - Ortho-fabric outer layer (blend of Gore-Tex, Nomex, and Kevlar) resisting abrasion and micrometeoroids.
   - Seven layers of aluminized Mylar reflecting solar infrared radiation.
   - Dacron scrim separators preventing conductive thermal bridging.
   - Urethane-coated nylon pressure retention bladder.
