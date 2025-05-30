# tap_to_shift.py

import streamlit as st
from fpdf import FPDF
import io

# Set page config and custom theme
st.set_page_config(page_title="Tap to Shift", layout="centered")
st.markdown("""
    <style>
        body {
            background-color: #0e0e23;
            color: #f0f0f5;
        }
        .stButton>button {
            background-color: #7e6ed6;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
        }
    </style>
""", unsafe_allow_html=True)

# App steps logic
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

questions = [
    "Awareness – What situation or moment is stirring something inside you?",
    "Acknowledgement – What truth beneath the feeling are you recognizing?",
    "Allowing – What emotion are you giving yourself permission to feel now?",
    "Acceptance – What are you choosing to embrace without judgment?",
    "Acting – Is there an action or stillness that naturally arises now?",
    "Activation – What shift or insight is becoming real for you?",
    "Alignment – How do you want to carry this into your next step?",
    "Appreciation – What gratitude do you feel in this moment?"
]

# --- Step-by-step flow ---

if st.session_state.step == 0:
    st.title("Tap to Shift")
    st.write("A gentle reset is one tap away.")
    if st.button("Tap to Begin"):
        st.session_state.step += 1

elif 1 <= st.session_state.step <= len(questions):
    idx = st.session_state.step - 1
    st.markdown(f"### {questions[idx]}")
    response = st.text_area("Your reflection:", key=f"q{idx}")
    if st.button("Next"):
        st.session_state.answers.append(response)
        st.session_state.step += 1

elif st.session_state.step == len(questions) + 1:
    st.markdown("## You’ve Completed Your 8A Shift")
    st.success("Let this new frequency guide your next steps.")

    st.markdown("### Your Reflections:")
    for i, answer in enumerate(st.session_state.answers):
        st.markdown(f"**{questions[i].split('–')[0].strip()}:** {answer}")

    # Create downloadable PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="My 8A Shift Reflections", ln=True, align='C')
    pdf.ln()
    for i, answer in enumerate(st.session_state.answers):
        pdf.multi_cell(0, 10, txt=f"{questions[i].split('–')[0].strip()}: {answer}")
    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    st.download_button("Download My Shift as PDF", pdf_buffer, file_name="my_8a_shift.pdf")

    if st.button("Next"):
        st.session_state.step += 1

elif st.session_state.step == len(questions) + 2:
    st.markdown("""
        ## 🌬️ Now breathe in... and breathe out.
        You are a force and beyond amazing.  
        You’re just getting started.  
        Come back anytime.
    """)
    if st.button("Next"):
        st.session_state.step += 1

elif st.session_state.step == len(questions) + 3:
    st.markdown("""
        ## Would you like to support this experience?
        This app is free and always will be. If it brought you peace, clarity, or alignment, you can support its evolution below.  
        ☕ [Buy Me a Coffee](https://www.buymeacoffee.com/sheilamaebalaga)

        Thanks for your support 🤍
    """)
    if st.button("Start Again"):
        st.session_state.step = 0
        st.session_state.answers = []
