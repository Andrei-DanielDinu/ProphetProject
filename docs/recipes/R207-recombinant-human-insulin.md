# R207 — Recombinant Human Insulin Production

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R207 · RECOMBINANT HUMAN INSULIN BIOMANUFACTURING         ║
║  End product: 500 g Crystalline Recombinant Human Insulin        ║
║  Activity: 28.5 IU/mg, Identical to endogenous pancreatic hormone║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The metabolic biotechnology prerequisite for:                 ║
║    • Treatment and survival of Type 1 diabetes mellitus patients ║
║    • Glycemic control in acute hospital critical care            ║
║    • Proving the modern recombinant DNA bioprocess platform     ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Engineered *Escherichia coli* Strain (BL21/pET Expression):║
║       Carries synthetic human proinsulin cDNA gene [→ R150]      ║
║    2. Fermentation Growth Medium (per 500 L batch):              ║
║       • Yeast extract: 15 kg, Tryptone peptone: 10 kg            ║
║       • Glycerol / Glucose carbon feed: 30 kg [→ R050, R054]     ║
║       • K₂HPO₄, KH₂PO₄, MgSO₄ mineral salts: 5 kg [→ R000]       ║
║       • IPTG Inducer (Isopropyl β-D-1-thiogalactopyranoside): 50g║
║    3. High-Pressure Cell Homogenizer (1,000 bar): 1 [→ R072]     ║
║    4. Urea / Guanidine-HCl Denaturant: 100 kg [→ R055 urea]      ║
║    5. Cleavage Enzymes (Trypsin & Carboxypeptidase B): 50 g      ║
║    6. Fast Protein Liquid Chromatography (FPLC / Prep HPLC): 1   ║
║    7. Zinc Chloride (ZnCl₂ analytical grade): 20 g [→ R030, R053]║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: HIGH-DENSITY FED-BATCH FERMENTATION                    ║
║    1a. Prepare 500 L defined medium in 316L fermenter [→ R036].  ║
║    1b. Inoculate with recombinant *E. coli* expressing proinsulin║
║        fusion protein under control of T7 lac promoter.          ║
║    1c. Grow at 37°C with dissolved oxygen maintained at 30% via  ║
║        cascade agitation and pure O₂ supplementation [→ R110].   ║
║    1d. When OD₆₀₀ reaches 60, add 1.0 mM IPTG to induce high-    ║
║        level transcription: proinsulin accumulates inside the    ║
║        cells as dense, insoluble intracellular inclusion bodies. ║
║    1e. Harvest bacterial cells via disk-stack centrifuge.        ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: CELL LYSIS & INCLUSION BODY REFOLDING                  ║
║    2a. Resuspend cell paste in Tris-EDTA buffer. Pass twice      ║
║        through high-pressure homogenizer at 1,000 bar to lyse    ║
║        100% of bacterial cell membranes.                         ║
║    2b. Centrifuge at 8,000 g: Pellet dense inclusion bodies.     ║
║    2c. Solubilize inclusion bodies in 8 M urea containing 50 mM  ║
║        dithiothreitol (DTT) reducing agent to break aberrant S-S.║
║    2d. Oxidative refolding: Dilute protein 50-fold into cold     ║
║        refolding buffer (pH 10.5, 2 M urea, 1 mM cysteine / 0.1  ║
║        mM cystine redox pair) at 4°C for 24 hours:               ║
║        Proinsulin spontaneously folds into its native tertiary   ║
║        conformation with the correct three disulfide bonds:      ║
║        CysA6-CysA11, CysA7-CysB7, and CysA20-CysB19.             ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: ENZYMATIC CLEAVAGE & PREPARATIVE HPLC                  ║
║    3a. Treat native folded proinsulin with human recombinant     ║
║        trypsin and carboxypeptidase B:                           ║
║        Enzymes precisely excise the connecting C-peptide chain   ║
║        and terminal basic residues, yielding mature two-chain    ║
║        insulin (A chain 21 amino acids, B chain 30 amino acids). ║
║    3b. Purify mature insulin by preparative reverse-phase C18    ║
║        HPLC column eluted with acetonitrile/water gradient [→ R100]║
║    3c. Crystallization: Pool pure insulin fractions, add zinc    ║
║        chloride (ZnCl₂) at pH 5.5: Insulin forms brilliant       ║
║        rhombohedral zinc-insulin hexamer crystals.               ║
║    3d. Centrifuge, lyophilize under vacuum into dry white powder.║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Molecular weight: 5,808 Da (ESI-MS mass spectrometry).      ║
║    • Chemical purity: >99.0% (Reversed-Phase HPLC).              ║
║    • Biological potency: 28.5 IU/mg. Bio-identity confirmed.     ║
╚══════════════════════════════════════════════════════════════════╝
```
