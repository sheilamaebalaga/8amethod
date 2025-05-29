import streamlit as st
from io import StringIO

# --- Custom Theme Styling ---
st.markdown("""
    <style>
        .stApp {
            background-color: #EAE6FA;
            font-family: 'Helvetica Neue', sans-serif;
        }
        h1, h2, h3, h4, h5, h6, p, label, div, span {
            color: #3C2C72;
        }
        .stTextInput>div>div>input, textarea {
            background-color: #F4F1FC;
            color: #3C2C72;
            border: none;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton>button, .stDownloadButton>button {
            background-color: #5A54C4;
            color: #ffffff;
            border: none;
            border-radius: 10px;
            font-weight: bold;
            padding: 10px 20px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Session State Setup ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# --- 8A Method Steps ---
steps = [
    ("Tap to Shift", "A gentle reset is one tap away."),
    ("Awareness", "What are you currently feeling or noticing inside you?"),
    ("Acknowledgement", "Can you gently acknowledge what this is really about?"),
    ("Allowing", "Let yourself feel it without trying to change it. What arises?"),
    ("Acceptance", "Can you embrace this part of you with compassion?"),
    ("Acting", "What inspired action (or non-action) naturally wants to arise?"),
    ("Activation", "Let the insight or energy shift happen inside. What shifted?"),
    ("Alignment", "What insight feels true and aligned for you moving forward?"),
    ("Appreciation", "Take a moment to feel gratitude. What are you thankful for?"),
    ("Completed", "You've completed your 8A Shift.")
]

# --- Main Logic ---
if st.session_state.step == 0:
    st.markdown(f"<h1>{steps[0][0]}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p>{steps[0][1]}</p>", unsafe_allow_html=True)
    if st.button("Tap to Begin"):
        st.session_state.step += 1
else:
    if st.session_state.step < len(steps) - 1:
        step_title, step_prompt = steps[st.session_state.step]
        st.markdown(f"<h2>{step_title}</h2>", unsafe_allow_html=True)
        user_input = st.text_area(step_prompt)
        if st.button("Next"):
            st.session_state.responses[step_title] = user_input
            st.session_state.step += 1
    else:
        st.success("You've aligned your energy. Let this new frequency guide your next steps.")
        st.markdown("<h3>Your Reflections:</h3>", unsafe_allow_html=True)
        for key, value in st.session_state.responses.items():
            st.markdown(f"**{key}:** {value}")

        # Download Button
        reflections = "\n".join([f"{k}: {v}" for k, v in st.session_state.responses.items()])
        file_buffer = StringIO(reflections)
        st.download_button("Download My Shift", file_buffer, file_name="my_8a_shift.txt")

        # Closing Message
        st.markdown("""
        <h4>🧘‍♀️ Now breathe in… and breathe out.</h4>
        <p>You are a force and beyond amazing.<br>
        You’re just getting started.<br>
        Come back anytime.</p>
        <hr>
        <h4>Would you like to support this experience?</h4>
        <p>This app is free and always will be. If it brought you peace, clarity, or alignment, you can support its evolution below.</p>
        <a href="https://www.buymeacoffee.com/yourname" target="_blank">☕ Buy Me a Coffee</a>
        """, unsafe_allow_html=True)

        if st.button("Reset App"):
            st.session_state.step = 0
            st.session_state.responses = {}
