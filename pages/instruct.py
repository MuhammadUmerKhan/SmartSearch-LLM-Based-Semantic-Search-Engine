import streamlit as st

def instruct():
    # 🎯 **Navigation Instructions**
    st.sidebar.markdown("## 🕵 Search Page")
    st.sidebar.markdown("""
    ### 💬 How to Use:
    1️⃣ **Enter Your Query** in the search box.  
    2️⃣ **Press Enter** to initiate the AI-powered search.  
    3️⃣ **Wait a few seconds** as the system fetches and processes results.  
    4️⃣ View **AI-generated responses** and **source links** for more details.  
    5️⃣ Click on any **source link** to read the full article.  

    📌 **Tip:** Be specific with your query for more accurate results!  
    """)

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