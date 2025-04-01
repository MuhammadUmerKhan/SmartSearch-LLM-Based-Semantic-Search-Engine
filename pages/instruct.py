import streamlit as st

def search_instruct():
    
    # ✅ Title with gradient effect
    st.markdown("""
        <h1 style="text-align: center;">
            🔍 AI-Powered Search Engine with LLMs 🤖
        </h1>
    """, unsafe_allow_html=True)
    
    # 🎯 **Navigation Instructions**
    with st.expander("💬 **README** ⬇️"):

        # ✅ Title with gradient effect
        st.markdown("""
            <h1 style="text-align: center;">
                🔍 AI-Powered Search Engine with LLMs 🤖
            </h1>
        """, unsafe_allow_html=True)

        # 🎨 Stylish Search Box
        st.markdown("""
            <style>
                .search-box {
                    font-size: 18px;
                    padding: 12px;
                    border-radius: 8px;
                    border: 2px solid #ff4d4d;
                    width: 100%;
                    background-color: #f9f9f9;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("### 💡 Example Queries:")
        st.markdown("""
        - 🔍 What are the latest AI trends in 2025?  
        - 🚀 How does Quantum Computing impact AI?  
        - 🏆 Who are the top football players in 2025?  
        - 🛠 Best AI tools for developers in 2025?  
        - 🛒 How AI is transforming e-commerce?  
        """)
        
        st.markdown("### 💬 How to Use:")
        st.markdown("""
        1️⃣ **Enter Your Query** in the search box.  
        2️⃣ **Press Enter** to initiate the AI-powered search.  
        3️⃣ **Wait a few seconds** as the system fetches and processes results.  
        4️⃣ View **AI-generated responses** and **source links** for more details.  
        5️⃣ Click on any **source link** to read the full article.  

        📌 **Tip:** Be specific with your query for more accurate results!  
        """)

def custom_instruct():
    
    # ✅ Title with gradient effect
    st.markdown("""
        <h1 style="text-align: center;">
            🔗 Custom URL-Based Search with AI 🤖
        </h1>
    """, unsafe_allow_html=True)
    
    # 🎯 **Navigation Instructions**
    with st.expander("💬 **README** ⬇️"):

        # 🎨 Stylish Instructions Box
        st.markdown("""
            <style>
                .instructions-box {
                    font-size: 18px;
                    padding: 15px;
                    border-radius: 8px;
                    border: 2px solid #ff4d4d;
                    width: 100%;
                    background-color: #f9f9f9;
                }
            </style>
        """, unsafe_allow_html=True)

        # 🎯 **Example Input**
        st.markdown("### 💡 Example URL Inputs:")
        st.markdown("""
        - 🔗 https://example.com/article1  
        - 🔗 https://www.donaldjtrump.com/  
        - 🔗 https://en.wikipedia.org/wiki/Donald_Trump  
        - 🔗 https://example.com/article2  
        - 🔗 https://www.example.org/news/article  
        """)

        st.markdown("""
        ### 🚀 Example Search Queries:
        - 🔍 What are the main points in Donald Trump's 2025 campaign?  
        - 🔍 Summarize the latest news on AI advancements in 2025.  
        - 🔍 How does the political landscape in the US affect global trade?  
        - 🔍 What are the challenges faced by tech startups in 2025?  
        - 🔍 Provide an analysis of recent changes in Wikipedia policies.  
        """)
        
        st.markdown("### 💬 How to Use:")
        st.markdown("""
        1️⃣ **Enter URLs** in the provided text area (one per line or multiple in a single line).  
        2️⃣ **Click on "Extract & Search"** to initiate the process.  
        3️⃣ **Wait a moment** while the system extracts content from the URLs.  
        4️⃣ The extracted content is indexed into a **vector database** for efficient searching.  
        5️⃣ **Enter your search query** in the search box and press Enter.  
        6️⃣ View the **AI-powered answers** generated from the content of the URLs.  
        7️⃣ **Review the search results** and explore the AI responses.  

        📌 **Tip:** Ensure URLs are valid and properly formatted for extraction to work correctly!  
        """)