
import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.resume_parser import extract_text, extract_details

router = APIRouter(prefix="/api/v1/resume", tags=["Resume"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/parse")
async def parse_resume(file: UploadFile = File(...)):
    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in [".pdf", ".docx"]:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX allowed")

    file_path = os.path.join(UPLOAD_DIR, os.path.basename(file.filename))

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        text = extract_text(file_path)
        details = extract_details(text)

        return {
            "message": "Resume parsed successfully",
            "filename": file.filename,
            "extracted_details": details
        }

    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))

    finally:
        await file.close()
