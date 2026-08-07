from fastapi import FastAPI
from app.routes.chat_route import app as upload_routes

app = FastAPI()

app.include_router(upload_routes)