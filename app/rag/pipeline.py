async def general_chat(message: str):
    return {
        "mode" : "General Chat",
        "response" : f"Received message: {message}"
    }
    
async def rag_chat(message: str, file):
    return {
        "mode" : "RAG Chat",
        "filename" : file.filename,
        "response" : f"Received message: {message}"
    }