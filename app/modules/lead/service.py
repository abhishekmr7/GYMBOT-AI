from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.lead.repository import LeadRepository
from app.modules.lead.schema import LeadCreate


class LeadService:

    @staticmethod
    def create_lead(
        db: Session,
        lead: LeadCreate
    ):
        return LeadRepository.create(
            db,
            lead
        )

    @staticmethod
    def get_all_leads(
        db: Session
    ):
        return LeadRepository.get_all(db)

    @staticmethod
    def get_lead_by_id(
        db: Session,
        lead_id: int
    ):
        lead = LeadRepository.get_by_id(
            db,
            lead_id
        )

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

    @staticmethod
    def create_ai_lead(
        db: Session,
        gym_id: int,
        data: dict
    ):

        print("\n==============================")
        print("AI Lead Creation")
        print("==============================")
        print(data)

        existing = LeadRepository.get_by_phone(
            db,
            data["phone"]
        )

        if existing:
            print("Lead already exists. Skipping creation.")
            return existing

        print("No existing lead found. Creating new lead...")

        lead = LeadCreate(
            gym_id=gym_id,
            customer_name=data["customer_name"],
            phone=data["phone"],
            interested_in=data["interested_in"],
            source="AI Chat",
            status="NEW",
            notes="Generated automatically by GymBot AI"
        )

        created = LeadRepository.create(
            db,
            lead
        )

        print("Lead inserted into database successfully!")

        return created