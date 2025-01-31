# RAG-based Document Retrieval with Ollama

This project demonstrates a **Retrieval Augmented Generation (RAG)** approach to document processing and question-answering, using Ollama and various document processing tools. It allows you to upload a document, split it into smaller chunks, index those chunks, and use them to answer user queries.

---

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Architecture](#architecture)
- [Usage](#usage)
- [Examples](#examples)
- [File Structure](#file-structure)
- [License](#license)

---

## Introduction

This system leverages Ollama for natural language generation (NLG) and other tools to create a scalable document retrieval system. It follows the steps below to process documents and retrieve relevant information:

1. **Load**: Load documents into the system.
2. **Split**: Split large documents into smaller chunks for easier processing.
3. **Store**: Store the chunks in a vector database with embeddings to enable fast and efficient searching.
4. **Query**: Accept user queries and retrieve relevant chunks using embeddings for context-based answers.

---

## Setup

### Requirements

Ensure you have the following installed:

- **Python 3.7+**
- **FastAPI** for backend services
- **Streamlit** for frontend interaction
- **Ollama** (NLP model for querying)
- **Google Cloud** (for cloud storage and AI models)
- **Other Python libraries**: `requests`, `pymupdf`, `langchain`, `faiss`, `numpy`

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/rag-ollama.git
    cd rag-ollama
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Google Cloud Setup:**
    - Set up your Google Cloud project and enable the necessary APIs (Vertex AI, Google Cloud Storage).
    - Authenticate using a service account JSON key:
    
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="[PATH_TO_YOUR_SERVICE_ACCOUNT_JSON]"
    ```

---

## Architecture

The system follows a modular approach:

1. **Load**: 
   - Documents are uploaded and loaded using **Document Loaders**. This allows you to bring in PDF, TXT, or other document formats.

2. **Split**:
   - Text is split into smaller chunks using **Text Splitters**. This helps in breaking large documents into more manageable pieces that can fit within model's context window and be indexed for easier retrieval.

3. **Store**:
   - We use a **VectorStore** to store embeddings of the text chunks. These embeddings are used for fast search retrieval based on similarity, making the RAG setup effective for question answering.

4. **Retrieval and Query**:
   - User queries are processed to retrieve relevant document chunks, and answers are generated using **Ollama**'s API.

![System Architecture](path_to_image.png)  <!-- Change the image path when available -->

---

## Usage

### Backend (FastAPI)

1. **Run the FastAPI Backend:**

   ```bash
   uvicorn main:app --reload
   ```

2. **Upload Document**:
   - Users can upload documents using the `/upload/` endpoint. The documents are processed and stored on Google Cloud Storage.
   
   Example request:

   ```bash
   curl -X 'POST' \
   'http://localhost:8000/upload/' \
   -F 'file=@path_to_your_file.pdf'
   ```

   This will upload the document, extract text, split it into chunks, and store the chunks in a vector store.

### Frontend (Streamlit)

1. **Run the Streamlit UI:**

   ```bash
   streamlit run app.py
   ```

2. **Use the Interface**:
   - After uploading a document, type your query in the Streamlit interface, and the system will return the most relevant text chunks along with a generated answer based on the context.

   Example Query:

   - **Question**: “What is the purpose of the document?”
   - The system will retrieve relevant chunks and generate an answer using Ollama's model.

![Streamlit UI Example](pictures\app_code.png) <!-- Change the image path when available -->

---

## Examples

### Example 1: Upload a PDF and Query it

- **Upload** a PDF document through the Streamlit interface.
- **Ask** a question such as “What is the conclusion of the report?”.
- The system will return an answer based on the document content.

```bash
curl -X 'POST' \
  'http://localhost:8000/upload/' \
  -F 'file=@report.pdf'
```

The system processes the file, splits the content, stores embeddings, and returns the most relevant chunk.

### Example 2: Run a Query without Uploading New Documents

If the document is already uploaded and stored in the system, you can directly query it:

```python
import requests

response = requests.post("http://localhost:8000/questions/ask/", json={"question": "What are the main points of the document?"})
print(response.json())
```

This would return an answer generated from the already indexed documents.

---

## File Structure

```plaintext
rag-ollama/
├── main.py                # FastAPI backend with Google Cloud integration
├── routes/
│   └── document_routes.py  # Document upload and processing logic
├── uploaded_files/        # Temporary directory for uploaded files
├── embeddings.py           # Logic for creating and storing embeddings
├── extractor.py            # Text extraction from PDF/TXT
├── app.py                 # Streamlit frontend
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

### **Explanation:**

1. **Document Processing Flow**: The README clearly explains the steps involved in document processing, including loading, splitting, storing, and querying.
2. **Setup Instructions**: The README includes detailed setup instructions, including installation, Google Cloud setup, and running the FastAPI and Streamlit services.
3. **Code Snippets**: Examples of how to interact with the system, including uploading documents and querying them, are provided.
4. **System Architecture Diagram**: Placeholder image links are used for architecture and UI screenshots. You can replace these with actual images once you have them.
5. **File Structure**: The file structure section outlines the organization of your project files.

Once you have everything set up and working, you can replace the placeholders like `path_to_image.png` with the actual image paths, and modify the content based on any changes made to your project.

Let me know if you need additional changes or clarifications!