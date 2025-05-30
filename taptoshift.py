import streamlit as st
from io import BytesIO

# Set page configuration
st.set_page_config(
    page_title="Tap to Shift",
    page_icon="🌬️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom styling: mushroom background and #D9CEC1 buttons
custom_css = """
<style>
body {
    background-color: #EDE6DD;
    color: #3B2F2F;
}
h1, h2, h3, p, label, textarea {
    color: #3B2F2F !important;
}
.stButton > button {
    background-color: #D9CEC1;
    color: white;
    border-radius: 10px;
    padding: 0.5em 2em;
    font-size: 18px;
    border: none;
}
footer {
    visibility: hidden;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Session state initialization
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

# 8A shift prompts
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

step = st.session_state.step

# Page 0: Welcome
if step == 0:
    st.markdown("## Tap to Shift")
    st.markdown("<div style='text-align:center; font-style:italic; font-size:16px; color:#4F4F4F;'>8A Method</div>", unsafe_allow_html=True)
    st.markdown("A gentle reset is one tap away.")
    if st.button("Tap to Begin"):
        st.session_state.step = 1
        st.rerun()


# Pages 1–8: Questions
elif 1 <= step <= 8:
    label, prompt = questions[step - 1]
    st.markdown(f"### {label}")
    st.markdown(f"**{prompt}**")
    response = st.text_area("Your Reflection", key=f"response_{step}")
    if st.button("Next"):
        st.session_state.answers[label] = response
        st.session_state.step += 1
        st.rerun()

# Page 9: Summary
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

# Page 10: Breath message
elif step == 10:
    st.markdown("## 🌬️ Now breathe in… and breathe out.")
    st.markdown("You are a force and beyond amazing.")
    st.markdown("You’re just getting started.")
    st.markdown("Come back anytime.")
    if st.button("Next"):
        st.session_state.step += 1
        st.rerun()

# Page 11: Support
elif step == 11:
    st.markdown("## Would you like to support this experience?")
    st.markdown(
        "This app is free and always will be.\n\n"
        "If it brought you peace, clarity, or alignment, you can support its evolution below."
    )
    st.markdown("[☕ Buy Me a Coffee](https://www.buymeacoffee.com/sheilamaebalaga)")
    st.markdown("🙏 Thank you for your support!")
    if st.button("Start Again"):
        st.session_state.step = 0
        st.session_state.answers = {}
        st.rerun()

# Footer message
st.markdown(
    "<div style='text-align: center; margin-top: 40px; font-size: 14px;'>"
    "Built for your nervous system. With care, always."
    "</div>",
    unsafe_allow_html=True
)
