import streamlit as st
from app_pages import home, custom_urls, search_engine, doc_chat

# 🎨 Set Streamlit page configuration
st.set_page_config(page_title="AI Search Engine", page_icon="🔍", layout="wide")

available_llms = {
    "Llama 3": "llama-3.3-70b-versatile",
    "Gemma": "gemma2-9b-it",
    "Qwen": "qwen/qwen3-32b",
    "Llama 4": "meta-llama/llama-4-scout-17b-16e-instruct",
    "GPT OSS 120B": "openai/gpt-oss-120b",
    "GPT OSS 20B": "openai/gpt-oss-20b"
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
    doc_chat.CustomDocChatbot()