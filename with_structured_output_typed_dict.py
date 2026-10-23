from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()

#schema

class Review(TypedDict):

    Key_themes: Annotated[list[str], " Write down all the key themes discussed in the list"]
    summary: Annotated[str, "A breif summary of the review"] #Annotated Dict
    sentiment: Annotated[Literal["pos","neg"], "Return sentiment of the review either negative, positive or neutral"] #Annotated Dict
    # summary:str #simple dict
    # sentiment:str #simple dict
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviwer"]

structred_model = model.with_structured_output(Review)

result = model.invoke("""The Apple iPhone 17 is a premium smartphone that offers a smooth user experience, an excellent display, impressive cameras, and reliable performance. Its modern design and integration with the Apple ecosystem make it a good choice for everyday use, photography, gaming, and productivity. 

Overall, the iPhone 17 is a strong option for users who value a premium design, smooth performance, reliable cameras, and long-term software support. However, its price and limited customization may be drawbacks for budget-conscious buyers or users who prefer Android.

Pros
The display delivers vibrant colors, sharp details, and smooth scrolling.
Handles everyday tasks, multitasking, and demanding applications smoothly.
Captures detailed photos with natural colors and performs well in various lighting conditions.
Features a stylish build with a high-quality finish.
iOS provides an intuitive interface, regular software updates, and useful security features.
Offers convenient connectivity with compatible modern accessories.

Cons

The iPhone 17 may be costly compared with several Android smartphones offering similar hardware.
Charging may feel slower than that of some competing smartphones.
iOS offers less flexibility for personalization than Android.
Storage cannot be expanded using a microSD card.
A charging adapter and other accessories may need to be purchased separately.
Some features work best when using other Apple devices and services.

Review by Shubham Chauhan

""")

print(result)

print(result['summary'])
print(result['sentiment'])

















