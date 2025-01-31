import os
import json
import logging
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.schema import Document as LangChainDocument
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

logger = logging.getLogger(__name__)

STORAGE_PATH = "storage/embeddings/"
llm = OllamaLLM(model="llama3.2:1b", url="http://localhost:11434")

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the retrieved context to answer the question. "
    "If you don't know the answer, say so.\n\n{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)

def load_embeddings(file_name):
    file_path = os.path.join(STORAGE_PATH, f"{file_name}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return None

def handle_question_for_document(file_name, user_question):
    embedding_data = load_embeddings(file_name)
    print(embedding_data)
    if not embedding_data:
        return "Document not found or embeddings not generated."

    document = LangChainDocument(page_content=user_question, metadata={"filename": file_name})
    print(document)
    retriever = Chroma.from_documents([document], embedding=OllamaEmbeddings(model="llama3.2:1b")).as_retriever()
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    response = rag_chain.invoke({"input": user_question})
    return response["answer"]
