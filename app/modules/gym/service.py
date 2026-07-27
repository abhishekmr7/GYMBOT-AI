from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.gym.repository import GymRepository
from app.modules.gym.schema import GymCreate


class GymService:

    @staticmethod
    def create_gym(db: Session, gym: GymCreate):
        return GymRepository.create(db, gym)

    @staticmethod
    def get_all_gyms(db: Session):
        return GymRepository.get_all(db)

    @staticmethod
    def get_gym_by_id(db: Session, gym_id: int):
        gym = GymRepository.get_by_id(db, gym_id)

        if not gym:
            raise HTTPException(
                status_code=404,
                detail="Gym not found"
            )

        return gym

    @staticmethod
    def delete_gym(db: Session, gym_id: int):
        gym = GymRepository.delete(db, gym_id)

        if not gym:
            raise HTTPException(
                status_code=404,
                detail="Gym not found"
            )

        return {
            "message": "Gym deleted successfully"
        }