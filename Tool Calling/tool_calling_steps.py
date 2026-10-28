from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests


#tool create

@tool
def multiply(a:int, b:int) -> int:
    """Given two numbers a and b, this tool returns their product"""
    return a*b

result = multiply.invoke({"a":23, "b":65})

print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)

#tool Bind

llm = ChatOpenAI()

llm_with_tools = llm.bind_tools([multiply]) #tool binding


# tool calling

# tc1 = llm_with_tools.invoke('Hi How are you')

query = HumanMessage('can you multiply 3 with 10')

messages = [query]

print(messages)

tc = llm_with_tools.invoke(messages)

messages.append(tc)

tc1 = tc.tool_calls[0] #['args']

#tool execuition
 
multiply.invoke(tc1)


#tool message
tool_result = multiply.invoke(tc1)     # without args  - tc.tool_calls[0]

message_tool_result = messages.append(tool_result)

print(llm_with_tools.invoke(messages).content)























