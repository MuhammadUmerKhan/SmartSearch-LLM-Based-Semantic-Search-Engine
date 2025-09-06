## 🧠 Project Components

### 1. `utils.py` 🛠️
- **Purpose**: Contains utility functions for configuring the LLM, managing embeddings, handling Streamlit session state, and logging Q&A interactions.
- **Key Functions**:
  - `query_llm(query, retrieved_chunks, model_name)`: Queries the Grok LLM with a structured prompt, combining user queries with retrieved document chunks to generate engaging, emoji-enhanced responses. 🎤
  - `configure_llm(model_name)`: Configures the Grok LLM using the `langchain_groq` library with the provided API key and model name.
  - `enable_chat_history(func)`: A decorator to persist chat history in Streamlit’s session state, ensuring seamless user interactions.
  - `display_msg(msg, author)`: Displays chat messages in the Streamlit UI and stores them in session state.
  - `print_qa(cls, question, answer)`: Logs Q&A interactions for debugging.
  - `configure_embedding_model()`: Loads and caches the `BAAI/bge-small-en-v1.5` model for generating text embeddings.
  - `configure_vector_embeddings()`: Configures HuggingFace embeddings for vector store creation.
  - `sync_st_session()`: Synchronizes Streamlit session state values.
- **Dependencies**: `langchain_groq`, `streamlit`, `sentence_transformers`, `logging`.

### 2. `config.py` ⚙️
- **Purpose**: Manages configuration settings and environment variables for the application.
- **Key Features**:
  - Loads API keys (`GOOGLE_SEARCH_API_KEY`, `SEARCH_ENGINE_ID`, `GROQ_API_KEY`) from a `.env` file using `dotenv`. 🔑
  - Defines constants: `CHUNK_SIZE` (1000), `CHUNK_OVERLAP` (100), `TOP_K_RESULTS` (3), `MAX_LENGTH` (5000).
  - Implements logging for configuration errors.
- **Dependencies**: `os`, `logging`, `dotenv`.

### 3. `google_search.py` 🔍
- **Purpose**: Handles web searches using the Google Custom Search API.
- **Key Functions**:
  - `google_custom_search(query)`: Performs a Google search with caching (`functools.lru_cache`) and returns the top results (title, URL, snippet). Filters results to `TOP_K_RESULTS` (3 by default).
- **Error Handling**: Catches and logs exceptions, returning an empty list if the search fails.
- **Dependencies**: `googleapiclient`, `logging`, `functools`.

### 4. `scraper.py` 📄
- **Purpose**: Extracts full-text content from URLs using the `newspaper3k` library.
- **Key Functions**:
  - `extract_full_article(url, max_length)`: Downloads and parses articles, returning text truncated to `MAX_LENGTH` (5000 characters). Validates URLs and ensures extracted text is meaningful (minimum 50 characters).
- **Error Handling**: Returns `None` for invalid URLs or empty content, with detailed logging for debugging.
- **Dependencies**: `newspaper`, `validators`, `logging`.

### 5. `vector_store.py` 🧠
- **Purpose**: Creates a FAISS vector database for semantic search using text embeddings.
- **Key Components**:
  - `VectorStore` class: Encapsulates a FAISS index and documents, providing a `similarity_search(query, k)` method to retrieve relevant document chunks.
  - `create_vector_db(texts)`: Builds a FAISS index from input texts using `faiss-cpu`. Filters invalid texts, splits texts into chunks, generates embeddings, and creates the vector store.
- **Error Handling**: Validates input texts, logs detailed errors, and returns `None` if creation fails.
- **Dependencies**: `faiss`, `numpy`, `langchain`, `logging`.

### 6. `custom_urls.py` 📌
- **Purpose**: Allows users to input custom URLs for content extraction and semantic search.
- **Key Functions**:
  - `split_urls(input_text)`: Uses regex to extract valid URLs from user input.
  - `custom_url_search()`: Provides a Streamlit UI for entering URLs, extracting content, creating a vector store, and querying the LLM with search results.
- **Features**:
  - Filters invalid texts and handles `None` vector stores to prevent errors.
  - Displays LLM responses in a formatted, emoji-enhanced UI.
- **Error Handling**: Shows user-friendly warnings for invalid URLs or failed extractions.
- **Dependencies**: `streamlit`, `re`, `logging`.

### 7. `search_engine.py` 🌐
- **Purpose**: Implements a web-based search engine using Google Custom Search.
- **Key Functions**:
  - `search_engine()`: Provides a Streamlit UI for real-time search queries, retrieves Google search results, extracts content, creates a vector store, and queries the LLM.
- **Features**:
  - Displays search results as formatted cards with titles, URLs, and snippets.
  - Handles errors gracefully with user-friendly messages.
- **Error Handling**: Filters invalid texts and checks for valid vector stores to avoid `NoneType` errors.
- **Dependencies**: `streamlit`, `logging`.