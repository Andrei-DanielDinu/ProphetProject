# Contributing to The Prophet Project

We welcome contributions to the Prophet Project! This repository is an open research and systems-engineering documentation project modeling the technological trajectory from primitive tools to advanced technology.

## 1. Principles for Contributions

1. **Evidence-Led**: Technical and historical claims must cite empirical sources, archaeological excavation data, or verified engineering equations.
2. **Explicit Confidence**: Categorize additions into `verified`, `calculated`, `estimated`, or `speculative`.
3. **Conservation Laws**: No hand-waving or magic shortcuts. Processes must balance mass, energy, and labor inputs.
4. **Structured Data Alignment**: Any new technology or resource added to documentation must be mirrored with an entry in `data/technologies.json` or `data/resources.json`.

## 2. Local Validation Before Submitting

Run the local validation suite to verify schemas, acyclicity, and docs build:

```bash
# 1. Validate JSON Schemas
python scripts/validate_data.py

# 2. Verify Dependency DAG
python scripts/validate_dependencies.py

# 3. Check Workforce Model
python scripts/calculate_workforce.py

# 4. Run Pytest Suite
python -m pytest

# 5. Strict MkDocs Build
python -m mkdocs build --strict
```

All pull requests must pass automated CI checks in `.github/workflows/validate.yml`.
