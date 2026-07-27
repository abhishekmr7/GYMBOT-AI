from sqlalchemy.orm import Session

from app.modules.gym.model import Gym
from app.modules.gym.schema import GymCreate


class GymRepository:

    @staticmethod
    def create(db: Session, gym: GymCreate):
        db_gym = Gym(
            name=gym.name,
            email=gym.email,
            phone=gym.phone,
            address=gym.address
        )

        db.add(db_gym)
        db.commit()
        db.refresh(db_gym)

        return db_gym

    @staticmethod
    def get_all(db: Session):
        return db.query(Gym).all()

    @staticmethod
    def get_by_id(db: Session, gym_id: int):
        return db.query(Gym).filter(Gym.id == gym_id).first()

    @staticmethod
    def delete(db: Session, gym_id: int):
        gym = db.query(Gym).filter(Gym.id == gym_id).first()

        if gym:
            db.delete(gym)
            db.commit()

        return gym