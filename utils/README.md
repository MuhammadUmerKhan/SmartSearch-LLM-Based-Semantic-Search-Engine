# Documentation for LangChain-Based Chatbot with Streamlit Integration

## Overview
This script integrates an AI chatbot using **LangChain**, **Groq LLM**, and **Streamlit** to enable interactive conversations. It includes functionalities such as LLM querying, chat history handling, logging, embedding configurations, and message synchronization.

## Features
- **LLM Querying**: Uses Groq API to generate structured responses.
- **Chat History Management**: Maintains persistent chat messages in Streamlit.
- **Session Handling**: Ensures a smooth user experience across interactions.
- **Logging**: Tracks interactions and errors for debugging.
- **Embeddings Configuration**: Loads sentence-transformer embeddings for NLP tasks.

---

## Dependencies
Ensure you have the following Python libraries installed before running the script:

```bash
pip install langchain streamlit sentence-transformers langchain_groq
```

---

## Configuration
The script requires an API key for **Groq API**. This is imported from `config/config.py`:
```python
from config.config import GROQ_API_KEY
```
Make sure to set up the `config.py` file with:
```python
GROQ_API_KEY = "your_api_key_here"
```

---

## Functions and Implementation

### 1. `query_llm(query, retrieved_chunks, model_name)`
Generates AI responses based on user queries and retrieved document chunks.

**Args:**
- `query (str)`: The user's question.
- `retrieved_chunks (list)`: Relevant extracted document chunks.
- `model_name (str)`: The LLM model to use.

**Returns:**
- `str`: AI-generated structured response.

**Functionality:**
1. Initializes the LLM model using **ChatGroq**.
2. Constructs a structured **prompt** with guidelines.
3. Queries the LLM and returns the response.
4. Logs the process and handles exceptions.

---

### 2. `configure_llm(model_name)`
Configures the LLM model for interaction.

**Args:**
- `model_name (str)`: The selected LLM model.

**Returns:**
- `ChatGroq` object: Configured LLM instance.

**Functionality:**
- Establishes the connection with Groq API.
- Logs and returns the LLM instance.

---

### 3. `enable_chat_history(func)`
A **decorator** that manages chat history and session handling.

**Functionality:**
1. Tracks the current chatbot session.
2. Clears session state when switching models.
3. Initializes and maintains chat history.
4. Displays chat messages in the Streamlit UI.

---

### 4. `display_msg(msg, author)`
Displays a chat message and appends it to session history.

**Args:**
- `msg (str)`: The chat message content.
- `author (str)`: The sender ("user" or "assistant").

**Functionality:**
- Stores messages in `st.session_state`.
- Displays them in the Streamlit UI.

---

### 5. `print_qa(cls, question, answer)`
Logs chatbot Q&A interactions for debugging.

**Args:**
- `cls (class)`: The calling class.
- `question (str)`: User's question.
- `answer (str)`: LLM's response.

**Functionality:**
- Formats and logs Q&A interactions.

---

### 6. `configure_embedding_model()`
Loads and caches a **sentence-transformer** model for embeddings.

**Returns:**
- `SentenceTransformer` object: Pretrained embeddings model.

**Functionality:**
- Loads `all-MiniLM-L6-v2` model for text similarity tasks.

---

### 7. `configure_vector_embeddings()`
Configures **vector embeddings** using Hugging Face models.

**Returns:**
- `HuggingFaceEmbeddings` object: Vector embeddings model.

**Functionality:**
- Loads `all-MiniLM-L6-v2` embeddings from Hugging Face.

---

### 8. `sync_st_session()`
Ensures all session state variables are synchronized properly.

**Functionality:**
- Iterates through `st.session_state` values and syncs them.

---

## Usage
To use this chatbot, run the script in **Streamlit**:
```bash
streamlit run app.py
```
This will launch an interactive UI for chatting with the AI model.

---

## Logging & Error Handling
- The script logs key interactions and errors using Python’s `logging` module.
- Errors are caught, logged, and displayed with appropriate messages.

---

## Conclusion
This script provides an **end-to-end AI chatbot** using **LangChain**, **Groq API**, and **Streamlit** with chat history, structured responses, and embedding support.

🚀 Ready to enhance your chatbot? Customize the prompt, tweak embeddings, or integrate advanced NLP features!

