 import streamlit as st

st.set_page_config(page_title="Tap to Align", layout="centered")

# Define the 8A prompts
prompts = {
    "Awareness": "What are you feeling right now?",
    "Acknowledgement": "What truth or moment are you noticing?",
    "Allowing": "Can you let that feeling be there, just for now?",
    "Acceptance": "Can you accept this moment as it is?",
    "Alignment": "What matters most to you right now?",
    "Adjustment": "What shift do you choose to make in this moment?",
    "Action": "What is one small action you can take next?",
    "Anchoring": "How will you carry this energy forward today?"
}

# Welcome screen
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.responses = {}

if st.session_state.step == 0:
    st.markdown("<h1 style='text-align: center;'>Tap to Align</h1>", unsafe_allow_html=True)
    st.write("Tap to Align is a sacred space in your pocket—designed to gently guide you back to yourself.")
    st.write("Through 8 intentional prompts, this app offers a moment of pause, presence, and personal power.")
    st.write("It’s not about fixing. It’s about remembering who you are.")
    st.markdown("---")
    st.markdown("**Create a Ritual of Return**  \nMake this your daily check-in. A tap becomes a reset.  \n**Accessible. Private. Deeply Yours.**  \nNo advice. No noise. No distractions.")
    st.markdown("> *The shift you’ve been seeking isn’t outside you. It’s within.*  \n✨Tap in. Align. Proceed.")
    if st.button("Begin My 8A Shift"):
        st.session_state.step = 1
    st.stop()

# Show current step
keys = list(prompts.keys())
if st.session_state.step <= len(keys):
    current_key = keys[st.session_state.step - 1]
    st.header(current_key)
    response = st.text_input(prompts[current_key], key=current_key)

    if st.button("Next"):
        if response:
            st.session_state.responses[current_key] = response
            st.session_state.step += 1
    st.stop()

# Completion screen
if st.session_state.step > len(keys):
    st.success("✨ You’ve aligned your energy. Let this new frequency guide your next steps.")
    st.markdown("### 🪞 Your Reflections:")
    for key, value in st.session_state.responses.items():
        st.write(f"**{key}:** {value}")

    st.markdown("---")
    st.markdown("**Now breathe in… and breathe out…**")
    st.markdown("Thank yourself for creating space to pause, connect with your body, calm down, and choose what’s best for you in this exact moment.")
    st.markdown("**You are a force and beyond amazing.**")
    st.markdown("You’re just getting started.")
    st.markdown("**Come back anytime.**")

    st.markdown("---")
    st.subheader("Would you like to support this experience?")
    st.write("This app is free and always will be. If it brought you peace, clarity, or alignment, you can support it below.")
    st.markdown("[☕ Buy Me a Coffee](https://www.buymeacoffee.com/sheilamaebalaga)")
