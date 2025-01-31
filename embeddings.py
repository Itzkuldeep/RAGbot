import os
import json
import logging
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document as LangChainDocument
from langchain_ollama import OllamaEmbeddings
import numpy as np

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

STORAGE_PATH = "storage/embeddings/"

if not os.path.exists(STORAGE_PATH):
    os.makedirs(STORAGE_PATH)

def create_and_store_embeddings(file_name, file_content):
    logger.debug(f"Creating embeddings for {file_name}")

    document = LangChainDocument(page_content=file_content, metadata={"filename": file_name})
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents([document])
    vectorstore = Chroma.from_documents(documents=splits, embedding=OllamaEmbeddings(model="llama3.2:1b"))

    results = vectorstore.get(include=["embeddings", "metadatas"])
    embeddings = results.get("embeddings", [])
    if isinstance(embeddings, np.ndarray):
        embeddings = embeddings.tolist()

    file_path = os.path.join(STORAGE_PATH, f"{file_name}.json")
    with open(file_path, "w") as f:
        json.dump({"filename": file_name, "embeddings": embeddings}, f)

    logger.debug(f"Embeddings saved at {file_path}")
