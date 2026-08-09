import faiss
import numpy as np

index = None
chunk_store = []

def store_embeddings(chunks, embeddings):
    global index, chunk_store
    chunk_store = chunks
    embeddings = np.array(embeddings).astype('float32')
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index