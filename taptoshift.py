import streamlit as st
from fpdf import FPDF
from io import BytesIO

# Set page config with your preferred theme color
st.set_page_config(page_title="Tap to Shift", page_icon="🔄", layout="centered")

# Apply custom CSS for background and button styling
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            background-color: #f3f0ff;
            color: #2e1065;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .stButton button {
            background-color: #8e80f9;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1.5em;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Store answers in session
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

questions = [
    "Awareness — What is stirring something inside you?",
    "Acknowledgement — What's the truth underneath the feeling?",
    "Allowing — Can you give yourself permission to feel it fully?",
    "Acceptance — What part of your experience can you embrace?",
    "Acting — Is there an action (or non-action) that wants to arise?",
    "Activation — What insight just became real within you?",
    "Alignment — How do you want to carry yourself forward?",
    "Appreciation — What can you thank yourself for in this moment?"
]

if st.session_state.step == 0:
    st.markdown("""
        ## Tap to Shift
        A gentle reset is one tap away.
    """)
    if st.button("Tap to Begin"):
        st.session_state.step += 1

elif 1 <= st.session_state.step <= len(questions):
    st.markdown(f"### {questions[st.session_state.step - 1]}")
    answer = st.text_area("Tap to type your reflection")
    if st.button("Next"):
        st.session_state.answers.append(answer)
        st.session_state.step += 1

elif st.session_state.step == len(questions) + 1:
    st.success("You've completed your 8A Shift")
    st.markdown("""
        ### 🌬️ Let this new frequency guide your next steps.
    """)
    st.markdown("#### Your Reflections:")
    for q, a in zip(questions, st.session_state.answers):
        st.markdown(f"**{q.split(' — ')[0]}:** {a}")

    # PDF Creation
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="My 8A Shift Reflections", ln=True, align="C")
    pdf.ln()
    for q, a in zip(questions, st.session_state.answers):
        pdf.multi_cell(0, 10, f"{q.split(' — ')[0]}: {a}")
        pdf.ln()
    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    st.download_button("Download My Shift", buffer, file_name="my_8a_shift.pdf")

    if st.button("Continue"):
        st.session_state.step += 1

elif st.session_state.step == len(questions) + 2:
    st.markdown("""
        ## 🌬️ Now breathe in... and breathe out.
        You are a force and beyond amazing.  
        You're just getting started.  
        Come back anytime.
    """)
    if st.button("Next"):
        st.session_state.step += 1

elif st.session_state.step == len(questions) + 3:
    st.markdown("""
        ## Would you like to support this experience?
        This app is free and always will be. If it brought you peace, clarity, or alignment, you can support its evolution below.  
        ☕ [Buy Me a Coffee](https://www.buymeacoffee.com/)  
    """)
    if st.button("Start Again"):
        st.session_state.step = 0
        st.session_state.answers = []
