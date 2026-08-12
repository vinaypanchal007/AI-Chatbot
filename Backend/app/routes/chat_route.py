from fastapi import APIRouter, Form, File, UploadFile
from typing import Optional
from app.rag.pipeline import general_chat, rag_chat

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
        return await rag_chat(
            message = message, 
            file = file
        )
    else:
        return await general_chat(
            message = message
        )