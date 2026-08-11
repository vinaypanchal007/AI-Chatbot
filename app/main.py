from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes.chat_route import router as chat_route

load_dotenv()

app = FastAPI()

app.include_router(chat_route)