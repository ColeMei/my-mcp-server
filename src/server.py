"""Daily Workflow MCP Server - Focused on productivity and note management"""

import sys
import os
from pathlib import Path

# Add the src directory to Python path for absolute imports
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent
import json

# Import only the essential tools and resources
from tools import DatabaseTools, FileTools
from resources import DataResources, FileResources
from prompts import (
    get_analyze_notes_prompt,
    get_optimize_database_prompt,
    get_database_migration_prompt,
    get_analyze_project_prompt,
    get_code_review_prompt,
    get_refactor_project_prompt,
    get_file_organization_prompt
)
from config.settings import get_settings
from utils.logging import setup_logging, get_logger

# Setup logging and configuration
setup_logging()
logger = get_logger(__name__)
settings = get_settings()

# Initialize MCP server with a more personal name
mcp = FastMCP("Cole-Daily-MCP")

# Initialize essential tool and resource classes
db_tools = DatabaseTools()
file_tools = FileTools()
data_resources = DataResources()
file_resources = FileResources()

# ==================== NOTES & KNOWLEDGE MANAGEMENT ====================

@mcp.tool()
def quick_note(title: str, content: str) -> str:
    """Quickly save a note - your primary capture tool"""
    result = db_tools.create_note(title, content)
    return str(result)

@mcp.tool()
def find_notes(search_term: str) -> str:
    """Find notes by searching title or content"""
    result = db_tools.search_notes(search_term)
    return str(result)

@mcp.tool()
def recent_notes(limit: int = 10) -> str:
    """Get your most recent notes (default: last 10)"""
    result = db_tools.get_notes(limit)
    return str(result)

@mcp.tool()
def sql_query(query: str, params: tuple = None) -> str:
    """Execute custom SQL query on your notes database"""
    result = db_tools.execute_query(query, params)
    return str(result)

# ==================== FILE & PROJECT OPERATIONS ====================

@mcp.tool()
def read_file(file_path: str) -> str:
    """Read any text file in your workspace"""
    result = file_tools.read_text_file(file_path)
    return str(result)

@mcp.tool()
def save_file(file_path: str, content: str) -> str:
    """Save content to a file"""
    result = file_tools.write_text_file(file_path, content)
    return str(result)

@mcp.tool()
def explore_directory(directory_path: str) -> str:
    """Explore what's in a directory"""
    result = file_tools.list_directory(directory_path)
    return str(result)

@mcp.tool()
def analyze_csv(file_path: str, max_rows: int = 100) -> str:
    """Quick CSV analysis and preview"""
    result = file_tools.read_csv_file(file_path, max_rows)
    return str(result)

# ==================== SMART RESOURCES ====================

@mcp.resource("notes://schema")
def notes_database_info() -> str:
    """Your notes database structure and stats"""
    result = data_resources.get_database_schema()
    return str(result)

@mcp.resource("workspace://current")
def current_workspace() -> str:
    """Current workspace overview"""
    try:
        import os
        workspace_info = {
            "current_directory": os.getcwd(),
            "total_files": len([f for f in os.listdir('.') if os.path.isfile(f)]),
            "total_directories": len([d for d in os.listdir('.') if os.path.isdir(d)]),
            "workspace_type": "Daily Productivity Workspace"
        }
        return json.dumps(workspace_info, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})

@mcp.resource("system://status")
def system_status() -> str:
    """Quick system information"""
    result = data_resources.get_system_info()
    return str(result)

@mcp.resource("config://current")
def server_settings() -> str:
    """Current MCP server configuration"""
    result = data_resources.get_configuration()
    return str(result)

@mcp.resource("project://file/{file_path}")
def file_details(file_path: str) -> str:
    """Get detailed file information"""
    import urllib.parse
    decoded_path = urllib.parse.unquote(file_path)
    result = file_resources.get_file_info(decoded_path)
    return str(result)

# ==================== WORKFLOW PROMPTS ====================

@mcp.prompt("daily_review")
def daily_review_prompt(focus: str = "recent") -> list[TextContent]:
    """Review your recent notes and identify patterns"""
    template = get_analyze_notes_prompt(focus)
    return [TextContent(type="text", text=template)]

@mcp.prompt("project_cleanup")
def project_cleanup_prompt() -> list[TextContent]:
    """Organize and clean up your current project"""
    template = get_file_organization_prompt()
    return [TextContent(type="text", text=template)]

@mcp.prompt("code_review")
def code_review_prompt(language: str = "python") -> list[TextContent]:
    """Review code quality and suggest improvements"""
    template = get_code_review_prompt(language)
    return [TextContent(type="text", text=template)]

@mcp.prompt("knowledge_gaps")
def knowledge_gaps_prompt() -> list[TextContent]:
    """Identify gaps in your knowledge base"""
    template = get_analyze_project_prompt("knowledge")
    return [TextContent(type="text", text=template)]

# ==================== SERVER STARTUP ====================

def main():
    """Daily workflow MCP server entry point"""
    logger.info("🚀 Starting Cole's Daily Workflow MCP Server")
    logger.info("=== Streamlined for Productivity ===")
    logger.info("📝 NOTES: 4 tools (quick_note, find_notes, recent_notes, sql_query)")
    logger.info("📁 FILES: 4 tools (read_file, save_file, explore_directory, analyze_csv)") 
    logger.info("📊 RESOURCES: 5 resources (workspace, notes, system, config, file details)")
    logger.info("💡 PROMPTS: 4 workflows (daily_review, project_cleanup, code_review, knowledge_gaps)")
    logger.info("TOTAL: 8 tools, 5 resources, 4 prompts optimized for daily use")
    
    try:
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
