# Modern Technology: Nuclear Fission Power Reactors

> "One kilogram of Uranium-235 yields approximately $8 \times 10^{13}$ Joules of thermal energy—the equivalent of burning 2,700,000 kilograms of high-grade coal. Nuclear fission is the transition from rearranging valence electron shells to unlocking the binding energy of the atomic nucleus."

---

## 1. Fundamental Nuclear Physics

### The Fission Reaction
When a low-energy thermal neutron ($E \approx 0.025\text{ eV}$, velocity $\approx 2200\text{ m/s}$) is absorbed by a fissile Uranium-235 nucleus, it forms a compound nucleus $^{236}\text{U}^*$ in an excited state. Within $10^{-14}$ seconds, the electrostatic repulsion between its 92 protons overcomes the short-range strong nuclear force, splitting the nucleus into two asymmetric fission fragments, accompanied by gamma radiation and prompt neutrons:

$$n + {}^{235}_{92}\text{U} \to {}^{236}_{92}\text{U}^* \to {}^{141}_{56}\text{Ba} + {}^{92}_{36}\text{Kr} + 3 n + 200\text{ MeV}$$

### Energy Distribution per Fission Event
- Kinetic energy of fission fragments: $\approx 167\text{ MeV}$ (dissipated as thermal heat in the fuel matrix)
- Kinetic energy of prompt neutrons: $\approx 5\text{ MeV}$
- Prompt gamma rays: $\approx 7\text{ MeV}$
- Radioactive beta and gamma decay of fission products: $\approx 13\text{ MeV}$ (source of decay heat post-shutdown)
- Neutrinos: $\approx 8\text{ MeV}$ (escapes core without interaction)
- **Total recoverable thermal energy**: $\approx 200\text{ MeV} = 3.204 \times 10^{-11}\text{ Joules}$

---

## 2. Neutron Kinetics and Criticality

The state of a reactor is governed by the effective neutron multiplication factor, $k_{\text{eff}}$:
$$k_{\text{eff}} = \frac{\text{Neutrons produced in generation } n}{\text{Neutrons absorbed or lost to leakage in generation } n-1}$$

- $k_{\text{eff}} < 1.0$: Subcritical (reaction dies out)
- $k_{\text{eff}} = 1.0$: Critical (steady-state power generation)
- $k_{\text{eff}} > 1.0$: Supercritical (power increases exponentially)

### The Role of Delayed Neutrons ($\beta$)
Fission releases prompt neutrons within $10^{-14}\text{ s}$. If a reactor relied solely on prompt neutrons, power would double in less than $10^{-4}\text{ s}$, making mechanical control impossible.

Fortunately, a small fraction ($\beta \approx 0.0065$ or $0.65\%$ for $^{235}\text{U}$) of neutrons are **delayed neutrons** emitted seconds to minutes later by the radioactive decay of fission products (precursors like $^{87}\text{Br}$ and $^{137}\text{I}$). As long as the reactor operates in the regime where $k_{\text{eff}} = 1.0$ only with the inclusion of delayed neutrons (delayed critical), the reactor period is extended to dozens of seconds, allowing mechanical control rods to regulate power safely.

---

## 3. The Nuclear Fuel Cycle

```
[ Uranium Ore (0.1-2% U3O8) ]
             |
             v (Acid leaching / Solvent extraction)
[ Yellowcake (Ammonium Diuranate) ]
             |
             v (Fluorination to Gas)
[ Uranium Hexafluoride (UF6) ]
             |
             v (Gas Centrifuge Isotope Separation: 0.7% -> 3.5-5% U-235)
[ Low-Enriched UF6 ]
             |
             v (De-conversion & Ceramic Sintering at 1700°C)
[ UO2 Ceramic Pellets ]
             |
             v (Hermetic Canning in Zircaloy Tubes)
[ Nuclear Fuel Assemblies ]
```

### Gas Centrifuge Enrichment
Uranium isotopes ($^{235}\text{UF}_6$ with molecular weight 349 vs $^{238}\text{UF}_6$ with molecular weight 352) have a mass difference of less than $1\%$.
- Centrifuges spin aluminum or carbon-fiber rotors at 50,000–90,000 RPM (surface speeds $> 500\text{ m/s}$).
- Centrifugal force ($F = m \omega^2 r$) drives heavier $^{238}\text{UF}_6$ toward the outer cylinder wall while lighter $^{235}\text{UF}_6$ concentrates near the center.
- Thousands of centrifuges are connected in countercurrent series-parallel cascades to enrich $^{235}\text{U}$ from natural abundance ($0.72\%$) up to commercial light-water reactor fuel grades ($3.0\text{--}5.0\%$).

---

## 4. Pressurized Water Reactor (PWR) Engineering

The Pressurized Water Reactor is the dominant civilian nuclear reactor type worldwide, utilizing two separate fluid loops to isolate radioactivity from the environment:

```
+================== Containment Structure ==================+
|                                                           |
|    +----------------+                  +----------------+ |
|    | Pressurizer    |                  | Steam          |====[ High-Pressure Steam ]===> [ Steam Turbine ]
|    | (155 bar)      |                  | Generator      | |                                    |
|    +-------+--------+                  +-------+--------+ |                                    v
|            |                                   |          |<===[ Feedwater Return ]====== [ Condenser ]
|            v                                   ^          |                                    |
|    +----------------+                          |          |                                    v
|    | Reactor Vessel |==========================+          |                           [ Cooling Tower ]
|    | (UO2 Fuel Core |                                     |
|    |  + Moderating  |                                     |
|    |  Water at 315C)|<====[ Primary Coolant Pump ]========+
|    +----------------+                                     |
+===========================================================+
```

### Subsystems and Specifications
1. **Reactor Pressure Vessel (RPV)**: Low-alloy manganese-molybdenum-nickel forged steel ($20\text{--}25\text{ cm}$ wall thickness, interior cladded with austenitic stainless steel to prevent corrosion), weighing over 400 metric tons and designed to withstand $17.5\text{ MPa}$ ($175\text{ bar}$) at $350^\circ\text{C}$.
2. **Primary Coolant and Moderator**: Demineralized light water maintained at $15.5\text{ MPa}$ ($155\text{ bar}$) by an electrically heated pressurizer. This pressure prevents water from boiling even at core exit temperatures of $325^\circ\text{C}$. The hydrogen nuclei (protons) in water scatter and slow fast fission neutrons down to thermal energies ($E \approx 0.025\text{ eV}$) where the fission cross-section is 500 times higher.
3. **Steam Generator**: Inverted U-tube heat exchangers with thousands of Inconel-690 alloy tubes. Primary radioactive water flows inside tubes, boiling non-radioactive secondary water outside tubes to produce dry saturated steam at $6.5\text{ MPa}$ ($65\text{ bar}$) and $280^\circ\text{C}$ to drive the turbogenerator.

---

## 5. Inherent Safety and Defense-in-Depth

Modern reactors rely on immutable physical laws rather than operator intervention to guarantee shutdown:

1. **Negative Moderator Temperature Coefficient**: If core temperature rises, water expands and its density drops. Fewer hydrogen atoms are present per volume to moderate neutrons, causing neutrons to escape or absorb without causing fission. Fission rate automatically falls, cooling the core.
2. **Negative Doppler Defect**: As fuel pellet temperature rises, the thermal motion of $^{238}\text{U}$ nuclei broadens their resonance absorption peaks (Doppler broadening), capturing more neutrons parasitically and instantly dampening reactivity within microseconds.
3. **Control Rod Scram**: Suspended above the core by electromagnetic clutches. Any loss of electrical power cuts current, allowing heavy Boron Carbide ($B_4C$) and Cadmium-Indium-Silver absorber rods to fall into the core via gravity in under 2.0 seconds.
4. **Multiple Physical Containment Barriers**:
   - Barrier 1: Insoluble ceramic $UO_2$ pellet lattice (retains $99\%$ of gaseous fission products).
   - Barrier 2: Hermetic Zircaloy-4 cladding tubes (wall thickness $0.6\text{ mm}$).
   - Barrier 3: Solid forged steel primary reactor pressure boundary ($20\text{ cm}$ thick).
   - Barrier 4: Post-tensioned prestressed reinforced concrete containment structure ($1.2\text{ m}$ thick) lined with $10\text{ mm}$ carbon steel plate, capable of withstanding internal steam pressure and commercial aircraft impact.
