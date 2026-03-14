#!/bin/bash
# Development Setup Script

set -e

echo "🚀 Setting up Humanizer development environment..."

# Check Python
echo "✓ Checking Python..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "  Python version: $python_version"

# Check Node
echo "✓ Checking Node.js..."
node_version=$(node --version)
npm_version=$(npm --version)
echo "  Node version: $node_version"
echo "  NPM version: $npm_version"

# Backend setup
echo ""
echo "📦 Setting up backend..."
cd backend

if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Created virtual environment"
fi

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "✓ Installed backend dependencies"

cp .env.example .env
echo "✓ Created .env file"

cd ..

# Frontend setup
echo ""
echo "⚛️  Setting up frontend..."
cd frontend

npm install
echo "✓ Installed frontend dependencies"

cp .env.example .env
echo "✓ Created .env file"

cd ..

echo ""
echo "✅ Development setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Backend:  cd backend && source venv/bin/activate && python run.py"
echo "2. Frontend: cd frontend && npm run dev"
echo ""
echo "🌐 Access:"
echo "  Frontend: http://localhost:5173"
echo "  Backend:  http://localhost:8000"
echo "  API Docs: http://localhost:8000/docs"
