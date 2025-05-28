"""Logging configuration and utilities"""

import logging
import os
from datetime import datetime
from typing import Optional
from config.settings import get_settings

def setup_logging() -> None:
    """Setup logging configuration"""
    settings = get_settings()
    
    # Create logs directory if it doesn't exist
    os.makedirs(settings.logs_dir, exist_ok=True)
    
    # Configure logging
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # File handler
    log_file = os.path.join(settings.logs_dir, f"mcp_server_{datetime.now().strftime('%Y%m%d')}.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter(log_format))
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format))
    
    # Root logger configuration
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, settings.log_level.upper()))
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

def get_logger(name: str) -> logging.Logger:
    """Get a logger instance"""
    return logging.getLogger(name)
