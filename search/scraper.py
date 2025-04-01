from newspaper import Article
from config.config import MAX_LENGTH
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract_full_article(url, max_length=MAX_LENGTH):
    """
    Extract full text from a given article URL.

    Args:
        url (str): The article URL.
        max_length (int): The maximum length of the text to extract.

    Returns:
        str: Extracted article text or error message.
    """
    try:
        logging.info(f"📄 Extracting article from: {url}")
        article = Article(url)
        # article.download()
        article.parse()
        logging.info("✅ Successfully extracted article.")
        return article.text[:max_length]  # Limit content length dynamically

    except Exception as e:
        logging.error(f"❌ Error extracting article: {str(e)}")
        return f"❌ Error extracting article: {str(e)}"
