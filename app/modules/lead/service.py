from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.lead.repository import LeadRepository
from app.modules.lead.schema import LeadCreate


class LeadService:

    @staticmethod
    def create_lead(db: Session, lead: LeadCreate):
        return LeadRepository.create(db, lead)

    @staticmethod
    def get_all_leads(db: Session):
        return LeadRepository.get_all(db)

    @staticmethod
    def get_lead_by_id(db: Session, lead_id: int):
        lead = LeadRepository.get_by_id(db, lead_id)

        if not lead:
            raise HTTPException(
                status_code=404,
                detail="Lead not found"
            )

        return lead

    @staticmethod
    def update_lead(
        db: Session,
        lead_id: int,
        lead: LeadCreate
    ):
        updated_lead = LeadRepository.update(
            db,
            lead_id,
            lead
        )

        if not updated_lead:
            raise HTTPException(
                status_code=404,
                detail="Lead not found"
            )

        return updated_lead

    @staticmethod
    def delete_lead(
        db: Session,
        lead_id: int
    ):
        lead = LeadRepository.delete(
            db,
            lead_id
        )

        if not lead:
            raise HTTPException(
                status_code=404,
                detail="Lead not found"
            )

        return {
            "message": "Lead deleted successfully"
        }