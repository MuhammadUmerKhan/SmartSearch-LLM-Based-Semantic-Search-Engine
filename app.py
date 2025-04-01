import streamlit as st
from search.google_search import google_custom_search
from search.scraper import extract_full_article
from vector_db.vector_store import create_vector_db
from llm.llm_handler import query_llm
from pages import instruct, home

# 🎨 Set Streamlit page configuration
st.set_page_config(page_title="AI Search Engine", page_icon="🔍", layout="wide")

available_llms = {
    "Llama": "llama-3.3-70b-versatile",
    "Gemma": "gemma2-9b-it",
    "Qwen 2.5": "qwen-2.5-32b",
    "DeepSeek R1 32b": "deepseek-r1-distill-qwen-32b",
    "DeepSeek R1 70b": "deepseek-r1-distill-llama-70b",
    "DeepSeek Qwen": "deepseek-r1-distill-qwen-32b"
}

# 🌟 **Sidebar: Select LLM**
selected_llm = st.sidebar.selectbox("🤖 Select an LLM Model", list(available_llms.keys()))

# Store the selected LLM in session state
st.session_state["selected_llm"] = available_llms[selected_llm]

# 🏠 Sidebar Navigation
st.sidebar.title("🔍 AI Search Engine")
page = st.sidebar.radio("📌 Select Page", ["🏠 Home", "🔍 Search Engine"])

# 🎯 Load Home Page
if page == "🏠 Home":
    home.show_home()

# 🔍 Load Search Engine
elif page == "🔍 Search Engine":
    # 🎯 **Navigation Instructions**
    instruct.instruct()

    # ⌨️ Real-Time Search Input (Press Enter to Search)
    query = st.text_input("🔎 Ask Anything:", key="search_input", placeholder="Enter your query")

    # ✅ Perform search automatically when user presses Enter
    if query:
        with st.spinner("⏳ Fetching results... Please wait!"):
            try:
                # 🔍 Google Search API Call
                search_results = google_custom_search(query)

                # 📄 Extract articles
                all_text = [extract_full_article(result["link"]) for result in search_results]

                # 🧠 Create FAISS Vector Database
                vector_db = create_vector_db(all_text)

                # 🔎 Retrieve relevant chunks
                retrieved_chunks = [doc.page_content for doc in vector_db.similarity_search(query, k=5)]

                # 🤖 Get LLM response
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
                # 🔗 Show Sources in Beautiful Cards
                st.markdown("<h3 style='color: #ff4d4d;'>🔗 Sources:</h3>", unsafe_allow_html=True)
                for result in search_results:
                    st.markdown(f"""
                        <div style="
                            padding: 12px;
                            border-radius: 8px;
                            margin-bottom: 10px;
                            border-left: 5px solid #ff4d4d;
                            ">
                            <b>🔹 {result['title']}</b><br>
                            <a href="{result['link']}" target="_blank">{result['link']}</a><br>
                            <i>{result['snippet']}</i>
                        </div>
                    """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"⚠️ An error occurred: {str(e)}")
