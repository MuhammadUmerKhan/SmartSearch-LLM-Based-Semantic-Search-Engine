# 📄 **AI-Powered Search Engine – Complete Documentation**  

## **📌 Overview**
This project is an **AI-powered search engine** that integrates:  
✅ **Google Search API** for **real-time web search**  
✅ **Web Scraper** to extract **full article text**  
✅ **FAISS Vector Database** for **semantic search**  
✅ **Multiple LLMs (Llama 3, Gemma, Qwen, DeepSeek)** for **AI-powered responses**  
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
available_llms = {
    "Llama": "llama-3.3-70b-versatile",
    "Gemma": "gemma2-9b-it",
    "Qwen 2.5 Coder": "qwen-2.5-coder-32b",
    "Qwen 2.5": "qwen-2.5-32b",
    "DeepSeek R1 32b": "deepseek-r1-distill-qwen-32b",
    "DeepSeek R1 70b": "deepseek-r1-distill-llama-70b",
    "DeepSeek Qwen": "deepseek-r1-distill-qwen-32b"
}

selected_llm = st.sidebar.selectbox("🤖 Select an LLM Model", list(available_llms.keys()))
st.session_state["selected_llm"] = available_llms[selected_llm]
```
- **Adds a sidebar dropdown for users to select an LLM**.
- **Stores the selected LLM in `session_state` for use across the app**.

```python
if query:
    search_results = google_custom_search(query)
    all_text = [extract_full_article(result["link"]) for result in search_results]
    vector_db = create_vector_db(all_text)
    retrieved_chunks = [doc.page_content for doc in vector_db.similarity_search(query, k=5)]
    ai_response = query_llm(query, retrieved_chunks, model_name=st.session_state["selected_llm"])
```
- **Steps:**  
✅ **Google search** → ✅ **Scrape articles** → ✅ **Store in FAISS** → ✅ **Query LLM for answers**.

---

## **2️⃣ `llm_handler.py` (LLM Query Handler)**
📌 **Brief:**  
- **Handles multiple LLMs** (Llama, Gemma, Qwen, DeepSeek)  
- **Queries the selected LLM** for structured AI responses.  

📌 **Updated Code to Support Multiple LLMs:**
```python
from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY
import logging

def query_llm(query, retrieved_chunks, model_name):
    """
    Generates a structured response using the selected LLM.

    Args:
        query (str): User query.
        retrieved_chunks (list): Retrieved document chunks.
        model_name (str): Selected LLM model.

    Returns:
        str: AI-generated structured response.
    """
    try:
        logging.info(f"🤖 Querying LLM: {model_name}")
        llm = ChatGroq(
            temperature=0,
            groq_api_key=GROQ_API_KEY,
            model_name=model_name
        )

        context_text = "\n".join(retrieved_chunks)

        prompt = f"""
        🔍 **User Query:** {query}
        🔎 **Extracted Info:** {context_text}
        📌 Generate an AI-powered structured response.
        """

        response = llm.invoke(prompt)
        logging.info("✅ LLM Response Generated Successfully.")
        return response

    except Exception as e:
        logging.error(f"❌ LLM Query Error: {str(e)}")
        return "❌ Error generating LLM response."
```
- **Now supports multiple LLM models dynamically based on user selection**.
- **Uses `st.session_state["selected_llm"]` to determine the model**.

---

## **📌 Supported LLMs**
| Model | API Name |
|--------|-------------------------------|
| Llama | `llama-3.3-70b-versatile` |
| Gemma | `gemma2-9b-it` |
| Qwen 2.5 | `qwen-2.5-32b` |
| DeepSeek R1 32B | `deepseek-r1-distill-qwen-32b` |
| DeepSeek R1 70B | `deepseek-r1-distill-llama-70b` |
| DeepSeek Qwen | `deepseek-r1-distill-qwen-32b` |

---

## **🔗 Conclusion**
### ✅ **What's New in This Update?**
- **Users can select from multiple LLMs** via the sidebar.
- **LLM selection dynamically updates API requests**.
- **Supports more LLM models: Llama, Gemma, Qwen, DeepSeek**.

💡 **This update makes the search engine more powerful and customizable for different AI models.** 🚀