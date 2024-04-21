# Importing necessary modules
from src.prompt import prompt
from src.helper import embeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import os
from dotenv import load_dotenv
import chainlit as cl 

# Load environment variables
load_dotenv()

# Load OpenAI API key and model
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Load vector index
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Function to perform retrieval-based question answering
def retrieval_qa_chain(user_input):
    # Create document chain
    document_chain = create_stuff_documents_chain(llm, prompt)
    # Create retriever
    retriver = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    # Create retrieval chain
    retrival_chain = create_retrieval_chain(retriver, document_chain)
    # Invoke retrieval chain with user input
    response = retrival_chain.invoke({"input": user_input})
    return response["answer"]

# Define main function for message handling
@cl.on_message
async def main(message: cl.Message):
    # Call retrieval-based question answering function
    response = retrieval_qa_chain(message.content)
    # Send a response back to the user
    await cl.Message(
        content=f"{response}",
    ).send()
