import streamlit as st
from search.google_search import google_custom_search
from search.scraper import extract_full_article
from vector_db.vector_store import create_vector_db
from utils.utils import query_llm
from app_pages import instruction, home, custom_urls, search_engine, doc_chat

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
selected_llm = st.sidebar.selectbox("🤖 **Select an LLM Model**", list(available_llms.keys()))

# Store the selected LLM in session state
st.session_state["selected_llm"] = available_llms[selected_llm]

# 🏠 Sidebar Navigation
st.sidebar.title("**🔍 AI Search Engine**")
page = st.sidebar.radio("📌 **Select Page**", ["🏠 Home", "🔍 Search Engine", "🔗 Custom URL Search", "📄 Chat with Documents"])

# 🎯 Load Home Page
if page == "🏠 Home":
    home.show_home()
# 🔍 Load Search Engine
elif page == "🔍 Search Engine":
    st.sidebar.markdown("# **🕵 Search Page**")
    search_engine.search_engine()
# 🔗 Load Custom URL Search
elif page == "🔗 Custom URL Search":
    st.sidebar.markdown("# **🔗 Custom Search Engine**")
    custom_urls.custom_url_search()
elif page == "📄 Chat with Documents":
    doc_chat.run_doc_chat()