from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine
from app.modules.gym.model import Gym
from app.modules.gym.router import router as gym_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="AI Receptionist for Gyms",
    version=settings.APP_VERSION
)

app.include_router(gym_router)


@app.get("/")
def home():
    return {
        "status": "running",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION
    }