import streamlit as st

def show_home():
    """Displays the Home Page content"""

    # 🎯 **Main Header**
    st.markdown('<h1 class="main-title">🚀 Welcome to the AI-Powered Search Engine</h1>', unsafe_allow_html=True)

    # 🔗 **GitHub and LinkedIn Links**
    st.markdown("""
        <div class="content">
            <a href="https://github.com/MuhammadUmerKhan/AI-Powered-Search-Engine" target="_blank" class="highlight">🔗 View Source Code on GitHub</a><br>
            <a href="https://www.linkedin.com/in/muhammad-umer-khan-61729b260/" target="_blank" class="highlight">🔗 Connect with Muhammad Umer on LinkedIn</a>
        </div>
    """, unsafe_allow_html=True)

    # 📝 **Introduction**
    st.markdown('<h2 class="section-title">🌍 What is this AI-Powered Search Engine?</h2>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content">
            This project is designed to <span class="highlight">fetch real-time search results</span>, extract <span class="highlight">key insights from web pages</span>, and use <span class="highlight">Large Language Models (LLMs)</span> to provide <span class="highlight">concise, structured answers</span> to your queries.
            <br><br>
            🔹 <b>How does it work?</b>
            <ul>
                <li><span class="highlight">🔍 Google Search</span>: Fetches the latest web search results using Google's custom search API, ensuring real-time and up-to-date information.</li>
                <li><span class="highlight">📄 Article Extraction</span>: Scrapes key content from relevant articles, summarizing the essential information for the query.</li>
                <li><span class="highlight">🧠 FAISS Vector Database</span>: Stores the extracted content in a vector database for efficient and relevant retrieval, ensuring fast and accurate results.</li>
                <li><span class="highlight">🤖 AI-Powered Answering</span>: Uses <b>Llama 3</b> or <b>Groq API</b> to generate insightful, concise answers, based on the retrieved content.</li>
            </ul>
            🎯 This tool is perfect for researchers, students, or professionals who need <span class="highlight">real-time, summarized, and structured information</span> at their fingertips.
        </div>
    """, unsafe_allow_html=True)

    # 🎭 **Features Section**
    st.markdown('<h2 class="section-title">✨ Key Features</h2>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content">
            <ul>
                <li><span class="highlight">🔍 Real-time Web Search</span>: Fetches the latest search results using Google Search API, ensuring you always get the most current information.</li>
                <li><span class="highlight">📄 Smart Article Scraper</span>: Extracts and condenses relevant sections from articles, highlighting key insights for your query.</li>
                <li><span class="highlight">🧠 FAISS Vector Database</span>: Stores and organizes the extracted content in a vector database, enabling efficient retrieval and similarity-based search.</li>
                <li><span class="highlight">🤖 LLM-Based Answering</span>: Leverages powerful AI models like <b>Llama 3</b> or <b>Groq API</b> to provide you with <span class="highlight">structured and concise answers</span> based on the search results.</li>
                <li><span class="highlight">🚀 Streamlit UI</span>: User-friendly interface that allows for easy interactions with the system, making the search process smooth and efficient.</li>
            </ul>
            💡 <b>Select 'Search Engine' from the sidebar to start searching!</b>
        </div>
    """, unsafe_allow_html=True)

    # 🎯 **Navigation Instructions**
    st.sidebar.markdown('<h2 class="section-title">🏠 Home Page</h2>', unsafe_allow_html=True)
    st.sidebar.markdown("""
        <div class="content">
            This is the <span class="highlight">Home Page</span>. To start searching, select the 
            <ul>
                <li><span class="highlight">🔍 Search Engine</span></li>
                <li><span class="highlight">🔗 Custom URL Search</span></li>
            </ul>
            options from the sidebar.
        </div>
    """, unsafe_allow_html=True)