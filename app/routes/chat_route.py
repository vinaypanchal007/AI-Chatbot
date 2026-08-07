from fastapi import APIRouter, Form, File, UploadFile
from typing import Optional

router = APIRouter()

@router.post("/")
def home():
    return {"message": "Welcome to AI Chatbot"}

@router.post("/chat")
async def chat(
    message: str = Form(...),
    file: Optional[UploadFile] = File(None)
):
    if file:
        return {
            "mode": "RAG",
            "message": message,
            "filename": file.filename,
        }
    else:
        return {
            "mode": "LLM",
            "message": message,
        }