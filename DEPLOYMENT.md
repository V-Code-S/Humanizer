# Deployment Guide

This guide provides step-by-step instructions for deploying the Humanizer application to production.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Backend Deployment](#backend-deployment)
3. [Frontend Deployment](#frontend-deployment)
4. [Database & Storage](#database--storage)
5. [Monitoring & Logging](#monitoring--logging)
6. [Troubleshooting](#troubleshooting)

## Prerequisites

- Git account and repository
- Docker installed locally
- Docker Hub account (for image repository)
- Railway/Render account (backend hosting)
- Vercel account (frontend hosting)
- Azure/AWS account (optional, for additional services)

## Backend Deployment

### Option 1: Railway (Recommended)

1. **Connect GitHub Repository**
   ```bash
   # Push code to GitHub
   git push origin main
   ```

2. **Create Project on Railway**
   - Go to [railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub"
   - Select your repository
   - Authorize Railway

3. **Configure Environment Variables**
   ```
   HOST=0.0.0.0
   PORT=8000
   ENV=production
   FRONTEND_URL=https://your-frontend.vercel.app
   PROD_FRONTEND_URL=https://your-frontend.vercel.app
   PARAPHRASE_MODEL=Vamsi/T5_Paraphrase_Paws
   HUMANIZATION_MODEL=google/flan-t5-large
   ```

4. **Configure Build Settings**
   - Set root directory: `backend`
   - Build command: `pip install -r requirements.txt`
   - Start command: `python run.py`

5. **Deploy**
   - Railway automatically deploys on commits
   - Monitor deployment in Railway dashboard

### Option 2: Render

1. **Create New Web Service**
   - Go to [render.com](https://render.com)
   - Click "New+" → "Web Service"
   - Connect your GitHub repository

2. **Configure Service**
   ```
   Name: humanizer-api
   Root Directory: backend
   Build Command: pip install -r requirements.txt
   Start Command: python run.py
   Instance Type: Standard (2 CPU, 4 GB RAM)
   ```

3. **Set Environment Variables**
   - Same as Railway configuration above

4. **Deploy**
   - Click "Deploy Service"
   - Render builds from your repository

### Option 3: Docker Hub & Cloud Run

1. **Build Docker Image**
   ```bash
   cd backend
   docker build -t yourusername/humanizer-backend:latest .
   docker push yourusername/humanizer-backend:latest
   ```

2. **Deploy to Google Cloud Run**
   ```bash
   gcloud run deploy humanizer-api \
     --image yourusername/humanizer-backend:latest \
     --platform managed \
     --region us-central1 \
     --set-env-vars ENV=production,FRONTEND_URL=https://your-frontend.vercel.app
   ```

## Frontend Deployment

### Option 1: Vercel (Recommended)

1. **Connect GitHub Repository**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Authorize Vercel

2. **Configure Project Settings**
   - Framework: React
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`

3. **Set Environment Variables**
   ```
   VITE_API_URL=https://your-api-domain.com/api
   ```

4. **Deploy**
   - Vercel automatically deploys on commits
   - View deployment status in Vercel dashboard

### Option 2: Netlify

1. **Connect GitHub Repository**
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Select GitHub and authorize

2. **Configure Build**
   ```
   Base directory: frontend
   Build command: npm run build
   Publish directory: frontend/dist
   ```

3. **Set Environment Variables**
   ```
   VITE_API_URL=https://your-api-domain.com/api
   ```

4. **Deploy**
   - Netlify deploys automatically on pushes

### Option 3: Static Hosting (AWS S3 + CloudFront)

1. **Build Frontend**
   ```bash
   cd frontend
   npm run build
   ```

2. **Upload to S3**
   ```bash
   aws s3 sync dist/ s3://your-bucket-name/
   ```

3. **Create CloudFront Distribution**
   - Origin: S3 bucket
   - Enable caching
   - Add custom domain

## Database & Storage

### Optional: Add PostgreSQL (for future features)

**Railway:**
```bash
# In Railway dashboard:
1. New → PostgreSQL
2. Configure environment variables
3. Connect to backend
```

**Render:**
```bash
# In Render dashboard:
1. New → PostgreSQL
2. Copy connection string
3. Set as DATABASE_URL environment variable
```

## Monitoring & Logging

### Railway/Render Monitoring

1. **View Logs**
   - Dashboard → Logs section
   - Real-time log streaming

2. **Set Up Alerts**
   - Configure notification for deployment failures
   - Set CPU/Memory alerts

3. **Uptime Monitoring**
   - Enable health checks
   - Configure ping intervals

### Application Logging

```python
# Backend logging is already configured in main.py
import logging
logger = logging.getLogger(__name__)
logger.info("Processing text...")
logger.error("Error occurred...")
```

### Third-Party Monitoring (Optional)

**Sentry (Error Tracking)**
```bash
pip install sentry-sdk
```

```python
import sentry_sdk

sentry_sdk.init(
    dsn="https://xxx@xxx.ingest.sentry.io/xxx",
    traces_sample_rate=1.0
)
```

## Production Checklist

- [ ] Environment variables configured
- [ ] CORS properly configured for production domains
- [ ] API rate limiting enabled
- [ ] HTTPS/SSL certificates installed
- [ ] Database backups configured (if applicable)
- [ ] Error logging and monitoring enabled
- [ ] Health checks configured
- [ ] Scalability settings adjusted
- [ ] CDN configured for frontend assets
- [ ] Caching policies set up
- [ ] Security headers configured
- [ ] API documentation updated with production URL

## Performance Optimization

### Backend

1. **Enable Caching**
   ```python
   from functools import lru_cache
   
   @lru_cache(maxsize=128)
   def expensive_operation():
       pass
   ```

2. **Async Operations**
   - Utilize FastAPI's async/await for non-blocking operations

3. **Database Connection Pooling**
   - Use connection pooling for database connections

### Frontend

1. **Production Build**
   ```bash
   npm run build  # Creates optimized dist/
   ```

2. **Enable Gzip Compression**
   - Automatically enabled on Vercel/Netlify

3. **Image Optimization**
   - Use appropriate image formats
   - Implement lazy loading

## Security Best Practices

1. **Environment Variables**
   - Never commit `.env` files
   - Use platform-specific secret management

2. **HTTPS**
   - Automatically enabled on Vercel, Railway, Render

3. **CORS**
   - Configure specific allowed origins
   - Review backend `main.py` CORS settings

4. **API Authentication** (Future)
   - Consider adding API keys for public endpoints
   - Implement JWT tokens for user accounts

5. **Rate Limiting** (Future)
   ```python
   from slowapi import Limiter
   
   limiter = Limiter(key_func=get_remote_address)
   @app.post("/api/humanize")
   @limiter.limit("10/minute")
   async def humanize_text(request: HumanizeRequest):
       pass
   ```

## Rollback Procedure

### Railway/Render

1. Go to deployment history
2. Identify previous stable deployment
3. Click "Redeploy" on that version
4. Confirm deployment

### Vercel

1. Go to Deployments tab
2. Click menu on previous deployment
3. Select "Promote to Production"

## Scaling Strategy

As traffic increases:

1. **Vertical Scaling**
   - Upgrade instance type (more CPU/RAM)
   - Increase available memory for models

2. **Horizontal Scaling**
   - Deploy multiple instances behind load balancer
   - Use auto-scaling groups

3. **Model Optimization**
   - Use model quantization
   - Cache frequent requests
   - Implement batch processing

## Cost Optimization

1. **Railway/Render Tiers**
   - Start with free tier during development
   - Upgrade based on usage

2. **CDN**
   - Vercel includes CDN
   - Use region-specific deployment

3. **Auto-scaling**
   - Configure to scale down during off-peak
   - Set minimum instances appropriately

## Troubleshooting

### Backend Issues

**Models not loading:**
```bash
# SSH into deployment
pip install transformers torch

# Download models manually
python -c "from transformers import AutoModel; AutoModel.from_pretrained('Vamsi/T5_Paraphrase_Paws')"
```

**Memory issues:**
- Upgrade instance type
- Reduce batch size
- Implement model quantization

**API timeouts:**
- Increase timeout settings
- Optimize text processing
- Implement request queuing

### Frontend Issues

**API connection errors:**
- Verify VITE_API_URL environment variable
- Check CORS configuration on backend
- Ensure backend is running

**Build failures:**
- Check Node version compatibility
- Clear node_modules and reinstall
- Review build logs

## Support

- **Documentation**: See [README.md](../README.md)
- **Issues**: GitHub Issues
- **Contact**: support@humanizer.app

---

For detailed architecture information, see [ARCHITECTURE.md](ARCHITECTURE.md).
