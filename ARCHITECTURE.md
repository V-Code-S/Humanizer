# System Architecture

Detailed documentation of the Humanizer system architecture.

## Overview

The Humanizer application is built on a modern, scalable architecture with:
- **Separated concerns**: Frontend and backend are completely decoupled
- **Stateless API**: Backend is horizontally scalable
- **Real-time processing**: Fast text transformation pipeline
- **Cloud-ready**: Containerized and deployment-agnostic

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     User Browser                             │
└────────────────────────────┬────────────────────────────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
         ┌──────────▼──────────┐     │
         │  Frontend (React)   │     │ REST API JSON
         │  - Components       │<────┤
         │  - State Mgmt       │     │
         │  - Tailwind CSS     │     │
         └──────────┬──────────┘     │
                    │                 │
         ┌──────────▼──────────────────────┐
         │    CORS Middleware & API Gateway│
         └──────────┬──────────────────────┘
                    │
         ┌──────────▼───────────────┐
         │   FastAPI Application    │
         │  - Route Handlers        │
         │  - Request Validation    │
         │  - Response Serialization│
         └──────────┬───────────────┘
                    │
         ┌──────────▼──────────────────────────┐
         │  Text Processing Pipeline          │
         │                                    │
         │ 1. Input Validation & Cleaning    │
         │ 2. Sentence Segmentation (NLTK)   │
         │ 3. AI Paraphrasing (T5)           │
         │ 4. Humanization Engine            │
         │ 5. Grammar Correction (LangTool)  │
         │ 6. Style Adjustment               │
         └──────────┬──────────────────────────┘
                    │
         ┌──────────▼──────────────────────────┐
         │   ML Models (HuggingFace)           │
         │                                    │
         │ - Vamsi/T5_Paraphrase_Paws        │
         │ - google/flan-t5-large            │
         │ - spacy/nltk (text processing)    │
         └──────────┬──────────────────────────┘
                    │
         ┌──────────▼──────────────┐
         │   Response Generation   │
         │  - Humanized Text       │
         │  - Metadata/Stats       │
         │  - Processing Time      │
         └──────────┬──────────────┘
                    │
                    │ JSON Response
                    │
         ┌──────────▼──────────────────┐
         │  Frontend Receives Result   │
         │  - Displays Text           │
         │  - Shows Metrics           │
         │  - Enables Actions         │
         └─────────────────────────────┘
```

## Technology Stack

### Backend Layer

```
┌─────────────────────────────────────────┐
│         FastAPI Web Framework           │
├─────────────────────────────────────────┤
│ Uvicorn ASGI Server                     │
│ - Async/Await Support                   │
│ - High Performance                      │
│ - Auto-reloading in Development        │
├─────────────────────────────────────────┤
│ Python 3.9+ Runtime                     │
└─────────────────────────────────────────┘
```

### Processing Pipeline

```
┌──────────────────────────────────┐
│    Text Preprocessing            │
│  - Regex normalization           │
│  - Whitespace cleaning           │
│  - Punctuation standardization   │
├──────────────────────────────────┤
│    Sentence Tokenization         │
│  - NLTK sent_tokenize()          │
│  - Fallback regex splitting      │
├──────────────────────────────────┤
│    Paraphrasing Service          │
│  - T5 Transformer Model          │
│  - Beam Search Decoding          │
│  - Multiple paraphrases          │
├──────────────────────────────────┤
│    Humanization Engine           │
│  - Sentence variation            │
│  - Transition phrases            │
│  - Synonym injection             │
│  - Tone adjustment               │
│  - Burstiness variation          │
├──────────────────────────────────┤
│    Grammar Correction            │
│  - LanguageTool API              │
│  - Basic regex fixes             │
│  - Capitalization normalization  │
├──────────────────────────────────┤
│    Style Adaptation              │
│  - Casual: contractions, informal│
│  - Professional: formal, structured
│  - Academic: sophisticated vocab │
│  - Blog: engaging, narrative     │
└──────────────────────────────────┘
```

### Frontend Layer

```
┌──────────────────────────────────┐
│    React 18.2 Components         │
│  - Functional Components         │
│  - React Hooks                   │
│  - State Management              │
├──────────────────────────────────┤
│    Vite Build Tool               │
│  - ES Module bundling            │
│  - Hot Module Replacement        │
│  - Optimized production builds   │
├──────────────────────────────────┤
│    Tailwind CSS Styling          │
│  - Utility-first CSS             │
│  - Dark mode support             │
│  - Responsive design             │
├──────────────────────────────────┤
│    Framer Motion Animations      │
│  - Smooth transitions            │
│  - Gesture animations            │
│  - Spring animations             │
├──────────────────────────────────┤
│    Fetch API Client              │
│  - Promise-based HTTP            │
│  - Error handling                │
│  - Request/Response mapping      │
└──────────────────────────────────┘
```

## Data Flow

### Request Flow

```
1. User Input
   ├─ Text entered in InputBox
   ├─ Validated for length (10-5000 chars)
   └─ Style selected (default, casual, etc.)
   
2. API Request
   ├─ JSON payload created
   ├─ Sent via POST /api/humanize
   └─ CORS headers validated
   
3. Backend Processing
   ├─ Pydantic validation
   ├─ Text preprocessing
   ├─ Model inference (2-5 seconds)
   └─ Response generation
   
4. Response Handling
   ├─ Parse JSON response
   ├─ Update OutputBox state
   ├─ Calculate metrics
   └─ Render UI

5. User Output
   ├─ Display humanized text
   ├─ Show copy button
   ├─ Enable download
   └─ Display stats
```

### Database/State Management

#### Frontend State (React Hooks)
```javascript
const [inputText, setInputText] = useState(''); // User input
const [outputText, setOutputText] = useState(''); // API response
const [style, setStyle] = useState('default'); // Style choice
const [loading, setLoading] = useState(false); // API call state
const [error, setError] = useState(''); // Error messages
const [stats, setStats] = useState(null); // Metrics
```

#### Backend State
- **Stateless API**: No user sessions or state persistence
- **Model Caching**: Models loaded once on startup
- **Request-level**: Data exists only during processing

## API Endpoints

### Core Endpoint

```
POST /api/humanize
├─ Request: { text, style }
├─ Process: Paraphrase → Humanize → Correct
└─ Response: { original_text, humanized_text, style, processing_time }
```

### Support Endpoints

```
POST /api/humanize/bulk
├─ Batch process multiple texts
└─ Return array of results

POST /api/analyze
├─ Return detailed metrics
└─ Compare before/after

GET /api/styles
├─ List available writing styles
└─ Return style descriptions

GET /health
├─ Health check endpoint
└─ Used by load balancers
```

## Performance Characteristics

### Latency

```
Input Validation:           50-100ms
Preprocessing:              50-150ms
Paraphrasing (T5):          1.5-3.5s
Humanization:               200-500ms
Grammar Correction:         300-800ms
Response Serialization:     20-50ms
─────────────────────────────────────
Total Average:              2-5 seconds
```

### Throughput

- Single instance: 10-15 requests/minute
- With GPU: 30-50 requests/minute
- Batch processing: 3-5 texts per request

### Memory Usage

```
Idle:                       ~500MB
During Inference:           {
  T5 Model:                 ~2GB
  Humanization:             ~800MB
  Grammar Tool:             ~600MB
}
Total Peak:                 ~3.5GB
```

### Scalability

```
Current: Single instance
├─ Max load: 15 req/min
├─ Response time: 2-5s
└─ Cost: Low

Scaled: Load Balanced
├─ Multiple backend instances
├─ Max load: 50-100 req/min
├─ Response time: 2-5s (consistent)
└─ Cost: Moderate
```

## Module Dependencies

### Backend Dependency Graph

```
FastAPI (Framework)
├── Pydantic (Request validation)
├── Uvicorn (Server)
└── Transformers (ML)
    ├── PyTorch (Neural networks)
    ├── Tokenizers (Text encoding)
    └── NumPy (Numerical computing)

Text Processing
├── NLTK (Sentence tokenization)
├── spaCy (NLP)
└── LanguageTool (Grammar)

Middleware
├── python-dotenv (Configuration)
├── CORS (Cross-origin)
└── Logging (Standard library)
```

### Frontend Dependency Graph

```
React
├── ReactDOM (Virtual rendering)
└── React Hooks (State management)

Build & Dev
├── Vite (Build tool)
├── @vitejs/plugin-react (JSX)
└── Tailwind CSS (Styling)

UI/UX
├── Framer Motion (Animations)
├── Fetch API (HTTP)
└── CSS Grid/Flexbox (Layout)

Development
├── ESLint (Linting)
├── PostCSS (CSS processing)
└── Autoprefixer (Browser support)
```

## Security Architecture

### Input Validation

```
Raw Text
├─ Length check (10-5000 chars)
├─ Character whitelist
├─ XSS prevention
└─ Encoding validation
```

### CORS Policy

```
Development:
─ http://localhost:3000
─ http://localhost:5173
─ http://localhost:8000

Production:
─ https://your-domain.com
─ https://your-frontend.vercel.app
```

### Data Privacy

- No user data persistence
- Requests exist only during processing
- Outputs returned to client immediately
- No logging of personal data

## Deployment Architecture

### Local Development

```
┌───────────────────┐     ┌───────────────────┐
│  Frontend Dev     │────▶│  Backend API      │
│  (npm run dev)    │     │  (python run.py)  │
│  Port: 5173/3000  │     │  Port: 8000       │
└───────────────────┘     └───────────────────┘
       localhost
```

### Docker Containerization

```
┌──────────────────────────────────┐
│    Docker Compose (Local)        │
├──────────────────────────────────┤
│ ┌──────────────┐ ┌────────────┐ │
│ │   Backend    │ │  Frontend  │ │
│ │  Container   │ │ Container  │ │
│ └──────────────┘ └────────────┘ │
│        Network: Compose          │
└──────────────────────────────────┘
```

### Production Deployment

```
┌─────────────────────────────────────┐
│         CDN / CloudFront            │
└────────────┬────────────────────────┘
             │
   ┌─────────┴──────────┐
   │                    │
┌──▼──────────────┐  ┌─▼──────────────┐
│   Vercel        │  │  Railway/Render│
│  (Frontend)     │  │  (Backend API) │
│                 │  │                │
│ - Next.js build │  │ - FastAPI app  │
│ - CDN caching   │  │ - Model server │
│ - Analytics     │  │ - Auto-scaling │
└─────────────────┘  └────────────────┘
```

## Monitoring & Observability

### Key Metrics

```
Backend:
├─ Request latency (p50, p95, p99)
├─ Model inference time
├─ Memory usage
├─ Error rate
├─ Throughput (req/sec)
└─ Model loading time

Frontend:
├─ Page load time
├─ Time to interactive
├─ Component render time
├─ API response time
└─ User interactions
```

### Logging Strategy

```
Backend:
- Request/Response logging
- Model loading logs
- Error traces with context
- Process timing

Frontend:
- API call logs
- React lifecycle logs
- Error boundaries
- Performance metrics
```

## Future Architecture Enhancements

1. **Caching Layer**
   - Redis for frequent requests
   - Response caching
   - Model output caching

2. **Queue System**
   - Async task processing
   - Celery integration
   - User request queuing

3. **Database**
   - User accounts
   - Request history
   - Analytics

4. **Authentication**
   - JWT tokens
   - OAuth2 integration
   - API key management

5. **Advanced Features**
   - WebSocket for real-time updates
   - Streaming responses
   - Batch processing API

---

For deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).
