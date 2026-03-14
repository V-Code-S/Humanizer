@echo off
REM Development Setup Script for Windows

echo 🚀 Setting up Humanizer development environment...

REM Check Python
echo ✓ Checking Python...
python --version

REM Check Node
echo ✓ Checking Node.js...
node --version
npm --version

REM Backend setup
echo.
echo 📦 Setting up backend...
cd backend

if not exist "venv" (
    python -m venv venv
    echo ✓ Created virtual environment
)

call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
echo ✓ Installed backend dependencies

copy .env.example .env
echo ✓ Created .env file

cd ..

REM Frontend setup
echo.
echo ⚛️  Setting up frontend...
cd frontend

call npm install
echo ✓ Installed frontend dependencies

copy .env.example .env
echo ✓ Created .env file

cd ..

echo.
echo ✅ Development setup complete!
echo.
echo 📝 Next steps:
echo 1. Backend:  cd backend ^&^& call venv\Scripts\activate.bat ^&^& python run.py
echo 2. Frontend: cd frontend ^&^& npm run dev
echo.
echo 🌐 Access:
echo   Frontend: http://localhost:5173
echo   Backend:  http://localhost:8000
echo   API Docs: http://localhost:8000/docs
