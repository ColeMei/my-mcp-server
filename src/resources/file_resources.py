"""File resource handlers"""

import os
import mimetypes
from typing import Any, Dict
from utils.logging import get_logger
from utils.validators import validate_file_path

logger = get_logger(__name__)

class FileResources:
    """File resource handlers for MCP server"""
    
    @staticmethod
    def get_file_info(file_path: str) -> Dict[str, Any]:
        """
        Get file information resource
        
        Args:
            file_path: Path to the file
            
        Returns:
            Dictionary with file information
        """
        try:
            is_valid, error = validate_file_path(file_path)
            if not is_valid:
                return {"error": error}
            
            file_stats = os.stat(file_path)
            mime_type, encoding = mimetypes.guess_type(file_path)
            
            return {
                "file_path": file_path,
                "file_name": os.path.basename(file_path),
                "file_size": file_stats.st_size,
                "mime_type": mime_type,
                "encoding": encoding,
                "created": file_stats.st_ctime,
                "modified": file_stats.st_mtime,
                "is_readable": os.access(file_path, os.R_OK),
                "is_writable": os.access(file_path, os.W_OK)
            }
            
        except Exception as e:
            logger.error(f"Error getting file info for {file_path}: {str(e)}")
            return {"error": str(e)}
    
    @staticmethod
    def get_directory_tree(directory_path: str, max_depth: int = 3) -> Dict[str, Any]:
        """
        Get directory tree structure
        
        Args:
            directory_path: Path to directory
            max_depth: Maximum depth to traverse
            
        Returns:
            Dictionary with directory tree
        """
        try:
            if not os.path.exists(directory_path):
                return {"error": "Directory does not exist"}
            
            if not os.path.isdir(directory_path):
                return {"error": "Path is not a directory"}
            
            def build_tree(path: str, current_depth: int = 0) -> Dict[str, Any]:
                """Recursively build directory tree"""
                if current_depth >= max_depth:
                    return {"name": os.path.basename(path), "type": "directory", "truncated": True}
                
                items = []
                try:
                    for item in sorted(os.listdir(path)):
                        item_path = os.path.join(path, item)
                        
                        if os.path.isdir(item_path):
                            items.append(build_tree(item_path, current_depth + 1))
                        else:
                            file_stats = os.stat(item_path)
                            items.append({
                                "name": item,
                                "type": "file",
                                "size": file_stats.st_size
                            })
                except PermissionError:
                    items.append({"name": "Permission denied", "type": "error"})
                
                return {
                    "name": os.path.basename(path) or path,
                    "type": "directory",
                    "children": items
                }
            
            return {
                "directory_tree": build_tree(directory_path),
                "max_depth": max_depth
            }
            
        except Exception as e:
            logger.error(f"Error getting directory tree for {directory_path}: {str(e)}")
            return {"error": str(e)}
