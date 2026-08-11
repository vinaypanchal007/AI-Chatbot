import os
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(os.environ.get("EMBEDDING_MODEL"))

def create_embeddings(chunks: list[str]):
    embeddings = model.encode(chunks)
    return embeddings