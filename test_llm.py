from app.ai.llm import llm

response = llm.invoke(
    "Introduce yourself as an AI receptionist for an MMA gym."
)

print(response.content)