from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory
import os

class PDF_Chatbot:
    def __init__(self, pdf_path):
        """Initializes the bot with the file path and AI model."""
        self.pdf_path = pdf_path
        self.persist_directory = "./chroma.db"
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.vector_store = None
        self.qa_chain = None

        self.memory = ConversationBufferMemory(memory_key = "chat_history",
                                                   return_messages = True)

    def ingest(self):
        """Loads the pdf, separates it and creates a vector store"""
        if os.path.exists(self.persist_directory):
            print("Loading existing directory...")
            self.vector_store = Chroma(persist_directory = self.persist_directory,
                                       embedding_function = self.embeddings)
        else:
            print("Creating new database...")
            loader = PyPDFLoader(self.pdf_path)
            documents = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
            docs = text_splitter.split_documents(documents)

            self.vector_store = Chroma.from_documents(documents = docs,
                                                      embedding = self.embeddings,
                                                      persist_directory = self.persist_directory)
            print("Database created successfully!")

        # Providing access to the previous database:
        self.qa_chain = ConversationalRetrievalChain.from_llm(llm = self.llm,
                                                              memory = self.memory,
                                                              retriever = self.vector_store.as_retriever(search_kwargs={"k":3}))

    def ask_question(self, question):
        """Takes a user question, searches the database, and returns the AI answer."""
        if not self.qa_chain:
            return {"answer": "Error: Please run ingest() first..."}

        response = self.qa_chain.invoke({"question": question})
        return response