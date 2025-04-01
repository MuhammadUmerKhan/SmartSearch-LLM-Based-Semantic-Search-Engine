### **📄 Documentation: `google_search.py` - Google Custom Search Handler**

#### **Purpose**
The **`google_search.py`** file is responsible for performing Google Custom Searches and returning the top search results based on a user-provided query. It integrates with the **Google Custom Search API** and caches results to improve performance and avoid repetitive queries. The file also includes proper logging for monitoring the search process and handling errors gracefully.

---

#### **Main Features**
1. **Google Custom Search Integration**: The file uses the Google Custom Search API to fetch search results based on a user query.
2. **Caching**: To optimize performance, the `google_custom_search` function is decorated with `@functools.lru_cache`, caching up to 100 queries.
3. **Logging**: Logs are generated at key stages of the process, from initiating the search to returning the results or encountering errors.
4. **Error Handling**: Errors during the search process are logged, and an empty list is returned if the search fails.

---

#### **Detailed Breakdown**

##### 1. **Logging Configuration**:
```python
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
```
- The `logging` module is configured to output log messages with an `INFO` level or higher.
- The format includes the timestamp, log level, and the message, making it easy to track the flow of the program and debug any issues.

##### 2. **Function: `google_custom_search(query)`**:
This function performs a Google Custom Search based on the user's query and returns the top results.

**Arguments**:
- **`query` (str)**: The search term or query entered by the user.

**Returns**:
- **`list`**: A list of dictionaries containing the search results, where each dictionary includes the title, URL, and snippet of the result.

**Steps**:
1. **Logging the Search**:
   - The function logs the search initiation, including the query being used.
   
2. **Building the Custom Search Service**:
   ```python
   service = build("customsearch", "v1", developerKey=GOOGLE_SEARCH_KEY)
   result = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=TOP_K_RESULTS).execute()
   ```
   - The `build` function from `googleapiclient.discovery` creates a service object for interacting with the Google Custom Search API using the provided **API key** (`GOOGLE_SEARCH_KEY`), **search engine ID** (`SEARCH_ENGINE_ID`), and the number of results to fetch (`TOP_K_RESULTS`).
   
3. **Processing the Results**:
   ```python
   search_results = [
       {"title": item["title"], "link": item["link"], "snippet": item["snippet"]}
       for item in result.get("items", [])
   ]
   ```
   - The results are processed into a list of dictionaries, where each dictionary contains the title, URL, and snippet of a search result.

4. **Logging and Returning the Results**:
   - The number of search results found is logged.
   - The function returns the list of search results.

5. **Error Handling**:
   ```python
   except Exception as e:
       logging.error(f"❌ Google Search Error: {str(e)}")
       return []
   ```
   - If any error occurs during the search (e.g., network issues, API key issues), the error is logged and an empty list is returned to the user.

##### 3. **Caching**:
```python
@functools.lru_cache(maxsize=100)
```
- The `@functools.lru_cache` decorator is applied to the `google_custom_search` function. This decorator caches up to 100 queries and their corresponding results, improving performance by preventing redundant API calls for the same query.

---

### **📄 Documentation: `scraper.py` - Article Text Extraction Handler**

#### **Purpose**
The **`scraper.py`** file is responsible for extracting the full text of an article from a given URL. It uses the **Newspaper3k** library to parse articles and return the content. The file also includes logging to monitor the scraping process and handles errors gracefully by returning appropriate error messages if any issue arises.

---

#### **Main Features**
1. **Article Extraction**: The file utilizes the **Newspaper3k** library to download and parse articles from URLs.
2. **Content Length Limitation**: The extracted article text is truncated to a configurable maximum length (`MAX_LENGTH`) to prevent excessively long responses.
3. **Logging**: Detailed logging at each step of the article extraction process, including when the extraction starts and whether it was successful or failed.
4. **Error Handling**: Errors during the extraction process are logged, and a message is returned indicating the failure.

---

#### **Detailed Breakdown**

##### 1. **Logging Configuration**:
```python
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
```
- The logging configuration is set to output messages at the `INFO` level or higher.
- The log messages include a timestamp, the log level, and the message itself for better tracking of operations.

##### 2. **Function: `extract_full_article(url, max_length=MAX_LENGTH)`**:
This function extracts the full text from an article at a given URL.

**Arguments**:
- **`url` (str)**: The URL of the article to scrape.
- **`max_length` (int)**: The maximum length of the text to be extracted. This helps to control the size of the returned content, preventing excessively large responses.

**Returns**:
- **`str`**: The extracted article text (or an error message if the extraction fails).

**Steps**:
1. **Logging the Extraction Start**:
   - The function logs the URL of the article being processed.

2. **Article Extraction**:
   ```python
   article = Article(url)
   article.parse()
   ```
   - An `Article` object is created using the given URL. The `parse` method is called to download and parse the article content.

3. **Returning the Extracted Text**:
   ```python
   return article.text[:max_length]
   ```
   - The extracted text is returned, truncated to the configured `max_length`.

4. **Logging Success**:
   - A log message indicates that the article was successfully extracted.

5. **Error Handling**:
   ```python
   except Exception as e:
       logging.error(f"❌ Error extracting article: {str(e)}")
       return f"❌ Error extracting article: {str(e)}"
   ```
   - If an error occurs during the extraction process (e.g., network issues, invalid URL, or unsupported format), the error is logged and a message is returned indicating the failure.

---

### **Best Practices**
1. **Logging**: Both scripts use logging extensively to monitor the process and provide detailed information for debugging. This makes it easier to track the flow of the program and catch any issues.
2. **Caching**: The `google_search.py` file uses caching to improve performance by avoiding repetitive API calls for the same queries.
3. **Error Handling**: Both files include error handling to ensure that any issues are logged, and the user receives an appropriate error message.
4. **Modularity**: Each function is focused on a single task (Google search or article extraction), making the code easy to maintain and extend.

---

#### **Conclusion**
The **`google_search.py`** and **`scraper.py`** files handle specific tasks related to searching and extracting information from external sources. The former integrates with the Google Custom Search API to fetch top search results based on user queries, while the latter uses the Newspaper3k library to extract and parse article text from a given URL. Both files are designed with performance optimization (caching), error handling, and logging to ensure smooth and reliable functionality.