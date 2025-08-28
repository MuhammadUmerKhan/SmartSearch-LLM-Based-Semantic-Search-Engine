import streamlit as st
from scripts.google_search import google_custom_search
from scripts.scraper import extract_full_article
from scripts.vector_store import create_vector_db
from scripts.utils import query_llm
from app_pages.instruction import search_instruct
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def search_engine():
    st.markdown('<div class="section-title">🔍 Search Engine</div>', unsafe_allow_html=True)
    search_instruct()

    # ⌨️ Real-Time Search Input (Press Enter to Search)
    query = st.text_input("🔎 **Ask Anything:**", key="search_input", placeholder="Enter your query")

    # ✅ Perform search automatically when user presses Enter
    if query:
        with st.spinner("⏳ **Fetching results... Please wait!**"):
            try:
                # 🔍 Google Search API Call
                search_results = google_custom_search(query)
                if not search_results:
                    logging.error("❌ No search results found")
                    st.error("⚠️ No search results found for the query.")
                    return

                # 📄 Extract articles and filter valid texts
                all_text = [extract_full_article(result["link"]) for result in search_results]
                valid_texts = [text for text in all_text if text is not None and text.strip()]
                if not valid_texts:
                    logging.error("❌ No valid texts extracted from search results")
                    st.error("⚠️ Could not extract meaningful content from search results. Try a different query.")
                    return

                # Log extracted texts for debugging
                for i, text in enumerate(valid_texts):
                    logging.info(f"Extracted text {i} (first 100 chars): {text[:100]}...")

                # 🧠 Create FAISS Vector Database
                vector_db = create_vector_db(valid_texts)
                if vector_db is None:
                    logging.error("❌ Failed to create vector database")
                    st.error("⚠️ Failed to create vector database. Try a different query.")
                    return

                # 🔎 Retrieve relevant chunks
                retrieved_chunks = [doc.page_content for doc in vector_db.similarity_search(query, k=5)]
                if not retrieved_chunks:
                    logging.warning("⚠️ No relevant chunks retrieved for query")
                    st.warning("⚠️ No relevant content found for your query.")
                    return

                # 🤖 Get LLM response
                ai_response = query_llm(query, retrieved_chunks, model_name=st.session_state["llm_model"])
                formatted_response = ai_response.content.replace("**", "<b>").replace("**", "</b>")

                st.markdown('<h3 class="section-title">📌 AI-Powered Answer:</h3>', unsafe_allow_html=True)
                st.markdown(f"""
                    <div class="source-card">
                        <p class="content">{formatted_response}</p>
                    </div>
                """, unsafe_allow_html=True)

                # 🔗 Show Sources in Beautiful Cards
                st.markdown('<h3 class="section-title">🔗 Sources:</h3>', unsafe_allow_html=True)
                for result in search_results:
                    st.markdown(f"""
                        <div class="source-card">
                            <b class="highlight">🔹 {result['title']}</b><br>
                            <a href="{result['link']}" target="_blank">{result['link']}</a><br>
                            <i class="content">{result['snippet']}</i>
                        </div>
                    """, unsafe_allow_html=True)

            except Exception as e:
                logging.error(f"❌ Search pipeline error: {str(e)}")
                st.error(f"⚠️ An error occurred: {str(e)}")