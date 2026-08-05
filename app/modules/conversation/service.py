from sqlalchemy.orm import Session

from app.modules.conversation.repository import ConversationRepository


class ConversationService:

    @staticmethod
    def save_user_message(
        db: Session,
        session_id: str,
        message: str
    ):
        return ConversationRepository.save_message(
            db=db,
            session_id=session_id,
            role="user",
            message=message
        )

    @staticmethod
    def save_ai_message(
        db: Session,
        session_id: str,
        message: str
    ):
        return ConversationRepository.save_message(
            db=db,
            session_id=session_id,
            role="assistant",
            message=message
        )

    @staticmethod
    def get_chat_history(
        db: Session,
        session_id: str
    ):

        messages = ConversationRepository.get_conversation(
            db=db,
            session_id=session_id
        )

        history = ""

        for msg in messages:
            history += f"{msg.role}: {msg.message}\n"

        return history