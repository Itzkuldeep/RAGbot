import os
from fastapi import APIRouter, UploadFile, File, Depends
from extractor import extract_text_from_pdf, extract_text_from_txt
from embeddings import create_and_store_embeddings
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join("uploads", file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    file_content = extract_text_from_pdf(file_path) if file.filename.endswith('.pdf') else extract_text_from_txt(file_path)
    create_and_store_embeddings(file.filename, file_content)

    return {"message": "File uploaded successfully"}
