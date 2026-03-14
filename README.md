# 🤖 AI Text to Human Text Converter

A free, open-source web application that transforms AI-generated text into natural, human-like writing. A free alternative to Undetectable AI, Quillbot, and HumanizeAI.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![React](https://img.shields.io/badge/React-18.2-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- **AI Paraphrasing**: Uses advanced T5 transformer models to intelligently rewrite text
- **Humanization Engine**: Adds natural variation, sentence diversity, and human touches
- **Grammar Correction**: Automatic grammar and spelling checking
- **Style Options**: Choose from casual, professional, academic, or blog writing styles
- **Dark Mode**: Comfortable dark theme support
- **Download & Share**: Export results as text files or share via links
- **Bulk Processing**: Humanize multiple texts at once
- **Analysis Metrics**: Get detailed statistics about your text transformations

## 🏗️ System Architecture

```
User (Browser)
    ↓
Frontend (React + Tailwind CSS)
    ↓
API Gateway (FastAPI)
    ↓
Text Processing Pipeline
├── Paraphrasing (T5)
├── Humanization Engine
├── Grammar Correction
└── Style Adjustment
    ↓
Humanized Output
```

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.9+
- **Server**: Uvicorn
- **API**: REST
- **ML Libraries**:
  - HuggingFace Transformers
  - PyTorch
  - spaCy
  - NLTK

### Frontend
- **Framework**: React 18.2
- **Styling**: Tailwind CSS 3.3
- **Animations**: Framer Motion
- **HTTP Client**: Fetch API
- **Build Tool**: Vite
- **Deployment**: Vercel

### AI/NLP Models
- **Paraphrasing**: `Vamsi/T5_Paraphrase_Paws`
- **Humanization**: `google/flan-t5-large`
- **Grammar**: LanguageTool

## 📋 Prerequisites

- Python 3.9+
- Node.js 16+
- Git
- 4GB+ RAM (for ML models)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/humanizer.git
cd humanizer
```

### 2. Setup Backend

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Run backend (downloads models on first run)
python run.py
```

Backend will be available at `http://localhost:8000`

### 3. Setup Frontend

```bash
cd frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Start development server
npm run dev
```

Frontend will be available at `http://localhost:5173`

### 4. Test the Application

Open `http://localhost:5173` in your browser and start humanizing text!

## 📖 API Documentation

### Health Check
```
GET /health
```

### Humanize Text
```
POST /api/humanize

Request:
{
  "text": "AI is transforming industries...",
  "style": "casual"  // optional: default, casual, professional, academic, blog
}

Response:
{
  "original_text": "AI is transforming industries...",
  "humanized_text": "Artificial intelligence is gradually changing...",
  "style": "casual",
  "processing_time": 2.45
}
```

### Bulk Humanize
```
POST /api/humanize/bulk

Request:
{
  "texts": ["Text 1...", "Text 2..."],
  "style": "professional"
}

Response:
{
  "results": [
    {"original": "...", "humanized": "..."},
    {"original": "...", "humanized": "..."}
  ],
  "total_time": 5.12
}
```

### Get Available Styles
```
GET /api/styles

Response:
{
  "styles": {
    "default": "Natural, balanced writing style",
    "casual": "Conversational and informal tone",
    "professional": "Formal and business-like tone",
    "academic": "Scholarly and detailed writing",
    "blog": "Engaging and narrative style"
  }
}
```

### Analyze Text
```
POST /api/analyze

Request:
{
  "text": "AI is transforming industries...",
  "style": "default"
}

Response:
{
  "original": {
    "text": "...",
    "metrics": {...}
  },
  "humanized": {
    "text": "...",
    "metrics": {...}
  },
  "improvements": {...}
}
```

### Interactive API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🗂️ Project Structure

```
humanizer/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app setup
│   │   ├── routes/
│   │   │   └── humanize.py      # API endpoints
│   │   ├── services/
│   │   │   ├── paraphraser.py   # T5 paraphrasing
│   │   │   ├── humanizer.py     # Humanization engine
│   │   │   └── grammar.py       # Grammar correction
│   │   └── utils/
│   │       └── text_processing.py
│   ├── requirements.txt
│   ├── run.py
│   ├── .env.example
│   └── .gitignore
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── InputBox.jsx
│   │   │   ├── OutputBox.jsx
│   │   │   └── HumanizeButton.jsx
│   │   ├── pages/
│   │   │   └── Home.jsx
│   │   ├── api.js               # API client
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── .env.example
│   ├── index.html
│   └── .gitignore
│
├── README.md
├── docker-compose.yml
└── .gitignore
```

## 🐳 Docker Deployment

### Using Docker Compose

```bash
docker-compose up --build
```

Access:
- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

### Individual Docker Images

```bash
# Build backend
cd backend
docker build -t humanizer-backend .
docker run -p 8000:8000 humanizer-backend

# Build frontend
cd frontend
docker build -t humanizer-frontend .
docker run -p 3000:3000 humanizer-frontend
```

## 🚀 Production Deployment

### Backend (Railway/Render)

1. Push code to GitHub
2. Connect repository to Railway or Render
3. Set environment variables:
   - `ENV=production`
   - `FRONTEND_URL=https://your-frontend.vercel.app`
4. Deploy

### Frontend (Vercel)

1. Push code to GitHub
2. Import project to Vercel
3. Set environment variable:
   - `VITE_API_URL=https://your-api.railway.app/api`
4. Deploy

### Environment Variables

**Backend (.env)**
```
HOST=0.0.0.0
PORT=8000
ENV=production
FRONTEND_URL=https://your-domain.com
PROD_FRONTEND_URL=https://your-domain.com
```

**Frontend (.env.production)**
```
VITE_API_URL=https://your-api.vercel.app/api
```

## 📊 Performance Metrics

- Average processing time: 2-5 seconds
- Support for texts up to 5000 characters
- GPU acceleration support
- Batch processing for multiple texts

## 🔄 Processing Pipeline

1. **Input Validation**: Check text length and format
2. **Preprocessing**: Clean and normalize text
3. **Sentence Segmentation**: Split into sentences
4. **AI Paraphrasing**: Rewrite using T5 model
5. **Humanization**: Add variation and natural flow
6. **Grammar Correction**: Fix grammar and spelling
7. **Style Adjustment**: Apply selected writing style
8. **Output**: Return humanized text

## 🎨 Key Techniques

### Sentence Variation
- Mix short, medium, and long sentences
- Combine and split sentences dynamically
- Add transition phrases naturally

### Humanization Techniques
- Synonym injection
- Punctuation variation
- Tone adjustment (casual/formal)
- Natural connector phrases
- Burstiness (sentence length variation)

### Style Adaptation
- **Casual**: Contractions, informal words, conversational tone
- **Professional**: Formal language, no contractions, structured
- **Academic**: Sophisticated vocabulary, citations, detailed
- **Blog**: Engaging, narrative, personal touches

## 🧪 Testing

```bash
# Test backend API
cd backend
pip install pytest pytest-httpx
pytest

# Test frontend
cd frontend
npm run test
```

## 📝 API Examples

### Example 1: Humanize AI Text

```bash
curl -X POST "http://localhost:8000/api/humanize" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Artificial intelligence has become increasingly important in modern society. AI systems are being deployed in various industries. Machine learning algorithms are used to automate tasks.",
    "style": "professional"
  }'
```

**Response:**
```json
{
  "original_text": "Artificial intelligence has become increasingly important...",
  "humanized_text": "In today's world, artificial intelligence plays a crucial role across multiple sectors. Organizations are increasingly leveraging AI solutions to streamline operations, while machine learning algorithms continue to automate complex processes.",
  "style": "professional",
  "processing_time": 3.45
}
```

### Example 2: Detect AI Pattern

```bash
curl -X POST "http://localhost:8000/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "In the context of modern technology, artificial intelligence represents a paradigm shift...",
    "style": "default"
  }'
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- HuggingFace for transformer models
- FastAPI team
- React community
- All contributors and users

## 📞 Support

- Issues: [GitHub Issues](https://github.com/yourusername/humanizer/issues)
- Discussions: [GitHub Discussions](https://github.com/yourusername/humanizer/discussions)
- Email: support@humanizer.app

## 🗺️ Roadmap

- [ ] Phase 2: Enhanced humanization techniques
- [ ] Phase 3: AI detection reduction features
- [ ] Phase 4: Plagiarism checker
- [ ] Browser extension
- [ ] Mobile app
- [ ] API for developers
- [ ] Multilingual support
- [ ] Real-time collaboration

---

Made with ❤️ for writers and students everywhere.
