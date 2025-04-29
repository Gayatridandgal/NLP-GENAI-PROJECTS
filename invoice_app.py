from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text, image):
    if input_text:  # Ensure input is not empty
        response = model.generate_content([input_text, image])
        parts = response.candidates[0].content.parts  # Correctly access parts
        text = ' '.join(part.text for part in parts if hasattr(part, "text"))  # Ensure part has text attribute
        return text
    return "No valid input provided."

# Streamlit UI
st.set_page_config(page_title="GEMINI Image Demo")
st.header("Invoice Extractor Application")

input_text = st.text_input("Input prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = None  # Initialize image variable

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.")

submit = st.button("Tell me about the image")

if submit and image is not None:
    response = get_gemini_response(input_text, image)
    st.subheader("The response is:")
    st.write(response)
elif submit:
    st.write("Please upload an image before submitting.")