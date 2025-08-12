from newspaper import Article
from scripts.config import MAX_LENGTH
import logging
import validators

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract_full_article(url, max_length=MAX_LENGTH):
    """
    Extract full text from a given article URL.

    Args:
        url (str): The article URL.
        max_length (int): The maximum length of the text to extract.

    Returns:
        str: Extracted article text or None if extraction fails or content is invalid.
    """
    try:
        # Validate URL
        if not validators.url(url):
            logging.error(f"❌ Invalid URL: {url}")
            return None

        logging.info(f"📄 Extracting article from: {url}")
        article = Article(url)
        article.download()
        article.parse()

        # Check if extracted text is valid
        if not article.text or len(article.text.strip()) < 50:  # Minimum length to ensure meaningful content
            logging.warning(f"⚠️ No meaningful content extracted from: {url}")
            return None

        logging.info("✅ Successfully extracted article.")
        return article.text[:max_length]  # Limit content length dynamically

    except Exception as e:
        logging.error(f"❌ Error extracting article from {url}: {str(e)}")
        return None