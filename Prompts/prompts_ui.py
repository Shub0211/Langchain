from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatOpenAI()

st.header('Resaerch Tool')

#user_input = st.text_input("Enter your prompt") # static Prompting

#dynamic prompting

paper_input = st.selectbox("select research paper name", ["attention is all you need","BERT","GPT-3","Diffusion"])

style_input = st.selectbox("select explanation style", ["begineer friendly","techgnical","code oriented","mathematical"])

length_input = st.selectbox("select explanation length", ["short (1-2 para)","Medium (3-5 para)","Long(detailed explanation)"])

template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | model 
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    #fill the placeholder
    # prompt = template.invoke()
    # result = model.invoke(prompt)
    st.write(result.content)
    # st.write("Hello")
    # print(result.content)










