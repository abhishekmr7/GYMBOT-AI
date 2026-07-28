from sqlalchemy.orm import Session

from app.modules.lead.model import Lead
from app.modules.lead.schema import LeadCreate


class LeadRepository:

    @staticmethod
    def create(db: Session, lead: LeadCreate):
        db_lead = Lead(
            gym_id=lead.gym_id,
            customer_name=lead.customer_name,
            phone=lead.phone,
            interested_in=lead.interested_in,
            source=lead.source,
            status=lead.status,
            notes=lead.notes
        )

        db.add(db_lead)
        db.commit()
        db.refresh(db_lead)

        return db_lead

    @staticmethod
    def get_all(db: Session):
        return db.query(Lead).all()

    @staticmethod
    def get_by_id(db: Session, lead_id: int):
        return (
            db.query(Lead)
            .filter(Lead.id == lead_id)
            .first()
        )

    @staticmethod
    def update(db: Session, lead_id: int, lead: LeadCreate):
        db_lead = (
            db.query(Lead)
            .filter(Lead.id == lead_id)
            .first()
        )

        if db_lead:
            db_lead.gym_id = lead.gym_id
            db_lead.customer_name = lead.customer_name
            db_lead.phone = lead.phone
            db_lead.interested_in = lead.interested_in
            db_lead.source = lead.source
            db_lead.status = lead.status
            db_lead.notes = lead.notes

            db.commit()
            db.refresh(db_lead)

        return db_lead

    @staticmethod
    def delete(db: Session, lead_id: int):
        db_lead = (
            db.query(Lead)
            .filter(Lead.id == lead_id)
            .first()
        )

        if db_lead:
            db.delete(db_lead)
            db.commit()

        return db_lead