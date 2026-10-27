from langchain_core.tools import tool


#step-1: create a function
def multiply(a,b):
    """Multiply two numbers"""
    return a*b

#step 2: add type hints
def multiply(a:int, b:int) -> int:
    """Multiply two numbers"""
    return a*b

#step3: add tool decorator
@tool
def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a":38, "b":59})

print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)

# LLM saw this json schema of tool when we send this to LLM
print(multiply.args_schema.model_json_schema()) 



 





































