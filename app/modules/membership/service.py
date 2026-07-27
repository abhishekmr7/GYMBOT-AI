from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.membership.repository import MembershipRepository
from app.modules.membership.schema import MembershipCreate


class MembershipService:

    @staticmethod
    def create_membership(db: Session, membership: MembershipCreate):
        return MembershipRepository.create(db, membership)

    @staticmethod
    def get_all_memberships(db: Session):
        return MembershipRepository.get_all(db)

    @staticmethod
    def get_membership_by_id(db: Session, membership_id: int):
        membership = MembershipRepository.get_by_id(db, membership_id)

        if not membership:
            raise HTTPException(
                status_code=404,
                detail="Membership not found"
            )

        return membership

    @staticmethod
    def update_membership(
        db: Session,
        membership_id: int,
        membership: MembershipCreate
    ):
        updated_membership = MembershipRepository.update(
            db,
            membership_id,
            membership
        )

        if not updated_membership:
            raise HTTPException(
                status_code=404,
                detail="Membership not found"
            )

        return updated_membership

    @staticmethod
    def delete_membership(db: Session, membership_id: int):
        membership = MembershipRepository.delete(db, membership_id)

        if not membership:
            raise HTTPException(
                status_code=404,
                detail="Membership not found"
            )

        return {
            "message": "Membership deleted successfully"
        }