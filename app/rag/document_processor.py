import io

from fastapi import UploadFile
from PyPDF2 import PdfReader
from io import BytesIO

async def process_document(file: UploadFile) -> str:
    if file.content_type == "text/plain":
        return await process_text(file)
    
    elif file.content_type == "application/pdf":
        return await process_pdf(file)
    
    else:
        return ValueError("Unsupported file type. Please upload a text or PDF file.")
    

async def process_text(file: UploadFile) -> str:
    context = await file.read()
    return context.decode("utf-8")

async def process_pdf(file: UploadFile) -> str:
    content = await file.read()
    pdf = PdfReader(BytesIO(content))
    text = ""
    
    for page in pdf.pages:
        page_text += page.extract_text()
        
        if page_text:
            text += page_text + "\n"
            
    return text