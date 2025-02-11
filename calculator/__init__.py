from calculator.operations import add, subtract, multiply, divide
from calculator.calculations import Calculations

class Calculator:
    def __init__(self):
        self.calculations = []
    
    @staticmethod
    def add(a, b):
        calc = Calculations(a, b, add)
        return calc.get_result()
    
    @staticmethod
    def subtract(a, b):
        calc = Calculations(a, b, subtract)
        return calc.get_result()
    
    @staticmethod
    def multiply(a, b):
        calc = Calculations(a, b, multiply)
        return calc.get_result()

    @staticmethod
    def divide(a, b):
        calc = Calculations(a, b, divide)
        return calc.get_result()

    '''
    @staticmethod
    def get_calculations(self):
        return self.calculations
    '''