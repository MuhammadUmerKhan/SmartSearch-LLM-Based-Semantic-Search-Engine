## 📂 **Page Documentation**

---

## 📄 **`custom_urls.py` - Custom URL Search Handler**

### **Purpose**
The **`custom_urls.py`** module is responsible for handling user queries related to custom URLs. It provides the functionality to process user-defined URLs and fetch data from those URLs if they are added manually, rather than relying solely on Google Search API or pre-configured search engines.

### **Key Features**
- **Custom URL Query Processing**: This module listens for user input containing URLs or queries about specific websites and handles them accordingly.
- **URL Validation**: Validates if the input is a proper URL format before attempting to scrape or fetch data.
- **Article Scraping**: If a valid URL is entered, it can extract the content from that URL using the scraping functionality.

### **Workflow**
1. **User Input**: The user can enter a URL directly into the search bar or choose an option to provide custom URLs for search.
2. **Validation**: The system first checks if the input is a valid URL. If it's not, it prompts the user to enter a valid URL.
3. **Scraping**: Upon receiving a valid URL, the module fetches the content by calling the scraping function from the `scraper.py` module.
4. **Display Results**: After extracting the content, the results are displayed in the Streamlit UI, allowing users to read the extracted text directly or use it to refine their query further.

### **Core Functions**
- **`process_custom_url`**: Accepts the user-provided URL, validates it, and then extracts the necessary information from the page.
- **`fetch_article_from_url`**: Scrapes the content of the URL and returns it for further processing.

---

## 📄 **`home.py` - Streamlit Home Page**

### **Purpose**
The **`home.py`** module serves as the landing page of the Streamlit web application. It introduces users to the core features of the AI-powered search engine and provides instructions on how to use the app effectively.

### **Key Features**
- **Introduction to the App**: This page gives an overview of what the app is and its primary functionalities.
- **Links to External Resources**: It includes direct links to the project's GitHub repository, LinkedIn profile, and documentation.
- **Navigation to Other Pages**: The home page serves as an entry point, providing easy access to other pages like search engine, instructions, and custom URLs.
- **User Guidance**: Provides clear instructions to the users on how to start using the app, including what each part of the app does and how to make the most of the search engine.

### **Workflow**
1. **User Access**: When a user first navigates to the app, they are presented with the home page, which gives them a brief introduction and an overview of the project.
2. **Instructions**: The page also includes step-by-step instructions to guide users on how to interact with the search engine, making it easier for beginners to understand the app.
3. **Navigation**: Users can click on a button or link to move to the search page or other pages like custom URLs or instructions.

### **Core Functions**
- **`display_intro`**: Shows the introductory content about the search engine.
- **`link_to_github`**: Provides users with a clickable link to the GitHub repository.
- **`navigate_to_search`**: Allows users to easily navigate to the search page from the home page.

---

## 📄 **`instruction.py` - Search Engine Instructions Page**

### **Purpose**
The **`instruction.py`** page provides users with detailed instructions on how to use the AI-powered search engine effectively. It explains the search process, the structure of results, and the available options for refining searches.

### **Key Features**
- **Detailed Search Instructions**: Explains how to enter queries, use filters, and interpret the AI-generated responses.
- **Understanding the Results**: Guides users on what they can expect from the search results, including links to sources, article content, and AI-generated answers.
- **Refining Search Queries**: Provides instructions on how to refine or modify queries to get more accurate or relevant answers.

### **Workflow**
1. **User Access**: Users can access the instructions page from the home page or search page to get more guidance on using the app.
2. **Displaying Instructions**: The page displays a series of step-by-step instructions, including screenshots or text explaining how to use the search engine's features.
3. **Advanced Tips**: For more advanced users, the page might also suggest tips for more efficient searching, such as using Boolean operators or other filters.

### **Core Functions**
- **`display_search_instructions`**: Shows step-by-step instructions for using the search engine.
- **`show_advanced_tips`**: Displays additional tips for experienced users.
- **`link_to_home_page`**: Provides a way to easily return to the home page.

---

## 📄 **`search_engine.py` - Search Engine Implementation**

### **Purpose**
The **`search_engine.py`** module is the core of the AI-powered search engine. It handles the entire search flow, including fetching search results from Google Search API, scraping content, processing it, storing embeddings in the FAISS vector database, and generating AI-powered responses via the LangChain LLM.

### **Key Features**
- **Google Search Integration**: Fetches top search results from Google Search API.
- **Web Scraping**: Scrapes full articles from the URLs obtained from the search results.
- **Vector Storage**: Stores the embeddings of extracted content in the FAISS vector database for efficient retrieval.
- **AI-Powered Answer Generation**: Uses LLMs (such as Llama or Grok) to generate structured, AI-powered responses based on the retrieved content.
- **Structured Display of Results**: Displays the AI-generated answers, along with source links, in a structured format.

### **Workflow**
1. **Query Input**: The user enters a search query on the UI.
2. **Fetching Results**: The search engine fetches the results via the Google Custom Search API.
3. **Scraping and Content Extraction**: It scrapes full-text content from the relevant URLs obtained from the search results.
4. **Embedding Storage**: The content is split into chunks, embeddings are generated, and stored in the FAISS vector database for efficient retrieval.
5. **AI Response Generation**: The user query and relevant content chunks are fed to the LLM for generating a response.
6. **Displaying Results**: The results, including AI-generated answers and source links, are displayed on the UI.

---

## **`doc_chat.py` - Multi-Document Upload & Smart Q&A System**

### **Purpose**
The **`doc_chat.py`** module powers the DocuMind AI, an intelligent document-based Q&A system. It allows users to upload multiple document formats (PDF, DOCX, TXT) and interact with their contents using AI-powered question-answering capabilities. The system leverages **LangChain**, **FAISS vector search**, and **sentence embeddings** to retrieve the most relevant information based on user queries.

### **Key Features**
- **Multi-Document Upload**: Users can upload **PDF, DOCX, and TXT** files for processing.
- **Text Chunking & Embeddings**: Splits documents into smaller chunks for efficient retrieval.
- **FAISS Vector Search**: Stores document embeddings for quick and relevant information retrieval.
- **Conversational AI**: Uses an LLM (Large Language Model) to provide context-aware responses.
- **Memory Retention**: Maintains chat history for seamless multi-turn conversations.

### **Workflow**
1. **User Uploads Documents**: Users can upload multiple **PDF, DOCX, or TXT** files via the Streamlit UI.
2. **Document Processing**: The system reads, extracts, and converts documents into structured text data.
3. **Text Chunking**: Documents are split into smaller, manageable chunks for embedding.
4. **Vectorization & FAISS Indexing**: Embeddings of the text chunks are created and stored in the FAISS vector database.
5. **User Queries the Document**: The user asks questions related to the uploaded documents.
6. **Retrieval & AI Response Generation**: Relevant document chunks are retrieved, and an AI-generated response is provided.
7. **Conversation Memory**: The system retains chat history for better user experience and context-aware responses.

### **Core Functions**
- **`fetch_search_results`**: Calls the Google Custom Search API to fetch results based on the query.
- **`scrape_content_from_urls`**: Scrapes full content from the URLs returned by the Google API.
- **`generate_embeddings`**: Generates embeddings for the extracted content using the HuggingFace API.
- **`generate_ai_answer`**: Uses an LLM to process the query and relevant content to generate a structured answer.
- **`display_results`**: Displays the AI-generated answers and source links on the UI.