import pytest
from scripts.calculate_workforce import calculate_workforce_balances

def test_workforce_calculation():
    assert calculate_workforce_balances() is True
