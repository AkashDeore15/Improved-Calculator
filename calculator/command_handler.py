"""
This module contains the CommandHandler class, which is responsible for creating Command objects based on user input.
"""
from decimal import Decimal, InvalidOperation
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand

class CommandHandler:
    def __init__(self):
        '''Initialize the CommandHandler class.'''
        self.command_dict = {
            'add': self.create_add_command,
            'subtract': self.create_subtract_command,
            'multiply': self.create_multiply_command,
            'divide': self.create_divide_command,
        }
        #Add menu command- this is a special command that displays the available commands
        self.command_dict['menu'] = self.create_menu_command

    def create_menu_command(self, args):
        """Create a MenuCommand to display available commands."""
        return MenuCommand(self.command_dict)


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
            print(f"Error creating add command: Please provide valid number for addition")
            return None
        
    def create_subtract_command(self, args):
        """Create a SubtractCommand with the given arguments."""
        try:
            a, b = map(Decimal, args)
            return SubtractCommand(a, b)
        except (InvalidOperation, ValueError) as e:
            print(f"Error creating subtract command: Please provide valid number for substraction")
            return None
        
    def create_multiply_command(self, args):
        """Create a MultiplyCommand with the given arguments."""
        try:
            a, b = map(Decimal, args)
            return MultiplyCommand(a, b)
        except (InvalidOperation, ValueError) as e:
            print(f"Error creating multiply command: Please provide valid number for multiplication")
            return None
        
    def create_divide_command(self, args):
        """Create a DivideCommand with the given arguments."""
        try:
            a, b = map(Decimal, args)
            return DivideCommand(a, b)
        except (InvalidOperation, ValueError) as e:
            print(f"Error creating divide command: Please provide valid number for division")
            return None

def _create_command(self, command_class, args):
    """Create a command instance from a command class."""
    try:
        # Convert arguments to Decimal
        decimal_args = list(map(Decimal, args))
        return command_class(*decimal_args)
    except (InvalidOperation, ValueError):
        command_name = command_class.__name__.lower().replace('command', '')
        print(f"Error: Please provide valid numbers for {command_name}.")
        return None
