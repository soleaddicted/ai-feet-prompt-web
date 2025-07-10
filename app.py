import streamlit as st
import random

# --- Prompt Pools ---
# Common across all modes
descriptors = ["soft", "pretty", "delicate", "sultry", "well-moisturized", "girly"]
toes_styles = ["light pink toes", "red polished toes", "french tips", "white-painted toes"]

# SFW settings
sfw_settings = ["in a milk bath", "on a satin pillow", "on a spa table", "by candlelight"]

# NSFW settings (more suggestive)
nsfw_settings = [
    "with whipped cream", "dripping in oil", "wrapped in latex straps", 
    "with toe rings and anklets", "gripping a banana", "with melted chocolate"
]

angles = ["from the soles", "with curled toes", "scrunched", "tiptoed", "spread"]

# Style themes
style_vibes = {
    "Romantic": ["soft lighting", "rose petals", "silky textures"],
    "Taboo": ["forbidden feel", "moody shadows", "close-up shot"],
    "Goddess": ["gold accessories", "worship position", "elevated angle"],
    "Playful": ["fun colors", "lollipop toes", "glitter background"],
    "Glamorous": ["high heels", "expensive jewelry", "lux setting"],
    "Submissive": ["bound ankles", "kneeling position", "humble mood"]
}

# --- Prompt Generator ---
def generate_prompt(is_nsfw, vibe):
    setting_pool = sfw_settings + nsfw_settings if is_nsfw else sfw_settings
    theme_addons = style_vibes.get(vibe, [])

    prompt = f"{random.choice(descriptors)} feet with {random.choice(toes_styles)}, "
    prompt += f"{random.choice(setting_pool)}, {random.choice(angles)}"
    
    if theme_addons:
        prompt += f", {random.choice(theme_addons)}"

    return prompt

# --- Streamlit UI ---
st.set_page_config(page_title="Feet Prompt Generator", page_icon="🦶")
st.title("🦶 AI Feet Prompt Generator")
st.markdown("Generate creative, themed AI prompts for feet content.")

# User input controls
is_nsfw = st.toggle("🔞 NSFW Mode", value=False)
vibe = st.selectbox("🎨 Style / Vibe", list(style_vibes.keys()))

if st.button("✨ Generate Prompt"):
    prompt = generate_prompt(is_nsfw, vibe)
    st.success(prompt)
