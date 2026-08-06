from fastapi import FastAPI
from routes.upload_routes import app as upload_routes

app = FastAPI()

app.include_router(upload_routes)
