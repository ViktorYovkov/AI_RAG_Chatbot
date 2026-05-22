# AI_RAG_Chatbot: 📄🤖
Retrieval-Augmented Generation (RAG) chatbot, built using Python and LangChain to enable  natural language conversations with PDF documents, including a vector database (ChromaDB) for  semantic search and a conversational memory buffer for context maintenance 

## ✨ Features
* **Document Ingestion:** Automatically loads, parses, and splits PDF documents into optimized, overlapping text chunks.
* **Semantic Search:** Uses OpenAI's advanced embedding models to vectorize text and ChromaDB to instantly retrieve the most relevant information.
* **Conversational Memory:** Retains chat history, allowing the bot to understand context and resolve pronouns (e.g., answering "Who is the CEO?" followed by "How old is he?").
* **Local Vector Storage:** Persists the database locally so you don't have to re-process the PDF every time you run the application.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Framework:** LangChain (Core, Community, and Classic)
* **LLM:** OpenAI (`gpt-4o-mini`)
* **Embeddings:** OpenAI (`text-embedding-3-small`)
* **Vector Database:** ChromaDB

## 🚀 Getting Started

### Prerequisites
1. Python 3.8+ installed on your machine.
2. An OpenAI API Key (with available API credits).

### **Executing:**
 ```bash
### Installation:

## Clone the repository:
   git clone [https://github.com/yourusername/AI_RAG_Chatbot.git](https://github.com/yourusername/AI_RAG_Chatbot.git)
   cd AI_RAG_Chatbot

## Create and activate a virtual environment (recommended):
   python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On Mac/Linux:
source .venv/bin/activate

### Usage:
# Running this in the terminal:
python main.py

## Install the required dependencies:
# pip install -r requirements.txt

## Set up your environment variables:
# Create a file named .env in the root directory of the project and add your OpenAI API key:
OPENAI_API_KEY="your-api-key-here"

### Project structure:
AI_PDF_Assistant/
│
├── main.py              # Application entry point and terminal UI
├── chatbot.py           # Core logic: LangChain, ChromaDB, and OpenAI integrations
├── data.pdf             # The source document
├── requirements.txt     # Python dependencies
├── .env                 # API keys (Not tracked by Git)
├── .gitignore           # Excludes system files and databases from version control
└── chroma_db/           # Auto-generated local vector database (Not tracked by Git)
