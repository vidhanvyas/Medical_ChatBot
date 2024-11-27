from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain_community.llms import Ollama
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]='true'
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app=FastAPI(title='Lanchain Server', version='1.0', description='A Simple API Server')

llm1 = Ollama(model='llama3.1')
llm2 = Ollama(model='gemma2')

prompt1 = ChatPromptTemplate.from_template("Describe {topic} in about 400 words for the general audience")
prompt2 = ChatPromptTemplate.from_template("List the medication required for {topic} general audience")

add_routes(
    app,
    prompt1|llm1, 
    path="/disease"
)

add_routes(
    app,
    prompt2|llm2,
    path="/medication"
)

if __name__=='__main__':
    uvicorn.run(app, host="localhost", port=8000)