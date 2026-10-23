from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    repo_id= "google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template1 = PromptTemplate(
    template= 'Give me the name , age and city of a fictional person \n {format_instructions}',
    input_variables=[],
    partial_variables= {'format_instructions': parser.get_format_instructions() }
)

# this code can be replaced by chains
'''prompt = template1.format()
print(prompt)
result = model.invoke(prompt)
final_result = parser.parse(result.content)'''

#chains

chain = template1 | model | parser

result = chain.invoke({}) # should provide blank dict if no input variables is given, in case of using chains



print(result)

# for without chains 
# print(final_result)  #dictionary
# print(type(final_result))






















