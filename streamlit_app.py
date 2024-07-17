import streamlit as st
import requests
from PIL import Image
import io

# Hugging Face API URL and headers
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit app layout
st.title("TextMage: Image Generation from Text Prompt")
st.write("Enter a prompt to generate an image:")

# Text input for the prompt
prompt = st.text_input("Prompt", value="Astronaut riding a horse")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        image_bytes = query({"inputs": prompt})
        image = Image.open(io.BytesIO(image_bytes))
        
        st.image(image, caption=f"Generated image for prompt: '{prompt}'")

# Run Streamlit app
if __name__ == "__main__":
    st.write("App is ready to generate images.")
