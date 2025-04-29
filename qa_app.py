from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(question):
    response = model.generate_content(question)
    print("Response: ",response)
    parts = response.candidates[0].content.parts
    text = ' '.join(part.text for part in parts)
    return text

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Q&A Application")
input = st.text_input("Ask your question here:",key="input")
submit = st.button("Submit")

## if button is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)