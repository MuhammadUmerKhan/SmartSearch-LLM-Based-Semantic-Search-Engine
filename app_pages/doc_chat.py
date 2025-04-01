import logging
import os
import numpy as np
from utils import utils
import streamlit as st
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.vectorstores import FAISS
from vector_db.vector_store import create_vector_db  
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document  

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

st.header("📄 DocuMind AI: Smart PDF Question Answering System")
st.write("Upload PDFs and ask questions based on their content.")

def save_file(self, file):
    """Save uploaded file to a temporary folder."""
    folder = "tmp"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, file.name)
    with open(file_path, "wb") as f:
        f.write(file.getvalue())
    return file_path

class CustomDocChatbot:
    """Chatbot for interacting with PDF documents using FAISS & RAG."""

    def __init__(self):
        utils.sync_st_session()
        self.llm = utils.configure_llm(model_name=st.session_state["selected_llm"])
        self.embedding_model = utils.configure_embedding_model()
        self.faiss_embeddings = utils.configure_vector_embeddings()

    def save_file(self, file):
        """Save uploaded PDF to a temporary folder."""
        folder = "tmp"
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getvalue())
        return file_path

    def setup_qa_chain(self, uploaded_files):
        """Processes multiple document formats and sets up Q&A retrieval system."""
        docs = []

        for file in uploaded_files:
            file_path = self.save_file(file)
            file_ext = file.name.split(".")[-1].lower()

            # Choose the correct loader based on file type
            if file_ext == "pdf":
                loader = PyPDFLoader(file_path)
            elif file_ext == "docx":
                loader = Docx2txtLoader(file_path)
            elif file_ext == "txt":
                loader = TextLoader(file_path)
            else:
                st.error(f"❌ Unsupported file format: {file_ext}")
                continue  # Skip unsupported files

            docs.extend(loader.load())

        if not docs:
            st.error("❌ No valid documents were loaded. Please upload supported file formats.")
            st.stop()

        # ✅ Process and store document chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)

        texts = [doc.page_content for doc in splits]

        # ✅ Generate embeddings
        text_embeddings = np.array(self.embedding_model.encode(texts))  

        # ✅ Convert texts into LangChain Document objects
        faiss_docs = [Document(page_content=text) for text in texts]

        # ✅ Initialize FAISS vector store
        vector_db = FAISS.from_documents(faiss_docs, self.faiss_embeddings)

        retriever = vector_db.as_retriever(search_type="mmr", search_kwargs={"k": 2, "fetch_k": 4})

        # ✅ Set up memory
        memory = ConversationBufferMemory(memory_key="chat_history", output_key="answer", return_messages=True)

        # ✅ Define retrieval-based QA system
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=retriever,
            memory=memory,
            return_source_documents=True,
            verbose=False
        )
        return qa_chain


    @utils.enable_chat_history  
    def main(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []  # ✅ Initialize messages list

        uploaded_files = st.sidebar.file_uploader(
            "📤 Upload Documents (PDF, DOCX, TXT)",
            type=["pdf", "docx", "txt"],
            accept_multiple_files=True
        )

        if not uploaded_files:
            st.error("Please upload PDF documents to continue!")
            st.stop()

        user_query = st.chat_input(placeholder="🔎 Ask something about your document!")

        if uploaded_files and user_query:
            qa_chain = self.setup_qa_chain(uploaded_files)
            utils.display_msg(user_query, "user")  

            with st.chat_message("assistant"):
                result = qa_chain.invoke({"question": user_query})  # Correct key usage
                response = result["answer"]
                st.write(response)  
                st.session_state.messages.append({"role": "assistant", "content": response})  # ✅ No more AttributeError
                utils.print_qa(CustomDocChatbot, user_query, response)


# Run chatbot when called from app.py
def run_doc_chat():
    obj = CustomDocChatbot()
    obj.main()
