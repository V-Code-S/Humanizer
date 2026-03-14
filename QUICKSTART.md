# Quick Start Guide

## 🚀 5-Minute Quick Start

### Prerequisites
- Python 3.9+ 
- Node.js 16+
- Git

### Step 1: Clone & Enter Directory
```bash
cd /path/to/Humanizer
```

### Step 2: Automated Setup (Recommended)

**macOS/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

**Windows:**
```bash
setup.bat
```

### Step 3: Start Backend
```bash
cd backend
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate.bat  # Windows

python run.py
```

Expect to see (first run downloads models ~2-3 minutes):
```
🚀 Initializing Humanizer API...
📦 Loading paraphrase model...
📦 Loading humanization engine...
✅ Humanizer API ready!
INFO: Uvicorn running on http://0.0.0.0:8000
```

### Step 4: Start Frontend (New Terminal)
```bash
cd frontend
npm run dev
```

Should see:
```
Local: http://localhost:5173/
```

### Step 5: Open Browser
Visit `http://localhost:5173` and start humanizing text!

---

## 📱 What You Should See

### Frontend Interface
- **Title**: "AI Text → Human Text"
- **Input Box**: "Paste your AI-generated text here..."
- **Humanize Button**: Blue button with ✨ icon
- **Output Box**: "Your humanized text will appear here..."

### First Test
1. Paste this text in input:
```
Artificial intelligence has become increasingly important in modern society due to its capabilities in automating tasks and improving efficiency across various sectors.
```

2. Click "Humanize Text"
3. Wait 2-5 seconds
4. See humanized text appear in output box

---

## 🔧 Troubleshooting

### "API not responding"
- ✓ Backend running on port 8000?
- ✓ Check terminal for error messages
- Try: `curl http://localhost:8000/health`

### Models not loading
- First run downloads ~3-4GB data
- Ensure internet connection
- Check disk space (5GB+ required)

### ModuleNotFoundError
```bash
cd backend
pip install -r requirements.txt
```

### Port already in use
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# OR use different port
PORT=8001 python run.py
```

---

## 📚 Next Steps

1. **Read Full Docs**: See [README.md](README.md)
2. **Explore API**: Visit http://localhost:8000/docs
3. **Check Architecture**: See [ARCHITECTURE.md](ARCHITECTURE.md)
4. **Deploy**: See [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 🎯 Common Tasks

### Run with Docker
```bash
docker-compose up --build
```

### Run only backend
```bash
cd backend
python run.py
```

### Run only frontend
```bash
cd frontend
npm run dev
```

### Build frontend for production
```bash
cd frontend
npm run build
```

### Clear all data
```bash
# Backend (removes venv & downloads)
cd backend
rm -rf venv models

# Frontend
cd frontend
rm -rf node_modules dist
```

---

## 📞 Need Help?

- **API Issues**: Check http://localhost:8000/docs
- **Build Issues**: See [DEPLOYMENT.md](DEPLOYMENT.md)
- **Architecture**: See [ARCHITECTURE.md](ARCHITECTURE.md)

Enjoy using Humanizer! 🎉
