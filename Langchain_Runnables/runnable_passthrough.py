from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()


# passthrough = RunnablePassthrough()
# print(passthrough.invoke(2))


prompt1 = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template = 'explain the followinbg joke {text}',
    input_variables=['text']
)

jokeGeneratorChain = RunnableSequence(prompt1, model, parser)

parallelChain = RunnableParallel({
        'joke' : RunnablePassthrough(),
        'explanation' : RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(jokeGeneratorChain, parallelChain)

print(final_chain.invoke({'topic': 'Cricket'}))




 








































