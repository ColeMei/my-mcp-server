"""File system operation tools"""

import os
import json
import pandas as pd
from typing import Any, Dict, List
from utils.logging import get_logger
from utils.validators import validate_file_path
from config.settings import get_settings

logger = get_logger(__name__)
settings = get_settings()

class FileTools:
    """File operation tools for MCP server"""
    
    @staticmethod
    def read_text_file(file_path: str) -> Dict[str, Any]:
        """
        Read content from a text file
        
        Args:
            file_path: Path to the text file
            
        Returns:
            Dictionary with file content and metadata
        """
        try:
            is_valid, error = validate_file_path(file_path)
            if not is_valid:
                return {"success": False, "error": error}
            
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
            file_stats = os.stat(file_path)
            
            return {
                "success": True,
                "content": content,
                "file_size": file_stats.st_size,
                "lines": len(content.splitlines()),
                "file_path": file_path
            }
            
        except Exception as e:
            logger.error(f"Error reading text file {file_path}: {str(e)}")
            return {"success": False, "error": str(e)}
    
    @staticmethod
    def read_csv_file(file_path: str, max_rows: int = 1000) -> Dict[str, Any]:
        """
        Read and analyze CSV file
        
        Args:
            file_path: Path to CSV file
            max_rows: Maximum rows to read
            
        Returns:
            Dictionary with CSV data and analysis
        """
        try:
            is_valid, error = validate_file_path(file_path)
            if not is_valid:
                return {"success": False, "error": error}
            
            # Read CSV with pandas
            df = pd.read_csv(file_path, nrows=max_rows)
            
            return {
                "success": True,
                "rows": len(df),
                "columns": len(df.columns),
                "column_names": df.columns.tolist(),
                "data_types": df.dtypes.to_dict(),
                "sample_data": df.head().to_dict('records'),
                "file_path": file_path
            }
            
        except Exception as e:
            logger.error(f"Error reading CSV file {file_path}: {str(e)}")
            return {"success": False, "error": str(e)}
    
    @staticmethod
    def write_text_file(file_path: str, content: str) -> Dict[str, Any]:
        """
        Write content to a text file
        
        Args:
            file_path: Path to write the file
            content: Content to write
            
        Returns:
            Dictionary with operation result
        """
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            logger.info(f"Successfully wrote file: {file_path}")
            return {
                "success": True,
                "message": f"File written successfully: {file_path}",
                "bytes_written": len(content.encode('utf-8'))
            }
            
        except Exception as e:
            logger.error(f"Error writing file {file_path}: {str(e)}")
            return {"success": False, "error": str(e)}
    
    @staticmethod
    def list_directory(directory_path: str) -> Dict[str, Any]:
        """
        List contents of a directory
        
        Args:
            directory_path: Path to directory
            
        Returns:
            Dictionary with directory contents
        """
        try:
            if not os.path.exists(directory_path):
                return {"success": False, "error": "Directory does not exist"}
            
            if not os.path.isdir(directory_path):
                return {"success": False, "error": "Path is not a directory"}
            
            items = []
            for item in os.listdir(directory_path):
                item_path = os.path.join(directory_path, item)
                item_stats = os.stat(item_path)
                
                items.append({
                    "name": item,
                    "type": "directory" if os.path.isdir(item_path) else "file",
                    "size": item_stats.st_size,
                    "modified": item_stats.st_mtime
                })
            
            return {
                "success": True,
                "directory": directory_path,
                "items": items,
                "total_items": len(items)
            }
            
        except Exception as e:
            logger.error(f"Error listing directory {directory_path}: {str(e)}")
            return {"success": False, "error": str(e)}
