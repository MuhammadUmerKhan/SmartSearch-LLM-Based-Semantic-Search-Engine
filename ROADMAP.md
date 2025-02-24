# 🚀 AI-Powered Real-Time Search Engine with RAG & LLMs

## 📌 Project Overview
This project is an **AI-powered real-time search engine** that leverages **Retrieval-Augmented Generation (RAG)** to provide up-to-date, well-structured, and concise responses to user queries. The system combines **Google Custom Search**, **Web Scraping**, **FAISS Vector Database**, and **LLaMA-3 LLM** for generating **accurate and summarized responses** with real-time data.

## 🎯 Features
- 🌐 **Real-Time Web Search:** Retrieves the latest information using Google Custom Search API.
- 📰 **Web Scraping & Article Extraction:** Extracts full content from web pages for deeper insights.
- 🧠 **Vector Database (FAISS):** Efficient similarity search for relevant documents.
- 🔍 **Retrieval-Augmented Generation (RAG):** Uses retrieved data to generate **concise and well-structured responses**.
- 🤖 **LLM-Powered Responses:** Uses **LLaMA-3.3-70B** via **Groq API** for enhanced AI-generated answers.
- 🎨 **Emoji-Formatted Responses:** Presents AI responses in a **professional, structured, and visually appealing format**.

## 🛠️ Tech Stack
- **Programming Language:** Python 🐍
- **Search API:** Google Custom Search API 🔎
- **Scraping:** Newspaper3k 📄
- **Vector Database:** FAISS 📂
- **Embeddings:** HuggingFace Transformers 🤗
- **LLM:** LLaMA-3 (via Groq API) 🧠
- **Deployment:** Streamlit (Upcoming) 🎬

## 🚀 How to Run the Project
### 1️⃣ **Clone the Repository**
```sh
 git clone https://github.com/MuhammadUmerKhan/AI-Powered-Search-Engine.git
 cd AI-Search-Engine
```

### 2️⃣ **Install Dependencies**
```sh
 pip install -r requirements.txt
```

### 3️⃣ **Set Up API Keys**
```sh
 export GOOGLE_SEARCH_KEY='your_google_api_key'
 export SEARCH_ENGINE_ID='your_search_engine_id'
 export GROQ_API_KEY='your_groq_api_key'
```

### 4️⃣ **Run the Application**
```sh
 python main.py  # To execute search & generate LLM responses
```

## 📍 Project Roadmap
### ✅ **Phase 1: Core Implementation** (🔄 Completed)
✔ Set up Google Custom Search API integration
✔ Extract full articles from web pages
✔ Implement FAISS vector database for document retrieval
✔ Encode text using HuggingFace Embeddings
✔ Implement RAG-based document retrieval
✔ Generate AI responses using LLaMA-3 LLM
✔ Format LLM responses for readability

### 🚀 **Phase 2: Code Refactoring & Optimization**
🔲 Implement modular functions & class-based architecture
🔲 Add proper error handling (Try-Except)
🔲 Improve embeddings quality for better document matching

### 🎨 **Phase 3: UI & Deployment**
🔲 Build an interactive **Streamlit UI**
🔲 Deploy project on **Hugging Face Spaces** or **AWS Lambda**

### 🔮 **Phase 4: Enhancements & Future Scope**
🔲 Support **multiple LLMs (GPT-4, Claude, Mistral, etc.)**
🔲 Implement **multi-modal search (text + images)**
🔲 Deploy a **REST API** for external integration

## 📢 Contribution
Want to improve this project? Feel free to fork and submit a PR! 🚀

## 📜 License
This project is licensed under **MIT License**. 📝

## 📬 Contact
- 📧 Email: muhammadumerk546@gmail.com
- 🔗 GitHub: [Your GitHub Profile](https://github.com/MuhammadUmerKhan?tab=repositories)

---
🔥 *This project is a step toward building a more intelligent and real-time AI search assistant!*