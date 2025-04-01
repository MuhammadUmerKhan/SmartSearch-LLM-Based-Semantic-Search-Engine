import streamlit as st
import re
from search.scraper import extract_full_article
from vector_db.vector_store import create_vector_db
from llm.llm_handler import query_llm
from pages.instruct import custom_instruct

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
            extracted_texts = [extract_full_article(url.strip()) for url in urls_list]

            # Create a FAISS vector database from extracted content
            vector_db = create_vector_db(extracted_texts)
            st.session_state["custom_vector_db"] = vector_db  # Store for later searches

            st.success("✅ Content extracted and stored successfully!")

    # Search query input
    query = st.text_input("🔍 **Search within extracted content:**", placeholder="Enter your query")

    if query and "custom_vector_db" in st.session_state:
        with st.spinner("⏳ Searching..."):
            vector_db = st.session_state["custom_vector_db"]
            retrieved_chunks = [doc.page_content for doc in vector_db.similarity_search(query, k=5)]

            # Get LLM response
            ai_response = query_llm(query, retrieved_chunks, model_name=st.session_state["selected_llm"])
            formatted_response = ai_response.content.replace("**", "<b>").replace("**", "</b>")

            st.markdown("<h3 style='color: #ff4d4d;'>📌 AI-Powered Answer:</h3>", unsafe_allow_html=True)
            st.markdown(f"""
                <div style="
                    padding: 15px;
                    border-radius: 10px;
                    margin-bottom: 20px;
                    border-left: 5px solid #ff4d4d;">
                    <p style="font-size: 18px;">{formatted_response}</p>
                </div>
            """, unsafe_allow_html=True)
