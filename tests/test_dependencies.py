import pytest
from scripts.validate_dependencies import validate_dependencies

def test_technology_graph_dag_and_prerequisites():
    assert validate_dependencies() is True
