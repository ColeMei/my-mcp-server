"""Template prompts for MCP server"""

from typing import Dict, List, Any
from utils.logging import get_logger

logger = get_logger(__name__)

class TemplatePrompts:
    """Template prompts for various tasks"""
    
    @staticmethod
    def get_data_analysis_prompt(data_type: str = "csv") -> Dict[str, Any]:
        """Get data analysis prompt template"""
        return {
            "name": "analyze_data",
            "description": f"Analyze {data_type} data and provide insights",
            "template": """
Please analyze the following {data_type} data:

{data}

Provide the following analysis:
1. Data overview (rows, columns, data types)
2. Key statistics and patterns
3. Data quality assessment
4. Insights and recommendations
5. Potential issues or anomalies

Format your response in a clear, structured manner.
            """.strip(),
            "variables": ["data_type", "data"]
        }
    
    @staticmethod
    def get_file_summary_prompt() -> Dict[str, Any]:
        """Get file content summary prompt template"""
        return {
            "name": "summarize_file",
            "description": "Summarize file content",
            "template": """
Please provide a comprehensive summary of the following file:

File: {file_path}
Content:
{content}

Include:
1. File type and structure
2. Main topics or themes
3. Key information
4. Length and complexity
5. Notable patterns or features

Keep the summary concise but informative.
            """.strip(),
            "variables": ["file_path", "content"]
        }
    
    @staticmethod
    def get_api_response_analysis_prompt() -> Dict[str, Any]:
        """Get API response analysis prompt template"""
        return {
            "name": "analyze_api_response",
            "description": "Analyze API response data",
            "template": """
Analyze the following API response:

Endpoint: {url}
Status Code: {status_code}
Response Data:
{response_data}

Please provide:
1. Response structure analysis
2. Data quality assessment
3. Key information extracted
4. Potential issues or errors
5. Suggestions for data usage

Format your analysis clearly and highlight important findings.
            """.strip(),
            "variables": ["url", "status_code", "response_data"]
        }
    
    @staticmethod
    def get_code_generation_prompt() -> Dict[str, Any]:
        """Get code generation prompt template"""
        return {
            "name": "generate_code",
            "description": "Generate code based on requirements",
            "template": """
Generate {language} code for the following requirements:

Task: {task_description}

Requirements:
{requirements}

Please provide:
1. Clean, well-commented code
2. Error handling where appropriate
3. Usage examples
4. Any dependencies or setup instructions

Ensure the code follows best practices and is production-ready.
            """.strip(),
            "variables": ["language", "task_description", "requirements"]
        }
    
    @staticmethod
    def get_problem_solving_prompt() -> Dict[str, Any]:
        """Get problem solving prompt template"""
        return {
            "name": "solve_problem",
            "description": "Systematic problem solving approach",
            "template": """
Help solve the following problem using a systematic approach:

Problem: {problem_description}

Context:
{context}

Please follow this structure:
1. Problem Understanding
   - Restate the problem clearly
   - Identify key constraints and requirements

2. Analysis
   - Break down the problem into components
   - Identify relevant information and data

3. Solution Approach
   - Propose potential solutions
   - Evaluate pros and cons of each approach

4. Recommended Solution
   - Provide detailed solution with steps
   - Include implementation considerations

5. Validation
   - How to verify the solution works
   - Potential risks and mitigation strategies
            """.strip(),
            "variables": ["problem_description", "context"]
        }
    
    @staticmethod
    def list_available_prompts() -> List[Dict[str, str]]:
        """List all available prompt templates"""
        return [
            {
                "name": "analyze_data",
                "description": "Analyze data and provide insights"
            },
            {
                "name": "summarize_file", 
                "description": "Summarize file content"
            },
            {
                "name": "analyze_api_response",
                "description": "Analyze API response data"
            },
            {
                "name": "generate_code",
                "description": "Generate code based on requirements"
            },
            {
                "name": "solve_problem",
                "description": "Systematic problem solving approach"
            }
        ]
