from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def setup_calculation():
    """Set up the Calculation class."""
    Calculations.clear_history()
    Calculation(Decimal('1'), Decimal('2'), add)
    Calculation(Decimal('1'), Decimal('2'), subtract)
    Calculation(Decimal('1'), Decimal('2'), multiply)
    Calculation(Decimal('1'), Decimal('2'), divide)

def test_add_calculation(setup_calculation):
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('15'), Decimal('28'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_last_calculation() == calc, "Failed to add calculation to history."

def test_get_history(setup_calculation):
    """Test retrieving the entire calculation history."""
    history = Calculations.get_history()
    assert len(history) == 2, "Failed to get history."

def test_clear_history(setup_calculation):
    """Test clearing the entire calculation history."""
    history = Calculations.clear_history()
    assert len(history) == 0, "Failed to clear history."

def test_last_calculation(setup_calculation):
    """Test getting the last calculation."""
    latest = Calculations.get_last_calculation()
    assert latest.a == Decimal('1') and latest.b == Decimal('2'), "Failed to get latest calculation."

def test_find_calculations_by_operation(setup_calculation):
    """Test finding calculations by operation."""
    add_operation = Calculations.find_calculations_by_operation('add')
    assert len(add_operation) == 1, "Failed to find calculations by add operation."

    subtract_operation = Calculations.find_calculations_by_operation('subtract')
    assert len(subtract_operation) == 1, "Failed to find calculations by subtract operation."

    multiply_operation = Calculations.find_calculations_by_operation('multiply')
    assert len(multiply_operation) == 1, "Failed to find calculations by multiply operation."   

    divide_operation = Calculations.find_calculations_by_operation('divide')
    assert len(divide_operation) == 1, "Failed to find calculations by divide operation."

def test_get_last_with_empty_history():
    """Test getting the last calculation with an empty history."""
    Calculations.clear_history()
    assert Calculations.get_last_calculation() == None, "Failed to get last calculation with empty history."