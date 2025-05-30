import streamlit as st
from fpdf import FPDF
import io

# Indigo Theme
st.set_page_config(page_title="Tap to Shift", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: #1e1b2e;
        color: white;
    }
    .stButton>button {
        background-color: #7b61ff;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 0.6em 2em;
    }
    .stMarkdown p {
        font-size: 16px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

questions = [
    "Awareness – What situation or moment is stirring something inside you?",
    "Acknowledgement – What's the deeper truth beneath this feeling?",
    "Allowing – Can you give yourself permission to feel it, fully?",
    "Acceptance – Can you embrace it without trying to change or fix it?",
    "Acting – Is there any action or stillness your body wants now?",
    "Activation – What shift has just occurred inside you?",
    "Alignment – What new energy or insight is now guiding you?",
    "Appreciation – What are you grateful for about yourself in this moment?"
]

if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = [""] * len(questions)

step = st.session_state.step

if step == 0:
    st.markdown("## Tap to Shift")
    st.markdown("A gentle reset is one tap away.")
    if st.button("Tap to Begin"):
        st.session_state.step += 1

elif 1 <= step <= len(questions):
    st.markdown(f"### {questions[step - 1]}")
    st.session_state.answers[step - 1] = st.text_area("Your response:", st.session_state.answers[step - 1], height=150)
    if st.button("Tap to continue"):
        st.session_state.step += 1

elif step == len(questions) + 1:
    st.markdown("## You’ve Completed Your 8A Shift")
    st.markdown("<div style='font-size:20px;'>🌬️ Let this new frequency guide your next steps.</div>", unsafe_allow_html=True)

    st.markdown("### Your Reflections:")
    for i, q in enumerate(questions):
        label = q.split("–")[0].strip()
        st.markdown(f"**{label}:** {st.session_state.answers[i]}")

    # PDF Generation
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="My 8A Shift Reflections", ln=True, align="C")
    pdf.ln(10)
    for i, q in enumerate(questions):
        label = q.split("–")[0].strip()
        pdf.multi_cell(0, 10, f"{label}: {st.session_state.answers[i]}")
        pdf.ln(2)

    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    st.download_button("📄 Download My Shift as PDF", data=pdf_buffer, file_name="My_8A_Shift.pdf", mime="application/pdf")

    if st.button("Next"):
        st.session_state.step += 1

elif step == len(questions) + 2:
    st.markdown("## 🌬️ Now breathe in... and breathe out.")
    st.markdown("""
    You are a force and beyond amazing.  
    You're just getting started.  
    Come back anytime.
    """)

    if st.button("Next"):
        st.session_state.step += 1

elif step == len(questions) + 3:
    st.markdown("## Would you like to support this experience?")
    st.markdown("""
    This app is free and always will be.  
    If it brought you peace, clarity, or alignment, you can support its evolution below.

    ☕ [Buy Me a Coffee](https://www.buymeacoffee.com/sheilamaebalaga)

    Thanks for your support 💜
    """, unsafe_allow_html=True)

    if st.button("Start Again"):
        st.session_state.step = 0
        st.session_state.answers = [""] * len(questions)
