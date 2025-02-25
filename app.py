import streamlit as st
from search.google_search import google_custom_search
from search.scraper import extract_full_article
from vector_db.vector_store import create_vector_db
from llm.llm_handler import query_llm

st.title("🔍 AI-Powered Search Engine with LLMs 🤖")

query = st.text_input("Ask something about AI 🔎")
if st.button("Search"):
    search_results = google_custom_search(query)

    # Extract articles
    all_text = [extract_full_article(result["link"]) for result in search_results]

    # Create FAISS DB
    vector_db = create_vector_db(all_text)

    # Retrieve relevant chunks
    retrieved_chunks = [doc.page_content for doc in vector_db.similarity_search(query, k=5)]

    # Get LLM response
    ai_response = query_llm(query, retrieved_chunks)

    st.write("📌 **AI-Powered Answer:**")
    st.success(ai_response.content)

    # Display Sources
    st.write("🔗 **Sources:**")
    for result in search_results:
        st.markdown(f"- [{result['title']}]({result['link']})")
