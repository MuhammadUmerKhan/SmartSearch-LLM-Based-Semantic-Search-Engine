import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

try:
# API Keys (Keep them private using .env)
    GOOGLE_SEARCH_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
    GROQ_API_KEY = os.getenv("LANGCHAIN_GROK_API_KEY")
except:
    logging.error("���️ API KEYS not found or not set.")

# Constants
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 50
TOP_K_RESULTS = 3

logging.info("✅ Configuration Loaded Successfully.")