import streamlit as st

st.set_page_config(page_title="Tap to Align", layout="centered")

# Define the 8A prompts
prompts = {
    "Awareness": "What are you feeling or noticing right now?",
    "Allowing": "Can you let that feeling exist without trying to fix it?",
    "Acknowledgement": "What truth or memory is behind this emotion?",
    "Acceptance": "Can you accept this part of your experience without resistance?",
    "Acting": "What aligned action (or stillness) feels true right now?",
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
    st.markdown("<h1 style='text-align: center;'>Tap to Align</h1>", unsafe_allow_html=True)

    st.write("**Tap to Align is a sacred space in your pocket—designed to gently guide you back to yourself.**")
    st.write("Through 8 intentional prompts, this app offers a moment of pause, presence, and personal power.")
    st.write("It’s not about fixing. It’s about remembering who you are.")
    st.markdown("*One tap at a time.*")

    st.markdown("---")
    st.subheader("The 8A Method")

st.write("""
The 8A Method is a moment-to-moment energetic shift.  
Whether you're navigating something heavy, uncertain, joyful, or overwhelming—this method helps you slow down, tune in, and realign.  
It’s not about fixing how you feel. It’s about being fully present with it, so something deeper can emerge.
""")

st.markdown("""
**The 8 Steps:**  
- **Awareness** – Recognize what situation or moment is stirring something inside you.  
- **Allowing** – Give yourself permission to feel it, without resistance or control.  
- **Acknowledgement** – Gently name the truth beneath the feeling—what it's really about.  
- **Acceptance** – Embrace this part of your experience without shame, shoulds, or stories.  
- **Acting** – Feel into whether any action (or non-action) naturally wants to arise.  
- **Activation** – Let the insight or shift become real within you, even if it's subtle.  
- **Alignment** – Integrate this shift—how do you want to carry yourself forward from here?  
- **Appreciation** – Close with gratitude—for your courage, your presence, and this inner moment.
""")

st.markdown("---")
if st.button("Begin My 8A Shift"):
    st.session_state.step = 1
st.stop()


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

    st.markdown("---")
    if st.button("Begin My 8A Shift"):
        st.session_state.step = 1
    st.stop()

# Show current step
keys = list(prompts.keys())
current_key = keys[st.session_state.step - 1]
current_prompt = prompts[current_key]

st.header(current_key)
response = st.text_input(current_prompt, key=current_key)

if st.button("Next"):
    if response:
        st.session_state.responses[current_key] = response
        st.session_state.step += 1

# Completion screen
if st.session_state.step > len(prompts):
    st.markdown("## You’ve Completed Your 8A Shift")
    st.success("You’ve aligned your energy. Let this new frequency guide your next steps.")
    st.markdown("### Your Responses:")
    for key, value in st.session_state.responses.items():
        st.write(f"**{key}:** {value}")

# Optional: About Section
with st.expander("✨ Why Tap to Align? (Mission + Benefits)"):
    st.markdown("**Tap to Align is a sacred space in your pocket—designed to gently guide you back to yourself.**")
    st.write("Through 8 intentional prompts, this app offers a moment of pause, presence, and personal power.")
    st.write("It’s not about fixing. It’s about remembering who you are.")
    st.markdown("*One tap at a time.*")

    st.markdown("---")
    st.subheader("The 8A Method")

    for key, value in prompts.items():
        st.markdown(f"**{key}** — {value}")

    st.markdown("---")
    st.subheader("Benefits of Tap to Align")

    st.markdown("**1. Reset Your Energy in Minutes**  \nFeel off? Overwhelmed? Disconnected? Tap through 8 steps to realign with your truth.")
    st.markdown("**2. Anchor Into Presence**  \nEach prompt invites you into the now—calm, conscious, and grounded.")
    st.markdown("**3. Hold Space for Your Emotions**  \nInstead of escaping what you feel, this app teaches you how to witness it without judgment.")
    st.markdown("**4. Activate Your Inner Wisdom**  \nThe journey ends in clarity, not confusion. These prompts help awaken insights already inside you.")
    st.markdown("**5. Create a Ritual of Return**  \nMake this your daily check-in. A tap becomes your sacred pause—morning, mid-storm, or just before sleep.")
    st.markdown("**6. Accessible. Private. Deeply Yours.**  \nNo advice. No noise. No distractions. Just you, your truth, and a quiet return to alignment.")

    st.markdown("---")
    st.markdown("> *The shift you’ve been seeking isn’t outside you. It’s within.*  \n**Tap in. Align. Begin again.**")
