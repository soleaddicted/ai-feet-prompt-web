import streamlit as st
import random

# ------------------------------------------
# 🔐 ACCESS CODE LOCK FOR FANVUE SUBSCRIBERS
# ------------------------------------------
st.set_page_config(page_title="Feet Prompt Generator", page_icon="🦶")
st.title("🦶 AI Feet Prompt Generator")

# Lock the generator behind a password
st.markdown("### 🔐 Subscribers Only")
password = st.text_input("Enter your access code:", type="password")

# Replace this with your Fanvue password
if password != "divinesoles123":
    st.warning("🚫 This prompt generator is for paying Fanvue subscribers only.")
    st.stop()

# ------------------------------------------
# ✨ PROMPT OPTIONS
# ------------------------------------------
descriptors = ["soft", "pretty", "delicate", "sultry", "well-moisturized", "girly"]
toes_styles = ["light pink toes", "red polished toes", "french tips", "white-painted toes"]

sfw_settings = ["in a milk bath", "on a satin pillow", "on a spa towel"]
nsfw_settings = [
    "with whipped cream", "gripping a banana", "dripping in oil",
    "wrapped in latex straps", "with melted chocolate"
]

angles = ["from the soles", "with curled toes", "scrunched", "tiptoed", "spread"]

style_vibes = {
    "Romantic": ["soft lighting", "rose petals", "silky textures"],
    "Taboo": ["forbidden feel", "moody shadows", "close-up shot"],
    "Goddess": ["gold accessories", "worship position", "elevated angle"],
    "Playful": ["fun colors", "lollipop toes", "glitter background"],
    "Glamorous": ["high heels", "expensive jewelry", "lux setting"],
    "Submissive": ["bound ankles", "kneeling position", "humble mood"]
}

# ------------------------------------------
# 🔮 PROMPT GENERATOR FUNCTION
# ------------------------------------------
def generate_prompt(is_nsfw, vibe):
    setting_pool = sfw_settings + nsfw_settings if is_nsfw else sfw_settings
    vibe_addons = style_vibes.get(vibe, [])
    prompt = f"{random.choice(descriptors)} feet with {random.choice(toes_styles)}, "
    prompt += f"{random.choice(setting_pool)}, {random.choice(angles)}"
    if vibe_addons:
        prompt += f", {random.choice(vibe_addons)}"
    return prompt

# ------------------------------------------
# 🎛️ USER INPUTS
# ------------------------------------------
is_nsfw = st.toggle("🔞 NSFW Mode", value=False)
vibe = st.selectbox("🎨 Style / Vibe", list(style_vibes.keys()))

# ------------------------------------------
# 🪄 GENERATE PROMPT
# ------------------------------------------
if st.button("✨ Generate Prompt"):
    st.success(generate_prompt(is_nsfw, vibe))
