# Importing necessary modules
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Extract data from PDF
def load_pdf(data_dir):
    """
    Function to load PDF documents from a directory.

    Args:
        data_dir (str): Directory path containing PDF documents.

    Returns:
        list: List of loaded documents.
    """
    # Initialize document loader
    loader = DirectoryLoader(data_dir,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader)
    # Load documents
    documents = loader.load()
    return documents

# Creating text chunks
def text_split(extracted_data):
    """
    Function to split text into chunks.

    Args:
        extracted_data (list): List of text data.

    Returns:
        list: List of text chunks.
    """
    # Initialize text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30
    )
    # Split documents into chunks
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

# Fetch OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 

# Initialize OpenAI Embeddings
embeddings = OpenAIEmbeddings()
