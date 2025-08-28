import streamlit as st
from app_pages import home, custom_urls, search_engine, doc_chat

# 🎨 Set Streamlit page configuration
st.set_page_config(page_title="AI Search Engine", page_icon="🔍", layout="wide")

# ----------------------------------Custom CSS for styling-----------------------------------------
st.markdown("""
    <style>
        /* Futuristic AI Search Engine Theme */
        .stApp {
            background: linear-gradient(rgba(17, 24, 39, 0.9), rgba(17, 24, 39, 0.9)), url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStFnheERaRBbImWaZsAzkib-yQ96evJQMWxA&s');
            background-size: cover;
            background-attachment: fixed;
            color: #ede9fe;
            font-family: 'Inter', sans-serif;
        }
        .main-container {
            background: linear-gradient(135deg, rgba(168, 85, 247, 0.85), rgba(6, 182, 212, 0.85));
            border-radius: 15px;
            padding: 30px;
            margin: 20px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
            border: 2px solid #f59e0b;
            backdrop-filter: blur(10px);
        }
        .main-title {
            font-size: 3.2em;
            font-weight: 700;
            color: #f59e0b;
            text-align: center;
            margin-bottom: 35px;
            text-shadow: 0 0 12px rgba(245, 158, 11, 0.8);
            animation: pulseGlow 2s ease-in-out infinite;
        }
        .section-title {
            font-size: 2.2em;
            font-weight: 600;
            color: #a855f7;
            margin: 40px 0 20px;
            text-shadow: 0 0 10px rgba(168, 85, 247, 0.8);
            border-left: 6px solid #a855f7;
            padding-left: 18px;
            animation: slideInLeft 0.6s ease-in-out;
        }
        .system-content {
            font-size: 2.2em;
            font-weight: 600;
            color: #06b6d4;
            text-align: center;
            text-shadow: 0 0 10px rgba(6, 182, 212, 0.8);
            animation: slideInLeft 0.6s ease-in-out;
        }
        .intro-title {
            font-size: 2.5em;
            color: #f59e0b;
            font-weight: bold;
            text-align: center;
        }
        .intro-subtitle {
            font-size: 1.5em;
            color: #a855f7;
            text-align: center;
            text-shadow: 0 0 8px rgba(168, 85, 247, 0.8);
        }
        .content {
            font-size: 1.15em;
            color: #ede9fe;
            line-height: 1.9;
            text-align: justify;
        }
        .highlight {
            color: #f59e0b;
            font-weight: bold;
        }
        .separator {
            height: 2px;
            background: linear-gradient(to right, #a855f7, #06b6d4);
            margin: 20px 0;
        }
        .stButton>button {
            background: linear-gradient(45deg, #a855f7, #06b6d4);
            color: #f59e0b;
            border-radius: 12px;
            padding: 14px 30px;
            font-weight: 600;
            font-size: 1.1em;
            border: none;
            box-shadow: 0 0 15px rgba(245, 158, 11, 0.8);
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #9333ea, #0891b2);
            box-shadow: 0 0 25px rgba(245, 158, 11, 1);
            transform: scale(1.1);
            color: #ede9fe;
        }
        .stButton>button::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300%;
            height: 300%;
            background: rgba(245, 158, 11, 0.2);
            transition: all 0.6s ease;
            transform: translate(-50%, -50%) scale(0);
            border-radius: 50%;
        }
        .stButton>button:hover::after {
            transform: translate(-50%, -50%) scale(1);
        }
        .stSelectbox, .stRadio, .stTextInput, .stTextArea {
            background: linear-gradient(135deg, rgba(168, 85, 247, 0.9), rgba(6, 182, 212, 0.9));
            border-radius: 10px;
            padding: 12px;
            border: 1px solid #f59e0b;
            color: #ede9fe;
            transition: all 0.3s ease;
        }
        .stSelectbox:hover, .stRadio:hover, .stTextInput:hover, .stTextArea:hover {
            border-color: #fbbf24;
            box-shadow: 0 0 8px rgba(245, 158, 11, 0.5);
        }
        .stSelectbox label, .stRadio label, .stTextInput label, .stTextArea label {
            color: #f59e0b;
            font-weight: 500;
        }
        .stSidebar {
            background: linear-gradient(135deg, rgba(168, 85, 247, 0.95), rgba(6, 182, 212, 0.95));
            border-right: 2px solid #f59e0b;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            padding: 20px;
        }
        .stSidebar .stRadio > label, .stSidebar .stSelectbox > label {
            color: #f59e0b;
            font-weight: 600;
        }
        .stSidebar [data-baseweb="radio"] {
            background: transparent;
            color: #ede9fe;
        }
        .stSidebar [data-baseweb="radio"] div {
            color: #ede9fe;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 1.3em;
            font-weight: 500;
            color: #ede9fe;
            padding: 15px 30px;
            border-radius: 12px 12px 0 0;
            transition: all 0.3s ease;
            background: linear-gradient(135deg, rgba(168, 85, 247, 0.9), rgba(6, 182, 212, 0.9));
        }
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: linear-gradient(45deg, #a855f7, #06b6d4);
            color: #f59e0b;
            font-weight: 600;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background: linear-gradient(135deg, #9333ea, #0891b2);
            color: #ede9fe;
        }
        .stDataFrame {
            border-radius: 10px;
            overflow: hidden;
            background-color: rgba(17, 24, 39, 0.95);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
        .stDataFrame table {
            color: #ede9fe;
        }
        .stMarkdown h3 {
            color: #f59e0b;
            font-weight: 600;
            text-shadow: 0 0 8px rgba(245, 158, 11, 0.8);
        }
        .stMarkdown a {
            color: #f59e0b;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s ease;
        }
        .stMarkdown a:hover {
            color: #a855f7;
            text-decoration: underline;
        }
        .source-card, .instructions-box {
            background: linear-gradient(135deg, rgba(168, 85, 247, 0.9), rgba(6, 182, 212, 0.9));
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            border-left: 5px solid #f59e0b;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
        .stExpander {
            background: linear-gradient(135deg, rgba(168, 85, 247, 0.9), rgba(6, 182, 212, 0.9));
            border-radius: 10px;
            border: 1px solid #f59e0b;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
        .stExpander summary {
            color: #f59e0b;
            font-weight: 600;
        }
        .stError, .stWarning, .stSuccess {
            background: linear-gradient(135deg, rgba(168, 85, 247, 0.9), rgba(6, 182, 212, 0.9));
            border-radius: 10px;
            border: 1px solid #f59e0b;
            color: #ede9fe;
        }
        .stError {
            border-left: 5px solid #ef4444;
        }
        .stWarning {
            border-left: 5px solid #f59e0b;
        }
        .stSuccess {
            border-left: 5px solid #06b6d4;
        }
        .footer {
            font-size: 0.95em;
            color: #ede9fe;
            margin-top: 50px;
            text-align: center;
            padding: 25px;
            background: linear-gradient(135deg, rgba(168, 85, 247, 0.85), rgba(6, 182, 212, 0.85));
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            border: 2px solid #f59e0b;
            backdrop-filter: blur(10px);
        }
        .footer a {
            color: #fbbf24;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s ease;
        }
        .footer a:hover {
            color: #a855f7;
            text-decoration: underline;
        }
        .content ul li::marker {
            color: #f59e0b;
        }
        /* Animations */
        @keyframes pulseGlow {
            0% { text-shadow: 0 0 10px rgba(245, 158, 11, 0.8); }
            50% { text-shadow: 0 0 20px rgba(245, 158, 11, 1); }
            100% { text-shadow: 0 0 10px rgba(245, 158, 11, 0.8); }
        }
        @keyframes slideInLeft {
            from { transform: translateX(-30px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        @keyframes scaleIn {
            from { transform: scale(0.95); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
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