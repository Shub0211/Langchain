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


url='https://www.amazon.in/dp/B0H297XH3K?aref=o8JYplTuf1&pd_rd_plhdr=t&pf_rd_r=XJVAJMVF9N7Q1RBNF42P'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question': 'what is the peak brightness of this product', 'text': docs[0].page_content})

print(result)

# print(len(docs))

# print(docs[0].page_content)
# # print(docs[0].metadata)


























































