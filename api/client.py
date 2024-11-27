import requests
import streamlit as st

def get_llama3_response(input_text):
    response=requests.post('http://localhost:8000/disease/invoke',
                           json={'input':{'topic':input_text}})
    return response.json()['output']['content']

def get_gemma2_response(input_text):
    response=requests.post('http://localhost:8000/medication/invoke',
                           json={'input':{'topic':input_text}})
    return response.json()['output']

st.title('LangChain API integration using LLAMA3.1 & Gemma2')
input_text = st.text_input('Mention the disease here!')
input_text1 = st.text_input('Mention the medication here!')

if input_text:
    st.write(get_llama3_response(input_text))
if input_text1:
    st.write(get_gemma2_response(input_text1))