from sqlalchemy.orm import Session

from app.modules.conversation.model import Conversation


class ConversationRepository:

    @staticmethod
    def save_message(
        db: Session,
        session_id: str,
        role: str,
        message: str
    ):

        conversation = Conversation(
            session_id=session_id,
            role=role,
            message=message
        )

        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        return conversation

    @staticmethod
    def get_conversation(
        db: Session,
        session_id: str,
        limit: int = 10
    ):

        return (
            db.query(Conversation)
            .filter(
                Conversation.session_id == session_id
            )
            .order_by(Conversation.created_at.asc())
            .limit(limit)
            .all()
        )