#!/usr/bin/env python3
"""
Quick test script to verify MCP server functionality
"""
import sys
import os
from pathlib import Path

# Add src to path
current_dir = Path(__file__).parent
project_root = current_dir.parent
src_dir = project_root / "src"
sys.path.insert(0, str(src_dir))

def test_imports():
    """Test that all modules can be imported successfully"""
    print("🧪 Testing module imports...")
    
    try:
        from tools import DatabaseTools, FileTools
        from resources import DataResources, FileResources
        from prompts import (
            get_analyze_notes_prompt,
            get_optimize_database_prompt, 
            get_database_migration_prompt,
            get_analyze_project_prompt,
            get_code_review_prompt,
            get_refactor_project_prompt,
            get_file_organization_prompt
        )
        from config.settings import get_settings
        from utils.logging import setup_logging, get_logger
        print("✅ All imports successful!")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_configuration():
    """Test configuration loading"""
    print("🔧 Testing configuration...")
    
    try:
        from config.settings import get_settings
        settings = get_settings()
        print(f"✅ Configuration loaded: {settings.server_name} v{settings.server_version}")
        return True
    except Exception as e:
        print(f"❌ Configuration failed: {e}")
        return False

def test_tools():
    """Test tool initialization"""
    print("🛠️ Testing tool initialization...")
    
    try:
        from tools import DatabaseTools, FileTools
        
        db_tools = DatabaseTools()
        file_tools = FileTools()
        
        print("✅ All tools initialized successfully!")
        return True
    except Exception as e:
        print(f"❌ Tool initialization failed: {e}")
        return False

def test_basic_functionality():
    """Test basic tool functionality"""
    print("⚡ Testing basic functionality...")
    
    try:
        from tools.database_tools import DatabaseTools
        from tools.file_tools import FileTools
        
        db_tools = DatabaseTools()
        file_tools = FileTools()
        
        # Test database connection
        result = db_tools.get_notes(5)
        assert "success" in str(result).lower() or "data" in str(result).lower()
        
        print("✅ Basic functionality tests passed!")
        return True
    except Exception as e:
        print(f"❌ Functionality test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 MCP Server Test Suite")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_configuration,
        test_tools,
        test_basic_functionality
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"📊 Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests passed! Your streamlined MCP server is ready to use.")
        print("   Run: mcp dev src/server.py")
        return 0
    else:
        print("⚠️ Some tests failed. Check the output above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
