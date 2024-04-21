from src.helper import load_pdf, text_split, embeddings
from langchain_community.vectorstores import FAISS

print("Loading PDF files...")
extracted_data = load_pdf(".\data")

print("Splitting text into chunks...")
text_chunks = text_split(extracted_data)

print("Storing dataset into vector database...")
db = FAISS.from_documents(documents=text_chunks, embedding=embeddings)

print("Saving vector database locally...")
db.save_local("faiss_index")
