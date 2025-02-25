"""
This module contains the CommandHandler class, which is responsible for creating Command objects based on user input.
"""
from decimal import Decimal, InvalidOperation
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class CommandHandler:
    def __init__(self):
        '''Initialize the CommandHandler class.'''
        self.command_dict = {
            'add': self.create_add_command,
            'subtract': self.create_subtract_command,
            'multiply': self.create_multiply_command,
            'divide': self.create_divide_command,
        }
    
    def get_command(self, command_name, args):
        '''Get the command based on the command name and arguments.'''
        if command_name in self.command_dict:
            return self.command_dict[command_name](args)
        return None
    
    def create_add_command(self, args):
        """Create an AddCommand with the given arguments."""
        try:
            a, b = map(Decimal, args)
            return AddCommand(a, b)
        except (InvalidOperation, ValueError) as e:
            print(f"Error creating add command: {e}")
            return None
        
    def create_subtract_command(self, args):
        """Create a SubtractCommand with the given arguments."""
        try:
            a, b = map(Decimal, args)
            return SubtractCommand(a, b)
        except (InvalidOperation, ValueError) as e:
            print(f"Error creating subtract command: {e}")
            return None
        
    def create_multiply_command(self, args):
        """Create a MultiplyCommand with the given arguments."""
        try:
            a, b = map(Decimal, args)
            return MultiplyCommand(a, b)
        except (InvalidOperation, ValueError) as e:
            print(f"Error creating multiply command: {e}")
            return None
        
    def create_divide_command(self, args):
        """Create a DivideCommand with the given arguments."""
        try:
            a, b = map(Decimal, args)
            return DivideCommand(a, b)
        except (InvalidOperation, ValueError) as e:
            print(f"Error creating divide command: {e}")
            return None