from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    ('system','you are a helpful {domain} expert'), #tuple
    ('human','Explain in simple terms, what is {topic}') #tuple
    # SystemMessage(content='you are a helpful {domain} expert'),
    # HumanMessage(content='Explain in simple terms, what is {topic}')

])

prompt = chat_template.invoke({'domain':'cricket','topic':'Doosra'})

print(prompt) 