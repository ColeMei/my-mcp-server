#!/bin/bash

# Cole's Daily Workflow MCP Server Setup Script
# Usage: source ./setup_dev.sh
echo "🚀 Setting up Cole's Daily Workflow MCP Server..."

# Create virtual environment if it doesn't exist
if [ ! -d "mcp-env" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv mcp-env
fi

# Temporarily activate for dependency installation
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
echo "🎉 Your streamlined daily workflow MCP server is ready!"
echo ""
echo "🚀 Start the server:"
echo "   mcp dev src/server.py"
echo ""
echo "🌐 Then open MCP Inspector:"
echo "   http://127.0.0.1:6274"
echo ""
echo "📖 See WORKFLOW_EXAMPLES.md for usage examples"
echo "📖 See README.md for full documentation"
