"""External API integration tools"""

import requests
import json
from typing import Any, Dict, Optional
from utils.logging import get_logger
from config.settings import get_settings

logger = get_logger(__name__)
settings = get_settings()

class APITools:
    """API integration tools for MCP server"""
    
    @staticmethod
    def make_get_request(url: str, headers: Optional[Dict[str, str]] = None, 
                        params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make a GET request to an external API
        
        Args:
            url: API endpoint URL
            headers: Optional request headers
            params: Optional query parameters
            
        Returns:
            Dictionary with API response
        """
        try:
            response = requests.get(
                url=url,
                headers=headers or {},
                params=params or {},
                timeout=settings.api_timeout
            )
            
            return {
                "success": True,
                "status_code": response.status_code,
                "data": response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text,
                "headers": dict(response.headers)
            }
            
        except requests.RequestException as e:
            logger.error(f"GET request failed for {url}: {str(e)}")
            return {"success": False, "error": str(e)}
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error for {url}: {str(e)}")
            return {"success": False, "error": "Invalid JSON response"}
    
    @staticmethod
    def make_post_request(url: str, data: Optional[Dict[str, Any]] = None,
                         headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Make a POST request to an external API
        
        Args:
            url: API endpoint URL
            data: Request payload
            headers: Optional request headers
            
        Returns:
            Dictionary with API response
        """
        try:
            response = requests.post(
                url=url,
                json=data,
                headers=headers or {"Content-Type": "application/json"},
                timeout=settings.api_timeout
            )
            
            return {
                "success": True,
                "status_code": response.status_code,
                "data": response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text,
                "headers": dict(response.headers)
            }
            
        except requests.RequestException as e:
            logger.error(f"POST request failed for {url}: {str(e)}")
            return {"success": False, "error": str(e)}
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error for {url}: {str(e)}")
            return {"success": False, "error": "Invalid JSON response"}
    
    @staticmethod
    def fetch_weather_data(city: str) -> Dict[str, Any]:
        """
        Fetch weather data for a city (example API integration)
        
        Args:
            city: City name
            
        Returns:
            Dictionary with weather information
        """
        try:
            # This is a mock implementation - replace with actual weather API
            base_url = "https://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": city,
                "appid": "your_api_key_here",  # Replace with actual API key
                "units": "metric"
            }
            
            # For demo purposes, return mock data
            return {
                "success": True,
                "city": city,
                "temperature": 22,
                "description": "Clear sky",
                "humidity": 60,
                "note": "This is mock data. Replace with actual API implementation."
            }
            
        except Exception as e:
            logger.error(f"Error fetching weather for {city}: {str(e)}")
            return {"success": False, "error": str(e)}
