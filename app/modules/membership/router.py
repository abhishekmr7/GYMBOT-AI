from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user

from app.modules.user.model import User

from app.modules.membership.schema import (
    MembershipCreate,
    MembershipResponse
)
from app.modules.membership.service import MembershipService

router = APIRouter(
    prefix="/memberships",
    tags=["Memberships"]
)


@router.post("/", response_model=MembershipResponse)
def create_membership(
    membership: MembershipCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return MembershipService.create_membership(db, membership)


@router.get("/", response_model=List[MembershipResponse])
def get_all_memberships(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return MembershipService.get_all_memberships(db)


@router.get("/{membership_id}", response_model=MembershipResponse)
def get_membership(
    membership_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return MembershipService.get_membership_by_id(db, membership_id)


@router.delete("/{membership_id}")
def delete_membership(
    membership_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return MembershipService.delete_membership(db, membership_id)