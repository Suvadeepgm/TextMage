# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:01:13 2024

@author: suvadeep
"""

import streamlit as st
from diffusers import DiffusionPipeline
import torch
from huggingface_hub import login

# Set your Hugging Face API key
hf_api_key = "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"
login(token=hf_api_key)

# Initialize the model and move it to the GPU
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", 
    torch_dtype=torch.float16, 
    use_safetensors=True, 
    variant="fp16"
)
#pipe.to("cuda")

# Streamlit app
st.title("Image Generation with Stable Diffusion")

# Prompt input
prompt = st.text_input("Enter your prompt:")

if prompt:
    with st.spinner("Generating image..."):
        images = pipe(prompt=prompt).images[0]
        st.image(images, caption=prompt)
