from fastapi import UploadFile
from app.rag.document_processor import process_document
from app.rag.chunker import chunk_text
from app.rag.text_cleaner import clean_text

async def general_chat(message: str):
    return {
        "mode" : "General Chat",
        "response" : f"Received message: {message}"
    }

async def rag_chat(message: str, file: UploadFile):
    text = await process_document(file)
    text = clean_text(text)
    chunks = chunk_text(text)
    return {
        "mode": "RAG",
        "message": message,
        "chunks": chunks
    }