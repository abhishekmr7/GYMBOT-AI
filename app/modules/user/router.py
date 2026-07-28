from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.user.schema import UserCreate, UserLogin, UserResponse
from app.modules.user.service import UserService
from app.modules.user.schema import (
    UserCreate,
    UserResponse,
    UserLogin
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return UserService.create_user(db, user)


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    return UserService.login_user(
        db,
        user
    )