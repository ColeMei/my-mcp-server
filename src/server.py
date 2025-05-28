"""Main MCP server entry point"""

import sys
import os
import asyncio
from pathlib import Path

# Add the src directory to Python path for absolute imports
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent, ImageContent, EmbeddedResource

# Import all tools and resources
from tools import DatabaseTools, APITools, FileTools, UtilityTools
from resources import DataResources, FileResources
from prompts import TemplatePrompts
from config.settings import get_settings
from utils.logging import setup_logging, get_logger

# Setup logging and configuration
setup_logging()
logger = get_logger(__name__)
settings = get_settings()

# Initialize MCP server
mcp = FastMCP(settings.server_name)

# Initialize tool and resource classes
db_tools = DatabaseTools()
api_tools = APITools()
file_tools = FileTools()
utility_tools = UtilityTools()
data_resources = DataResources()
file_resources = FileResources()
template_prompts = TemplatePrompts()

# ==================== TOOLS ====================

@mcp.tool()
def read_text_file(file_path: str) -> str:
    """Read content from a text file"""
    result = file_tools.read_text_file(file_path)
    return str(result)

@mcp.tool()
def read_csv_file(file_path: str, max_rows: int = 1000) -> str:
    """Read and analyze CSV file"""
    result = file_tools.read_csv_file(file_path, max_rows)
    return str(result)

@mcp.tool()
def write_text_file(file_path: str, content: str) -> str:
    """Write content to a text file"""
    result = file_tools.write_text_file(file_path, content)
    return str(result)

@mcp.tool()
def list_directory(directory_path: str) -> str:
    """List contents of a directory"""
    result = file_tools.list_directory(directory_path)
    return str(result)

@mcp.tool()
def make_api_request(url: str, method: str = "GET", data: dict = None, headers: dict = None) -> str:
    """Make HTTP request to external API"""
    if method.upper() == "GET":
        result = api_tools.make_get_request(url, headers)
    elif method.upper() == "POST":
        result = api_tools.make_post_request(url, data, headers)
    else:
        result = {"success": False, "error": "Unsupported HTTP method"}
    
    return str(result)

@mcp.tool()
def get_weather(city: str) -> str:
    """Get weather information for a city"""
    result = api_tools.fetch_weather_data(city)
    return str(result)

@mcp.tool()
def execute_sql_query(query: str, params: tuple = None) -> str:
    """Execute SQL query on the database"""
    result = db_tools.execute_query(query, params)
    return str(result)

@mcp.tool()
def create_note(title: str, content: str) -> str:
    """Create a new note in the database"""
    result = db_tools.create_note(title, content)
    return str(result)

@mcp.tool()
def get_notes(limit: int = 50) -> str:
    """Get all notes from the database"""
    result = db_tools.get_notes(limit)
    return str(result)

@mcp.tool()
def search_notes(search_term: str) -> str:
    """Search notes by title or content"""
    result = db_tools.search_notes(search_term)
    return str(result)

@mcp.tool()
def generate_hash(text: str, algorithm: str = "sha256") -> str:
    """Generate hash for given text"""
    result = utility_tools.generate_hash(text, algorithm)
    return str(result)

@mcp.tool()
def encode_base64(text: str) -> str:
    """Encode text to base64"""
    result = utility_tools.encode_decode_base64(text, "encode")
    return str(result)

@mcp.tool()
def decode_base64(text: str) -> str:
    """Decode base64 text"""
    result = utility_tools.encode_decode_base64(text, "decode")
    return str(result)

@mcp.tool()
def generate_password(length: int = 12, include_symbols: bool = True) -> str:
    """Generate a secure password"""
    result = utility_tools.generate_password(length, include_symbols)
    return str(result)

@mcp.tool()
def format_json(json_string: str, indent: int = 2) -> str:
    """Format JSON string"""
    result = utility_tools.format_json(json_string, indent)
    return str(result)

@mcp.tool()
def calculate_age(birth_date: str) -> str:
    """Calculate age from birth date (YYYY-MM-DD format)"""
    result = utility_tools.calculate_age(birth_date)
    return str(result)

# ==================== RESOURCES ====================

@mcp.resource("system://info")
def get_system_info() -> str:
    """Get system information"""
    result = data_resources.get_system_info()
    return str(result)

@mcp.resource("database://schema")  
def get_database_schema() -> str:
    """Get database schema information"""
    result = data_resources.get_database_schema()
    return str(result)

@mcp.resource("config://current")
def get_current_config() -> str:
    """Get current server configuration"""
    result = data_resources.get_configuration()
    return str(result)

@mcp.resource("file://{file_path}")
def get_file_info(file_path: str) -> str:
    """Get file information"""
    result = file_resources.get_file_info(file_path)
    return str(result)

@mcp.resource("directory://{directory_path}")
def get_directory_tree(directory_path: str) -> str:
    """Get directory tree structure"""
    result = file_resources.get_directory_tree(directory_path, 3)  # Default max_depth
    return str(result)

# ==================== PROMPTS ====================

@mcp.prompt("analyze_data")
def analyze_data_prompt(data_type: str = "csv") -> list[TextContent]:
    """Data analysis prompt template"""
    prompt = template_prompts.get_data_analysis_prompt(data_type)
    return [TextContent(type="text", text=prompt["template"])]

@mcp.prompt("summarize_file")
def summarize_file_prompt() -> list[TextContent]:
    """File summary prompt template"""
    prompt = template_prompts.get_file_summary_prompt()
    return [TextContent(type="text", text=prompt["template"])]

@mcp.prompt("analyze_api_response")
def analyze_api_response_prompt() -> list[TextContent]:
    """API response analysis prompt template"""
    prompt = template_prompts.get_api_response_analysis_prompt()
    return [TextContent(type="text", text=prompt["template"])]

@mcp.prompt("generate_code")
def generate_code_prompt() -> list[TextContent]:
    """Code generation prompt template"""
    prompt = template_prompts.get_code_generation_prompt()
    return [TextContent(type="text", text=prompt["template"])]

@mcp.prompt("solve_problem")
def solve_problem_prompt() -> list[TextContent]:
    """Problem solving prompt template"""
    prompt = template_prompts.get_problem_solving_prompt()
    return [TextContent(type="text", text=prompt["template"])]

# ==================== SERVER STARTUP ====================

def main():
    """Main server entry point"""
    logger.info(f"Starting {settings.server_name} v{settings.server_version}")
    logger.info(f"Debug mode: {settings.debug}")
    
    try:
        # Run the MCP server
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
