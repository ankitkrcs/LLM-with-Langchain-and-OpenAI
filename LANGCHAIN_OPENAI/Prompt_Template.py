# Integrate to our Code for OpenAI
import os
from constant import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

#streamlit framework
st.title("Celebrity Search Result")
input_text = st.text_input("Search the topic you Want")

#Prompt Template
first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)
## OPENAI LLMS
llm = OpenAI(temperature=0.9)  
chain = LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='title')
llm = OpenAI(temperature=0.9)  

#second Template
first_input_prompt=PromptTemplate(
    input_variables=['person'],
    template="when was {person} born"
)
chain2 = LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='dob')

#third template
third_input_prompt=PromptTemplate(
    input_variables=['sentence','target_language'],
    template='In an easy way translate this {sentence} into target {target_language}',
)
chain3 = LLMChain(llm==llm,prompt=third_input_prompt,verbose=True)
parent_chain=SimpleSequentialChain(chains=[chain,chain3],verbose=True)


if input_text:
    st.write(llm(parent_chain.run(input_text)))

