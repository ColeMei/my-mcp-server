"""Database operation tools"""

import sqlite3
import json
from typing import Any, Dict, List, Optional
from utils.logging import get_logger
from config.settings import get_settings

logger = get_logger(__name__)
settings = get_settings()

class DatabaseTools:
    """Database operation tools for MCP server"""
    
    def __init__(self, db_path: str = "data/app.db"):
        self.db_path = db_path
        self._ensure_db_exists()
    
    def _ensure_db_exists(self):
        """Ensure database and basic tables exist"""
        try:
            import os
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Create a sample table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS notes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        content TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                
                conn.commit()
                
        except Exception as e:
            logger.error(f"Error creating database: {str(e)}")
    
    def execute_query(self, query: str, params: Optional[tuple] = None) -> Dict[str, Any]:
        """
        Execute a SQL query
        
        Args:
            query: SQL query string
            params: Optional query parameters
            
        Returns:
            Dictionary with query results
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row  # Enable dict-like access
                cursor = conn.cursor()
                
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                # For SELECT queries, fetch results
                if query.strip().upper().startswith('SELECT'):
                    rows = cursor.fetchall()
                    return {
                        "success": True,
                        "data": [dict(row) for row in rows],
                        "count": len(rows)
                    }
                else:
                    # For INSERT, UPDATE, DELETE
                    conn.commit()
                    return {
                        "success": True,
                        "affected_rows": cursor.rowcount,
                        "last_row_id": cursor.lastrowid
                    }
                    
        except Exception as e:
            logger.error(f"Database query error: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def create_note(self, title: str, content: str) -> Dict[str, Any]:
        """
        Create a new note
        
        Args:
            title: Note title
            content: Note content
            
        Returns:
            Dictionary with creation result
        """
        query = "INSERT INTO notes (title, content) VALUES (?, ?)"
        return self.execute_query(query, (title, content))
    
    def get_notes(self, limit: int = 50) -> Dict[str, Any]:
        """
        Get all notes
        
        Args:
            limit: Maximum number of notes to return
            
        Returns:
            Dictionary with notes data
        """
        query = "SELECT * FROM notes ORDER BY created_at DESC LIMIT ?"
        return self.execute_query(query, (limit,))
    
    def search_notes(self, search_term: str) -> Dict[str, Any]:
        """
        Search notes by title or content
        
        Args:
            search_term: Term to search for
            
        Returns:
            Dictionary with search results
        """
        query = """
            SELECT * FROM notes 
            WHERE title LIKE ? OR content LIKE ? 
            ORDER BY created_at DESC
        """
        search_pattern = f"%{search_term}%"
        return self.execute_query(query, (search_pattern, search_pattern))
