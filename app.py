import streamlit as st
import random
import requests
from io import BytesIO
from PIL import Image
import base64

# -------------------------
# Load your API key securely
# -------------------------
api_key = st.secrets["stability"]["api_key"]

# -------------------------
# Password protection for Fanvue subscribers
# -------------------------
st.title("🦶 AI Feet Prompt & Image Generator")
st.markdown("### 🔐 Subscribers Only")
password = st.text_input("Enter your access code:", type="password")
if password != "divinesoles123":
    st.warning("🚫 This prompt generator is for paying Fanvue subscribers only.")
    st.stop()

# -------------------------
# Prompt generator function
# -------------------------
def generate_prompt():
    descriptors = ["soft", "pretty", "delicate", "sultry"]
    toes_styles = ["red polished toes", "light pink toes", "french tips"]
    settings = ["in a milk bath", "on a spa towel", "with rose petals"]
    return f"{random.choice(descriptors)} feet with {random.choice(toes_styles)}, {random.choice(settings)}"

prompt = generate_prompt()
st.markdown(f"### Generated Prompt:\n*{prompt}*")

# -------------------------
# Generate image button
# -------------------------
if st.button("Generate Image"):
    st.markdown("Generating image, please wait...")

    url = "https://api.stability.ai/v1/generation/stable-diffusion-v1-5/text-to-image"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    json_data = {
        "text_prompts": [{"text": prompt}],
        "cfg_scale": 7,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 512,
        "width": 512,
        "samples": 1,
        "steps": 30
    }

    response = requests.post(url, headers=headers, json=json_data)

    if response.status_code == 200:
        data = response.json()
        image_data = data['artifacts'][0]['base64']
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        st.image(image, caption="AI Generated Feet Art")
    else:
        st.error(f"Image generation failed: {response.text}")


