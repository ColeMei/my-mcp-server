# Daily Workflow Examples

This document shows how to use Cole's Daily Workflow MCP Server for common productivity tasks.

## 🚀 Quick Start

```bash
# Activate environment and start server
source mcp-env/bin/activate
mcp dev src/server.py
```

Then open http://127.0.0.1:6274 to use the MCP Inspector.

## 📝 Note Management Workflows

### 1. Quick Capture
Use `quick_note()` for rapid thought capture:
```
quick_note("Meeting Notes", "Discussed project timeline - deadline moved to June 15th")
quick_note("Learning", "Python asyncio - need to review event loops")
quick_note("Ideas", "MCP server for task management - integrate with calendar")
```

### 2. Find and Review
Search through your knowledge base:
```
find_notes("python")           # Find all Python-related notes
find_notes("deadline")         # Find deadline discussions
recent_notes(5)                # Get last 5 notes
```

### 3. Advanced Queries
Use SQL for complex analysis:
```
sql_query("SELECT title, created_at FROM notes WHERE content LIKE '%deadline%' ORDER BY created_at DESC")
sql_query("SELECT COUNT(*) as note_count, DATE(created_at) as date FROM notes GROUP BY DATE(created_at)")
```

## 📁 File Operations

### 1. Project Exploration
```
explore_directory(".")                    # See current project structure
explore_directory("src")                  # Explore source code
read_file("README.md")                    # Read documentation
```

### 2. Data Analysis
```
analyze_csv("data/analytics.csv")         # Quick CSV insights
read_file("logs/mcp_server_20250529.log") # Check recent logs
```

### 3. Content Management
```
save_file("notes/daily-review.md", "# Daily Review\n\n## Accomplishments\n- Streamlined MCP server\n")
read_file("notes/daily-review.md")
```

## 💡 Workflow Prompts

### 1. Daily Review
Use the `daily_review` prompt to analyze your recent notes and identify patterns:
- What themes are emerging?
- What needs follow-up?
- Are there knowledge gaps?

### 2. Project Cleanup
Use `project_cleanup` to organize your workspace:
- Remove unused files
- Improve directory structure
- Update documentation

### 3. Code Review
Use `code_review` for systematic code analysis:
- Check best practices
- Identify improvements
- Review security considerations

### 4. Knowledge Gaps
Use `knowledge_gaps` to identify learning opportunities:
- What topics appear frequently in notes?
- What areas need more research?
- Where are the documentation gaps?

## 📊 Resource Monitoring

### Workspace Overview
- `workspace://current` - See file counts and workspace type
- `notes://schema` - Review notes database structure
- `system://status` - Check system resources
- `config://current` - View current server settings

### File Analysis
- `project://file/README.md` - Get detailed file metadata
- `project://file/src/server.py` - Analyze source files

## 🔄 Daily Routine Integration

### Morning Setup
1. Check `recent_notes(10)` for yesterday's work
2. Use `daily_review` prompt to plan the day
3. Check `workspace://current` for workspace status

### During Work
1. Use `quick_note()` for rapid capture
2. Use `find_notes()` to reference previous work  
3. Use `save_file()` for documentation

### Evening Review
1. Use `daily_review` prompt to reflect on the day
2. Use `project_cleanup` to organize workspace
3. Capture tomorrow's priorities with `quick_note()`

## 🎯 Pro Tips

### 1. Note Naming Conventions
- **Ideas**: "Ideas - [topic]"
- **Meeting**: "Meeting - [date] - [subject]"
- **Learning**: "Learning - [technology/concept]"
- **Tasks**: "Tasks - [project] - [date]"

### 2. SQL Shortcuts
Common queries to save time:
```sql
-- Most recent notes
SELECT * FROM notes ORDER BY created_at DESC LIMIT 10;

-- Notes by keyword
SELECT * FROM notes WHERE content LIKE '%keyword%';

-- Daily note count
SELECT DATE(created_at), COUNT(*) FROM notes GROUP BY DATE(created_at);

-- Note length analysis
SELECT title, LENGTH(content) as length FROM notes ORDER BY length DESC;
```

### 3. File Organization
- Keep daily notes in `notes/` directory
- Use ISO date format: `YYYY-MM-DD-topic.md`
- Regular cleanup with `project_cleanup` prompt

### 4. Prompt Combinations
Use prompts in sequence:
1. `daily_review` → identify patterns
2. `knowledge_gaps` → find learning opportunities  
3. `project_cleanup` → organize findings
4. `code_review` → improve implementations

---

This streamlined MCP server is designed to get out of your way and enhance your natural workflow. Focus on capturing thoughts, organizing information, and building knowledge systematically.
