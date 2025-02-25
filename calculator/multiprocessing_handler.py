"""This module contains the MultiprocessingHandler class."""
import multiprocessing
from decimal import Decimal
from calculator.commands import Command

class MultiprocessingHandler:
    @staticmethod
    def execute_command(command: Command, result_queue):
        """Execute a command and put the result in a queue."""
        try:
            result = command.execute()
            result_queue.put(('success', result))
        except Exception as e:
            result_queue.put(('error', str(e)))
    
    @staticmethod
    def run_command_async(command: Command):
        """Run a command in a separate process."""
        # Create a multiprocessing queue to get the result
        result_queue = multiprocessing.Queue()
        # Create and start a process
        process = multiprocessing.Process(
            target=MultiprocessingHandler.execute_command,
            args=(command, result_queue)
        )
        process.start()
        # Wait for the process to complete and get the result
        process.join()
        # Get the result from the queue
        if not result_queue.empty():
            status, result = result_queue.get()
            if status == 'success':
                return result
            else:
                raise ValueError(result)
        else:
            raise RuntimeError("Command execution failed")
