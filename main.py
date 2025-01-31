from fastapi import FastAPI
from routes.document_routes import router as document_router
from routes.question_routes import router as question_router

app = FastAPI(title="Document Processing API")


@app.get("/")
def read_root():
    return {"message": "Welcome to the RAG-based document retrieval API!"}


app.include_router(document_router, prefix="/documents", tags=["Documents"])
app.include_router(question_router, prefix="/questions", tags=["Questions"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
