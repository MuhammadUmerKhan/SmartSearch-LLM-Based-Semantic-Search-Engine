from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def query_llm(query, retrieved_chunks):
    """
    Generates a structured response using LLM.

    Args:
        query (str): User query.
        retrieved_chunks (list): Retrieved document chunks.

    Returns:
        str: AI-generated structured response.
    """
    try:
        logging.info("🤖 Querying LLM...")
        llm = ChatGroq(
            temperature=0,
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile"
        )

        # Combine retrieved text chunks
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
