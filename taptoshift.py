import streamlit as st
from io import BytesIO

# Set the page config
st.set_page_config(
    page_title="Tap to Shift",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Indigo Theme Styling
st.markdown("""
    <style>
        body {
            background-color: #5A54C4;
        }
        h1, h2, h3, p, label, textarea, button {
            color: white !important;
        }
        .stButton > button {
            background-color: #7F76D9;
            color: white;
            border-radius: 8px;
            padding: 0.6em 2em;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Session Setup
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

# 8A Reflection Prompts
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

# --- Page 0: Welcome ---
if step == 0:
    st.title(" Tap to Shift")
    st.write("A gentle reset is one tap away.")
    if st.button("Tap to Begin"):
        st.session_state.step += 1
        st.rerun()

# --- Pages 1-8: 8A Questions ---
elif 1 <= step <= 8:
    label, prompt = questions[step - 1]
    st.subheader(label)
    st.write(prompt)
    response = st.text_area("Your Reflection", key=f"response_{step}")
    if st.button("Next"):
        st.session_state.answers[label] = response
        st.session_state.step += 1
        st.rerun()

# --- Page 9: Reflections Summary + Download ---
elif step == 9:
    st.markdown("## 🌬️ Let this new frequency guide your next steps.")
    st.markdown("### Your Reflections:")

    summary = ""
    for label, _ in questions:
        answer = st.session_state.answers.get(label, "")
        st.markdown(f"**{label}:** {answer}")
        summary += f"{label}:\n{answer}\n\n"

    # Create downloadable .txt file
    buffer = BytesIO()
    buffer.write(summary.encode())
    buffer.seek(0)
    st.download_button("📄 Download My Shift", buffer, file_name="my_8a_shift.txt", mime="text/plain")

    if st.button("Continue"):
        st.session_state.step += 1
        st.rerun()

# --- Page 10: Breathe + Affirmation ---
elif step == 10:
    st.markdown("## 🌬️ Now breathe in… and breathe out.")
    st.write("You are a force and beyond amazing.")
    st.write("You’re just getting started.")
    st.write("Come back anytime.")
    if st.button("Next"):
        st.session_state.step += 1
        st.rerun()

# --- Page 11: Support Page ---
elif step == 11:
    st.markdown("## ☕ Would you like to support this experience?")
    st.write("This app is free and always will be.")
    st.write("If it brought you peace, clarity, or alignment, you can support its evolution below.")
    st.markdown("[Buy Me a Coffee](https://www.buymeacoffee.com/sheilamaebalaga)")
    st.markdown("🙏 Thank you for your support!")
    if st.button("Start Again"):
        st.session_state.step = 0
        st.session_state.answers = {}
        st.rerun()
