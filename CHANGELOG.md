# Changelog

All notable changes to the Prophet Project will be documented in this file.

## [v0.2.0] - 2026-11-16

### Added
- **Full Technology Stack**: Authoritative technical documentation spanning from primitive flint knapping and controlled fire to advanced modern frontiers:
  - Primordial lithics and pyrotechnology (`primordial-and-stone-tools.md`)
  - Metallurgy: copper, bronze, bloomery iron, quench-tempered steel, Bessemer converter (`metallurgy.md`)
  - Machine tools: Whitworth scraping, Maudslay lathes, Wilkinson boring mills (`mechanics-and-machine-tools.md`)
  - Industrial chemistry: sulfuric acid, Solvay process, petrochemistry (`industrial-chemistry.md`)
  - Electrification: dynamos, polyphase AC, high-voltage transformers (`electricity-and-grid.md`)
  - Computing: semiconductors, photolithography, CMOS microprocessors, internet (`computing-and-microelectronics.md`)
  - Targeted Modern Frontiers:
    - Smartphones & mobile ecosystems (`smartphones.md`)
    - Large Language Models & Deep Transformer AI (`large-language-models.md`)
    - Controlled civilian nuclear fission power reactors (`nuclear-reactors.md`)
    - Superconducting particle accelerators & CERN Large Hadron Collider (`particle-accelerators-cern.md`)
    - Staged cryogenic rocketry & orbital launch systems (`rocketry-and-spacecraft.md`)
    - Modular space stations (ISS) & closed-loop ECLSS life support (`orbital-stations-iss.md`)
    - Robotics, harmonic drives, SLAM, and dynamic humanoid control (`robotics-and-automation.md`)
- **Phase Dossiers**: Phase 0 through Phase 7 documentation in `docs/phases/`.
- **Lore & Systems Methodology**: Full guides covering the Prophet, the Machine, the Threat, dependency modeling, resource accounting, and manpower models.
- **Geography, Baseline & Institutions**: Comprehensive analyses for Early Dynastic Egypt, Nile logistics, resource atlas, guilds, education, and standards bureaus.
- **Structured Data Engine**:
  - `data/schemas/` JSON Schemas for technologies, resources, phases, workforce, and risks.
  - `data/technologies.json` 33-node DAG spanning 18 critical-path tiers with zero cycles.
  - `data/resources.json`, `data/phases.json`, `data/workforce.json`, `data/risks.json`, `data/trade_routes.json`.
- **Validation Engine & CI/CD**:
  - `scripts/validate_data.py`, `scripts/validate_dependencies.py`, `scripts/calculate_workforce.py`.
  - Pytest automated test suite in `tests/`.
  - GitHub Actions workflows for automated validation and GitHub Pages static deployment.
