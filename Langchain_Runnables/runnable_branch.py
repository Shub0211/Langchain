from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel, RunnableBranch

load_dotenv()

prompt1 = PromptTemplate(
    template = ' write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Summarize the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

report_generation_chain = RunnableSequence(prompt1, model, parser)

# report_generation_chain = prompt1 | model | parser  # LCEL

branch_chain = RunnableBranch(
    (lambda x: len(x.split()>500), RunnableSequence(prompt2, model, parser)),#tuple 1- if condition (condition, runnable-executes if condition is true)  #tuple 2 - second if condition (condition, runnable)
    RunnablePassthrough() # default condition / else condtion
)

final_chain = RunnableSequence(report_generation_chain, branch_chain)

print(final_chain.invoke({'topic':'Russian vs Ukraine'}))






















































