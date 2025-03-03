"""
Module for loading environment variables for the calculator application.
"""
import os
from dotenv import load_dotenv

def load_environment():
    """
    Load environment variables from .env file.
    
    Returns:
        dict: Dictionary containing environment variables
    """
    # Load .env file if it exists
    load_dotenv()
    
    # Get configuration values with defaults
    config = {
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO'),
        'PLUGINS_PATH': os.getenv('PLUGINS_PATH', 'calculator/plugins'),
        'DEBUG_MODE': os.getenv('DEBUG_MODE', 'False').lower() == 'true'
    }
    
    return config
