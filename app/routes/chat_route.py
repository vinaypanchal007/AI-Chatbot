from fastapi import FastAPI

app = FastAPI()

@app.post("/chat")
def upload_file():
    return {
        "message":"File uploaded successfully",
        "status":"success"
    }