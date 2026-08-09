import faiss
import numpy as np

index = None
def store_embeddings(embeddings):
    global index
    embeddings = np.array(embeddings).astype('float32')
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index