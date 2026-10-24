# topic -> LLM -> Report -> LLM -> Summary (code process)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    templates = 'Generate a detailed report on {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    templates = 'Generate a 5 pointer Summary the following report: {text}',
    input_variables = ['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

#Sequential chain
chain = prompt1 | model | parser | prompt2 | model | parser


result = chain.invoke({'topic': 'space exploration'})

print(result)

chain.get_graph().print_ascii() # to check our chain structure



































