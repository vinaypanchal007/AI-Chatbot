from app.rag.embedding import create_embeddings
from app.rag.vector_db import vector_db

def retrieve_chunks(query: str, top_k: int= 3):
    
    #convert the user queries into vectors
    query_embedding = create_embeddings([query])
    
    #search FAISS index for the top_k search results
    _, positions = vector_db.index.search(
        query_embedding.astype('float32'),
        top_k
    )
    
    #gets the original chunks
    results = []
    
    for pos in positions[0]:
        if pos != -1:
            results.append(vector_db.chunk_store[pos])
    
    return results