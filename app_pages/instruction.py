import streamlit as st

def search_instruct():
    # ✅ Title with gradient effect
    st.markdown('<h1 class="main-title">🔍 AI-Powered Search Engine with LLMs 🤖</h1>', unsafe_allow_html=True)
    
    # 🎯 **Navigation Instructions**
    with st.expander("💬 **README** ⬇️"):
        st.markdown('<h1 class="intro-title">🔍 AI-Powered Search Engine with LLMs 🤖</h1>', unsafe_allow_html=True)
        st.markdown('<h2 class="section-title">💡 Example Queries</h2>', unsafe_allow_html=True)
        st.markdown("""
            <div class="content">
                <ul>
                    <li>🔍 What are the latest AI trends in 2025?</li>
                    <li>🚀 How does Quantum Computing impact AI?</li>
                    <li>🏆 Who are the top football players in 2025?</li>
                    <li>🛠 Best AI tools for developers in 2025?</li>
                    <li>🛒 How AI is transforming e-commerce?</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<h2 class="section-title">💬 How to Use</h2>', unsafe_allow_html=True)
        st.markdown("""
            <div class="content">
                <ul>
                    <li>1️⃣ <b>Enter Your Query</b> in the search box.</li>
                    <li>2️⃣ <b>Press Enter</b> to initiate the AI-powered search.</li>
                    <li>3️⃣ <b>Wait a few seconds</b> as the system fetches and processes results.</li>
                    <li>4️⃣ View <b>AI-generated responses</b> and <b>source links</b> for more details.</li>
                    <li>5️⃣ Click on any <b>source link</b> to read the full article.</li>
                </ul>
                📌 <b>Tip:</b> Be specific with your query for more accurate results!
            </div>
        """, unsafe_allow_html=True)

def custom_instruct():
    # ✅ Title with gradient effect
    st.markdown('<h1 class="main-title">🔗 Custom URL Search with LLMs 🤖</h1>', unsafe_allow_html=True)
    
    # 🎯 **Example Input**
    st.markdown('<h2 class="section-title">💡 Example URL Inputs</h2>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content">
            <ul>
                <li>🔗 https://example.com/article1</li>
                <li>🔗 https://www.donaldjtrump.com/</li>
                <li>🔗 https://en.wikipedia.org/wiki/Donald_Trump</li>
                <li>🔗 https://example.com/article2</li>
                <li>🔗 https://www.example.org/news/article</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-title">🚀 Example Search Queries</h2>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content">
            <ul>
                <li>🔍 What are the main points in Donald Trump's 2025 campaign?</li>
                <li>🔍 Summarize the latest news on AI advancements in 2025.</li>
                <li>🔍 How does the political landscape in the US affect global trade?</li>
                <li>🔍 What are the challenges faced by tech startups in 2025?</li>
                <li>🔍 Provide an analysis of recent changes in Wikipedia policies.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-title">💬 How to Use</h2>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content">
            <ul>
                <li>1️⃣ <b>Enter URLs</b> in the provided text area (one per line or multiple in a single line).</li>
                <li>2️⃣ <b>Click on "Extract & Search"</b> to initiate the process.</li>
                <li>3️⃣ <b>Wait a moment</b> while the system extracts content from the URLs.</li>
                <li>4️⃣ The extracted content is indexed into a <b>vector database</b> for efficient searching.</li>
                <li>5️⃣ <b>Enter your search query</b> in the search box and press Enter.</li>
                <li>6️⃣ View the <b>AI-powered answers</b> generated from the content of the URLs.</li>
                <li>7️⃣ <b>Review the search results</b> and explore the AI responses.</li>
            </ul>
            📌 <b>Tip:</b> Ensure URLs are valid and properly formatted for extraction to work correctly!
        </div>
    """, unsafe_allow_html=True)