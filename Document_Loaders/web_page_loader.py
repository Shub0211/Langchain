from langchain_community.document_loaders import WebBaseLoader
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the follwoing question \n {question} from the follwoing - \n {text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser()


url=''

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question': 'what is the peak brightness of this product', 'text': docs[0].page_content})

print(result)

# print(len(docs))

# print(docs[0].page_content)
# # print(docs[0].metadata)


























































