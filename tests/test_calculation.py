"""
This module contains the tests for the calculator operations and calculation class.
"""
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('1'), Decimal('2'), add, Decimal('3')),
    (Decimal('1'), Decimal('2'), subtract, Decimal('-1')),
    (Decimal('1'), Decimal('2'), multiply, Decimal('2')),
    (Decimal('1'), Decimal('2'), divide, Decimal('0.5')),
    (Decimal('1'), Decimal('0'), divide, ValueError),
    (Decimal('101.8'), Decimal('0.258'), add, Decimal('102.058')),
    (Decimal('101.8'), Decimal('0.258'), subtract, Decimal('101.542')),
    (Decimal('101.8'), Decimal('0.258'), multiply, Decimal('26.2644')),
    (Decimal('101.8'), Decimal('0.258'), divide, Decimal('394.5736434108527131782945736')),
])

def test_calculation(a, b, operation, expected):
    """Test the Calculation class."""
    calc = Calculation(a, b, operation)
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calc.get_result()
    else:
        assert calc.get_result() == expected
        expected_repr = f"Calculation({a}, {b}, {operation.__name__})"
        assert calc.__repr__() == expected_repr, "The __repr__ method is not correct"

def test_divide_by_zero():
    """Test divide by zero."""
    calc = Calculation(Decimal('1'), Decimal('0'), divide)
    with pytest.raises(ValueError, match='Cannot divide by zero'):
        calc.get_result()
