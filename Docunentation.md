You're right! Here’s the **complete documentation**, covering **all files** in detail. 🚀  

---

# 📄 **AI-Powered Search Engine – Complete Documentation**  

## **📌 Overview**
This project is an **AI-powered search engine** that integrates:  
✅ **Google Search API** for **real-time web search**  
✅ **Web Scraper** to extract **full article text**  
✅ **FAISS Vector Database** for **semantic search**  
✅ **Llama 3.3-70B (Groq API)** for **AI-powered responses**  
✅ **Streamlit** for a **user-friendly web interface**  

---

## **🗂️ Project Structure**
```
📂 AI-Powered-Search-Engine/
│── 📄 app.py             # Main Streamlit app
│── 📄 home.py            # Home page UI
│── 📄 google_search.py   # Google Search API integration
│── 📄 scraper.py         # Web scraping for full-text extraction
│── 📄 vector_store.py    # FAISS vector database for search
│── 📄 llm_handler.py     # Queries LLM for AI responses
│── 📄 config.py          # Configuration and API keys
│── 📄 requirements.txt   # Required Python packages
│── 📄 README.md          # Project overview & instructions
│── 📂 config/            # Stores API keys and environment variables
│── 📂 search/            # Google search & web scraping scripts
│── 📂 vector_db/         # FAISS storage for semantic search
│── 📂 llm/               # LLM query handler
```

---

## **📌 File-by-File Code Explanation**
Each file is explained **briefly** and **in detail**.

---

## **1️⃣ `app.py` (Main Application)**
📌 **Brief:**  
- Main **Streamlit app** for the **AI search engine**  
- Handles **UI, search, article scraping, FAISS, and LLM**  

📌 **Detailed Explanation:**
```python
import streamlit as st
import home
from search.google_search import google_custom_search
from search.scraper import extract_full_article
from vector_db.vector_store import create_vector_db
from llm.llm_handler import query_llm
```
- **Imports** various modules including **Google Search API, web scraper, vector DB, and LLM handler**.

```python
st.set_page_config(page_title="AI Search Engine", page_icon="🔍", layout="wide")
```
- **Sets up the Streamlit UI** with a **custom page title and layout**.

```python
st.sidebar.title("🔍 AI Search Engine")
page = st.sidebar.radio("📌 Select Page", ["🏠 Home", "🔎 Search Engine"])
```
- **Creates a sidebar menu** for navigation.

```python
if query:
    search_results = google_custom_search(query)
    all_text = [extract_full_article(result["link"]) for result in search_results]
    vector_db = create_vector_db(all_text)
    retrieved_chunks = [doc.page_content for doc in vector_db.similarity_search(query, k=5)]
    ai_response = query_llm(query, retrieved_chunks)
```
- **Steps:**  
✅ **Google search** → ✅ **Scrape articles** → ✅ **Store in FAISS** → ✅ **Query LLM for answers**.

---

## **2️⃣ `home.py` (Home Page UI)**
📌 **Brief:**  
- **Displays project information, features, and navigation instructions**.

📌 **Detailed Explanation:**
```python
import streamlit as st

def show_home():
    st.header("🚀 Welcome to the AI-Powered Search Engine")
```
- **Displays a welcome message**.

```python
st.write("""
[![GitHub Repository](https://img.shields.io/badge/View%20Source%20Code-gray?logo=github)](https://github.com/MuhammadUmerKhan/AI-Powered-Search-Engine)
""")
```
- **Adds GitHub & LinkedIn buttons**.

```python
st.markdown("""
## 🌍 What is this AI-Powered Search Engine?
It uses **Google Search, FAISS, and LLMs** to provide **real-time, AI-generated answers**.
""")
```
- **Explains how the system works**.

---

## **3️⃣ `google_search.py` (Google Search API)**
📌 **Brief:**  
- Uses the **Google Custom Search API** to **fetch search results**.

📌 **Detailed Explanation:**
```python
from googleapiclient.discovery import build
from config.config import GOOGLE_SEARCH_KEY, SEARCH_ENGINE_ID, TOP_K_RESULTS
```
- **Imports API keys** from `config.py`.

```python
def google_custom_search(query):
    service = build("customsearch", "v1", developerKey=GOOGLE_SEARCH_KEY)
    result = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=TOP_K_RESULTS).execute()
```
- **Queries Google** for search results.

---

## **4️⃣ `scraper.py` (Web Scraper)**
📌 **Brief:**  
- Uses **`newspaper3k`** to **extract full-text content** from news articles.

📌 **Detailed Explanation:**
```python
from newspaper import Article

def extract_full_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text[:5000]
```
- **Downloads the article**, **extracts text**, and **limits it to 5000 characters**.

---

## **5️⃣ `vector_store.py` (FAISS Vector Database)**
📌 **Brief:**  
- **Converts extracted text into vector embeddings** and **stores them in FAISS**.

📌 **Detailed Explanation:**
```python
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
```
- **Uses Hugging Face embeddings** to **convert text into vectors**.

```python
def create_vector_db(texts):
    text_embeddings = embedding_model.embed_documents(texts)
    return FAISS.from_documents(texts, embedding_model)
```
- **Stores the text embeddings in FAISS** for **semantic search**.

---

## **6️⃣ `llm_handler.py` (LLM Query Handler)**
📌 **Brief:**  
- **Queries Llama 3.3-70B via Groq API** for **structured AI responses**.

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
- **Generates an AI-powered response** using **extracted web content**.

---

## **7️⃣ `config.py` (Configuration)**
📌 **Brief:**  
- **Loads API keys** and **stores constants**.

📌 **Detailed Explanation:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_SEARCH_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
GROQ_API_KEY = os.getenv("LANGCHAIN_GROK_API_KEY")
```
- **Loads API keys** securely using `.env`.

```python
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100
TOP_K_RESULTS = 3
```
- **Defines constants** for **text processing and search limits**.

---

## **🔗 Conclusion**
This documentation covers **every file** in **detail**. Let me know if you need **further refinements or enhancements**! 🚀