"""Tests for the multiprocessing handler."""
from decimal import Decimal
import pytest
from calculator.commands import AddCommand, MultiplyCommand
from calculator.multiprocessing_handler import MultiprocessingHandler

def test_multiprocessing_add():
    """Test multiprocessing with add command."""
    command = AddCommand(Decimal('5'), Decimal('3'))
    result = MultiprocessingHandler.run_command_async(command)
    assert result == Decimal('8')

def test_multiprocessing_multiply():
    """Test multiprocessing with multiply command."""
    command = MultiplyCommand(Decimal('4'), Decimal('7'))
    result = MultiprocessingHandler.run_command_async(command)
    assert result == Decimal('28')

def test_multiprocessing_error_handling():
    """Test error handling in multiprocessing."""
    # Create a command that will raise an exception
    class ErrorCommand:
        def execute(self):
            raise ValueError("Test error")
    # Test that the error is properly propagated
    with pytest.raises(ValueError, match="Test error"):
        MultiprocessingHandler.run_command_async(ErrorCommand())
