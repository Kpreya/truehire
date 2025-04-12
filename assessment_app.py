"""
Assessment Application for TrueHire

This is a simplified version of the main application that focuses only on the
assessment functionality. This allows for easier testing and debugging.
"""

import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

# Import assessment routes
from assessment_routes import router as assessment_router, get_assessment_routes

# Create FastAPI app
app = FastAPI(title="TrueHire Assessment")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Include assessment routes
app.include_router(assessment_router)

# Add HTML routes
get_assessment_routes(app, templates)

# Home route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the home page that redirects to the assessment page"""
    return templates.TemplateResponse("index.html", {"request": request})

# Serve favicon
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Serve favicon"""
    return FileResponse("static/images/favicon.ico")

# Add standalone assessment route
@app.get("/assessment-standalone", response_class=HTMLResponse)
async def assessment_standalone(request: Request):
    """Serve the standalone assessment page"""
    return templates.TemplateResponse("assessment_standalone.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("assessment_app:app", host="127.0.0.1", port=8000, reload=True)
