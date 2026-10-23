from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    repo_id= "google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


class Person(BaseModel):

    name: str = Field(description="The name of the person")
    age: int = Field(gt=18, description="The age of the person")
    city: str = Field(description="The city where the person lives")


parser = PydanticOutputParser(pydantic_object=Person)

template1 = PromptTemplate(
    template= 'Give me the name , age and city of a fictional {place} person \n {format_instructions}',
    input_variables=['place'],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# chain = template1 | model | parser
# result = chain.invoke({'place': 'Indian'})
# print(result)  # Person(name='John Doe', age=30, city='New Delhi')

prompt = template1.format(place="Indian")
print(prompt)
result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)  # Person(name='John Doe', age=30, city='New Delhi')






























