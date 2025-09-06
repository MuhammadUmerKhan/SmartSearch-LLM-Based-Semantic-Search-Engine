from langchain_groq import ChatGroq
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from scripts.config import GROQ_API_KEY, EMBEDDING_MODEL
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def query_llm(query, retrieved_chunks, model_name):
    """
    Generates a structured response using LLM.

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
        🎯 You are an **AI expert** providing **concise, well-structured, and engaging** responses.

        🔍 **User Query:** {query}

        🔎 **Extracted Information from Trusted Sources:** 
        {context_text}

        ✨ **Response Guidelines:**  
        - Use **structured bullet points** ✅  
        - Highlight **key facts** with **emojis** 🎯  
        - Keep it **concise yet highly informative** 📌  
        - **No unnecessary filler text**—focus on **value-driven insights** 🚀  
        - Maintain a **professional yet engaging** tone 🎤  
        - End with a **brief but powerful conclusion** ✍️  

        Now, generate the structured response using **emojis** to enhance clarity and engagement.  
        """

        response = llm.invoke(prompt)
        logging.info("✅ LLM Response Generated Successfully.")
        return response

    except Exception as e:
        logging.error(f"❌ LLM Query Error: {str(e)}")
        return "❌ Error generating LLM response."
    
# ✅ Decorator to enable chat history
def enable_chat_history(func):
    """
    Decorator to handle chat history and UI interactions.
    Ensures chat messages persist across interactions.
    """
    current_page = func.__qualname__  # Get function name to track current chatbot session

    # Clear session state if model/chatbot is switched
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = current_page  # Store the current chatbot session
    if st.session_state["current_page"] != current_page:
        try:
            st.cache_resource.clear()  # Clear cached resources
            del st.session_state["current_page"]
            del st.session_state["messages"]
        except Exception:
            pass  # Ignore errors if session state keys do not exist

    # Initialize chat history if not already present
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    # Display chat history in the UI
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    def execute(*args, **kwargs):
        func(*args, **kwargs)  # Execute the decorated function

    return execute


def display_msg(msg, author):
    """
    Displays a chat message in the UI and appends it to session history.

    Args:
        msg (str): The message content to display.
        author (str): The author of the message ("user" or "assistant").
    """
    st.session_state.messages.append({"role": author, "content": msg})  # Store message in session
    st.chat_message(author).write(msg)  # Display message in Streamlit UI


def print_qa(cls, question, answer):
    """
    Logs the Q&A interaction for debugging and tracking.

    Args:
        cls (class): The calling class.
        question (str): User question.
        answer (str): Model response.
    """
    log_str = f"\nUsecase: {cls.__name__}\nQuestion: {question}\nAnswer: {answer}\n" + "-" * 50
    logging.info(log_str)  # Log the interaction using Streamlit's logger

@st.cache_resource
def configure_vector_embeddings():
    """
    Configures and caches the vector embeddings for Groq API.

    Returns:
        vector_embeddings (HuggingFaceEmbeddings): The loaded vector embeddings.
    """
    return HuggingFaceEmbeddings(
                model_name=EMBEDDING_MODEL,
                model_kwargs={"device": "cpu"},
                encode_kwargs={"normalize_embeddings": True}
            )  # Load and return the vector embeddings

def sync_st_session():
    """
    Ensures Streamlit session state values are properly synchronized.
    """
    for k, v in st.session_state.items():
        st.session_state[k] = v  # Sync all session state values