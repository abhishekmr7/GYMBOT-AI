from app.ai.rag import ask_gymbot


class ChatService:

    @staticmethod
    def ask_question(question: str):

        answer = ask_gymbot(question)

        return {
            "answer": answer
        }