"""
This module contains the CommandHandler class, which is responsible for creating Command objects based on user input.
"""
import os
import importlib
import inspect
from decimal import Decimal, InvalidOperation
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand, Command

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

        # Load plugins
        self.load_plugins()
    
    def load_plugins(self):
        """Load command plugins from the plugins directory."""
        plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
        
        # Skip if plugins directory doesn't exist
        if not os.path.exists(plugins_dir):
            return
        
        # Get all Python files in the plugins directory
        plugin_files = [f for f in os.listdir(plugins_dir) 
                       if f.endswith('.py') and not f.startswith('__')]
        
        for plugin_file in plugin_files:
            # Convert filename to module name (remove .py extension)
            module_name = plugin_file[:-3]
            
            try:
                # Import the plugin module
                plugin_module = importlib.import_module(f'calculator.plugins.{module_name}')
                
                # Find all Command subclasses in the module
                for _, obj in inspect.getmembers(plugin_module):
                    if (inspect.isclass(obj) and issubclass(obj, Command) and 
                        obj.__module__ == plugin_module.__name__ and 
                        obj is not Command):
                        
                        # Get command name from class name (remove 'Command' suffix)
                        command_name = obj.__name__.lower()
                        if command_name.endswith('command'):
                            command_name = command_name[:-7]
                        
                        # Add to command dictionary
                        self.command_dict[command_name] = lambda args, cls=obj: self._create_command(cls, args)
                        print(f"Loaded plugin command: {command_name}")
            
            except Exception as e:
                print(f"Error loading plugin {module_name}: The reuired operation is not available")

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
