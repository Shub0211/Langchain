from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel

load_dotenv()

def word_counter(text):
    return len(text.split())

# runnable_word_counter = RunnableLambda(word_counter)
# print(runnable_word_counter.invoke('Shubham is a good boy'))


prompt = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_generate_chain = RunnableSequence(prompt, model, parser)

# parallel_chain = RunnableParallel({
#     'joke' : RunnablePassthrough(),
#     'word_count' : RunnableLambda(lambda x: len(x.split()))
# })

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_counter)
})


final_chain = RunnableSequence(joke_generate_chain, parallel_chain)

result = final_chain.invoke({'topic' : 'AI'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)






































