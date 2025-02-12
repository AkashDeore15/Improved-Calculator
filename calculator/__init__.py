from decimal import Decimal
from typing import Callable
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculator:
    
    @staticmethod
    def _get_calculations(a: Decimal, b: Decimal, operation: Callable) -> Decimal:
        """Create and Perform a calculation, then return the result."""
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation
    
    @staticmethod
    def add(a:Decimal, b:Decimal) -> Decimal:
        calculation = Calculator._get_calculations(a, b, add)
        return calculation.get_result()
    
    @staticmethod
    def subtract(a:Decimal, b:Decimal) -> Decimal:
        calculation = Calculator._get_calculations(a, b, subtract)
        return calculation.get_result()
    
    @staticmethod
    def multiply(a:Decimal, b:Decimal) -> Decimal:
        calculation = Calculator._get_calculations(a, b, multiply)
        return calculation.get_result()

    @staticmethod
    def divide(a:Decimal, b:Decimal) -> Decimal:
        calculation = Calculator._get_calculations(a, b, divide)
        return calculation.get_result()
