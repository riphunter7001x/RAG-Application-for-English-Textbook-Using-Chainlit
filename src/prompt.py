# lets design prompt template 

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template(
    """
    Answer the following question based on the provided context.
    Think step by step before providing a detailed answer.
    I will tip you $1000 if the user finds the answer helpful.
    <context> 
    {context}
    </context>
    question:
    {context}
    
    Please provide a concise and informative answer below:
    helpful answer :
    """
)