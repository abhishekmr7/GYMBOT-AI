from langchain_core.prompts import ChatPromptTemplate

from app.ai.llm import llm
from app.ai.vector_store import vector_store


retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)


prompt = ChatPromptTemplate.from_template(
"""
You are GymBot AI, the AI receptionist of Knockout Fitness.

Use both the conversation history and the knowledge base to answer naturally.

Conversation History:
{history}

Knowledge Base:
{context}

Customer Question:
{question}

Answer naturally.

If the answer is not available in the knowledge base,
politely say that you don't know instead of guessing.
"""
)


def ask_gymbot(
    question: str,
    history: str
):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "history": history,
            "context": context,
            "question": question
        }
    )

    return response.content