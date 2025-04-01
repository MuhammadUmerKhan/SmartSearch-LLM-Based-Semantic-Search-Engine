# 📌 AI-Powered Semantic Search Engine with LLMs

## 🚀 Introduction
The **AI-Powered Search Engine** is a web-based application that combines **Google Search API**, **web scraping**, **FAISS vector database**, **LLMs**, and **custom URL search** to fetch, extract, and summarize real-time search results. This tool is designed to **enhance information retrieval** by providing structured, AI-generated responses from both web results and custom URL inputs.

![](https://media.licdn.com/dms/image/v2/D5612AQEmQPzwyDhgbw/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1716132344917?e=2147483647&v=beta&t=vUIJxi_t4HCoQxV8HqEDWm3U7Uzz40Kp4YFCB-C5RuU)
---

### 🔹 **Key Features**
- **🔍 Real-time Web Search**: Fetches search results via **Google Custom Search API**.
- **📄 Article Extraction**: Scrapes full-text articles from links.
- **🌐 Custom URL Search**: Allows users to input URLs for content extraction and indexing.
- **🧠 FAISS Vector Database**: Stores and retrieves key content.
- **🤖 AI-Powered Answering**: Uses **Llama 3** via **LangChain** to generate structured answers.
- **🚀 Streamlit UI**: Provides an interactive and user-friendly interface.


---

## 📂 **Project Structure & File Explanations**
```
AI_Search_Engine/
│
├── app.py                    # 🎨 Streamlit UI for User Interaction
│
├── notebook/
│   ├── AI_Powered_Search_Engine.ipynb  # 📚 Jupyter Notebook for Experimentation
│
├── config/
│   ├── config.py              # ⚙️ API Keys & Global Configurations
│
├── search/
│   ├── google_search.py       # 🔍 Google Search API Handling
│   ├── scraper.py             # 📄 Web Scraping & Article Extraction
│
├── vector_store/
│   ├── vector_store.py        # 📚 FAISS Vector Database Handling
│
├── llm/
│   ├── llm_handler.py         # 🤖 LLM Query Processing
│
├── pages/
│   ├── custom_urls.py         # 🌐 Custom URL Search Handler
│   ├── home.py                # 🏠 Home Page
│   ├── instruct.py            # 📜 Search Engine Instructions
│   ├── search_engine.py       # 🔎 Search Engine Implementation
│
├── requirements.txt           # 📦 Dependencies for the Project
│
├── .env                # Stores API keys (Not shared for security)
│
└── README.md                  # 📖 Project Documentation & Setup Guide
```

### **📜 File Explanations**

#### 1️⃣ **`config.py` - Configuration File**
- Loads **API keys** and project constants from `.env`.
- Stores:
  - `GOOGLE_SEARCH_KEY` (Google API Key)
  - `SEARCH_ENGINE_ID` (Custom Search Engine ID)
  - `GROQ_API_KEY` (LLM API Key)
  - `CHUNK_SIZE`, `CHUNK_OVERLAP`, `MAX_LENGTH`, and `TOP_K_RESULTS`

#### 2️⃣ **`google_search.py` - Google Search API Integration**
- Calls **Google Custom Search API** to fetch top results.
- Uses caching to avoid repeated API calls.
- Implements **exponential backoff retry mechanism** for rate limits.

#### 3️⃣ **`scraper.py` - Web Scraper**
- Uses `newspaper3k` to extract full article text from URLs.
- Limits text to **5000 characters** to avoid unnecessary large responses.
- Handles exceptions for failed extractions.

#### 4️⃣ **`vector_store.py` - FAISS Vector Database**
- Uses **HuggingFace Embeddings (`all-MiniLM-L6-v2`)**.
- Splits extracted text into **overlapping chunks**.
- Stores **embeddings** in a FAISS vector database for efficient retrieval.

#### 5️⃣ **`llm_handler.py` - LLM Query Processor**
- Calls **DIFFERENT** via **LangChain-Groq API**.
- Takes user query + relevant text chunks → **generates AI response**.
- Formats responses into **structured bullet points with emojis**.

#### 6️⃣ **`home.py` - Streamlit Home Page**
- Displays an **introduction**, **features**, and **GitHub/LinkedIn links**.
- Provides **user instructions** on how to use the app.

#### 7️⃣ **`app.py` - Main Streamlit UI**
- Implements **Sidebar Navigation**.
- Accepts user query → Fetches search results → Extracts articles → Creates a vector DB → Calls LLM for response.
- Displays:
  - **AI-generated structured answer**
  - **List of sources with clickable links**

#### 8️⃣ **`custom_urls.py` - Custom URL Search Handler**
- Allows users to **input URLs** for content extraction.
- Extracted content is indexed into a **FAISS vector database**.
- Users can search using this custom content, enhancing search results.


---
## **🤖 Supported LLMs**
| Model | API Name |
|--------|-------------------------------|
| Llama | `llama-3.3-70b-versatile` |
| Gemma | `gemma2-9b-it` |
| Qwen 2.5 | `qwen-2.5-32b` |
| DeepSeek R1 32B | `deepseek-r1-distill-qwen-32b` |
| DeepSeek R1 70B | `deepseek-r1-distill-llama-70b` |
| DeepSeek Qwen | `deepseek-r1-distill-qwen-32b` |

---
## 🛠 **Setup & Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/MuhammadUmerKhan/AI-Powered-Search-Engine.git
cd AI-Powered-Search-Engine
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up API Keys**
Create a `.env` file in the root directory and add:
```env
GOOGLE_SEARCH_API_KEY=your_google_api_key
SEARCH_ENGINE_ID=your_search_engine_id
LANGCHAIN_GROK_API_KEY=your_llm_api_key
```

### **4️⃣ Run the Application**
```bash
streamlit run app.py
```

---

## 🎯 **Usage Guide**
### 🔍 **How to Use the AI-Powered Search Engine**
1️⃣ **Navigate to the Home Page** → Read about features & how it works.  
2️⃣ **Go to the Search Page** → Enter a query in the search box or input URLs to add custom content.  
3️⃣ **Press Enter** → The app will fetch, extract, process, and generate AI responses.  
4️⃣ **View AI Response & Sources** → Click links for more details.

### 🌐 **Using Custom URL-Based Search**
1️⃣ **Enter a URL** in the provided text area.  
2️⃣ **Click "Extract & Search"** to index content from the URL.  
3️⃣ Use the search box to query the indexed URL content for AI-generated answers.

📌 **Example Queries:**
- *"What are the latest advancements in AI?"*
- *"Explain quantum computing in simple terms."*
- *"What are the benefits of intermittent fasting?"*

---

## 🔥 **Tech Stack**
✅ **Python** - Main programming language.  
✅ **Streamlit** - Frontend UI framework.  
✅ **Google Custom Search API** - Fetches search results.  
✅ **Newspaper3k** - Extracts article content.  
✅ **FAISS** - Vector storage for fast retrieval.  
✅ **LangChain & Llama 3** - LLM for generating AI-powered responses.  
✅ **Custom URL Search** - Indexes and searches user-provided URLs.

---

## 📌 **To-Do & Future Improvements**
✅ Implement caching & retries for API requests.  
✅ Improve LLM response formatting with markdown & bullet points.  
🔜 Add **user feedback mechanism** to improve responses.  
🔜 Support **multiple search APIs** for better coverage.  
🔜 Implement **document upload** for personalized search.  

---

## 🔴 Live Demo:
- [Web App](https://ai-powered-search-engine-using-llm.streamlit.app/?embed_options=show_toolbar,dark_theme,show_colored_line,show_footer)
---

## 👨‍💻 **Author & Contact**
💡 **Developed by:** [Muhammad Umer Khan](https://www.linkedin.com/in/muhammad-umer-khan-61729b260/)  
📧 **Contact:** Reach out via LinkedIn or GitHub.  

🌟 **If you found this project helpful, give it a ⭐ on GitHub!** 🚀