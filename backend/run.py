#!/usr/bin/env python3
"""
Entry point for running the Humanizer API backend.
"""
import os
import sys
from pathlib import Path

# Add the app directory to the path
sys.path.insert(0, str(Path(__file__).parent))

import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Expose the ASGI application for platforms like Render that use `uvicorn run:app`
from app.main import app

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    reload = os.getenv("RELOAD", "false").lower() == "true"
    
    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )
