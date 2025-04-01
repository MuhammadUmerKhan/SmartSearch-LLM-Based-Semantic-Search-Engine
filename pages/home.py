import streamlit as st

def show_home():
    """Displays the Home Page content"""

    # 🎯 **Main Header**
    st.markdown("""
        <h1 style="text-align: center;">
            🚀 Welcome to the AI-Powered Search Engine
        </h1>
    """, unsafe_allow_html=True)

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
    1. **🔍 Google Search**: Fetches the latest web search results using Google's custom search API, ensuring real-time and up-to-date information.
    2. **📄 Article Extraction**: Scrapes key content from relevant articles, summarizing the essential information for the query.
    3. **🧠 FAISS Vector Database**: Stores the extracted content in a vector database for efficient and relevant retrieval, ensuring fast and accurate results.
    4. **🤖 AI-Powered Answering**: Uses **Llama 3** or **Groq API** to generate insightful, concise answers, based on the retrieved content.

    🎯 This tool is perfect for researchers, students, or professionals who need **real-time, summarized, and structured information** at their fingertips.
    """)

    # 🎭 **Features Section**
    st.markdown("""
    ## ✨ Key Features:
    - **🔍 Real-time Web Search**: Fetches the latest search results using Google Search API, ensuring you always get the most current information.
    - **📄 Smart Article Scraper**: Extracts and condenses relevant sections from articles, highlighting key insights for your query.
    - **🧠 FAISS Vector Database**: Stores and organizes the extracted content in a vector database, enabling efficient retrieval and similarity-based search.
    - **🤖 LLM-Based Answering**: Leverages powerful AI models like **Llama 3** or **Groq API** to provide you with **structured and concise answers** based on the search results.
    - **🚀 Streamlit UI**: User-friendly interface that allows for easy interactions with the system, making the search process smooth and efficient.

    💡 **Select 'Search Engine' from the sidebar to start searching!**
    """)

    # 🎯 **Navigation Instructions**
    st.sidebar.markdown("## 🏠 Home Page")
    st.sidebar.markdown("""
    This is the **Home Page**. To start searching, select the 
    - **🔍 Search Engine**
    - **🔗 Custom URL Search** 
    <br>
    options from the sidebar.
    """, unsafe_allow_html=True)
