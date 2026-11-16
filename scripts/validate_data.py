#!/usr/bin/env python3
"""
Validates all structured JSON datasets against their formal JSON Schemas.
"""
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator, validate, ValidationError

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
SCHEMA_DIR = DATA_DIR / "schemas"

SCHEMAS = {
    "technologies.json": SCHEMA_DIR / "technology.schema.json",
    "resources.json": SCHEMA_DIR / "resource.schema.json",
    "phases.json": SCHEMA_DIR / "phase.schema.json",
    "risks.json": SCHEMA_DIR / "risk.schema.json",
    "workforce.json": SCHEMA_DIR / "workforce.schema.json",
}

def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_validation():
    errors = []
    print("=" * 60)
    print("PROPHET PROJECT: DATA VALIDATION SUITE")
    print("=" * 60)

    for data_file_name, schema_file_path in SCHEMAS.items():
        data_file_path = DATA_DIR / data_file_name
        if not data_file_path.exists():
            errors.append(f"Missing data file: {data_file_path}")
            continue
        if not schema_file_path.exists():
            errors.append(f"Missing schema file: {schema_file_path}")
            continue

        try:
            schema = load_json(schema_file_path)
            data = load_json(data_file_path)
            validator = Draft202012Validator(schema)

            if isinstance(data, list):
                print(f"Validating {data_file_name} ({len(data)} records)...")
                seen_ids = set()
                for idx, record in enumerate(data):
                    rec_id = record.get("id", record.get("phase", f"index_{idx}"))
                    if "id" in record:
                        if record["id"] in seen_ids:
                            errors.append(f"Duplicate ID '{record['id']}' in {data_file_name}")
                        seen_ids.add(record["id"])
                    
                    for err in validator.iter_errors(record):
                        errors.append(f"{data_file_name}[{rec_id}]: {err.message} at path {list(err.path)}")
            else:
                print(f"Validating {data_file_name} (object)...")
                for err in validator.iter_errors(data):
                    errors.append(f"{data_file_name}: {err.message} at path {list(err.path)}")

        except Exception as ex:
            errors.append(f"Error parsing {data_file_name}: {ex}")

    if errors:
        print("\nValidation FAILED with the following errors:")
        for e in errors:
            print(f"  [!] {e}")
        return False
    else:
        print("\nAll datasets validated successfully against JSON Schemas!")
        return True

if __name__ == "__main__":
    success = run_validation()
    sys.exit(0 if success else 1)
