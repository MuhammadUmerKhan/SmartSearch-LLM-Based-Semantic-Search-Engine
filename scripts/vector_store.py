import faiss
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from scripts.config import CHUNK_SIZE, CHUNK_OVERLAP
from scripts.utils import configure_vector_embeddings
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class VectorStore:
    def __init__(self, index, documents):
        """
        Initialize the VectorStore with a FAISS index and documents.
        
        Args:
            index (faiss.Index): The FAISS index containing embeddings.
            documents (list): List of Document objects.
        """
        self.index = index
        self.documents = documents

    def similarity_search(self, query, k=4):
        """
        Perform similarity search using the FAISS index.
        
        Args:
            query (str): The query text.
            k (int): Number of top results to return.
            
        Returns:
            list: List of Document objects matching the query.
        """
        try:
            # Embed the query
            embeddings = configure_vector_embeddings()
            query_embedding = embeddings.embed_query(query)
            query_embedding = np.array([query_embedding]).astype('float32')
            
            # Search the FAISS index
            distances, indices = self.index.search(query_embedding, k)
            
            # Retrieve matching documents
            results = [self.documents[i] for i in indices[0] if i < len(self.documents)]
            logging.info(f"✅ Retrieved {len(results)} documents for query: {query}")
            return results
        except Exception as e:
            logging.error(f"❌ Error in similarity search: {str(e)}")
            return []

def create_vector_db(texts):
    """
    Create FAISS vector database from extracted texts using faiss-cpu.
    
    Args:
        texts (list): List of extracted article texts.

    Returns:
        VectorStore: Object containing FAISS index and documents, or None if creation fails.
    """
    try:
        # Validate and filter input texts
        valid_texts = [text for text in texts if isinstance(text, str) and text.strip()]
        if not valid_texts:
            logging.error("❌ No valid texts provided after filtering")
            for i, text in enumerate(texts):
                logging.debug(f"Text {i}: {text[:100] if text else 'None'}...")
            return None

        logging.info(f"📚 Creating Vector Database with {len(valid_texts)} valid texts...")

        # Split texts into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        documents = text_splitter.create_documents(valid_texts)
        if not documents:
            logging.error("❌ No documents created after text splitting")
            return None

        # Generate embeddings
        embeddings = configure_vector_embeddings()
        text_embeddings = embeddings.embed_documents([doc.page_content for doc in documents])
        if not text_embeddings:
            logging.error("❌ No embeddings generated")
            return None

        # Convert embeddings to numpy array
        embedding_array = np.array(text_embeddings).astype('float32')
        if embedding_array.size == 0:
            logging.error("❌ Embedding array is empty")
            return None

        # Create FAISS index
        dimension = embedding_array.shape[1]
        index = faiss.IndexFlatL2(dimension)  # L2 distance index
        index.add(embedding_array)  # Add embeddings to the index

        logging.info("✅ Vector database created successfully.")
        return VectorStore(index, documents)

    except Exception as e:
        logging.error(f"❌ Error creating vector DB: {str(e)}")
        return None