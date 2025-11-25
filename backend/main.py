from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth, projects

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PresentWallah - AI Document Creation",
    description="Professional AI-powered document and presentation generation platform",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "https://*.netlify.app",  # Netlify deployments
        "https://*.render.com"     # Render deployments (if needed)
    ],
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
