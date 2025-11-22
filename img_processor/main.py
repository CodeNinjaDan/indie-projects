from fastapi import FastAPI, UploadFile, File, Response
from fastapi.responses import RedirectResponse
from process_img import process_image

app = FastAPI()

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    content = await file.read()
    color_codes = process_image(content)

    return color_codes



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
