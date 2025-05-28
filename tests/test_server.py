#!/usr/bin/env python3
"""
Quick test script to verify MCP server functionality
"""
import sys
import os
from pathlib import Path

# Add src to path
current_dir = Path(__file__).parent
src_dir = current_dir / "src"
sys.path.insert(0, str(src_dir))

def test_imports():
    """Test that all modules can be imported successfully"""
    print("🧪 Testing module imports...")
    
    try:
        from tools import DatabaseTools, APITools, FileTools, UtilityTools
        from resources import DataResources, FileResources
        from prompts import TemplatePrompts
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
        from tools import DatabaseTools, APITools, FileTools, UtilityTools
        
        db_tools = DatabaseTools()
        api_tools = APITools()
        file_tools = FileTools()
        utility_tools = UtilityTools()
        
        print("✅ All tools initialized successfully!")
        return True
    except Exception as e:
        print(f"❌ Tool initialization failed: {e}")
        return False

def test_basic_functionality():
    """Test basic tool functionality"""
    print("⚡ Testing basic functionality...")
    
    try:
        from tools.utility_tools import UtilityTools
        utility_tools = UtilityTools()
        
        # Test hash generation
        result = utility_tools.generate_hash("test", "md5")
        assert result["success"] == True
        
        # Test base64 encoding
        result = utility_tools.encode_decode_base64("hello", "encode")
        assert result["success"] == True
        
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
        print("🎉 All tests passed! Your MCP server is ready to use.")
        print("   Run: mcp dev src/server.py")
        return 0
    else:
        print("⚠️ Some tests failed. Check the output above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
