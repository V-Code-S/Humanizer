# 📂 Humanizer Project - Complete File Index

## 🎯 Quick Navigation

| Document | Best For |
|----------|----------|
| 🚀 **[QUICKSTART.md](QUICKSTART.md)** | First-time setup (5 minutes) |
| 📖 **[README.md](README.md)** | Full project overview |
| 🏗️ **[ARCHITECTURE.md](ARCHITECTURE.md)** | Understanding system design |
| 💻 **[DEVELOPMENT.md](DEVELOPMENT.md)** | Local development workflow |
| 🚢 **[DEPLOYMENT.md](DEPLOYMENT.md)** | Production deployment |
| ✅ **[PROJECT_STATUS.md](PROJECT_STATUS.md)** | Completion status & summary |

---

## 📂 Project Root Files

### Configuration & Setup
- **setup.sh** - Automated setup for macOS/Linux
- **setup.bat** - Automated setup for Windows
- **docker-compose.yml** - Docker multi-container setup
- **.env.local** - Local environment metadata
- **.gitignore** - Git ignore rules

### Documentation
- **README.md** - Complete project documentation (5000+ lines)
- **QUICKSTART.md** - 5-minute quick start guide
- **DEVELOPMENT.md** - Developer guide & workflow
- **DEPLOYMENT.md** - Production deployment guide
- **ARCHITECTURE.md** - System architecture details
- **CONTRIBUTING.md** - Contribution guidelines
- **LICENSE** - MIT License
- **PROJECT_STATUS.md** - Project completion status

---

## 📁 Backend Directory Structure

### Core Application (`backend/app/`)

#### Main Application
- **main.py** (150 lines)
  - FastAPI app initialization
  - CORS middleware configuration
  - Route registration
  - Startup/shutdown events
  - Health check endpoints
  - Global exception handler

#### Routes (`backend/app/routes/`)
- **humanize.py** (300+ lines)
  - `POST /humanize` - Main humanization endpoint
  - `POST /humanize/bulk` - Batch processing
  - `GET /styles` - Available styles
  - `POST /analyze` - Text analysis
  - Request/response models
  - Comprehensive error handling

#### Services (`backend/app/services/`)

**paraphraser.py** (120 lines)
- T5 transformer paraphrasing
- HuggingFace integration
- Beam search decoding
- Batch paraphrasing support
- Singleton model caching

**humanizer.py** (250+ lines)
- Sentence variation techniques
- Transition phrase injection
- Style-based rewriting
- Tone adjustment
- Burstiness variation
- Synonym injection
- Styles: casual, professional, academic, blog

**grammar.py** (100+ lines)
- Grammar correction using LanguageTool
- Basic regex fixes
- Capitalization correction
- Grammar analysis
- Error detection

#### Utils (`backend/app/utils/`)
- **text_processing.py** (200+ lines)
  - Sentence tokenization (NLTK/spaCy)
  - Word tokenization
  - Text metrics calculation
  - AI pattern detection
  - Text cleaning utilities

### Configuration & Setup
- **requirements.txt** - Python dependencies (13 packages)
- **run.py** - Entry point for running the server
- **Dockerfile** - Backend containerization
- **.env.example** - Example environment variables
- **.gitignore** - Backend-specific ignore rules

---

## 📁 Frontend Directory Structure

### Source Code (`frontend/src/`)

#### Components (`frontend/src/components/`)

**InputBox.jsx** (50 lines)
- Text input textarea
- Character counter with progress bar
- Real-time character validation
- Styled input warning

**OutputBox.jsx** (100 lines)
- Output display textarea (read-only)
- Style selector dropdown
- Copy button with feedback
- Download functionality
- Share button
- Text metrics display (words, chars, sentences)

**HumanizeButton.jsx** (30 lines)
- Main action button
- Loading state with spinner
- Disabled state handling
- Animation effects

#### Pages (`frontend/src/pages/`)

**Home.jsx** (250 lines)
- Main landing page
- API health check
- Error alert handling
- Features showcase
- "How it Works" section
- Stats display
- Input/Output layout
- Action buttons arrangement

#### Core Files
- **App.jsx** (100 lines)
  - Root component
  - Navigation bar with theme toggle
  - Route setup
  - Footer with links
  - Dark mode support

- **api.js** (100 lines)
  - API client class
  - Humanize endpoint
  - Bulk humanize endpoint
  - Styles endpoint
  - Analyze endpoint
  - Health check
  - Error handling

- **main.jsx** (10 lines)
  - React rendering setup
  - Root mount point

- **index.css** (100+ lines)
  - Global styles
  - Tailwind directives
  - Custom scrollbar
  - Animations (spin, fadeIn)
  - Button & textarea styles

### Configuration & Build

- **package.json** - npm dependencies & scripts
- **vite.config.js** - Vite build configuration
- **tailwind.config.js** - Tailwind CSS configuration
- **postcss.config.js** - PostCSS configuration
- **.eslintrc.cjs** - ESLint rules
- **Dockerfile** - Frontend containerization
- **.env.example** - Frontend environment variables
- **.gitignore** - Frontend ignore rules

### Static Files
- **public/** - Static assets directory
- **index.html** - HTML entry point

---

## 📁 GitHub Workflows (`.github/workflows/`)

### CI/CD Pipelines

**backend-tests.yml**
- Runs on Python 3.9, 3.10, 3.11
- Linting with flake8
- Testing with pytest
- Docker build validation
- Triggered on backend changes

**frontend-tests.yml**
- Runs on Node 16, 18, 20
- Dependency installation
- ESLint checking
- Build verification
- Auto-deploy to Vercel on main
- Triggered on frontend changes

---

## 📊 File Statistics

### Backend
| Category | Count | Lines |
|----------|-------|-------|
| Python Files | 7 | ~1,200 |
| Config Files | 3 | ~50 |
| **Total** | **10** | **~1,250** |

### Frontend
| Category | Count | Lines |
|----------|-------|-------|
| JSX Files | 7 | ~850 |
| JS Files | 2 | ~150 |
| Config Files | 5 | ~100 |
| HTML | 1 | ~20 |
| CSS | 1 | ~120 |
| **Total** | **16** | **~1,240** |

### Documentation
| Document | Lines |
|----------|-------|
| README.md | ~600 |
| DEPLOYMENT.md | ~400 |
| ARCHITECTURE.md | ~500 |
| DEVELOPMENT.md | ~300 |
| QUICKSTART.md | ~150 |
| Others | ~300 |
| **Total** | **~2,250** |

### **Grand Total: ~50+ files, 5,000+ lines of code & documentation**

---

## 🔗 File Dependencies

### Backend Dependencies
```
main.py
├── app/routes/humanize.py
│   ├── app/services/paraphraser.py (T5 models)
│   ├── app/services/humanizer.py (humanization)
│   ├── app/services/grammar.py (grammar correction)
│   └── app/utils/text_processing.py (text utilities)
└── app/main.py (FastAPI setup)

run.py
└── app/main.py
```

### Frontend Dependencies
```
main.jsx
├── App.jsx
│   ├── pages/Home.jsx
│   │   ├── components/InputBox.jsx
│   │   ├── components/OutputBox.jsx
│   │   ├── components/HumanizeButton.jsx
│   │   └── api.js
│   └── index.css
└── index.css
```

---

## 🎯 Finding Information

### I want to...
- **Get started quickly** → Read [QUICKSTART.md](QUICKSTART.md)
- **Understand the system** → Read [ARCHITECTURE.md](ARCHITECTURE.md)
- **Deploy to production** → Read [DEPLOYMENT.md](DEPLOYMENT.md)
- **Develop locally** → Read [DEVELOPMENT.md](DEVELOPMENT.md)
- **Contribute code** → Read [CONTRIBUTING.md](CONTRIBUTING.md)
- **Check project status** → Read [PROJECT_STATUS.md](PROJECT_STATUS.md)
- **See full documentation** → Read [README.md](README.md)

### I need to find...
- **API endpoint documentation** → `backend/app/routes/humanize.py`
- **Text processing logic** → `backend/app/utils/text_processing.py`
- **Paraphrasing algorithm** → `backend/app/services/paraphraser.py`
- **Humanization techniques** → `backend/app/services/humanizer.py`
- **React components** → `frontend/src/components/`
- **API client code** → `frontend/src/api.js`
- **Styling rules** → `frontend/src/index.css`
- **Tailwind config** → `frontend/tailwind.config.js`

---

## 📦 Environment Files

### Backend Configuration
- **backend/.env.example** (reference)
  ```
  HOST=0.0.0.0
  PORT=8000
  ENV=development
  FRONTEND_URL=http://localhost:3000
  PROD_FRONTEND_URL=https://your-domain.com
  ```

### Frontend Configuration
- **frontend/.env.example** (reference)
  ```
  VITE_API_URL=http://localhost:8000/api
  ```

---

## 🔍 Key Implementation Details

### Where are the AI models?
- **Loaded in**: `backend/app/services/paraphraser.py`
- **Models used**:
  - `Vamsi/T5_Paraphrase_Paws` (paraphrasing)
  - `google/flan-t5-large` (humanization)

### Where is humanization logic?
- **Main file**: `backend/app/services/humanizer.py`
- **Techniques**:
  - Sentence variation
  - Transition phrases
  - Synonym injection
  - Tone adjustment
  - Burstiness variation

### Where is the API definition?
- **All endpoints**: `backend/app/routes/humanize.py`
- **Auto-docs**: http://localhost:8000/docs (when running)

### Where is the React UI?
- **Main page**: `frontend/src/pages/Home.jsx`
- **Components**: `frontend/src/components/`
- **Styling**: `frontend/src/index.css` + `tailwind.config.js`

---

## 🚀 Running the Project

### File execution order
```
1. setup.sh / setup.bat          (Initial setup)
2. backend/run.py                (Start API)
3. frontend/package.json (npm)   (Start UI)
4. http://localhost:5173         (Open in browser)
```

### Docker execution
```
1. docker-compose.yml            (Start containers)
2. http://localhost:3000         (Access frontend)
```

---

## 📋 Checklist for Setup

```
□ Read QUICKSTART.md
□ Run setup.sh / setup.bat
□ Start backend (backend/run.py)
□ Start frontend (frontend/package.json)
□ Open http://localhost:5173
□ Test humanization
□ Review ARCHITECTURE.md
□ Check DEVELOPMENT.md for workflows
□ Read DEPLOYMENT.md for production
```

---

## 🎓 Learning Path

1. **Beginner**: QUICKSTART.md → setup → use the app
2. **Intermediate**: DEVELOPMENT.md → explore code → modify
3. **Advanced**: ARCHITECTURE.md → extend features → deploy
4. **Expert**: DEPLOYMENT.md → production → monitoring

---

## 📞 Quick Reference

| Requirement | Location |
|-------------|----------|
| API Endpoints | `backend/app/routes/humanize.py` |
| Text Processing | `backend/app/utils/text_processing.py` |
| Paraphrasing | `backend/app/services/paraphraser.py` |
| Humanization | `backend/app/services/humanizer.py` |
| Grammar | `backend/app/services/grammar.py` |
| React Components | `frontend/src/components/` |
| Styling | `frontend/src/index.css` |
| API Client | `frontend/src/api.js` |
| Main Page | `frontend/src/pages/Home.jsx` |
| Config | Various `.example` files |

---

**Last Updated**: March 8, 2024
**Project Status**: ✅ Complete and ready to use!
