import streamlit as st

def show_home():
    """Displays the Home Page content"""
    
    # Set Streamlit page configuration
    # st.set_page_config(page_title="AI-Powered Search Engine", page_icon='🔍', layout='wide')

    # 🎯 **Main Header**
    st.header("🚀 Welcome to the AI-Powered Search Engine")

    # 🔗 **GitHub and LinkedIn Links**
    st.write("""
    [![GitHub Repository](https://img.shields.io/badge/View%20Source%20Code-gray?logo=github)](https://github.com/MuhammadUmerKhan/AI-Powered-Search-Engine)
    [![LinkedIn](https://img.shields.io/badge/Muhammad%20Umer-blue?logo=linkedin&color=gray)](https://www.linkedin.com/in/muhammad-umer-khan-61729b260/)
    """)

    # 📝 **Introduction**
    st.markdown("""
    ## 🌍 What is this AI-Powered Search Engine?
    This project is designed to **fetch real-time search results**, extract **key insights from web pages**, and use **Large Language Models (LLMs)** to provide **concise, structured answers** to your queries.  

    🔹 **How does it work?**
    1. **🔍 Google Search**: Fetches the latest web search results.
    2. **📄 Article Extraction**: Scrapes key content from relevant articles.
    3. **🧠 FAISS Vector Database**: Stores and retrieves the most relevant chunks.
    4. **🤖 AI-Powered Answering**: Uses **Llama 3** or **Groq API** to generate insightful answers.

    🎯 This tool is perfect for researchers, students, or professionals who need **real-time, summarized, and structured information** at their fingertips.
    """)

    # 🎭 **Features Section**
    st.markdown("""
    ## ✨ Key Features:
    - **🔍 Real-time Web Search**: Fetches the latest search results using Google Search API.
    - **📄 Smart Article Scraper**: Extracts key information from search results.
    - **🧠 FAISS Vector Database**: Stores and retrieves the most relevant content.
    - **🤖 LLM-Based Answering**: Generates **concise, structured answers** with AI.
    - **🚀 Streamlit UI**: Easy-to-use interface for seamless interaction.

    💡 **Select 'Search Engine' from the sidebar to start searching!**
    """)

    # 🎯 **Navigation Instructions**
    st.sidebar.markdown("## 🏠 Home Page")
    st.sidebar.markdown("Navigate to the **Search Engine** from the sidebar to start searching!")
