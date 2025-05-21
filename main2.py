import streamlit as st

st.set_page_config(page_title="Tap to Align", layout="centered")

# Welcome screen
if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.markdown("<h1 style='text-align: center;'>Tap to Align</h1>", unsafe_allow_html=True)
    st.write("Welcome to your energetic reset. Breathe in. Let’s begin.")
    if st.button("Begin My 8A Shift"):
        st.session_state.started = True
    st.stop()

# 8A Prompt Method
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

st.title("Your 8A Shift")

for key, prompt in prompts.items():
    if st.button(key):
        st.markdown(f"### {prompt}")
        st.stop()

# Optional: Closing message
st.markdown("---")
st.write("You’ve reached the end of your alignment cycle. Breathe in. You’re home.")
