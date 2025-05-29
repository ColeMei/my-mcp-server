# src/prompts/file_prompts.py
"""File and project-specific prompt templates and workflows"""

from mcp.types import TextContent

def get_analyze_project_prompt(focus: str = "structure") -> str:
    """Project analysis and organization prompt template"""
    return f"""
Analyze the current project focusing on {focus}:

1. **Project Structure**:
   - Review directory organization
   - Identify key files and their purposes
   - Check for standard project files (README, requirements, etc.)

2. **Code Quality**:
   - Look for consistent naming patterns
   - Check file sizes and complexity
   - Identify potential refactoring opportunities

3. **Documentation**:
   - Assess documentation completeness
   - Find missing or outdated docs
   - Suggest documentation improvements

Use the available file tools to gather information and provide actionable insights.
"""

def get_code_review_prompt(language: str = "python") -> str:
    """Code review and analysis prompt"""
    return f"""
Perform comprehensive {language} code review:

1. **Code Quality**:
   - Check {language}-specific best practices
   - Identify potential bugs and issues
   - Review error handling

2. **Performance**:
   - Look for performance bottlenecks
   - Suggest optimization opportunities
   - Check resource usage patterns

3. **Maintainability**:
   - Assess code readability
   - Check for code duplication
   - Review naming conventions

4. **Security**:
   - Identify security vulnerabilities
   - Check input validation
   - Review access controls

Provide specific, actionable feedback with examples.
"""

def get_refactor_project_prompt() -> str:
    """Project refactoring and cleanup prompt"""
    return """
Plan project refactoring and cleanup:

1. **Structure Improvement**:
   - Reorganize files and directories
   - Improve module separation
   - Clean up import dependencies

2. **Code Cleanup**:
   - Remove unused code and files
   - Consolidate duplicate functionality
   - Improve naming consistency

3. **Documentation Update**:
   - Update outdated documentation
   - Add missing docstrings
   - Improve README and setup instructions

4. **Dependency Management**:
   - Review and update dependencies
   - Remove unused packages
   - Check for security vulnerabilities

Provide a prioritized refactoring plan with clear steps.
"""

def get_file_organization_prompt() -> str:
    """File organization and management prompt"""
    return """
Organize and manage project files:

1. **File Structure Analysis**:
   - Review current organization
   - Identify misplaced files
   - Check naming conventions

2. **Cleanup Opportunities**:
   - Find temporary and backup files
   - Identify large or unused files
   - Check for duplicate content

3. **Organization Strategy**:
   - Suggest better directory structure
   - Recommend file naming patterns
   - Plan archive and cleanup process

Use file tools to analyze current state and provide specific organization recommendations.
"""
