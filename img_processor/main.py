from fastapi import UploadFile, APIRouter, File
from process_img import process_image
router = APIRouter()

@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    content = await file.read()
    color_codes = process_image(content)

    return {"Most common colors": color_codes}
