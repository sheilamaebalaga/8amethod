import streamlit as st
from io import BytesIO

# Set up the app config
st.set_page_config(
    page_title="Tap to Shift",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Apply mushroom background and indigo button theme
custom_style = """
<style>
body {
    background-color: #d2c9c3;
    color: black;
}

h1, h2, h3, p, button, label, input, textarea, .stTextInput, .stTextArea {
    color: black !important;
}

.stButton > button {
    background-color: #6f00ff;
    color: white !important;
    border-radius: 10px;
    padding: 0.6em 2em;
    font-size: 18px;
    font-weight: 500;
    border: none;
}

.stMarkdown {
    color: black;
}
</style>
"""
st.markdown(custom_style, unsafe_allow_html=True)

# Session state setup
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

# 8A Questions
questions = [
    ("Awareness", "What are you currently feeling or facing?"),
    ("Acknowledgement", "Can you honor what’s real for you right now?"),
    ("Allowing", "Can you allow yourself to feel this without resistance?"),
    ("Acceptance", "What part of this can you embrace without judgment?"),
    ("Acting", "Is there an inspired action (or inaction) you feel?"),
    ("Activation", "What new insight is surfacing for you?"),
    ("Alignment", "How can you carry this forward from here?"),
    ("Appreciation", "What are you grateful for in this exact moment?")
]

# App Flow
step = st.session_state.step

if step == 0:
    st.markdown("## Tap to Shift")
    st.markdown("A gentle reset is one tap away.")
    if st.button("Tap to Begin"):
        st.session_state.step += 1
        st.rerun()

elif 1 <= step <= 8:
    label, prompt = questions[step - 1]
    st.markdown(f"### {label}")
    st.markdown(f"**{prompt}**")
    response = st.text_area("Your Reflection", key=f"response_{step}")
    if st.button("Next"):
        st.session_state.answers[label] = response
        st.session_state.step += 1
        st.rerun()

elif step == 9:
    st.markdown("## Let this new frequency guide your next steps.")
    st.markdown("### Your Reflections:")
    summary = ""
    for label, _ in questions:
        answer = st.session_state.answers.get(label, "")
        st.markdown(f"**{label}:** {answer}")
        summary += f"{label}: {answer}\n\n"

    buffer = BytesIO()
    buffer.write(summary.encode())
    buffer.seek(0)
    st.download_button("Download My Shift", buffer, file_name="my_8a_shift.txt", mime="text/plain")

    if st.button("Continue"):
        st.session_state.step += 1
        st.rerun()

elif step == 10:
    st.markdown("## 🌬️ Now breathe in… and breathe out.")
    st.markdown("You are a force and beyond amazing.")
    st.markdown("You’re just getting started.")
    st.markdown("Come back anytime.")
    if st.button("Next"):
        st.session_state.step += 1
        st.rerun()

elif step == 11:
    st.markdown("## Would you like to support this experience?")
    st.markdown("""
        This app is free and always will be.
        
        If it brought you peace, clarity, or alignment, you can support its evolution below.

        [☕ Buy Me a Coffee](https://www.buymeacoffee.com/sheilamaebalaga)  
        🙏 Thank you for your support!
    """)
    if st.button("Start Again"):
        st.session_state.step = 0
        st.session_state.answers = {}
        st.rerun()
