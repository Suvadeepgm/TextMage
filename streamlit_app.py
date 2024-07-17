import streamlit as st
import requests
from PIL import Image
import io

# Hugging Face API URL and headers
#API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
#API_URL = "https://api-inference.huggingface.co/models/fal/AuraFlow"
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit app layout
st.title("TextMage ")
st.write("Image Generation from Text Prompt")

# Text input for the prompt
prompt = st.text_input("Enter a prompt to generate an image", value="")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        image_bytes = query({"inputs": prompt})
        image = Image.open(io.BytesIO(image_bytes))
        
        st.image(image, caption=f"Generated image for prompt: '{prompt}'")

# Run Streamlit app
#if __name__ == "__main__":
    #st.write("App is ready to generate images.")
