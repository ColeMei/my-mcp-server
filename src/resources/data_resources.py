"""Data resource handlers"""

import json
from typing import Any, Dict
from utils.logging import get_logger
from tools.database_tools import DatabaseTools

logger = get_logger(__name__)

class DataResources:
    """Data resource handlers for MCP server"""
    
    def __init__(self):
        self.db_tools = DatabaseTools()
    
    def get_system_info(self) -> Dict[str, Any]:
        """Get system information resource"""
        try:
            import platform
            import psutil
            
            return {
                "system": {
                    "platform": platform.platform(),
                    "python_version": platform.python_version(),
                    "cpu_count": psutil.cpu_count(),
                    "memory_total": psutil.virtual_memory().total,
                    "disk_usage": {
                        "total": psutil.disk_usage('/').total,
                        "used": psutil.disk_usage('/').used,
                        "free": psutil.disk_usage('/').free
                    }
                }
            }
        except ImportError:
            return {
                "system": {
                    "platform": "Unknown",
                    "python_version": "Unknown",
                    "note": "Install psutil for detailed system information"
                }
            }
        except Exception as e:
            logger.error(f"Error getting system info: {str(e)}")
            return {"error": str(e)}
    
    def get_database_schema(self) -> Dict[str, Any]:
        """Get database schema information"""
        try:
            query = """
                SELECT name, sql 
                FROM sqlite_master 
                WHERE type='table' AND name NOT LIKE 'sqlite_%'
            """
            result = self.db_tools.execute_query(query)
            
            if result["success"]:
                return {
                    "schema": result["data"],
                    "table_count": result["count"]
                }
            else:
                return {"error": result["error"]}
                
        except Exception as e:
            logger.error(f"Error getting database schema: {str(e)}")
            return {"error": str(e)}
    
    def get_configuration(self) -> Dict[str, Any]:
        """Get current server configuration"""
        try:
            # Fix: Use absolute import instead of relative
            import sys
            import os
            
            # Add the parent directory to path if needed
            current_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(current_dir)
            if parent_dir not in sys.path:
                sys.path.insert(0, parent_dir)
                
            from config.settings import get_settings  # ✅ Absolute import
            
            settings = get_settings()
            return {
                "server_name": settings.server_name,
                "server_version": settings.server_version,
                "debug": settings.debug,
                "log_level": settings.log_level,
                "api_timeout": settings.api_timeout,
                "max_file_size": settings.max_file_size
            }
        except Exception as e:
            logger.error(f"Error getting configuration: {str(e)}")
            return {"error": str(e)}

