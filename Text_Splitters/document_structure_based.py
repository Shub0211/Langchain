from langchain_text_splitters import RecursiveCharacterTextSplitter, Language



text = """
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
"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,   #python based text splitter. Same way can be splitted with different kind of language
    chunk_size = 300,
    chunk_overlap= 0
)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks[1])















































