"""
This module contains the commands for the calculator application.
"""
from decimal import Decimal
from abc import ABC, abstractmethod
from calculator import Calculator

class Command(ABC):
    @abstractmethod
    def execute(self):        
        '''Execute the command.'
        '''
        pass

class AddCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        '''Initialize the AddCommand class'''
        self.a = a
        self.b = b
    
    def execute(self):
        '''Execute the add command'''
        return Calculator.add(self.a, self.b)

class SubtractCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        '''Initialize the SubtractCommand class'''
        self.a = a
        self.b = b
    
    def execute(self):
        '''Execute the subtract command'''
        return Calculator.subtract(self.a, self.b)

class MultiplyCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        '''Initialize the MultiplyCommand class'''
        self.a = a
        self.b = b
    
    def execute(self):
        '''Execute the multiply command'''
        return Calculator.multiply(self.a, self.b)

class DivideCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        '''Initialize the DivideCommand class'''
        self.a = a
        self.b = b
    
    def execute(self):
        '''Execute the divide command'''
        return Calculator.divide(self.a, self.b)