import streamlit as st

st.set_page_config(page_title="Tap to Align", layout="centered")

# Define the 8A prompts
prompts = {
    "Awareness": "What are you feeling or noticing right now?",
    "Allowing": "Can you let that feeling exist without trying to fix it?",
    "Acknowledgement": "What truth or memory is behind this emotion?",
    "Acceptance": "Can you accept this part of your experience without resistance?",
    "Acting": "What aligned action (or stillness) feels true right now?",
    "Activation": "What new truth or energy is awakening in you?",
    "Alignment": "How does this shift your energy and perspective?",
    "Appreciation": "What can you thank yourself or this moment for?"
}

# Session setup
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.responses = {}

# Welcome screen
if st.session_state.step == 0:
    st.markdown("<h1 style='text-align: center;'>Tap to Align</h1>", unsafe_allow_html=True)
    st.write("Welcome to your energetic reset. Breathe in. Let’s begin.")
    if st.button("Begin My 8A Shift"):
        st.session_state.step = 1
    st.stop()

# Show current step
keys = list(prompts.keys())
current_key = keys[st.session_state.step - 1]
current_prompt = prompts[current_key]

st.header(current_key)
response = st.text_input(current_prompt, key=current_key)

if st.button("Next"):
    if response:
        st.session_state.responses[current_key] = response
        st.session_state.step += 1

# Completion screen
if st.session_state.step > len(prompts):
    st.markdown("## You’ve Completed Your 8A Shift")
    st.success("You’ve aligned your energy. Let this new frequency guide your next steps.")
    st.markdown("### Your Responses:")
    for key, value in st.session_state.responses.items():
        st.write(f"**{key}:** {value}")
