import json

from langchain_core.prompts import ChatPromptTemplate

from app.ai.llm import llm


prompt = ChatPromptTemplate.from_template(
"""
You are an AI assistant.

Extract customer information from the conversation.

Return ONLY valid JSON.

JSON format:

{{
    "customer_name": "",
    "phone": "",
    "interested_in": ""
}}

Conversation:

{conversation}
"""
)


def extract_customer_info(conversation: str):

    chain = prompt | llm

    response = chain.invoke(
        {
            "conversation": conversation
        }
    )

    content = response.content.strip()

    # Remove markdown code fences if present
    if content.startswith("```json"):
        content = content.replace("```json", "").replace("```", "").strip()
    elif content.startswith("```"):
        content = content.replace("```", "").strip()

    try:
        return json.loads(content)

    except Exception as e:
        print("JSON Parsing Error:", e)
        print("LLM Response:")
        print(content)

        return {
            "customer_name": "",
            "phone": "",
            "interested_in": ""
        }