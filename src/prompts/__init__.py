"""Prompts module for MCP server"""

from prompts.database_prompts import (
    get_analyze_notes_prompt,
    get_optimize_database_prompt,
    get_database_migration_prompt
)

from prompts.file_prompts import (
    get_analyze_project_prompt,
    get_code_review_prompt,
    get_refactor_project_prompt,
    get_file_organization_prompt
)

__all__ = ["get_analyze_notes_prompt", "get_optimize_database_prompt", "get_database_migration_prompt", "get_analyze_project_prompt", "get_code_review_prompt", "get_refactor_project_prompt", "get_file_organization_prompt"]
