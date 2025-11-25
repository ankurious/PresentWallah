from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth, projects
import os

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PresentWallah - AI Document Creation",
    description="Professional AI-powered document and presentation generation platform",
    version="1.0.0"
)

# CORS middleware - allow all origins for simplicity (you can restrict later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Netlify, localhost, etc.)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(projects.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to PresentWallah - AI Document Creation Platform",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
