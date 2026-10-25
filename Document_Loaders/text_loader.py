# from langchain_community.document_loaders import TextLoader
# loader = TextLoader('cricket.txt') # object of  docuement loader
# docs = loader.load()
# print(docs)




from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='write a summary of following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

# Get the folder where text_loader.py is located
file_path = Path(__file__).parent / "cricket.txt"

loader = TextLoader(str(file_path), encoding="utf-8")

docs = loader.load()

print(len(docs))

print(type(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem': docs[0].page_content}))







































