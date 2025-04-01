import numpy as np
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from config.config import CHUNK_SIZE, CHUNK_OVERLAP
from utils.utils import configure_vector_embeddings
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

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

        text_embeddings = configure_vector_embeddings().embed_documents([doc.page_content for doc in documents])
        faiss_docs = [Document(page_content=text) for text in texts]

        logging.info("✅ Vector database created successfully.")
        return FAISS.from_documents(faiss_docs, configure_vector_embeddings())

    except Exception as e:
        logging.error(f"❌ Error creating vector DB: {str(e)}")
        return None