"""
This module contains the tests for the calculator operations and calculation class.
"""

# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
import pytest

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('1'), Decimal('2'), add, Decimal('3')),
    (Decimal('1'), Decimal('2'), subtract, Decimal('-1')),
    (Decimal('1'), Decimal('2'), multiply, Decimal('2')),
    (Decimal('1'), Decimal('2'), divide, Decimal('0.5')),
    (Decimal('1'), Decimal('0'), divide, ValueError),
    (Decimal('101.8'), Decimal('0.258'), add, Decimal('102.058')),
    (Decimal('101.8'), Decimal('0.258'), subtract, Decimal('101.542')),
    (Decimal('101.8'), Decimal('0.258'), multiply, Decimal('26.2964')),
    (Decimal('101.8'), Decimal('0.258'), divide, Decimal('394.5736434108527131782945736')),
])
def test_calculation(a, b, operation, expected):
    """Test the Calculation class."""
    if expected == ValueError:
        with pytest.raises(ValueError):
            Calculation.create(a, b, operation)
    else:
        calc = Calculation.create(a, b, operation)
        assert calc.get_result() == expected
        assert str(calc) == f"Calculation({a}, {b}, {operation.__name__})"

def test_divide_by_zero():
    """Test divide by zero."""
    with pytest.raises(ValueError, match='Cannot divide by zero'):
        Calculation.create(Decimal('1'), Decimal('0'), divide)