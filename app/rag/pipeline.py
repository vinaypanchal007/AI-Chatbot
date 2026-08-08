from fastapi import UploadFile
from app.rag.document_processor import process_document

async def general_chat(message: str):
    return {
        "mode" : "General Chat",
        "response" : f"Received message: {message}"
    }

async def rag_chat(message: str, file: UploadFile):

    text = await process_document(file)

    return {
        "message": message,
        "document_text": text
    }