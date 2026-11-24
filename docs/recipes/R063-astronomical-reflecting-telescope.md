# R063 — Astronomical Reflecting Telescope & Parabolic Mirror

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R063 · 1.0-METER RITCHEY-CHRÉTIEN REFLECTING TELESCOPE   ║
║  End product: 1 × 1.0-Meter f/8 Classical/RC Optical Telescope   ║
║  Surface accuracy: $\lambda/10$ wavefront (55 nm), Limiting mag: 21║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The deep-space cosmology and planetary observation tool for:  ║
║    • Precise planetary ephemeris, orbital mechanics, astrometry  ║
║    • Deep-sky galactic structure and cosmological red-shift      ║
║    • Tracking satellites, asteroids, and aerospace trajectories  ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Low-Expansion Borosilicate / Zerodur Mirror Blank: 1       ║
║       (Diameter: 1,020 mm, Thickness: 150 mm) [→ R060]           ║
║    2. Silicon Carbide Grinding Grits (80 to 1200 mesh): 50 kg    ║
║       [→ Sintered SiC, R037]                                     ║
║    3. Optical Pitch & Cerium Oxide Polishing Slurry: 10 kg       ║
║       [→ Pine pitch R025 + refined ceria]                        ║
║    4. High-Purity Aluminium Wire (99.999% Al): 100 g [→ R034]    ║
║    5. Vacuum Thermal Evaporator Chamber (1.5 m dia): 1 [→ R092]  ║
║    6. Foucault Knife-Edge & Ronchi Optical Test Benches: 1       ║
║    7. Equatorial Fork Mount with Worm Gear Drive: 1 [→ R072]     ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: MIRROR BLANK CASTING & ROUGH CURVATURE GENERATION      ║
║    1a. Melt low-expansion borosilicate glass ($SiO_2\text{-}B_2O_3$)║
║        at 1,550°C in refractory furnace [→ R060].                ║
║    1b. Cast into ceramic honeycomb rib mold to reduce mirror     ║
║        weight by 60% while maintaining structural bending rigidity║
║    1c. Anneal in computer-controlled annealing lehr: Cool from   ║
║        560°C to ambient at 0.5°C/hour over 4 weeks to eliminate  ║
║        all internal thermal stress birefringence.                ║
║    1d. Curve generation: Grind concave spherical depression      ║
║        using cast iron tool with coarse SiC 80-grit slurry:      ║
║        Sagitta depth $s = \frac{r^2}{2 R} = 15.6\text{ mm}$ for  ║
║        radius of curvature $R = 8.0\text{ meters}$ (f/4 primary).║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: FINE GRINDING & PITCH-LAP PARABOLIZATION               ║
║    2a. Fine grind sequentially through 220, 400, 600, and 1200   ║
║        grit silicon carbide powders to remove all subsurface pits║
║    2b. Pour faceted optical pitch lap (natural pine pitch +      ║
║        rosin, hardness checked by fingernail indent test).       ║
║    2c. Polish to optical specular shine using cerium oxide       ║
║        slurry suspended in distilled water for 60 hours.         ║
║    2d. Parabolization: Use star-lap and localized stroke polishing║
║        to deepen the center from a sphere into a true paraboloid:║
║        Shape profile: $z = \frac{r^2}{2R} + \frac{(1+K) r^4}{8 R^3}$║
║        where conic constant $K = -1.000$ (Parabola).             ║
║    2e. Foucault Knife-Edge & Hartmann Mask Testing: Position pin-║
║        hole light source and razor knife edge at center of       ║
║        curvature. Measure shadow cut-off zonal radii across 10   ║
║        concentric mirror zones: Accuracy must match paraboloidal ║
║        zonal formula $\Delta x = \frac{r^2}{2R}$ within 30 nm!   ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: VACUUM ALUMINIZING & OPTICAL ASSEMBLY                  ║
║    3a. Clean polished mirror with pure ethanol and glow-discharge║
║        ion bombardment inside vacuum chamber at $10^{-4}\text{ Pa}$║
║    3b. Thermal evaporation: Vaporize 99.999% aluminium staples   ║
║        from glowing tungsten filament coils [→ R091]:            ║
║        Uniform 100 nm mirror aluminium film deposits across face.║
║    3c. Protective overcoat: Evaporate 150 nm Silicon Monoxide    ║
║        ($SiO$) or $MgF_2$ to prevent aluminium oxidation and     ║
║        allow routine cleaning without scratching. Reflectivity >92%║
║    3d. Mount in Serrurier truss open steel tube: Equalizes       ║
║        primary and secondary mirror deflections under gravity at ║
║        all telescope pointing angles, keeping optical axes aligned!║
║    3e. Precision worm drive gear (720 teeth, 1.2 m dia [→ R072]) ║
║        driven by sidereal stepper motor tracks stars smoothly.   ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Optical surface figure: Peak-to-valley error $<\lambda/8$   ║
║      ($<65\text{ nm}$ across 1.0 meter aperture).                ║
║    • Strehl ratio: $>0.85$ (diffraction-limited performance).    ║
║    • Tracking error: $<0.5$ arcseconds over 10-minute exposure.  ║
╚══════════════════════════════════════════════════════════════════╝
```
