from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def home():
#     return {
#         "message":"Welcome to AI Document Assistant",
#         "status":"successfully connected"
#     }
    
@app.post("/chat")
def upload_file():
    return {
        "message":"File uploaded successfully",
        "status":"success"
    }