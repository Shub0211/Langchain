from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.tools import InjectedToolArg
import requests, json
from typing import Annotated



#tool create
@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    This function fetches the currency conversion factor between a base currency and a target currency
    """
    url = f"https://v6/ {base_currency}/{target_currency}"  # api key url

    response = requests.get(url)
    return response.json()

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """
    given a currency conversion rate, this function calculates the target currency value from a given base currency value
    """
    return base_currency_value * conversion_rate


get_conversion_factor.invoke({'base_currency':'USD', 'target_currency':'INR'})

convert.invoke({'base_currency_value':10, 'conversion_rate':85.16})

#tool binding

llm = ChatOpenAI()

llm_with_tools = llm.bind_tools([get_conversion_factor, convert])


# tool calling
messages = [HumanMessage('what is the conversion factor between USD and INR, and based on that can you convert 10 usd to inr')]

ai_message = llm_with_tools.invoke(messages)

ai_message.tool_calls



for tool_call in ai_message.tool_calls:
    print(tool_call)

#execute the first tool and get the value of conversion rate
if tool_call['name'] == 'get_conversion_factor':
    tool_message1 = get_conversion_factor.invoke(tool_call)
    print(tool_message1)

    #fetch this conversion rate
    conversion_rate  = json.loads(tool_message1.content['conversion_rate'])
    #append this tool message to message list
    messages.append(tool_message1)


# execute the second tool using the conversion rate from tool 1
    if tool_call['name'] == 'convert':
        #fetch the current argument
        tool_message2 = convert.invoke(tool_call)
        messages.append(tool_message2)

    print(messages)

    print(llm_with_tools.invoke(messages).content)

































































