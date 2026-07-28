from app.ai.embeddings import embeddings

vector = embeddings.embed_query(
    "What is MMA?"
)

print(len(vector))