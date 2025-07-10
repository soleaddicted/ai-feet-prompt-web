import streamlit as st
import random
import requests
from io import BytesIO
from PIL import Image

# Your existing prompt generator code here...

# Sample prompt generation function (simplified)
def generate_prompt():
    descriptors = ["soft", "pretty", "delicate"]
    toes = ["red polished toes", "light pink toes"]
    settings = ["in a milk bath", "on a spa towel"]
    return f"{random.choice(descriptors)} feet with {random.choice(toes)}, {random.choice(settings)}"

st.title("🦶 AI Feet Prompt & Image Generator")

prompt = generate_prompt()

st.markdown(f"### Generated Prompt:\n*{prompt}*")

if st.button("Generate Image"):
    st.markdown("Generating image, please wait...")

    # Call Stability API
    api_key = "YOUR_STABILITY_API_KEY"
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

