from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import structured_output_parser, response_schema



load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    repo_id= "google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


schema = [
    ResponseSchema(name="fact_1", description="fact1 about the topic"),
    ResponseSchema(name="fact_2", description="fact2 about the topic"),
    ResponseSchema(name="fact_3", description="fact3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template1 = PromptTemplate(
    template= 'Give me 3 facts about the {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables= {'format_instructions': parser.get_format_instructions() }
)

# chain = template1 | model | parser
# result = chain.invoke({'topic': 'black hole'})
# print(result)  


prompt = template1.format(topic="black hole")

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)  





























