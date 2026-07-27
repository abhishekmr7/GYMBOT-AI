from sqlalchemy.orm import Session

from app.modules.membership.model import Membership
from app.modules.membership.schema import MembershipCreate


class MembershipRepository:

    @staticmethod
    def create(db: Session, membership: MembershipCreate):
        db_membership = Membership(
            gym_id=membership.gym_id,
            name=membership.name,
            duration_months=membership.duration_months,
            price=membership.price,
            joining_fee=membership.joining_fee,
            description=membership.description,
            is_active=membership.is_active
        )

        db.add(db_membership)
        db.commit()
        db.refresh(db_membership)

        return db_membership

    @staticmethod
    def get_all(db: Session):
        return db.query(Membership).all()

    @staticmethod
    def get_by_id(db: Session, membership_id: int):
        return (
            db.query(Membership)
            .filter(Membership.id == membership_id)
            .first()
        )

    @staticmethod
    def update(db: Session, membership_id: int, membership: MembershipCreate):
        db_membership = (
            db.query(Membership)
            .filter(Membership.id == membership_id)
            .first()
        )

        if db_membership:
            db_membership.gym_id = membership.gym_id
            db_membership.name = membership.name
            db_membership.duration_months = membership.duration_months
            db_membership.price = membership.price
            db_membership.joining_fee = membership.joining_fee
            db_membership.description = membership.description
            db_membership.is_active = membership.is_active

            db.commit()
            db.refresh(db_membership)

        return db_membership

    @staticmethod
    def delete(db: Session, membership_id: int):
        db_membership = (
            db.query(Membership)
            .filter(Membership.id == membership_id)
            .first()
        )

        if db_membership:
            db.delete(db_membership)
            db.commit()

        return db_membership