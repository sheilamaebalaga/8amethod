import streamlit as st

st.set_page_config(page_title="Tap to Shift", layout="centered")

# Define the 8A prompts
prompts = {
    "Awareness": "What are you feeling or noticing right now?",
    "Acknowledgement": "What truth or memory is behind this emotion?",
    "Allowing": "Can you let that feeling exist without trying to fix it?",
    "Acceptance": "Can you accept this part of your experience without resistance?",
    "Acting": "What aligned action (or nonaction) feels true right now?",
    "Activation": "What new truth or energy is awakening in you?",
    "Alignment": "How does this shift your energy and perspective?",
    "Appreciation": "What can you thank yourself or this moment for?"
}

# Session setup
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.responses = {}

# Welcome screen
if st.session_state.step == 0:
    st.markdown("<h1 style='text-align: center;'>Tap to Shift</h1>", unsafe_allow_html=True)

    st.write("""
    The 8A Method is a moment-to-moment energetic shift.  
    Whether you're navigating something heavy, uncertain, joyful, or overwhelming, this method helps you slow down, tune in, discern, and realign.  
    It’s not about fixing how you feel. It’s about being fully present with it, so something deeper can emerge—tuning into better outcomes that support your well-being.
    """)

    st.markdown("---")
    st.subheader("The 8 Steps")
    st.markdown("""
- **Awareness** – Recognize what situation or moment is stirring something inside you.  
- **Acknowledgement** – Gently name the truth beneath the feeling—what it's really about.  
- **Allowing** – Give yourself permission to feel it, without resistance or control.  
- **Acceptance** – Embrace this part of your experience without shame, shoulds, or stories.  
- **Acting** – Feel into whether any action (or non-action) naturally wants to arise.  
- **Activation** – Let the insight or shift become real within you, even if it's subtle.  
- **Alignment** – Integrate this shift—how do you want to carry yourself forward from here?  
- **Appreciation** – Close with gratitude—for your courage, your presence, and this inner moment.
    """)

    st.markdown("---")
    st.subheader("✨ Benefits")
    st.markdown("**1. Reset Your Energy in Minutes**  \nFeel off? Overwhelmed? Disconnected? Tap through 8 steps to realign with your truth.")
    st.markdown("**2. Anchor Into Presence**  \nEach prompt invites you into the now—calm, conscious, and grounded.")
    st.markdown("**3. Hold Space for Your Emotions**  \nInstead of escaping what you feel, this app teaches you how to witness it without judgment.")
    st.markdown("**4. Activate Your Inner Wisdom**  \nThe journey ends in clarity, not confusion. These prompts help awaken insights already inside you.")
    st.markdown("**5. Create a Ritual of Return**  \nMake this your daily check-in. A tap becomes your sacred pause—morning, mid-storm, or just before sleep.")
    st.markdown("**6. Accessible. Private. Deeply Yours.**  \nNo advice. No noise. No distractions. Just you, your truth, and a quiet return to alignment.")

    st.markdown("---")
    st.markdown("> *The shift you’ve been seeking isn’t outside you. It’s within.*  \n**Tap in. Align. Begin again.**")

    if st.button("Begin My 8A Shift"):
        st.session_state.step = 1
    st.stop()

# Prompt steps
keys = list(prompts.keys())
if 1 <= st.session_state.step <= len(keys):
    current_key = keys[st.session_state.step - 1]
    current_prompt = prompts[current_key]
    response_key = f"response_{current_key}"

    if response_key not in st.session_state:
        st.session_state[response_key] = ""

    st.header(current_key)
    st.session_state[response_key] = st.text_input(
        label=current_prompt,
        value=st.session_state[response_key],
        key=response_key
    )

    if st.session_state[response_key].strip():
        if st.button("Next"):
            st.session_state.responses[current_key] = st.session_state[response_key]
            st.session_state.step += 1
    else:
        st.write("⏳ Please enter your response to continue.")

# Completion screen
if st.session_state.step > len(prompts):
    st.markdown("## You’ve Completed Your 8A Shift")
    st.success("You’ve aligned your energy. Let this new frequency guide your next steps.")

    st.markdown("### Your Reflections:")
    for key, value in st.session_state.responses.items():
        st.write(f"**{key}:** {value}")

    st.markdown("---")
    st.markdown("""
### 🌬️ Now breathe in... and breathe out...

Thank yourself for creating space to pause, connect with your body, calm down, and choose what’s best for you in this exact moment.

**You are a force and beyond amazing.  
You are just getting started.**  
Come back anytime.
    """)

    st.markdown("---")
    st.subheader("Would you like to support this experience?")
    st.write("This app is free and always will be. If it brought you peace, clarity, or alignment, you can support its evolution below.")
    st.markdown("[☕ Buy Me a Coffee](https://www.buymeacoffee.com/sheilamaebalaga)")
