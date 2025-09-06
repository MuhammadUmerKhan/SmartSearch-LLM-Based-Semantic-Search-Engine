import streamlit as st
import PyPDF2
from scripts.vector_store import create_vector_db
from scripts.utils import query_llm, enable_chat_history, display_msg
from scripts.config import CHUNK_SIZE, CHUNK_OVERLAP
from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract_text_from_pdf(uploaded_file):
    """
    Extract text from an uploaded PDF file.
    
    Args:
        uploaded_file: Streamlit uploaded file object (PDF).
    
    Returns:
        str: Extracted text from the PDF, or None if extraction fails.
    """
    try:
        logging.info(f"📄 Extracting text from PDF: {uploaded_file.name}")
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        
        if not text.strip():
            logging.warning(f"⚠️ No meaningful content extracted from PDF: {uploaded_file.name}")
            return None
        
        logging.info(f"✅ Successfully extracted text from PDF: {uploaded_file.name}")
        return text
    except Exception as e:
        logging.error(f"❌ Error extracting text from PDF {uploaded_file.name}: {str(e)}")
        return None

@enable_chat_history
def CustomDocChatbot():
    """
    A Streamlit-based chatbot that processes uploaded PDFs and allows querying with LLM.
    Maintains chat history and integrates with existing vector database and LLM utilities.
    """
    st.markdown('<h1 class="main-title">📄 DocuMind AI: Smart PDF Question Answering System</h1>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content">
            Upload a PDF document in the sidebar and ask questions about its content. 
            The system will extract the text, create a vector database, and provide AI-powered answers.
        </div>
    """, unsafe_allow_html=True)

    # Sidebar for PDF upload
    with st.sidebar:
        st.markdown('<h3 class="section-title">📤 Upload PDF</h3>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
        
        if uploaded_file is not None:
            with st.spinner("⏳ **Processing PDF... Please wait!**"):
                # Extract text from the uploaded PDF
                pdf_text = extract_text_from_pdf(uploaded_file)
                if pdf_text is None:
                    st.error(f"⚠️ Could not extract meaningful content from {uploaded_file.name}. Please try another file.")
                    return

                # Split text into chunks
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
                documents = text_splitter.create_documents([pdf_text])
                
                # Create vector database
                vector_db = create_vector_db([pdf_text])
                if vector_db is None:
                    st.error("⚠️ Failed to create vector database. Please try again.")
                    return
                
                st.session_state["custom_vector_db"] = vector_db
                st.success(f"✅ PDF '{uploaded_file.name}' processed and indexed successfully!")

    # Chat input for querying
    if "custom_vector_db" in st.session_state:
        query = st.chat_input("🔍 Ask a question about the uploaded PDF:")
        if query:
            with st.spinner("⏳ **Searching and generating answer...**"):
                vector_db = st.session_state["custom_vector_db"]
                if vector_db is None:
                    logging.error("❌ Vector database is None")
                    st.error("⚠️ No vector database available. Please upload a PDF first.")
                    return

                # Retrieve relevant chunks
                retrieved_chunks = [doc.page_content for doc in vector_db.similarity_search(query, k=5)]
                if not retrieved_chunks:
                    logging.warning("⚠️ No relevant chunks retrieved for query")
                    st.warning("⚠️ No relevant content found for your query.")
                    return

                # Get LLM response
                ai_response = query_llm(query, retrieved_chunks, model_name=st.session_state.get("llm_model", "llama3-8b-8192"))
                formatted_response = ai_response.content
                # print(formatted_response)

                # Display user question and AI response
                display_msg(query, "user")
                display_msg(formatted_response, "assistant")
                
                # Render formatted response in a styled card
                # st.markdown(f"""
                #     <div class="source-card">
                #         <p class="content">{formatted_response}</p>
                #     </div>
                # """, unsafe_allow_html=True)

if __name__ == "__main__":
    CustomDocChatbot()