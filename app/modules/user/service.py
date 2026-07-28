from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.user.model import User
from app.modules.user.repository import UserRepository
from app.modules.user.schema import (
    UserCreate,
    UserLogin
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


class UserService:

    @staticmethod
    def create_user(db: Session, user: UserCreate):

        existing_username = UserRepository.get_by_username(
            db,
            user.username
        )

        if existing_username:
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

        existing_email = UserRepository.get_by_email(
            db,
            user.email
        )

        if existing_email:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        hashed_password = hash_password(user.password)

        db_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password,
            role="ADMIN",
            is_active=True
        )

        return UserRepository.create(
            db,
            db_user
        )

    @staticmethod
    def login_user(db: Session, user: UserLogin):

        db_user = UserRepository.get_by_username(
            db,
            user.username
        )

        if not db_user:
            raise HTTPException(
                status_code=401,
                detail="Invalid username or password"
            )

        if not verify_password(
            user.password,
            db_user.hashed_password
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid username or password"
            )

        access_token = create_access_token(
            {
                "sub": db_user.username
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }