'''user provide feedback for a product -> we have to analyze the sentiment of feedback if either it's a positive feedback and negative and we provide reply to the user based on the sentiment of feedback.

feedback -> analyze sentiment -> positve - feedback form
negative feedback -> email to user for apology

user feedback -> model -> sentiment extrtact -> positive or negative -> based on sentiment we provide reply to user 

only 1 path will execute at once either or positive or negative path will execute based on the sentiment of feedback. This allows for efficient processing and generation of appropriate responses to user feedback, improving the overall user experience.

this is conditional chain where we have to check the condition of sentiment and based on that we have to execute either positive or negative path.

'''
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal




load_dotenv()

model1 = ChatOpenAI()

parser = StrOutputParser()

class feedback_sentiment(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description = 'The sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object = feedback_sentiment)


prompt1 = PromptTemplate(
    templates = 'classify the sentiment of the following feedback and provide either positive or negative sentiment \n {feedback} \n {format_instructions}',
    input_variables = ['feedback'],
    partial_variables = {'format_instructions': parser2.get_format_instructions()}      
)

classifier_chain = prompt1 | model1 | parser2

# result = classifier_result = classifier_chain.invoke({'feedback': 'The product is really good and I am satisfied with the quality.'})

# print(result)

prompt2 = PromptTemplate(
    template = 'write an appropriate response for the following positive feedback   \n {feedback}',
    input_variables = ['feedback']     
)

prompt3 = PromptTemplate(
    template = 'write an appropriate response for the following negative feedback   \n {feedback}',
    input_variables = ['feedback']     
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model1 | parser), #(condition, chain to execute if condition is true)
    (lambda x:x.sentiment == 'negative', prompt3 | model1 | parser), #(condition, chain to execute if condition is true)
    RunnableLambda(lambda x: 'could not found sentiment') # default chain to execute if none of the conditions are true
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': 'The product is really good and I am satisfied with the quality.'})

print(result)
























































