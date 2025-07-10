import streamlit as st
import random

# Prompt data
descriptors = ["soft", "pretty", "delicate", "sultry", "well-moisturized", "girly"]
toes_styles = ["light pink toes", "red polished toes", "french tips", "white-painted toes"]
settings = ["in a milk bath", "on a beach", "in a pool", "on a satin pillow"]
angles = ["from the soles", "with curled toes", "scrunched", "posed on tiptoes"]

def generate_prompt():
    return f"{random.choice(descriptors)} feet with {random.choice(toes_styles)}, {random.choice(settings)}, {random.choice(angles)}"

# Streamlit UI
st.set_page_config(page_title="Feet Prompt Generator", page_icon="🦶")
st.title("🦶 AI Feet Prompt Generator")
st.markdown("Create custom image prompts for AI fetish content.")

if st.button("Generate Prompt"):
    st.success(generate_prompt())
