"""Tests for the plugin system."""
from decimal import Decimal
import os
import pytest
from calculator.command_handler import CommandHandler

def test_plugin_loading():
    """Test that plugins are loaded correctly."""
    handler = CommandHandler()
    
    # Check if the power command was loaded
    assert 'power' in handler.command_dict
    
    # Test power command if available
    if 'power' in handler.command_dict:
        power_cmd = handler.get_command('power', ['2', '3'])
        assert power_cmd.execute() == Decimal('8')

def test_invalid_plugin_args():
    """Test invalid arguments for plugin commands."""
    handler = CommandHandler()
    
    # Test with invalid arguments if power command exists
    if 'power' in handler.command_dict:
        assert handler.get_command('power', ['invalid', '3']) is None
