# **AI-Powered Search Engine Documentation**

This notebook demonstrates how to build an AI-powered search engine using a combination of Google Custom Search API, Newspaper3k for article extraction, HuggingFace for embeddings, FAISS for vector search, and LangChain's Groq API for large language model (LLM) responses. The system performs the following tasks:

1. **Searches the Web**: Retrieves search results using Google Custom Search.
2. **Extracts Article Text**: Scrapes the full text of articles using Newspaper3k.
3. **Processes and Embeds Text**: Creates document embeddings for efficient vector-based search.
4. **Retrieves Relevant Information**: Searches for the most relevant document chunks based on user queries.
5. **Generates AI Responses**: Combines retrieved document chunks to generate structured AI-driven responses using LangChain’s Groq API.

---

## **1. Setup and Configuration**

The first part of the notebook initializes environment variables, imports necessary libraries, and sets up logging and API keys:

```python
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

google_search_key = os.getenv("GOOGLE_SEARCH_API_KEY")
search_engine_id = os.getenv("SEARCH_ENGINE_ID")
grok_api_key = os.getenv("LANGCHAIN_GROK_API_KEY")
hugginface_api_key = os.getenv("HUGGINFACE_LOGIN_API_KEY")
```

- **Environment Variables**: API keys are stored in a `.env` file for security and are loaded using the `dotenv` library.
- **Logging**: Warnings are suppressed to reduce noise in the output.

## **2. Google Search API Integration**

The `google_custom_search` function performs a search query using the **Google Custom Search API** and retrieves the top results. It returns a list of search result dictionaries containing titles, URLs, and snippets.

```python
from googleapiclient.discovery import build

def google_custom_search(query):
    service = build("customsearch", "v1", developerKey=google_search_key)
    result = service.cse().list(q=query, cx=search_engine_id, num=3).execute()
    
    search_results = []
    if "items" in result:
        for item in result["items"]:
            search_results.append({
                "title": item["title"],
                "link": item["link"],
                "snippet": item["snippet"]
            })
    
    return search_results
```

- **Input**: A user query string.
- **Output**: A list of dictionaries containing the title, link, and snippet of each search result.

---

## **3. Article Extraction Using Newspaper3k**

The `extract_full_article` function extracts the full text from a given URL using the **Newspaper3k** library. It limits the text to 5000 characters to avoid extremely long articles.

```python
from newspaper import Article

def extract_full_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text[:5000]  # Limit extracted text to 5000 characters
    except Exception as e:
        return f"Could not extract article: {str(e)}"
```

- **Input**: URL of the article.
- **Output**: The full article text (up to 5000 characters).

---

## **4. Displaying Search Results**

The `print_pretty_results` function formats and displays the search results in a readable manner using **Rich** for beautiful console output.

```python
from rich.console import Console
from rich.markdown import Markdown

def print_pretty_results(search_results, extracted_articles):
    for idx, result in enumerate(search_results):
        article_content = extracted_articles[idx][:500]  # Limit display to first 500 chars
        
        print("=" * 80)
        print(f"🔹 [Title]: {result['title']}\n")
        print(f"🔗 [URL]: {result['link']}\n")
        print(f"📝 [Snippet]: {result['snippet']}\n")
        print(f"📄 [Extracted Article]: {article_content}...\n")
        print("=" * 80)
```

- **Input**: A list of search results and corresponding extracted article texts.
- **Output**: A formatted display of search results, snippets, and extracted article content.

---

## **5. Text Processing and Chunking**

The text extracted from the articles is split into smaller chunks for embedding generation using the **RecursiveCharacterTextSplitter**. This ensures that each chunk is manageable for creating embeddings.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.create_documents(all_text)
```

- **Input**: A list of extracted texts.
- **Output**: A list of documents, each split into smaller chunks.

---

## **6. Embedding Generation**

The **SentenceTransformer** model is used to generate sentence embeddings for each chunk of text. The embeddings are then stored in a **FAISS** vector database for efficient similarity search.

```python
from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
texts = [doc.page_content for doc in documents]
text_embeddings = embedding_model.encode(texts)

vector_db = FAISS.from_documents(faiss_docs, HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
```

- **Input**: A list of document chunks.
- **Output**: A FAISS vector store containing the embeddings of all document chunks.

---

## **7. Vector Search for Relevant Chunks**

The `retrieve_relevant_chunks` function uses vector similarity search to retrieve the most relevant document chunks based on a user query. It calculates the query embedding and retrieves the top-k most similar document chunks.

```python
def retrieve_relevant_chunks(query, vector_db, embedding_model, top_k=3):
    query_embedding = embedding_model.encode([query])
    relevant_docs = vector_db.similarity_search_by_vector(query_embedding[0], top_k=top_k)
    return [doc.page_content for doc in relevant_docs]
```

- **Input**: A user query, FAISS vector database, and embedding model.
- **Output**: A list of the most relevant document chunks based on vector similarity.

---

## **8. Generating AI Responses Using Groq API**

The `stream_llm_response` function generates a structured and engaging AI response to the user query. It uses the **LangChain Groq API** to invoke a large language model (LLM) and produce a response based on the retrieved document chunks.

```python
from langchain_groq import ChatGroq

def stream_llm_response(query, retrieved_chunks):
    llm = ChatGroq(
        temperature=0,
        groq_api_key=grok_api_key,
        model_name="llama-3.3-70b-versatile"
    )
    
    context_text = "\n".join(retrieved_chunks)
    
    prompt = f"""
    🎯 You are an AI expert providing well-structured, **concise**, and **engaging** responses.
    
    🔍 **User Query:** {query}
    
    🔎 **Extracted Information from Trusted Sources:** 
    {context_text}
    
    ✨ **Task:** 
    - Highlight **key points** in **structured bullet points** ✅
    - Use **emojis** to enhance readability 🎭
    - Avoid unnecessary details 🚀
    - Ensure a **professional yet engaging tone** 🎤
    - Provide a **brief yet impactful conclusion** ✍️

    Now, generate the structured response with **emojis**.
    """
    
    return llm.invoke(prompt)
```

- **Input**: A user query and the retrieved document chunks.
- **Output**: A structured and engaging AI-generated response.

---

## **Conclusion**

This notebook demonstrates a comprehensive AI-powered search engine that integrates Google Search, web scraping, text embedding, vector search, and LLM-based response generation. It provides an effective way to retrieve and process information, then use AI to generate insightful, engaging responses based on real-time web data.

By combining these powerful tools, we have a highly flexible and scalable system capable of delivering personalized, AI-driven insights to users based on their queries.