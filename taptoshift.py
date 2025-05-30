import streamlit as st
from io import BytesIO

# Page setup
st.set_page_config(
    page_title="Tap to Shift",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
custom_css = """
    <style>
        body {
            background-color: #FDF6EC;
        }
        .title-text {
            font-size: 2.5em;
            font-weight: bold;
            color: #2D1F17;
            margin-bottom: 0.1em;
        }
        .subtitle-text {
            font-size: 1.2em;
            color: #444;
            margin-top: 0.1em;
            margin-bottom: 2em;
        }
        .custom-button button {
            background-color: #9E8A7C;
            color: white;
            font-size: 1.1em;
            padding: 0.8em 2em;
            border-radius: 25px;
            border: none;
        }
        .footer-message {
            margin-top: 4em;
            text-align: center;
            color: #2D1F17;
            font-size: 0.9em;
            opacity: 0.8;
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

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

# Page 0: Welcome with styled layout
if step == 0:
    st.image("https://cdn-icons-png.flaticon.com/512/3062/3062634.png", width=150)
    st.markdown("<div class='title-text'>Tap to Shift</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle-text'>A gentle reset is one tap away.</div>", unsafe_allow_html=True)
    if st.button("Tap to Begin", key="start", help="Start the 8A method"):
        st.session_state.step += 1
        st.rerun()

# Pages 1-8: Reflection Questions
elif 1 <= step <= 8:
    label, prompt = questions[step - 1]
    st.markdown(f"### {label}")
    st.markdown(f"**{prompt}**")
    response = st.text_area("Your Reflection", key=f"response_{step}")
    if st.button("Next"):
        st.session_state.answers[label] = response
        st.session_state.step += 1
        st.rerun()

# Page 9: Summary and Download
elif step == 9:
    st.markdown("## 🌬️ Let this new frequency guide your next steps.")
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

# Page 10: Affirmation
elif step == 10:
    st.markdown("## 🌬️ Now breathe in… and breathe out.")
    st.markdown("You are a force and beyond amazing.")
    st.markdown("You’re just getting started. Come back anytime.")
    if st.button("Next"):
        st.session_state.step += 1
        st.rerun()

# Page 11: Support message
elif step == 11:
    st.markdown("## Would you like to support this experience?")
    st.markdown("This app is free and always will be.\n\nIf it brought you peace, clarity, or alignment, you can support its evolution below.")
    st.markdown("[☕ Buy Me a Coffee](https://www.buymeacoffee.com/sheilamaebalaga)")
    st.markdown("🙏 Thank you for your support!")

# Page Footer for all pages except the first
if step > 0:
    st.markdown("<div class='footer-message'>Built for your nervous system. With care, always.</div>", unsafe_allow_html=True)
