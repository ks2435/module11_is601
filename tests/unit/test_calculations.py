import pytest
from calculation_schemas import CalculationCreate, OperationType
from calculation_factory import calculate

def test_add():
    result = calculate(10, 5, OperationType.add)
    assert result == 15

def test_subtract():
    result = calculate(10, 5, OperationType.subtract)
    assert result == 5

def test_multiply():
    result = calculate(4, 5, OperationType.multiply)
    assert result == 20

def test_divide():
    result = calculate(10, 2, OperationType.divide)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculate(10, 0, OperationType.divide)

def test_schema_valid():
    calc = CalculationCreate(a=10, b=5, type=OperationType.add)
    assert calc.a == 10
    assert calc.b == 5
    assert calc.type == OperationType.add

def test_schema_divide_by_zero():
    with pytest.raises(ValueError):
        calculate(10, 0, OperationType.divide)

def test_schema_invalid_type():
    with pytest.raises(Exception):
        CalculationCreate(a=10, b=5, type="invalid")