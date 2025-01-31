from fastapi import APIRouter
from pydantic import BaseModel
from retriever import handle_question_for_document

router = APIRouter()


class QuestionRequest(BaseModel):
    filename: str
    question: str

@router.post("/ask/")
async def ask_question(request: QuestionRequest):
    answer = handle_question_for_document(request.filename, request.question)
    return {"answer": answer}