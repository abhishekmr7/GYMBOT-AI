from sqlalchemy.orm import Session

from app.ai.rag import ask_gymbot
from app.modules.conversation.service import ConversationService


class ChatService:

    @staticmethod
    def ask_question(
        db: Session,
        session_id: str,
        question: str
    ):

        # Save user's message
        ConversationService.save_user_message(
            db=db,
            session_id=session_id,
            message=question
        )

        # Load previous conversation
        history = ConversationService.get_chat_history(
            db=db,
            session_id=session_id
        )

        # Ask the AI
        answer = ask_gymbot(
            question=question,
            history=history
        )

        # Save AI response
        ConversationService.save_ai_message(
            db=db,
            session_id=session_id,
            message=answer
        )

        return {
            "answer": answer
        }