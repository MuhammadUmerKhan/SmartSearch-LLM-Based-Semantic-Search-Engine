import streamlit as st

def CustomDocChatbot():
    st.header("📄 DocuMind AI: Smart PDF Question Answering System")
    st.markdown("If you want to chat with your document, please visit here: 📄[DocuMind AI](https://langchain-chatbots.streamlit.app/chat_with_your_documents)")

# Run chatbot when called from app.py
def run_doc_chat():
    obj = CustomDocChatbot()