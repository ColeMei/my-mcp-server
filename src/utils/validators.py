"""Input validation utilities"""

import os
import re
from typing import Optional
from urllib.parse import urlparse

def validate_file_path(file_path: str) -> tuple[bool, Optional[str]]:
    """
    Validate file path for security and existence
    Args:
        file_path: Path to validate
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not file_path:
        return False, "File path cannot be empty"
    
    # Allow absolute paths and relative paths
    # Only block obvious path traversal attacks
    if file_path.startswith("../") or "/../" in file_path:
        return False, "Invalid file path: potential security risk"
    
    # Resolve to absolute path for validation
    try:
        abs_path = os.path.abspath(file_path)
    except Exception:
        return False, "Invalid file path format"
    
    # Check if file exists
    if not os.path.exists(abs_path):
        return False, f"File does not exist: {file_path}"
    
    # Check if it's actually a file
    if not os.path.isfile(abs_path):
        return False, f"Path is not a file: {file_path}"
    
    return True, None


def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_url(url: str) -> bool:
    """Validate URL format"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
