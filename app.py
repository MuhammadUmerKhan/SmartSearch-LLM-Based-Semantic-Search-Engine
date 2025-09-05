import streamlit as st, os
from app_pages import home, custom_urls, search_engine, doc_chat
from scripts.config import CSS_FILE_PATH

# 🎨 Set Streamlit page configuration
st.set_page_config(page_title="AI Search Engine", page_icon="🔍", layout="wide")

# ----------------------------------Custom CSS for styling----------------------------------------- 
# Path to the CSS file
try:
    # Check if the file exists
    if os.path.exists(CSS_FILE_PATH):
        # Read the CSS file
        with open(CSS_FILE_PATH, "r") as file:
            css_content = file.read()
        # Apply the CSS using st.markdown
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    else:
        st.error(f"⚠️ CSS file not found at: {CSS_FILE_PATH}")
except Exception as e:
    st.error(f"⚠️ Error reading CSS file: {str(e)}")

available_llms = {
    "Llama 3": "llama-3.3-70b-versatile",
    "Gemma": "gemma2-9b-it",
    "Qwen": "qwen/qwen3-32b",
    "Llama 4": "meta-llama/llama-4-scout-17b-16e-instruct",
    "GPT OSS 120B": "openai/gpt-oss-120b",
    "GPT OSS 20B": "openai/gpt-oss-20b"
}

# 🌟 **Sidebar: Select LLM**
selected_llm = st.sidebar.selectbox("🤖 **Select an LLM Model**", list(available_llms.keys()), key="selected_llm")
# Store the mapped LLM model in a different session state key
st.session_state["llm_model"] = available_llms[selected_llm]

# 🏠 Sidebar Navigation
st.sidebar.markdown('<div class="main-title"><h1>🔍 AI Search Engine</h1></div>', unsafe_allow_html=True)
page = st.sidebar.radio("📌 **Select Page**", ["🏠 Home", "🔍 Search Engine", "🔗 Custom URL Search", "📄 Chat with Documents"])

# 🎯 Load Home Page
if page == "🏠 Home":
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    home.show_home()
    st.markdown('</div>', unsafe_allow_html=True)
# 🔍 Load Search Engine
elif page == "🔍 Search Engine":
    st.sidebar.markdown('<div class="section-title"><h3>🕵 Search Page</h3></div>', unsafe_allow_html=True)
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    search_engine.search_engine()
    st.markdown('</div>', unsafe_allow_html=True)
# 🔗 Load Custom URL Search
elif page == "🔗 Custom URL Search":
    st.sidebar.markdown('<div class="section-title"><h3>🔗 Custom Search Engine</h3></div>', unsafe_allow_html=True)
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    custom_urls.custom_url_search()
    st.markdown('</div>', unsafe_allow_html=True)
elif page == "📄 Chat with Documents":
    doc_chat.CustomDocChatbot()
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        Developed by <a href="https://portfolio-sigma-mocha-67.vercel.app/" target="_blank">Muhammad Umer Khan</a>. Powered by Advanced AI Models. 🧠
    </div>""", unsafe_allow_html=True)