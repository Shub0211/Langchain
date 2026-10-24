
'''chain 1 = joke generate =-> output is joke
chain 2 -> input getting from chain 1 an dprovide explantion

chain1 + chain2 = bigger chain

'''


from abc import ABC, abstractmethod
import random
from typer import prompt


class Runnable(ABC):

    @abstractmethod
    def invoke(self, input_data):
        pass


class nakliLLM(Runnable):

    def __init__(self):
        print('LLM Created')

    def invoke(self, prompt):
        response_list = [
            "This is a simulated response to the prompt.",
            "The LLM has generated this response based on the input.",
            "Here is a random response from the LLM."
        ]
        return {'response': random.choice(response_list)}

    def predict(self, prompt):
        # Simulate LLM response
        response_list = [
            "This is a simulated response to the prompt.",
            "The LLM has generated this response based on the input.",
            "Here is a random response from the LLM."
        ]
        return {'response': random.choice(response_list)}

llm = nakliLLM()

class nakliPromptTemplate(Runnable):

    def __init__(self, input_variables, template):
        self.input_variables = input_variables
        self.template = template

    def invoke(self, input_dict):
        formatted_prompt = self.template.format(**input_dict)
        return {'formatted_prompt': formatted_prompt}

    def format(self, input_data):
        # Simulate prompt formatting
        formatted_prompt = self.template.format(**input_data)
        return {'formatted_prompt': formatted_prompt}   

class nakliStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        # Simulate parsing the output
        return input_data['response']
    

    def invoke(self, input_dict):
        # Simulate parsing the output
        parsed_output = input_dict.get('response', 'No response found')
        return {'parsed_output': parsed_output}

# Primitive runnables =  help creating workflow -> to call or work task specific runnables work together
class RunnableConnector(Runnable):

    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
           input_data = runnable.invoke(input_data)
        return input_data

template = nakliPromptTemplate(
    input_variables=['topic'],
    template='write a {length} poem about {topic}'
)

parser = nakliStrOutputParser()

# chain = RunnableConnector([template, llm, parser])

# result =chain.invoke({'topic': 'space exploration', 'length': 'short'})

template1 = nakliPromptTemplate(
    template = 'write a joke about {topic}',
    input_variables = ['topic']
)

template2 = nakliPromptTemplate(
    template='Explain the following joke {response}',
    input_variables = ['response']
)

llm = nakliLLM()

parser = nakliStrOutputParser()

chain1 = RunnableConnector([template1, llm])

# chain1.invoke({'topic':'AI'})

chain2 = RunnableConnector([template2, llm, parser])

# chain2.invoke({'response':'This is a joke'})

final_chain = RunnableConnector([chain1, chain2])


print(final_chain.invoke({'topic': 'cricket'}))































