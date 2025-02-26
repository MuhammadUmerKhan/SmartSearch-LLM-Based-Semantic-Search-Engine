from newspaper import Article
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract_full_article(url):
    """
    Extract full text from a given article URL.

    Args:
        url (str): The article URL.

    Returns:
        str: Extracted article text or error message.
    """
    try:
        logging.info(f"📄 Extracting article from: {url}")
        article = Article(url)
        article.download()
        article.parse()
        logging.info("✅ Successfully extracted article.")
        return article.text[:10000]  # Limit content length

    except Exception as e:
        logging.error(f"❌ Error extracting article: {str(e)}")
        return f"❌ Error extracting article: {str(e)}"
