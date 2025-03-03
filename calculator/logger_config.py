"""
Module for configuring logging for the calculator application.
"""
import os
import logging
import logging.config
from dotenv import load_dotenv

def setup_logging():
    """
    Set up the logging configuration for the calculator application.
    
    Uses logging.conf file for configuration and respects .env settings
    if present. File logging captures all events, while console output
    is suppressed for a cleaner user experience.
    
    Returns:
        logging.Logger: A configured logger instance
    """
    # Load environment variables from .env file if it exists
    load_dotenv()
    
    # Get log level from environment variable or default to INFO
    log_level = os.getenv('LOG_LEVEL', 'INFO')
    
    # Ensure log directory exists
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Load logging configuration from file
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logging.conf')
    if os.path.exists(config_path):
        # Configure logging system from file
        logging.config.fileConfig(config_path, disable_existing_loggers=False)
        
        # Get the logger and set its level
        logger = logging.getLogger('calculator')
        logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
        
        # Find and modify the console handler to prevent logging to console
        for handler in logger.handlers:
            if isinstance(handler, logging.StreamHandler) and not isinstance(handler, logging.FileHandler):
                # Set console handler to CRITICAL+1 to disable all console output
                handler.setLevel(logging.CRITICAL + 1)
        
        # Also check and modify root logger handlers
        root_logger = logging.getLogger()
        for handler in root_logger.handlers:
            if isinstance(handler, logging.StreamHandler) and not isinstance(handler, logging.FileHandler):
                # Set console handler to CRITICAL+1 to disable all console output
                handler.setLevel(logging.CRITICAL + 1)
    else:
        # Fallback configuration if logging.conf is not found
        logger = logging.getLogger('calculator')
        logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
        
        # Clear any existing handlers to avoid duplication
        while logger.handlers:
            logger.handlers.pop()
        
        # Create file handler only (no console handler)
        file_handler = logging.FileHandler(os.path.join(log_dir, 'app.log'))
        file_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        # Add only the file handler
        logger.addHandler(file_handler)
        
        # Prevent propagation to root logger (which might have console handlers)
        logger.propagate = False
    
    # This log entry will only appear in the log file, not on console
    logger.info("Logging configured for calculator application")
    return logger
