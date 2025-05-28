import os
from mcp.server.fastmcp import FastMCP
from src.config.settings import get_settings
from src.tools import register_all_tools
from src.resources import register_all_resources
from src.prompts import register_all_prompts
from src.utils.logging import setup_logging

# Initialize logging
setup_logging()

# Load configuration
settings = get_settings()

# Initialize MCP server
mcp = FastMCP(
    name=settings.server_name,
    version=settings.server_version
)

# Register all components
register_all_tools(mcp)
register_all_resources(mcp)
register_all_prompts(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
