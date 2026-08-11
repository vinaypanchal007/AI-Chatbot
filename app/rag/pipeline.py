from fastapi import UploadFile
from app.rag.document_processor import process_document
from app.rag.chunker import chunk_text
from app.rag.text_cleaner import clean_text
from app.rag.embedding import create_embeddings
from app.rag.vector_db import store_embeddings
from app.rag.retriever import retrieve_chunks

async def general_chat(message: str):
    return {
        "mode" : "General Chat",
        "response" : f"Received message: {message}"
    }

async def rag_chat(message: str, file: UploadFile):
    text = await process_document(file)
    text = clean_text(text)
    chunks = chunk_text(text)
    embeddings = create_embeddings(chunks)
    store_embeddings(chunks,embeddings)
    relevant_chunks = retrieve_chunks(message)
    return {
        "mode": "RAG",
        "message": message,
        "chunks_count": len(chunks),
        "embeddings_count": len(embeddings)
    }