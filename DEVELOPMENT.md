# Development Guide

## Local Development Setup

### Initial Setup

```bash
# 1. Clone repository
git clone <repository-url>
cd Humanizer

# 2. Run setup script
./setup.sh  # macOS/Linux
# OR
setup.bat   # Windows

# 3. Start both services
# In terminal 1:
cd backend && source venv/bin/activate && python run.py

# In terminal 2:
cd frontend && npm run dev
```

## Development Workflow

### Backend Development

#### File Structure
```
backend/
├── app/
│   ├── main.py           # FastAPI app setup
│   ├── routes/           # API endpoints
│   └── services/         # Business logic
├── requirements.txt      # Dependencies
└── run.py               # Entry point
```

#### Common Tasks

**Run with debug mode:**
```bash
cd backend
RELOAD=true python run.py
```

**Install new package:**
```bash
pip install <package-name>
pip freeze > requirements.txt
```

**Run specific test:**
```bash
pytest tests/test_humanize.py -v
```

**Check code style:**
```bash
flake8 app/
black app/  # Auto-format
```

### Frontend Development

#### File Structure
```
frontend/
├── src/
│   ├── components/       # React components
│   ├── pages/           # Page components
│   ├── api.js           # API client
│   └── App.jsx          # Root component
├── public/              # Static assets
└── index.html           # HTML entry point
```

#### Common Tasks

**Run dev server:**
```bash
npm run dev
```

**Build for production:**
```bash
npm run build
npm run preview
```

**Update dependencies:**
```bash
npm update
npm install <package-name>
```

**Fix code style:**
```bash
npm run lint
npm run lint -- --fix
```

## API Development

### Adding New Endpoint

1. **Create route in `app/routes/humanize.py`:**
```python
@router.post("/new-endpoint")
async def new_endpoint(request: NewRequest):
    """
    Endpoint description
    """
    # Implementation
    return {"result": "success"}
```

2. **Define request/response models:**
```python
class NewRequest(BaseModel):
    param1: str = Field(..., description="Parameter 1")
    param2: Optional[int] = None

class NewResponse(BaseModel):
    result: str
    status: str
```

3. **Test in API docs:**
- Visit `http://localhost:8000/docs`
- Find your endpoint
- Click "Try it out"
- Add sample data
- Execute

### Error Handling

```python
from fastapi import HTTPException

if not valid:
    raise HTTPException(
        status_code=400,
        detail="Detailed error message"
    )
```

## Frontend Development

### Adding New Component

1. **Create component file:**
```jsx
// src/components/NewComponent.jsx
import React from 'react';
import { motion } from 'framer-motion';

function NewComponent() {
  return (
    <motion.div>
      {/* Component content */}
    </motion.div>
  );
}

export default NewComponent;
```

2. **Use component:**
```jsx
import NewComponent from '../components/NewComponent';

export default function App() {
  return <NewComponent />;
}
```

### State Management

Using React Hooks:
```jsx
const [state, setState] = useState(initialValue);
const [data, setData] = useEffect(() => { /* ... */ }, []);
```

## Environment Variables

### Backend (.env)
```
HOST=0.0.0.0
PORT=8000
ENV=development
RELOAD=true
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:8000/api
```

## Testing

### Backend Tests
```bash
cd backend
pytest --verbose
pytest tests/test_humanize.py::test_function -v
```

### Frontend Tests
```bash
cd frontend
npm run test
npm run test -- --coverage
```

## Debugging

### Backend
```python
import logging
logger = logging.getLogger(__name__)
logger.debug("Debug message")
logger.error("Error message", exc_info=True)
```

### Frontend
```javascript
console.log('Debug message');
console.error('Error:', error);
debugger; // Pause execution
```

## Browser DevTools

1. **Open DevTools**: F12 or Cmd+Option+I
2. **Console**: See logs and errors
3. **Network**: Monitor API calls
4. **Performance**: Check rendering speed
5. **Application**: Inspect localStorage, cookies

## Git Workflow

```bash
# Create feature branch
git checkout -b feature/feature-name

# Make changes and commit
git add .
git commit -m "Add feature description"

# Push to repository
git push origin feature/feature-name

# Create Pull Request on GitHub
# After review, merge to main
```

## Common Issues

### Models Not Loading
```bash
# Clear cache and reinstall
cd backend
rm -rf ~/.cache/huggingface
pip install --upgrade transformers torch
python run.py
```

### Port Conflicts
```bash
# Find process using port
lsof -ti:8000  # Backend
lsof -ti:5173  # Frontend

# Kill process
kill -9 <PID>
```

### Memory Issues
- Reduce batch size
- Use fewer models
- Increase available RAM
- Consider using GPU

### CORS Issues
- Check backend CORS configuration
- Verify frontend API URL
- Check browser console for detailed errors

## Performance Optimization

### Backend
```python
# Use async functions
async def process_text(text: str):
    return await model.process(text)

# Implement caching
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_operation():
    pass
```

### Frontend
```jsx
// Lazy load components
const Component = React.lazy(() => import('./Component'));

// Memoize expensive components
const MemoComponent = React.memo(Component);

// Optimize re-renders
useMemo(() => expensiveComputation(), [deps]);
```

## Code Style Guide

### Python
- Follow PEP 8
- Use type hints
- Document with docstrings
- Meaningful variable names

### JavaScript
- Use ES6+ syntax
- Prefer functional components
- Use descriptive names
- Add JSDoc comments

## Deployment to Development Server

```bash
# Railway
git push origin main  # Automatic deployment

# Docker
docker-compose up --build
```

## Monitoring During Development

### Backend Logs
```bash
cd backend
python run.py 2>&1 | tee logs.txt
```

### Frontend Console
- Open browser DevTools (F12)
- Check Console tab for errors
- Monitor Network tab for API calls

### Performance Monitoring
```javascript
// Frontend
const startTime = performance.now();
// ... operation
const endTime = performance.now();
console.log(`Time: ${endTime - startTime}ms`);
```

---

For production deployment, see [DEPLOYMENT.md](DEPLOYMENT.md).
