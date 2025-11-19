from fastapi import FastAPI, File, UploadFile, Response
from contextlib import asynccontextmanager
from convert import extract_pdf_from_bytes, synthesize_text_to_audio


app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()

    extracted_text = extract_pdf_from_bytes(content)

    audio = synthesize_text_to_audio(extracted_text)

    if audio:
        print("Audio received successfully")
        return Response(content=audio, media_type="audio/mpeg")
    else:
        print("No audio")
        return {"error": "could not synthesize audio"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
