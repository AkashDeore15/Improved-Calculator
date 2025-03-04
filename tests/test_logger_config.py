"""Tests for the logger_config module."""
import logging
from unittest.mock import patch, MagicMock
from calculator.logger_config import setup_logging

def test_setup_logging_with_conf_file():
    """Test setup_logging with a logging.conf file."""
    # Create a mock fileConfig that does nothing
    with patch('logging.config.fileConfig') as mock_fileconfig, \
         patch('os.path.exists', return_value=True), \
         patch('os.makedirs') as mock_makedirs, \
         patch('os.path.dirname', return_value='/mock/path'), \
         patch('os.getenv', return_value='INFO'):
        # Mock the logger to avoid actual logging
        mock_logger = MagicMock()
        mock_handler = MagicMock()
        mock_handler.__class__ = logging.StreamHandler
        mock_logger.handlers = [mock_handler]
        with patch('logging.getLogger', return_value=mock_logger):
            logger = setup_logging()
            # Verify the logger was configured correctly
            assert logger is mock_logger
            mock_fileconfig.assert_called_once()
            # Not called because directory exists
            assert not mock_makedirs.called

def test_setup_logging_without_conf_file():
    """Test setup_logging without a logging.conf file."""
    # Correctly patching the behaviors we need
    def side_effect_exists(path):
        # Return False only for the logging.conf file, True for directory
        if 'logging.conf' in path:
            return False
        return True
    with patch('os.path.exists', side_effect=side_effect_exists), \
         patch('os.makedirs') as mock_makedirs, \
         patch('logging.FileHandler') as mock_file_handler, \
         patch('os.path.dirname', return_value='/mock/path'), \
         patch('os.getenv', return_value='INFO'):
        # Create mock handler and formatter
        mock_handler = MagicMock()
        mock_file_handler.return_value = mock_handler
        # Mock the logger to avoid actual logging
        mock_logger = MagicMock()
        mock_logger.handlers = []
        with patch('logging.getLogger', return_value=mock_logger):
            logger = setup_logging()
            # Verify the logger was configured correctly
            assert logger is mock_logger
            mock_file_handler.assert_called_once()
            assert mock_handler.setFormatter.called
            assert mock_logger.addHandler.called
            assert mock_logger.setLevel.called
            # The directory already exists so makedirs won't be called
            assert not mock_makedirs.called

def test_setup_logging_create_log_dir():
    """Test setup_logging creates log directory if it doesn't exist."""
    def side_effect_exists(path):
        '''Mock os.path.exists to return False for logs directory.'''
        # Return False for logs directory
        if 'logs' in path:
            return False
        if 'logging.conf' in path:
            return False  # Make sure the config file check returns False
        return True
    with patch('os.path.exists', side_effect=side_effect_exists), \
         patch('os.makedirs') as mock_makedirs, \
         patch('logging.FileHandler') as mock_file_handler, \
         patch('os.path.dirname', return_value='/mock/path'), \
         patch('os.getenv', return_value='INFO'), \
         patch('logging.config.fileConfig'):  # Mock fileConfig to avoid error
        # Create mock handler
        mock_handler = MagicMock()
        mock_file_handler.return_value = mock_handler
        # Mock the logger to avoid actual logging
        mock_logger = MagicMock()
        mock_logger.handlers = []
        with patch('logging.getLogger', return_value=mock_logger):
            # Call the function we're testing
            setup_logging()
            # The directory should be created if it doesn't exist
            assert mock_makedirs.call_count > 0

def test_setup_logging_with_handlers():
    """Test setup_logging when logger already has handlers."""
    with patch('os.path.exists', return_value=False), \
         patch('os.makedirs'), \
         patch('logging.FileHandler') as mock_file_handler, \
         patch('os.path.dirname', return_value='/mock/path'), \
         patch('os.getenv', return_value='INFO'), \
         patch('dotenv.find_dotenv', return_value=''), \
         patch('dotenv.load_dotenv'):  # Mock dotenv completely
        # Create mock handler
        mock_handler = MagicMock()
        mock_file_handler.return_value = mock_handler
        # Create a custom mock logger implementation
        class MockLogger(MagicMock):
            ''''Mock logger class with handlers attribute.'''
            def __init__(self, *args, **kwargs):
                '''Initialize the logger with a handler.'''
                super().__init__(*args, **kwargs)
                self.handlers = [MagicMock()]  # Start with one handler
            def remove_handler(self, handler):
                '''Remove a handler from the logger.'''
                if handler in self.handlers:
                    self.handlers.remove(handler)
        mock_logger = MockLogger()
        with patch('logging.getLogger', return_value=mock_logger):
            # Actually call the function to test it
            setup_logging()
            # Check that a new handler was added (file handler)
            assert mock_logger.addHandler.called
