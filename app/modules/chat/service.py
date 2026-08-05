from sqlalchemy.orm import Session

from app.ai.rag import ask_gymbot
from app.ai.extractor import extract_customer_info
from app.ai.validator import validate_lead

from app.modules.conversation.service import ConversationService
from app.modules.lead.service import LeadService


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

        # Load conversation history
        history = ConversationService.get_chat_history(
            db=db,
            session_id=session_id
        )

        # Get AI response
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

        # Reload complete conversation
        updated_history = ConversationService.get_chat_history(
            db=db,
            session_id=session_id
        )

        # Extract lead information
        lead_data = extract_customer_info(updated_history)

        print("\n==============================")
        print("AI Lead Extraction")
        print("==============================")
        print(lead_data)

        is_valid = validate_lead(lead_data)

        print("Lead Valid:", is_valid)

        if is_valid:

            print("Creating AI Lead...")

            try:
                LeadService.create_ai_lead(
                    db=db,
                    gym_id=1,
                    data=lead_data
                )

                print("Lead Created Successfully!")

            except Exception as e:
                print("Lead Creation Failed:")
                print(e)

        else:
            print("Lead not created. Required information missing.")

        return {
            "answer": answer
        }