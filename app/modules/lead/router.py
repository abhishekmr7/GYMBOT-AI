from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.lead.schema import (
    LeadCreate,
    LeadResponse,
)
from app.modules.lead.service import LeadService

router = APIRouter(
    prefix="/leads",
    tags=["Leads"]
)


@router.post("/", response_model=LeadResponse)
def create_lead(
    lead: LeadCreate,
    db: Session = Depends(get_db)
):
    return LeadService.create_lead(db, lead)


@router.get("/", response_model=List[LeadResponse])
def get_all_leads(
    db: Session = Depends(get_db)
):
    return LeadService.get_all_leads(db)


@router.get("/{lead_id}", response_model=LeadResponse)
def get_lead(
    lead_id: int,
    db: Session = Depends(get_db)
):
    return LeadService.get_lead_by_id(
        db,
        lead_id
    )


@router.put("/{lead_id}", response_model=LeadResponse)
def update_lead(
    lead_id: int,
    lead: LeadCreate,
    db: Session = Depends(get_db)
):
    return LeadService.update_lead(
        db,
        lead_id,
        lead
    )


@router.delete("/{lead_id}")
def delete_lead(
    lead_id: int,
    db: Session = Depends(get_db)
):
    return LeadService.delete_lead(
        db,
        lead_id
    )