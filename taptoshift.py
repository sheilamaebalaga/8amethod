import streamlit as st
from io import BytesIO

# Set page config
st.set_page_config(page_title="Tap to Shift", layout="centered", initial_sidebar_state="collapsed")

# Define app state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.responses = {}

# App styling
st.markdown("""
    <style>
        body {
            background-color: #E6E1F4;
        }
        .title {
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            color: #4B3F72;
        }
        .subtitle {
            font-size: 1.2em;
            text-align: center;
            color: #4B3F72;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Shift prompts
prompts = [
    ("Awareness", "What are you currently feeling or noticing?"),
    ("Acknowledgement", "What truth are you ready to face?"),
    ("Allowing", "Can you allow this feeling to be here for a moment?"),
    ("Acceptance", "Can you embrace this experience without judgment?"),
    ("Acting", "What gentle action or inaction feels right now?"),
    ("Activation", "What insight is becoming real inside you?"),
    ("Alignment", "What truth will carry you forward?"),
    ("Appreciation", "What can you thank yourself for in this moment?")
]

# Step flow
if st.session_state.step == 0:
    st.markdown('<div class="title">Tap to Shift</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">A gentle reset is one tap away.</div>', unsafe_allow_html=True)
    if st.button("Tap to Begin"):
        st.session_state.step = 1

elif 1 <= st.session_state.step <= len(prompts):
    label, question = prompts[st.session_state.step - 1]
    st.markdown(f"### {label}")
    response = st.text_area(question, key=label)
    if st.button("Next"):
        st.session_state.responses[label] = response
        st.session_state.step += 1

elif st.session_state.step == len(prompts) + 1:
    st.success("You've Completed Your 8A Shift")
    st.markdown("Let this new frequency guide your next steps.")
    st.markdown("### Your Reflections:")

    reflection_text = ""
    for label, _ in prompts:
        user_input = st.session_state.responses.get(label, "")
        st.markdown(f"**{label}:** {user_input}")
        reflection_text += f"{label}: {user_input}\n"

    file_buffer = BytesIO(reflection_text.encode('utf-8'))
    st.download_button("Download My Shift", file_buffer, file_name="my_8a_shift.txt", mime="text/plain")

    st.divider()
    st.markdown("### 😬 Now breathe in... and breathe out.")
    st.markdown("You are a force and beyond amazing. You're just getting started. Come back anytime.")

    st.divider()
    st.markdown("### Would you like to support this experience?")
    st.markdown("This app is free and always will be. If it brought you peace, clarity, or alignment, you can support its evolution below.")
    st.markdown("[☕ Buy Me a Coffee](https://www.buymeacoffee.com/sheilamaebalaga)")
