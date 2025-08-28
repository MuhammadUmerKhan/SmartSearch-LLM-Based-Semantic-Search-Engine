import streamlit as st

def CustomDocChatbot():
    st.markdown('<h1 class="main-title">📄 DocuMind AI: Smart PDF Question Answering System</h1>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content">
            If you want to chat with your document, please visit here: 
            <a href="https://langchain-chatbots.streamlit.app/chat_with_your_documents" target="_blank" class="highlight">
                📄 DocuMind AI
            </a>
        </div>
    """, unsafe_allow_html=True)

# Run chatbot when called from app.py
def run_doc_chat():
    obj = CustomDocChatbot()