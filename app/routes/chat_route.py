from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def home():
    return {"message": "Welcome to AI Chatbot"}

@router.post("/chat")
def chat():
    return {"message": "Chat route is working", "status": "success"}