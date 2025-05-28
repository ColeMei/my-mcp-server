"""General utility tools"""

import hashlib
import base64
import json
import random
import string
from datetime import datetime, timedelta
from typing import Any, Dict, List
from utils.logging import get_logger

logger = get_logger(__name__)

class UtilityTools:
    """General utility tools for MCP server"""
    
    @staticmethod
    def generate_hash(text: str, algorithm: str = "sha256") -> Dict[str, Any]:
        """
        Generate hash for given text
        
        Args:
            text: Text to hash
            algorithm: Hash algorithm (md5, sha1, sha256, sha512)
            
        Returns:
            Dictionary with hash result
        """
        try:
            algorithms = {
                "md5": hashlib.md5,
                "sha1": hashlib.sha1,
                "sha256": hashlib.sha256,
                "sha512": hashlib.sha512
            }
            
            if algorithm not in algorithms:
                return {"success": False, "error": f"Unsupported algorithm: {algorithm}"}
            
            hash_func = algorithms[algorithm]()
            hash_func.update(text.encode('utf-8'))
            
            return {
                "success": True,
                "algorithm": algorithm,
                "input_text": text,
                "hash": hash_func.hexdigest()
            }
            
        except Exception as e:
            logger.error(f"Error generating hash: {str(e)}")
            return {"success": False, "error": str(e)}
    
    @staticmethod
    def encode_decode_base64(text: str, operation: str = "encode") -> Dict[str, Any]:
        """
        Encode or decode base64
        
        Args:
            text: Text to encode/decode
            operation: "encode" or "decode"
            
        Returns:
            Dictionary with operation result
        """
        try:
            if operation == "encode":
                encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
                return {
                    "success": True,
                    "operation": "encode",
                    "input": text,
                    "result": encoded
                }
            elif operation == "decode":
                decoded = base64.b64decode(text.encode('utf-8')).decode('utf-8')
                return {
                    "success": True,
                    "operation": "decode",
                    "input": text,
                    "result": decoded
                }
            else:
                return {"success": False, "error": "Operation must be 'encode' or 'decode'"}
                
        except Exception as e:
            logger.error(f"Error in base64 operation: {str(e)}")
            return {"success": False, "error": str(e)}
    
    @staticmethod
    def generate_password(length: int = 12, include_symbols: bool = True) -> Dict[str, Any]:
        """
        Generate a secure password
        
        Args:
            length: Password length
            include_symbols: Whether to include symbols
            
        Returns:
            Dictionary with generated password
        """
        try:
            characters = string.ascii_letters + string.digits
            if include_symbols:
                characters += "!@#$%^&*"
            
            password = ''.join(random.choice(characters) for _ in range(length))
            
            return {
                "success": True,
                "password": password,
                "length": length,
                "includes_symbols": include_symbols
            }
            
        except Exception as e:
            logger.error(f"Error generating password: {str(e)}")
            return {"success": False, "error": str(e)}
    
    @staticmethod
    def format_json(json_string: str, indent: int = 2) -> Dict[str, Any]:
        """
        Format JSON string
        
        Args:
            json_string: JSON string to format
            indent: Indentation level
            
        Returns:
            Dictionary with formatted JSON
        """
        try:
            parsed = json.loads(json_string)
            formatted = json.dumps(parsed, indent=indent, sort_keys=True)
            
            return {
                "success": True,
                "formatted_json": formatted,
                "is_valid": True
            }
            
        except json.JSONDecodeError as e:
            return {
                "success": False,
                "error": f"Invalid JSON: {str(e)}",
                "is_valid": False
            }
        except Exception as e:
            logger.error(f"Error formatting JSON: {str(e)}")
            return {"success": False, "error": str(e)}
    
    @staticmethod
    def calculate_age(birth_date: str) -> Dict[str, Any]:
        """
        Calculate age from birth date
        
        Args:
            birth_date: Birth date in YYYY-MM-DD format
            
        Returns:
            Dictionary with age calculation
        """
        try:
            birth = datetime.strptime(birth_date, "%Y-%m-%d")
            today = datetime.now()
            age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
            
            return {
                "success": True,
                "birth_date": birth_date,
                "current_date": today.strftime("%Y-%m-%d"),
                "age_years": age,
                "days_lived": (today - birth).days
            }
            
        except ValueError as e:
            return {"success": False, "error": "Invalid date format. Use YYYY-MM-DD"}
        except Exception as e:
            logger.error(f"Error calculating age: {str(e)}")
            return {"success": False, "error": str(e)}
