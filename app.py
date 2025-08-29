import streamlit as st
from app_pages import home, custom_urls, search_engine, doc_chat

# 🎨 Set Streamlit page configuration
st.set_page_config(page_title="AI Search Engine", page_icon="🔍", layout="wide")

# ----------------------------------Custom CSS for styling----------------------------------------- 
st.markdown("""
    <style>
        /* Professional Dark Theme */
        .stApp {
            background: linear-gradient(rgba(17, 24, 39, 0.95), rgba(17, 24, 39, 0.95)), url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStFnheERaRBbImWaZsAzkib-yQ96evJQMWxA&s');
            background-size: cover;
            background-attachment: fixed;
            color: #d1d5db;
            font-family: 'Inter', sans-serif;
        }
        .main-container {
            background: rgba(31, 41, 55, 0.95);
            border-radius: 8px;
            padding: 20px;
            margin: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            border: 1px solid #4b5563;
        }
        .main-title {
            font-size: 2.5em;
            font-weight: 600;
            color: #60a5fa;
            text-align: center;
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 1.8em;
            font-weight: 500;
            color: #60a5fa;
            margin: 20px 0 10px;
            padding-left: 10px;
            border-left: 4px solid #60a5fa;
        }
        .system-content {
            font-size: 1.8em;
            font-weight: 500;
            color: #60a5fa;
            text-align: center;
        }
        .intro-title {
            font-size: 2em;
            color: #60a5fa;
            font-weight: 600;
            text-align: center;
        }
        .intro-subtitle {
            font-size: 1.2em;
            color: #9ca3af;
            text-align: center;
        }
        .content {
            font-size: 1em;
            color: #d1d5db;
            line-height: 1.6;
            text-align: justify;
        }
        .highlight {
            color: #60a5fa;
            font-weight: 600;
        }
        .separator {
            height: 1px;
            background: #4b5563;
            margin: 15px 0;
        }
        .stButton>button {
            background: #60a5fa;
            color: #1f2937;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: 500;
            font-size: 1em;
            border: none;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background: #3b82f6;
            color: #ffffff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        .stSelectbox, .stRadio, .stTextInput, .stTextArea {
            background: #374151;
            border-radius: 6px;
            padding: 8px;
            border: 1px solid #4b5563;
            color: #d1d5db;
        }
        .stSelectbox:hover, .stRadio:hover, .stTextInput:hover, .stTextArea:hover {
            border-color: #60a5fa;
        }
        .stSelectbox label, .stRadio label, .stTextInput label, .stTextArea label {
            color: #9ca3af;
            font-weight: 500;
        }
        .stSidebar {
            background: #1f2937;
            border-right: 1px solid #4b5563;
            padding: 15px;
        }
        .stSidebar .stRadio > label, .stSidebar .stSelectbox > label {
            color: #60a5fa;
            font-weight: 500;
        }
        .stSidebar [data-baseweb="radio"] {
            background: transparent;
            color: #d1d5db;
        }
        .stSidebar [data-baseweb="radio"] div {
            color: #d1d5db;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 1.1em;
            font-weight: 500;
            color: #d1d5db;
            padding: 10px 20px;
            border-radius: 6px 6px 0 0;
            background: #374151;
        }
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: #60a5fa;
            color: #1f2937;
            font-weight: 600;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background: #4b5563;
            color: #ffffff;
        }
        .stDataFrame {
            border-radius: 6px;
            background-color: #1f2937;
            border: 1px solid #4b5563;
        }
        .stDataFrame table {
            color: #d1d5db;
        }
        .stMarkdown h3 {
            color: #60a5fa;
            font-weight: 500;
        }
        .stMarkdown a {
            color: #60a5fa;
            text-decoration: none;
            font-weight: 500;
        }
        .stMarkdown a:hover {
            color: #3b82f6;
            text-decoration: underline;
        }
        .source-card, .instructions-box {
            background: #374151;
            border-radius: 6px;
            padding: 10px;
            margin-bottom: 15px;
            border-left: 4px solid #60a5fa;
        }
        .stExpander {
            background: #374151;
            border-radius: 6px;
            border: 1px solid #4b5563;
        }
        .stExpander summary {
            color: #60a5fa;
            font-weight: 500;
        }
        .stError, .stWarning, .stSuccess {
            background: #374151;
            border-radius: 6px;
            border: 1px solid #4b5563;
            color: #d1d5db;
        }
        .stError {
            border-left: 4px solid #ef4444;
        }
        .stWarning {
            border-left: 4px solid #f59e0b;
        }
        .stSuccess {
            border-left: 4px solid #10b981;
        }
        .footer {
            font-size: 0.9em;
            color: #9ca3af;
            margin-top: 30px;
            text-align: center;
            padding: 15px;
            background: #1f2937;
            border-radius: 6px;
            border: 1px solid #4b5563;
        }
        .footer a {
            color: #60a5fa;
            text-decoration: none;
            font-weight: 500;
        }
        .footer a:hover {
            color: #3b82f6;
            text-decoration: underline;
        }
        .content ul li::marker {
            color: #60a5fa;
        }
    </style>
""", unsafe_allow_html=True)

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
st.sidebar.markdown('<div class="main-title">🔍 AI Search Engine</div>', unsafe_allow_html=True)
page = st.sidebar.radio("📌 **Select Page**", ["🏠 Home", "🔍 Search Engine", "🔗 Custom URL Search", "📄 Chat with Documents"])

# 🎯 Load Home Page
if page == "🏠 Home":
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    home.show_home()
    st.markdown('</div>', unsafe_allow_html=True)
# 🔍 Load Search Engine
elif page == "🔍 Search Engine":
    st.sidebar.markdown('<div class="section-title">🕵 Search Page</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    search_engine.search_engine()
    st.markdown('</div>', unsafe_allow_html=True)
# 🔗 Load Custom URL Search
elif page == "🔗 Custom URL Search":
    st.sidebar.markdown('<div class="section-title">🔗 Custom Search Engine</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    custom_urls.custom_url_search()
    st.markdown('</div>', unsafe_allow_html=True)
elif page == "📄 Chat with Documents":
    st.sidebar.markdown('<div class="section-title">📄 Document Chatbot</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    doc_chat.CustomDocChatbot()
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        Developed by <a href="https://portfolio-sigma-mocha-67.vercel.app/" target="_blank">Muhammad Umer Khan</a>. Powered by Advanced AI Models. 🧠
    </div>""", unsafe_allow_html=True)