# My MCP Server

A comprehensive **Model Context Protocol (MCP)** server with modular architecture supporting file operations, database queries, API integrations, and utility functions. Built with Python using the FastMCP library and following MCP protocol standards.

## 🚀 Project Status

✅ **COMPLETED** - Fully functional MCP server with:
- 12 working tools across 4 categories
- 5 resource handlers for metadata access  
- 5 prompt templates for AI interactions
- Comprehensive logging and configuration
- SQLite database integration
- Modular, extensible architecture

## 🌟 Features

### 📁 **File Operations**
- Read/write text files with validation
- CSV file analysis with pandas integration
- Directory tree traversal and listing
- File metadata and information access

### 🗄️ **Database Tools** 
- SQLite integration with automatic schema creation
- Note management system (CRUD operations)
- SQL query execution with parameter binding
- Database schema introspection

### 🌐 **API Integration**
- HTTP GET/POST request handling
- Weather data fetching (example integration)
- Configurable timeout and error handling
- JSON response formatting

### 🔧 **Utility Functions**
- Cryptographic hash generation (MD5, SHA256, SHA512)
- Base64 encoding/decoding
- Secure password generation
- JSON formatting and validation
- Age calculation from birth date

### 📊 **Resource Handlers**
- System information access
- Database schema metadata
- Server configuration details
- File and directory metadata
- Real-time resource updates

### 💭 **AI Prompt Templates**
- Data analysis workflows
- File summarization prompts
- API response analysis
- Code generation templates
- Problem-solving frameworks

## 🏗️ Architecture

The server follows a **clean, modular architecture** with clear separation of concerns:

```
src/
├── server.py              # Main MCP server entry point & FastMCP setup
├── config/
│   ├── __init__.py
│   └── settings.py         # Pydantic settings with env variable support
├── tools/                  # Business logic implementations
│   ├── __init__.py
│   ├── database_tools.py   # SQLite operations & note management
│   ├── api_tools.py        # HTTP requests & external API calls
│   ├── file_tools.py       # File system operations & CSV analysis
│   └── utility_tools.py    # Hash, encoding, password generation
├── resources/              # Metadata & system information handlers
│   ├── __init__.py
│   ├── data_resources.py   # System info, DB schema, configuration
│   └── file_resources.py   # File metadata & directory trees
├── prompts/                # AI interaction templates
│   ├── __init__.py
│   └── template_prompts.py # Reusable prompt templates
└── utils/                  # Shared utilities
    ├── __init__.py
    ├── logging.py          # Centralized logging configuration
    └── validators.py       # Input validation & security
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+ 
- Virtual environment (recommended)

### Setup Instructions

1. **Clone and navigate to project**
   ```bash
   cd my-mcp-server
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv mcp-env
   source mcp-env/bin/activate  # Linux/Mac
   # mcp-env\Scripts\activate   # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Test with MCP Inspector**
   ```bash
   mcp dev src/server.py
   ```
   The inspector will open at `http://127.0.0.1:6274` 🎉

5. **Environment Configuration (Optional)**
   Create `.env` file:
   ```env
   SERVER_NAME=MyMCPServer
   DEBUG=false
   LOG_LEVEL=INFO
   API_TIMEOUT=30
   MAX_FILE_SIZE=10485760
   ```

## 🛠️ Available Tools (12 total)

### File Operations
- `read_text_file(file_path: str)` - Read text file content
- `read_csv_file(file_path: str, max_rows: int = 1000)` - Analyze CSV with pandas
- `write_text_file(file_path: str, content: str)` - Write text to file
- `list_directory(directory_path: str)` - List directory contents

### Database Operations  
- `execute_sql_query(query: str, params: tuple = None)` - Execute SQL with parameters
- `create_note(title: str, content: str)` - Create new note
- `get_notes(limit: int = 50)` - Retrieve notes with pagination
- `search_notes(search_term: str)` - Full-text note search

### API & Network
- `make_api_request(url: str, method: str = "GET", data: dict = None, headers: dict = None)` - HTTP requests
- `get_weather(city: str)` - Weather data (example API integration)

### Utilities
- `generate_hash(text: str, algorithm: str = "sha256")` - Cryptographic hashing
- `encode_base64(text: str)` / `decode_base64(text: str)` - Base64 operations
- `generate_password(length: int = 12, include_symbols: bool = True)` - Secure passwords
- `format_json(json_string: str, indent: int = 2)` - JSON formatting
- `calculate_age(birth_date: str)` - Age calculation (YYYY-MM-DD format)

## 📊 Available Resources (5 total)

- `system://info` - System information (OS, Python version, etc.)
- `database://schema` - Database schema and table information
- `config://current` - Current server configuration
- `file://{file_path}` - File metadata (size, modified date, etc.)
- `directory://{directory_path}` - Directory tree structure

## 💭 Available Prompts (5 total)

- `analyze_data(data_type: str = "csv")` - Data analysis workflow templates
- `summarize_file()` - File content summarization prompts
- `analyze_api_response()` - API response analysis templates
- `generate_code()` - Code generation prompts
- `solve_problem()` - Problem-solving framework prompts

## 🔧 Configuration

The server uses **Pydantic settings** with environment variable support:

| Setting | Default | Environment Variable | Description |
|---------|---------|---------------------|-------------|
| `server_name` | "MyMCPServer" | `SERVER_NAME` | Server identifier |
| `debug` | `false` | `DEBUG` | Debug mode toggle |
| `log_level` | "INFO" | `LOG_LEVEL` | Logging verbosity |
| `api_timeout` | 30 | `API_TIMEOUT` | HTTP request timeout |
| `max_file_size` | 10MB | `MAX_FILE_SIZE` | Maximum file size |

## 🗂️ Data Management

- **Database**: SQLite stored in `data/app.db`
- **Logs**: Rotating daily logs in `logs/` directory  
- **Configuration**: `.env` file support for environment variables

## 🧪 Testing & Development

### Using MCP Inspector
The MCP Inspector provides a web interface to:
- Browse and test all available tools
- View resource schemas and live data
- Test prompt templates
- Monitor server logs in real-time
- Debug protocol communication

### Adding New Features

1. **New Tool**: Add to appropriate `tools/*.py` file and register in `server.py`
2. **New Resource**: Add to `resources/*.py` and register with URI template
3. **New Prompt**: Add to `prompts/template_prompts.py` and register in `server.py`

## 📦 Dependencies

- `mcp>=1.0.0` - Model Context Protocol core
- `fastapi>=0.104.0` - FastAPI framework (used by FastMCP)
- `uvicorn>=0.24.0` - ASGI server
- `python-dotenv>=1.0.0` - Environment variable loading
- `pandas>=2.0.0` - Data analysis for CSV operations
- `requests>=2.31.0` - HTTP client library
- `aiofiles>=23.0.0` - Async file operations
- `pydantic>=2.0.0` - Data validation and settings

## 🤝 Integration

This MCP server can be integrated with:
- **Claude Desktop** - Add to `claude_desktop_config.json`
- **Custom AI Applications** - Use as MCP protocol server
- **Development Tools** - Via MCP Inspector for testing

Example Claude Desktop configuration:
```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "uv",
      "args": ["run", "--with", "mcp", "mcp", "run", "src/server.py"],
      "cwd": "/path/to/my-mcp-server"
    }
  }
}
```

## 🔍 Troubleshooting

### Common Issues
- **Import Errors**: Ensure virtual environment is activated
- **Permission Errors**: Check file/directory permissions for `data/` and `logs/`
- **Port Conflicts**: MCP Inspector uses ports 6274 and 6277

### Debugging
- Set `DEBUG=true` in `.env` for verbose logging
- Check `logs/mcp_server_*.log` for detailed error information  
- Use MCP Inspector's real-time monitoring

## 📈 Performance Notes

- **File Operations**: Validated for files up to 10MB (configurable)
- **Database**: SQLite with connection pooling for concurrent access
- **API Requests**: 30-second timeout with retry logic
- **Memory**: Efficient streaming for large file operations

---

**Built with ❤️ using the Model Context Protocol** | [MCP Documentation](https://docs.modelcontextprotocol.ai/)
