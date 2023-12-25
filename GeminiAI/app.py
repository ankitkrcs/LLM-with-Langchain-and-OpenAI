from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(ques):
    response = model.generate_content(ques)
    return response.text


st.header("Gemini Application")
input = st.text_input("Input",key="input")
submit = st.button("Ask the Questions")

if submit:
    response = get_gemini_response(input)
    st.write(response)