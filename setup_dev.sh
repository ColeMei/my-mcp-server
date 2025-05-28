#!/bin/bash

# MCP Server Development Setup Script
echo "🚀 Setting up MCP Server development environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "mcp-env" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv mcp-env
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source mcp-env/bin/activate

# Install/upgrade dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p data logs

# Clean up any Python cache files
echo "🧹 Cleaning up cache files..."
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true

echo "✅ Development environment setup complete!"
echo ""
echo "🎯 Next steps:"
echo "1. Activate environment: source mcp-env/bin/activate"
echo "2. Run MCP Inspector: mcp dev src/server.py"
echo "3. Open browser: http://127.0.0.1:6274"
echo ""
echo "📖 See README.md for more details"
