from langchain_core.prompts import ChatPromptTemplate

from app.ai.llm import llm
from app.ai.vector_store import vector_store


retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)


prompt = ChatPromptTemplate.from_template(
"""
You are an AI Receptionist for Knockout Fitness Gym.

Answer ONLY using the context below.

If the answer is not available in the context,
reply politely that you don't have that information.

Context:
{context}

Question:
{question}
"""
)


def ask_gymbot(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content