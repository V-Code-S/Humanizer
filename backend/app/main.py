"""
FastAPI application entry point.
Handles CORS, routes, and global middleware.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import routes
from app.routes.humanize import router as humanize_router

# Initialize FastAPI app
app = FastAPI(
    title="AI Text to Human Text Converter",
    description="Transform AI-generated text into natural, human-like writing",
    version="1.0.0"
)

# CORS Middleware configuration
allowed_origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:8000",
    os.getenv("FRONTEND_URL", "http://localhost:3000"),
    os.getenv("FRONTEND_URL_ALT", "http://localhost:5173"),
]

if os.getenv("ENV") == "production":
    allowed_origins.extend([
        os.getenv("PROD_FRONTEND_URL", "https://humanizer.vercel.app"),
    ])

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(humanize_router, prefix="/api", tags=["humanizer"])

# Root endpoint
@app.get("/", tags=["health"])
async def root():
    """Root endpoint - health check"""
    return {
        "status": "ok",
        "message": "AI Text to Human Text Converter API",
        "version": "1.0.0"
    }

@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "humanizer-api"
    }

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc)
        }
    )

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    print("🛑 Shutting down Humanizer API...")
