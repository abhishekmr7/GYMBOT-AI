from fastapi import FastAPI
from app.modules.user.model import User
from app.core.config import settings
from app.core.database import Base, engine
from app.modules.lead.model import Lead
from app.modules.gym.model import Gym
from app.modules.membership.model import Membership
from app.modules.lead.router import router as lead_router
from app.modules.gym.router import router as gym_router
from app.modules.membership.router import router as membership_router
from app.modules.user.router import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="AI Receptionist for Gyms",
    version=settings.APP_VERSION
)

# Register Routers
app.include_router(gym_router)
app.include_router(membership_router)
app.include_router(lead_router)
app.include_router(user_router)

@app.get("/")
def home():
    return {
        "status": "running",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION
    }