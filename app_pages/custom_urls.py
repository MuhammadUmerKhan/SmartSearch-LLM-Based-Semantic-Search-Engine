import streamlit as st
import re
from scripts.scraper import extract_full_article
from scripts.vector_store import create_vector_db
from scripts.utils import query_llm
from app_pages.instruction import custom_instruct
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def split_urls(input_text):
    """
    Split a string containing multiple URLs into a list of valid URLs.
    
    Args:
        input_text (str): Input string containing URLs.
    
    Returns:
        list: List of valid URLs.
    """
    # Regex to find all valid URLs
    url_pattern = re.compile(r'https?://[^\s]+')
    return url_pattern.findall(input_text)

def custom_url_search():
    st.markdown('<div class="section-title">🔗 Custom URL Search</div>', unsafe_allow_html=True)
    custom_instruct()

    # Text area to allow users to enter multiple URLs
    urls = st.text_area("📌 **Enter URLs (one per line)**", placeholder="https://example.com/article1\nhttps://example.com/article2")

    if st.button("Extract & Search"):
        if not urls.strip():
            st.warning("⚠️ Please enter at least one URL.")
            return
        
        # Split the input URLs using the helper function
        urls_list = split_urls(urls)

        if not urls_list:
            st.warning("⚠️ No valid URLs found. Please enter valid URLs.")
            return

        with st.spinner("⏳ **Extracting content... Please wait!**"):
            # Extract texts and filter out None/empty results
            extracted_texts = [extract_full_article(url.strip()) for url in urls_list]
            valid_texts = [text for text in extracted_texts if text is not None and text.strip()]
            
            if not valid_texts:
                logging.error("❌ No valid texts extracted from provided URLs")
                st.error("⚠️ Could not extract meaningful content from the provided URLs. Please try different URLs.")
                return

            # Log extracted texts for debugging
            for i, text in enumerate(valid_texts):
                logging.info(f"Extracted text {i} (first 100 chars): {text[:100]}...")

            # Create a FAISS vector database from extracted content
            vector_db = create_vector_db(valid_texts)
            if vector_db is None:
                logging.error("❌ Failed to create vector database")
                st.error("⚠️ Failed to create vector database. Please try again with different URLs.")
                return

            st.session_state["custom_vector_db"] = vector_db  # Store for later searches
            st.success("✅ Content extracted and stored successfully!")

    # Search query input
    query = st.text_input("🔍 **Search within extracted content:**", placeholder="Enter your query")

    if query and "custom_vector_db" in st.session_state:
        with st.spinner("⏳ Searching..."):
            vector_db = st.session_state["custom_vector_db"]
            if vector_db is None:
                logging.error("❌ Vector database is None")
                st.error("⚠️ No vector database available. Please extract content first.")
                return

            retrieved_chunks = [doc.page_content for doc in vector_db.similarity_search(query, k=5)]
            if not retrieved_chunks:
                logging.warning("⚠️ No relevant chunks retrieved for query")
                st.warning("⚠️ No relevant content found for your query.")
                return

            # Get LLM response
            ai_response = query_llm(query, retrieved_chunks, model_name=st.session_state["llm_model"])
            formatted_response = ai_response.content.replace("**", "<b>").replace("**", "</b>")

            st.markdown('<h3 class="section-title">📌 AI-Powered Answer:</h3>', unsafe_allow_html=True)
            st.markdown(f"""
                <div class="source-card">
                    <p class="content">{formatted_response}</p>
                </div>
            """, unsafe_allow_html=True)