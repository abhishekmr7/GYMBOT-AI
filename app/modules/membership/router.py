from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.membership.schema import (
    MembershipCreate,
    MembershipResponse,
)
from app.modules.membership.service import MembershipService

router = APIRouter(
    prefix="/memberships",
    tags=["Memberships"]
)


@router.post("/", response_model=MembershipResponse)
def create_membership(
    membership: MembershipCreate,
    db: Session = Depends(get_db)
):
    return MembershipService.create_membership(db, membership)


@router.get("/", response_model=List[MembershipResponse])
def get_all_memberships(
    db: Session = Depends(get_db)
):
    return MembershipService.get_all_memberships(db)


@router.get("/{membership_id}", response_model=MembershipResponse)
def get_membership(
    membership_id: int,
    db: Session = Depends(get_db)
):
    return MembershipService.get_membership_by_id(
        db,
        membership_id
    )


@router.put("/{membership_id}", response_model=MembershipResponse)
def update_membership(
    membership_id: int,
    membership: MembershipCreate,
    db: Session = Depends(get_db)
):
    return MembershipService.update_membership(
        db,
        membership_id,
        membership
    )


@router.delete("/{membership_id}")
def delete_membership(
    membership_id: int,
    db: Session = Depends(get_db)
):
    return MembershipService.delete_membership(
        db,
        membership_id
    )