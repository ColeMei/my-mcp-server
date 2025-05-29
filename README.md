# Cole's Daily Workflow MCP Server

A **streamlined Model Context Protocol (MCP)** server focused on daily productivity workflows. Optimized for note management, file operations, and knowledge capture using Python with the FastMCP library.

## 🚀 Project Status

✅ **STREAMLINED & FOCUSED** - Daily workflow optimized MCP server with:
- 8 essential tools for notes and files
- 5 smart resources for workspace insights  
- 4 workflow prompts for productivity
- SQLite-based note management
- Clean, minimal architecture

## 🎯 Core Philosophy

**Less is More**: This server focuses on the 20% of features you use 80% of the time:
- Quick note capture and search
- File operations for your workspace
- Smart prompts for daily workflows
- No API distractions or unused utilities

## 🌟 Features

### 📝 **Notes & Knowledge Management**
- Quick note capture with `quick_note()`
- Intelligent note search with `find_notes()`
- Recent notes access with `recent_notes()`
- Custom SQL queries with `sql_query()`

### 📁 **File & Project Operations** 
- Read any text file with `read_file()`
- Save content with `save_file()`
- Directory exploration with `explore_directory()`
- CSV analysis with `analyze_csv()`

### 📊 **Smart Resources**
- Workspace overview and statistics
- Notes database schema and insights
- System status monitoring
- File metadata access
- Configuration management

### 💡 **Workflow Prompts**
- Daily review and note analysis
- Project cleanup and organization
- Code review workflows
- Knowledge gap identification

## 🏗️ Architecture

The server follows a **clean, modular architecture** with clear separation of concerns:

```
my-mcp-server/
├── .env.example        # Environment configuration template
├── .gitignore          # Git ignore rules
├── README.md           # Documentation
├── requirements.txt    # Python dependencies
├── setup_dev.sh        # One-command setup script (source it!)
├── data/               # SQLite database (auto-created)
├── logs/               # Application logs (auto-created)
├── mcp-env/            # Virtual environment (auto-created)
├── tests/              # Test suite
│   └── test_server.py  # Functionality verification tests
└── src/                # Main source code
    ├── server.py       # Main MCP server (streamlined & focused)
    ├── config/         # Configuration & settings
    ├── tools/          # Core business logic (database & file tools)
    ├── resources/      # System information & metadata handlers
    ├── prompts/        # Daily workflow templates
    └── utils/          # Shared utilities (logging, validation)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+ 
- macOS/Linux (zsh/bash shell)

### One-Command Setup ⚡

```bash
source ./setup_dev.sh
```

This single command will:
- ✅ Create virtual environment
- ✅ Activate it in your current shell
- ✅ Install all dependencies
- ✅ Create necessary directories
- ✅ Clean up cache files

> **Important**: Use `source ./setup_dev.sh` (not `./setup_dev.sh`) to ensure the virtual environment stays activated in your current shell.

### Run the Server

```bash
mcp dev src/server.py
```
The MCP Inspector will open at `http://127.0.0.1:6274` 🎉

### Environment Configuration (Optional)

Copy `.env.example` to `.env` and customize:
```bash
cp .env.example .env
```

Example configuration:
```env
SERVER_NAME=MyMCPServer
DEBUG=false
LOG_LEVEL=INFO
API_TIMEOUT=30
MAX_FILE_SIZE=10485760
```

## 🛠️ Available Tools (8 total)

### 📝 Note Management
- `quick_note(title: str, content: str)` - Quickly capture thoughts and ideas
- `find_notes(search_term: str)` - Search through your notes
- `recent_notes(limit: int = 10)` - Get your most recent notes
- `sql_query(query: str, params: tuple = None)` - Custom database queries

### 📁 File Operations  
- `read_file(file_path: str)` - Read any text file
- `save_file(file_path: str, content: str)` - Save content to file
- `explore_directory(directory_path: str)` - Browse directory contents
- `analyze_csv(file_path: str, max_rows: int = 100)` - Quick CSV analysis

## 📊 Available Resources (5 total)

- `notes://schema` - Notes database structure and statistics
- `workspace://current` - Current workspace overview and file counts
- `system://status` - System information (OS, Python version, etc.)
- `config://current` - Current server configuration
- `project://file/{file_path}` - Detailed file metadata and information

## 💡 Available Workflow Prompts (4 total)

- `daily_review(focus: str = "recent")` - Review and analyze your recent notes
- `project_cleanup()` - Organize and clean up your current project  
- `code_review(language: str = "python")` - Review code quality and best practices
- `knowledge_gaps()` - Identify gaps in your knowledge base

## 🔧 Configuration

The server uses **Pydantic settings** with environment variable support:

| Setting | Default | Environment Variable | Description |
|---------|---------|---------------------|-------------|
| `server_name` | "Cole-Daily-MCP" | `SERVER_NAME` | Server identifier |
| `debug` | `false` | `DEBUG` | Debug mode toggle |
| `log_level` | "INFO" | `LOG_LEVEL` | Logging verbosity |
| `api_timeout` | 30 | `API_TIMEOUT` | Request timeout (future use) |
| `max_file_size` | 10MB | `MAX_FILE_SIZE` | Maximum file size |

## 🗂️ Data Management

- **Notes Database**: SQLite stored in `data/app.db` with automatic schema creation
- **Logs**: Daily rotating logs in `logs/` directory for debugging
- **Configuration**: `.env` file support for personalized settings

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

See in `requirements.txt`

## 🤝 Integration

This MCP server can be integrated with:
- **Claude Desktop** - Add to `claude_desktop_config.json`
- **Custom AI Applications** - Use as MCP protocol server
- **Development Tools** - Via MCP Inspector for testing, like Cursor, VSCode

Example Claude Desktop configuration:
```json
{
  "mcpServers": {
    "cole-daily-mcp": {
      "command": "uv",
      "args": ["run", "--with", "mcp", "mcp", "run", "src/server.py"],
      "cwd": "/path/to/my-mcp-server"
    }
  }
}
```

## 📈 Performance Notes

- **File Operations**: Optimized for files up to 10MB
- **Database**: SQLite with efficient indexing for note searches
- **Memory**: Lightweight design focused on essential operations only
- **Startup**: Fast initialization with minimal dependencies

## 🎯 What's Different?

This streamlined version focuses on:

✅ **Essential Tools Only**: 8 carefully chosen tools for daily productivity
✅ **Intuitive Naming**: `quick_note()` instead of `create_note()`  
✅ **Workflow-Focused**: Prompts designed for actual daily use
✅ **Reduced Complexity**: Removed unused API and utility tools
✅ **Better Defaults**: Sensible limits and configurations
✅ **Clear Purpose**: Note management + file operations = productivity

## 📚 Additional Resources

- **WORKFLOW_EXAMPLES.md** - Practical usage examples and daily routine integration
- **MCP Inspector** - Web interface for testing and development at http://127.0.0.1:6274
- **Logs** - Daily logs in `logs/` directory for troubleshooting

---

**Built for daily productivity** | [MCP Documentation](https://modelcontextprotocol.io/introduction)
