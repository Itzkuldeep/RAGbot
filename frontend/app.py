import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Document Q&A System")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt"])
filename = uploaded_file.name if uploaded_file else None
if uploaded_file:
    files = {"file": uploaded_file}
    response = requests.post(f"{API_URL}/documents/upload/", files=files)
    # st.write("Raw Response:", response.text)
    if response.status_code == 200:
        st.success(response.json().get("message", "File uploaded successfully"))
    else:
        st.error(f"Error: {response.status_code}")
        st.error(response.text)

st.subheader("Ask a Question")
# filename = st.text_input("Enter document filename:")
question = st.text_area("Enter your question:")

if st.button("Ask"):
    response = requests.post(f"{API_URL}/questions/ask/", json={"filename": filename, "question": question})
    if response.status_code == 200:
        st.write("Answer:", response.json().get("answer", "No answer found"))
    else:
        st.error(f"Error: {response.status_code}")
        st.error(response.text)