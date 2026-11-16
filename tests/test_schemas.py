import pytest
from scripts.validate_data import run_validation

def test_data_schemas_validation():
    assert run_validation() is True
