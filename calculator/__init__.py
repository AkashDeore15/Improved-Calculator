from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable

class Calculator:
    
    @staticmethod
    def _get_calculations(a: Decimal, b: Decimal, operation: Callable) -> Decimal:
        """Create and Perform a calculation, then return the result."""
        calculation = Calculation.create(a, b, operation)
        Calculation.add_calculation(calculation)
        return calculation.get_result()
    
    @staticmethod
    def add(a:Decimal, b:Decimal) -> Decimal:
        calc = Calculator._get_calculations(a, b, add)
        return calc.get_result()
    
    @staticmethod
    def subtract(a, b):
        calc = Calculator._get_calculations(a, b, subtract)
        return calc.get_result()
    
    @staticmethod
    def multiply(a, b):
        calc = Calculator._get_calculations(a, b, multiply)
        return calc.get_result()

    @staticmethod
    def divide(a, b):
        calc = Calculator._get_calculations(a, b, divide)
        return calc.get_result()

    