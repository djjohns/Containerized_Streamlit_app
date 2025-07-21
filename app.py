import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError


# Load environment variables from the .env file
load_dotenv()
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL")

# Validate API key
if not api_key:
    raise ValueError("API_KEY not found in .env file")

# Validate base_url
if base_url:
    # Initialize OpenAI client (new SDK style)
    client = OpenAI(base_url=base_url, api_key=api_key)
else:
    # Initialize OpenAI client (new SDK style)
    client = OpenAI(api_key=api_key)

st.set_page_config(page_title="OpenAI Chat", layout="centered")
st.title(f"💬 Chat with {model}")

prompt = st.text_area("Enter your prompt:")

if st.button("Submit") and prompt:
    with st.spinner(f"Waiting for {model}'s response..."):
        try:
            # Call the latest chat completion method
            response = client.chat.completions.create(
                model=model, messages=[{"role": "user", "content": prompt}]
            )
            st.success("Response:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
