from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.gym.schema import GymCreate, GymResponse
from app.modules.gym.service import GymService

router = APIRouter(
    prefix="/gyms",
    tags=["Gyms"]
)


@router.post("/", response_model=GymResponse)
def create_gym(
    gym: GymCreate,
    db: Session = Depends(get_db)
):
    return GymService.create_gym(db, gym)


@router.get("/", response_model=List[GymResponse])
def get_all_gyms(
    db: Session = Depends(get_db)
):
    return GymService.get_all_gyms(db)


@router.get("/{gym_id}", response_model=GymResponse)
def get_gym(
    gym_id: int,
    db: Session = Depends(get_db)
):
    return GymService.get_gym_by_id(db, gym_id)


@router.delete("/{gym_id}")
def delete_gym(
    gym_id: int,
    db: Session = Depends(get_db)
):
    return GymService.delete_gym(db, gym_id)