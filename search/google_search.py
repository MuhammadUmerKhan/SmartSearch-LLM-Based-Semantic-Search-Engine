from googleapiclient.discovery import build
from config.config import GOOGLE_SEARCH_KEY, SEARCH_ENGINE_ID, TOP_K_RESULTS
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def google_custom_search(query):
    """
    Perform Google Custom Search and return top results.
    
    Args:
        query (str): User search query.

    Returns:
        list: List of search results (title, URL, snippet).
    """
    try:
        logging.info(f"🔍 Searching Google for: {query}")
        service = build("customsearch", "v1", developerKey=GOOGLE_SEARCH_KEY)
        result = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=TOP_K_RESULTS).execute()

        search_results = [
            {"title": item["title"], "link": item["link"], "snippet": item["snippet"]}
            for item in result.get("items", [])
        ]
        logging.info(f"✅ Found {len(search_results)} results.")
        return search_results

    except Exception as e:
        logging.error(f"❌ Google Search Error: {str(e)}")
        return []
