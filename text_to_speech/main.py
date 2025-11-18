from fastapi import FastAPI, File, UploadFile
import io
import httpx
import os
from dotenv import load_dotenv
import boto3
from pypdf import PdfReader

load_dotenv()

app = FastAPI()

polly = boto3.client('polly')

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()

    return io.BytesIO(content)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
