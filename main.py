"""Main module for the calculator application with REPL."""
from calculator.command_handler import CommandHandler
from calculator.multiprocessing_handler import MultiprocessingHandler

def main():
    '''Main function for the calculator application with REPL.'''
    print("Welcome to the calculator application!")
    print("Type 'exit' to quit the application.")
    command_handeler = CommandHandler()
    # Display available commands at startup using menu command
    menu_command = command_handeler.get_command('menu', [])
    if menu_command:
        menu_command.execute()
    
    # REPL loop
    while True:
        user_input = input("Enter a command: ")
        #check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting the calculator application. Goodbye!")
            break
        # Parse the user input
        parts = user_input.split(' ')
        if not parts:
            print("Invalid input. Please try again.")
            continue
        command_name = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        # Special commands that don't need arguments
        if command_name == 'menu':
            menu_command = command_handeler.get_command('menu', [])
            if menu_command:
                menu_command.execute()
            continue
        #Evaluate the command
        if command_name in command_handeler.command_dict:
            if len(args) != 2:
                print(f"The {command_name} command requires exactly 2 numeric arguments.Please try again.")
                continue

            command = command_handeler.get_command(command_name, args)
            if command:
                try:
                    print("Executing command...")
                    result = MultiprocessingHandler.run_command_async(command)
                    # print result
                    print(f"The result is: {result}")
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Error executing command. Please try again.")
        else:
            print(f"Unknown command: {command_name}. Please try again.")
            print("Available operations:",",".join(command_handeler.command_dict.keys()))
    
    # if len(sys.argv) != 4:
    #   print("Usage: python calculator_main.py <number1> <number2> <operation>")
    #    sys.exit(1)
    
    # _, a, b, operation = sys.argv
    # calculate_and_print(a, b, operation)

if __name__ == '__main__':
    main()

# def calculate_and_print(a, b, operation_name):
#    operation_mappings = {
#         'add': Calculator.add,
#         'subtract': Calculator.subtract,
#         'multiply': Calculator.multiply,
#         'divide': Calculator.divide
#     }

#     # Unified error handling for decimal conversion
#     try:
#         a_decimal, b_decimal = map(Decimal, [a, b])
#         result = operation_mappings.get(operation_name) # Use get to handle unknown operations
#         if result:
#             print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
#         else:
#             print(f"Unknown operation: {operation_name}")
#     except InvalidOperation:
#         print(f"Invalid number input: {a} or {b} is not a valid number.")
#     except ZeroDivisionError:
#         print("Error: Division by zero.")
#     except Exception as e: # Catch-all for unexpected errors
#         print(f"An error occurred: {e}")
