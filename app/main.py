

from fastapi import FastAPI
from app.routers.resume import router as resume_router
from app.routers.auth import router as auth_router
from app.routers.verification import router as verification_router
from app.routers.profile import router as profile_router
from app.routers.dashboard import router as dashboard_router

app = FastAPI(
    title="TalentFlow",
    description="AI-Powered Resume Parser & Student Onboarding System",
    version="1.0.0"
)

app.include_router(resume_router)
app.include_router(auth_router)
app.include_router(verification_router)
app.include_router(profile_router)
app.include_router(dashboard_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to TalentFlow!",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
