# src/prompts/database_prompts.py
"""Database-specific prompt templates and workflows"""

from mcp.types import TextContent

def get_analyze_notes_prompt(focus: str = "content") -> str:
    """Note analysis and insights prompt template"""
    return f"""
Analyze my notes database focusing on {focus}:

1. **Content Analysis**:
   - Identify common themes and topics
   - Find patterns in note-taking habits
   - Suggest organization improvements

2. **Usage Patterns**:
   - Most active time periods
   - Note length and complexity trends
   - Search query insights

3. **Actionable Insights**:
   - Notes that might need updating
   - Related notes that could be linked
   - Potential knowledge gaps

Please use the available database tools to gather information and provide detailed analysis.
"""

def get_optimize_database_prompt(table_name: str = "notes") -> str:
    """Database optimization and performance prompt"""
    return f"""
Optimize the {table_name} database:

1. **Schema Analysis**:
   - Review table structure and relationships
   - Identify missing indexes
   - Check for normalization opportunities

2. **Query Performance**:
   - Analyze slow queries
   - Suggest optimization strategies
   - Review query patterns

3. **Data Quality**:
   - Check for duplicate entries
   - Validate data consistency
   - Identify orphaned records

Use the database tools to examine the current state and provide specific recommendations.
"""

def get_database_migration_prompt() -> str:
    """Database migration and maintenance prompt"""
    return """
Plan database migration and maintenance:

1. **Migration Planning**:
   - Assess current schema version
   - Plan upgrade path
   - Identify breaking changes

2. **Data Backup**:
   - Create backup strategy
   - Verify backup integrity
   - Plan rollback procedures

3. **Maintenance Tasks**:
   - Vacuum and analyze tables
   - Update statistics
   - Clean up old data

Provide step-by-step migration plan with safety checks.
"""
