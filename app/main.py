from fastapi import FastAPI
from app.routes.chat_route import router as chat_route

app = FastAPI()

app.include_router(chat_route)