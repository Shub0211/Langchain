from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#Initialize the LLM
llm = OpenAI(model_name = 'text-davinci-003', temperature = 0.9)

#create a prompt template for the LLM
prompt = PromptTemplate(
    input_variables = ['topic'],
    template = 'Suggest a catchy blog title for the topic: {topic}'
)

# create an LLM chain
chain = LLMChain(llm = llm, prompt = prompt)

# Define the input for the prompt template
topic = input("Enter a topic for the blog title: ")
output = chain.run(topic)

# #format the prompt manually using prompt template
# formatted_prompt = prompt.format(topic=topic)

# # call the LLM with the formatted prompt
# blog_title= llm.predict(formatted_prompt)

# print the output
# print("Suggested Blog Title:", blog_title)

print("Suggested Blog Title:", output)
