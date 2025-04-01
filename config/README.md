### **📄 Documentation: `config.py` - Configuration and API Key Setup**

#### **Purpose**
The **`config.py`** file is responsible for setting up and managing configuration parameters for the application. It loads environment variables, including API keys for external services, and defines constants that control the behavior of the application. This file ensures sensitive information like API keys is kept secure by using environment variables, and it also configures logging for tracking the application’s operation.

---

#### **Main Features**
1. **Environment Variable Management**:
   - Uses the `dotenv` library to load API keys and configuration variables securely from a `.env` file.
   - Ensures that sensitive data like API keys is not hardcoded into the source code.

2. **Logging Setup**:
   - Configures logging with `INFO` level to capture events, errors, and other important messages.
   - Logs critical events, such as successful loading of configuration or errors if API keys are missing or constants are not set correctly.

3. **API Key Management**:
   - Loads essential API keys (Google Search, Groq API, etc.) from environment variables.
   - Provides error handling in case the keys are not found or improperly set.

4. **Constants Definition**:
   - Defines essential constants like `CHUNK_SIZE`, `TOP_K_RESULTS`, and `MAX_LENGTH` that govern the behavior of the application (e.g., chunking of data, number of results to consider, etc.).

---

#### **Detailed Breakdown**

##### 1. **Loading Environment Variables**:
```python
load_dotenv()
```
- The `load_dotenv()` function is called to load environment variables from a `.env` file into the application. This allows the application to securely store and access sensitive information such as API keys and configuration parameters, without exposing them in the source code. The `.env` file should contain key-value pairs such as:
    ```
    GOOGLE_SEARCH_API_KEY=your_google_search_key_here
    SEARCH_ENGINE_ID=your_search_engine_id_here
    LANGCHAIN_GROK_API_KEY=your_grok_api_key_here
    ```

##### 2. **API Key Configuration**:
```python
try:
    GOOGLE_SEARCH_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
    GROQ_API_KEY = os.getenv("LANGCHAIN_GROK_API_KEY")
except:
    logging.error("⚠️ API KEYS not found or not set.")
```
- The application retrieves API keys from the `.env` file using `os.getenv()`. The keys are loaded into variables:
    - **GOOGLE_SEARCH_KEY**: Used for Google Custom Search Engine (CSE).
    - **SEARCH_ENGINE_ID**: The ID of the search engine to use for Google Custom Search.
    - **GROQ_API_KEY**: Used to interact with Langchain’s Groq service.
- If any of these keys are missing or incorrectly set, an error is logged using `logging.error()`, with the message "⚠️ API KEYS not found or not set."

##### 3. **Logging Configuration**:
```python
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
```
- The `logging` module is configured to log messages at the `INFO` level. This means messages of level INFO and higher (e.g., WARNING, ERROR) will be recorded.
- The format for the log messages is set to include the timestamp, log level (INFO, ERROR, etc.), and the message itself, providing clarity on the event being logged.

##### 4. **Constants Definition**:
```python
try:
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 100
    TOP_K_RESULTS = 3
    MAX_LENGTH = 5000
except Exception as e:
    logging.error(f"⚠️ Error loading Constants: {str(e)}")
```
- Several constants are defined to control how the application processes data:
    - **CHUNK_SIZE**: Determines the size of chunks when processing large datasets or text. This helps in breaking down large files into manageable parts for processing.
    - **CHUNK_OVERLAP**: Specifies the overlap between consecutive chunks when chunking data. This ensures that no important data is lost at the boundaries.
    - **TOP_K_RESULTS**: Defines the number of top search results to retrieve when conducting a search. This limits the number of search results the application will process.
    - **MAX_LENGTH**: Sets the maximum length for processed text or documents, ensuring that only a manageable amount of data is handled at any given time.
- Any errors that occur while loading these constants are captured, and an error message is logged.

##### 5. **Successful Configuration Load**:
```python
logging.info("✅ Configuration Loaded Successfully.")
```
- Once the environment variables are loaded and constants are set, the log records a success message: "✅ Configuration Loaded Successfully." This indicates that the configuration file has been executed successfully, and the necessary setup is in place for the application to run.

---

#### **Error Handling**

The configuration file includes two main sections of error handling:
1. **API Key Errors**:
   - If the API keys are missing or improperly set, an error message is logged. This ensures the application does not attempt to run without the necessary credentials.
   
2. **Constants Errors**:
   - If any constants cannot be loaded due to an issue in the configuration, an error message is logged. This prevents issues in data processing from going unnoticed.

#### **Best Practices**:
- **Security**: The use of environment variables to store sensitive information such as API keys ensures that the application does not expose any private credentials in the codebase.
- **Modular Design**: By keeping configuration and constant definitions in a separate file (`config.py`), the application remains organized and modular. It also simplifies maintenance, as changes to configuration settings only need to be made in one place.

---

#### **Conclusion**
The **`config.py`** file is crucial for ensuring the application runs securely and smoothly by managing environment variables, API keys, and essential configuration constants. The use of proper logging allows for easy tracking of the configuration loading process, while error handling ensures that any issues are captured and communicated clearly to the user. This structure makes it easier to maintain, debug, and extend the application.