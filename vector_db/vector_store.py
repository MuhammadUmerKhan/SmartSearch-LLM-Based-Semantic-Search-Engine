import numpy as np
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from config.config import CHUNK_SIZE, CHUNK_OVERLAP
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_vector_db(texts):
    """
    Create FAISS vector database from extracted texts.
    
    Args:
        texts (list): List of extracted article texts.

    Returns:
        FAISS vector store.
    """
    try:
        logging.info("📚 Creating Vector Database...")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        documents = text_splitter.create_documents(texts)

        text_embeddings = embedding_model.embed_documents([doc.page_content for doc in documents])
        faiss_docs = [Document(page_content=text) for text in texts]

        logging.info("✅ Vector database created successfully.")
        return FAISS.from_documents(faiss_docs, embedding_model)

    except Exception as e:
        logging.error(f"❌ Error creating vector DB: {str(e)}")
        return None