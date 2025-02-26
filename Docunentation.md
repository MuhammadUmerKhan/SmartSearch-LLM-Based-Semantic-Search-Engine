Here’s a **detailed documentation** for your project, explaining each file both **briefly** and **in detail**. 🚀  

---

# 📄 **Project Documentation: AI-Powered Search Engine**

## **📌 Overview**
This project is an **AI-powered search engine** that integrates **Google Search, web scraping, FAISS vector database, and LLMs (Llama 3.3-70B via Groq API)** to provide **structured, concise answers** to user queries. It is built with **Streamlit** for the UI and LangChain for LLM interaction.  

---

## **🗂️ File Structure**
```
📦 AI-Powered-Search-Engine
├── 📂 config
│   ├── config.py       # Stores API keys and constants
├── 📂 search
│   ├── google_search.py  # Fetches search results from Google API
│   ├── scraper.py       # Extracts full text from articles
├── 📂 vector_db
│   ├── vector_store.py  # Handles FAISS vector database
├── 📂 llm
│   ├── llm_handler.py   # Processes user query with LLaMA 3.3-70B
├── app.py              # Streamlit web app
├── home.py             # Homepage UI setup
├── requirements.txt    # Dependencies
├── .env                # Stores API keys (Not shared for security)
```

---

## **📌 Code Explanation for Each File**
### **1️⃣ `app.py` (Main Streamlit App)**
📌 **Brief:**  
- The main entry point for the **AI-powered search engine**.  
- Handles **UI**, **Google search integration**, **article scraping**, **vector search**, and **LLM processing**.  

📌 **Detailed Explanation:**
```python
import streamlit as st
import home
from search.google_search import google_custom_search
from search.scraper import extract_full_article
from vector_db.vector_store import create_vector_db
from llm.llm_handler import query_llm
```
- Imports the **home page**, **search engine**, **scraper**, **vector database**, and **LLM query handler**.

```python
st.set_page_config(page_title="AI Search Engine", page_icon="🔍", layout="wide")
```
- Configures Streamlit’s page title and layout.

```python
# Sidebar Navigation
st.sidebar.title("🔍 AI Search Engine")
page = st.sidebar.radio("📌 Select Page", ["🏠 Home", "🔎 Search Engine"])
```
- Creates a sidebar for **navigation** between "Home" and "Search Engine".

```python
if page == "🏠 Home":
    home.show_home()
```
- Loads the **home page**.

```python
elif page == "🔎 Search Engine":
    query = st.text_input("🔎 Ask Anything:", key="search_input")
```
- Loads the **search page** and provides a **search input field**.

```python
if query:
    search_results = google_custom_search(query)
    all_text = [extract_full_article(result["link"]) for result in search_results]
    vector_db = create_vector_db(all_text)
    retrieved_chunks = [doc.page_content for doc in vector_db.similarity_search(query, k=5)]
    ai_response = query_llm(query, retrieved_chunks)
```
- **Fetches search results** using Google API.  
- **Extracts article content** from URLs.  
- **Creates a FAISS vector database** for semantic search.  
- **Queries the LLM** for structured answers.

---

### **2️⃣ `home.py` (Home Page UI)**
📌 **Brief:**  
- Creates a **welcome page** with an introduction and feature list.  

📌 **Detailed Explanation:**
```python
import streamlit as st

def show_home():
    st.header("🚀 Welcome to the AI-Powered Search Engine")
```
- Displays the **main title** of the app.

```python
st.write("""
[![GitHub Repository](https://img.shields.io/badge/View%20Source%20Code-gray?logo=github)](https://github.com/MuhammadUmerKhan/AI-Powered-Search-Engine)
""")
```
- **Adds GitHub and LinkedIn buttons**.

```python
st.markdown("""
## 🌍 What is this AI-Powered Search Engine?
This project uses **Google Search, LLMs, and FAISS** to provide **real-time, AI-generated answers**.
""")
```
- **Describes project features and workflow**.

---

### **3️⃣ `google_search.py` (Google Search API)**
📌 **Brief:**  
- Uses **Google Custom Search API** to fetch **real-time web results**.  

📌 **Detailed Explanation:**
```python
from googleapiclient.discovery import build
from config.config import GOOGLE_SEARCH_KEY, SEARCH_ENGINE_ID, TOP_K_RESULTS
import logging
```
- **Imports the Google API client** and configuration settings.

```python
def google_custom_search(query):
    service = build("customsearch", "v1", developerKey=GOOGLE_SEARCH_KEY)
    result = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=TOP_K_RESULTS).execute()
```
- **Queries Google Search API** and retrieves results.

```python
search_results = [
    {"title": item["title"], "link": item["link"], "snippet": item["snippet"]}
    for item in result.get("items", [])
]
```
- Extracts **title, URL, and description** from the results.

---

### **4️⃣ `scraper.py` (Web Scraper)**
📌 **Brief:**  
- Uses `newspaper3k` to **extract full article content** from URLs.

📌 **Detailed Explanation:**
```python
from newspaper import Article

def extract_full_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text[:5000]
```
- **Downloads and extracts** full text from the **given URL**.  
- **Limits** extracted text to **5000 characters** to avoid long processing times.

---

### **5️⃣ `vector_store.py` (FAISS Vector Database)**
📌 **Brief:**  
- Converts **text into embeddings** and stores them in **FAISS** for fast retrieval.

📌 **Detailed Explanation:**
```python
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
```
- Uses **Hugging Face embeddings** to generate **vector representations**.

```python
def create_vector_db(texts):
    text_embeddings = embedding_model.embed_documents(texts)
    return FAISS.from_documents(texts, embedding_model)
```
- **Embeds document text** and stores it in **FAISS** for similarity search.

---

### **6️⃣ `llm_handler.py` (LLM Query Handler)**
📌 **Brief:**  
- Queries **Llama 3.3-70B** via **Groq API** for AI-generated answers.

📌 **Detailed Explanation:**
```python
from langchain_groq import ChatGroq

def query_llm(query, retrieved_chunks):
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=GROQ_API_KEY)
    context_text = "\n".join(retrieved_chunks)
```
- **Loads the LLM model** and **sends extracted text** as context.

```python
prompt = f"""
🔍 **User Query:** {query}
🔎 **Extracted Info:** {context_text}
📌 Generate an AI-powered structured response.
"""
response = llm.invoke(prompt)
```
- Generates **AI-powered responses** based on retrieved content.

---

## **🔗 Conclusion**
This documentation provides a **detailed breakdown** of each **file and functionality**. If you need **modifications** or **explanations for additional features**, let me know! 🚀