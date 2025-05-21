import streamlit as st

st.set_page_config(page_title="Tap to Align", layout="centered")

# Welcome screen
if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.markdown("<h1 style='text-align: center;'>Tap to Align</h1>", unsafe_allow_html=True)
    
    st.write("**Tap to Align is a sacred space in your pocket—designed to gently guide you back to yourself.**")
    st.write("Through 8 intentional prompts, this app offers a moment of pause, presence, and personal power.")
    st.write("It’s not about fixing. It’s about remembering who you are.")
    st.markdown("*One tap at a time.*")

    st.markdown("---")
    if st.button("Begin My 8A Shift"):
        st.session_state.started = True
    st.stop()

# 8A Prompt Method
st.title("Your 8A Shift")

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

for key, prompt in prompts.items():
    if st.button(key):
        st.markdown(f"### {prompt}")
        st.stop()

st.markdown("---")
st.write("You’ve reached the end of your alignment cycle. Breathe in. You’re home.")

# Optional: Mission + Benefits Button
if st.button("Why Tap to Align?"):
    st.subheader("🌿 Mission")
    st.write("Tap to Align is a sacred space in your pocket—designed to gently guide you back to yourself.")
    st.write("Through 8 intentional prompts, this app offers a moment of pause, presence, and personal power.")
    st.write("It’s not about fixing. It’s about remembering who you are.")
    st.markdown("*One tap at a time.*")

    st.markdown("---")
    st.subheader("✨ Benefits of Tap to Align")

    st.markdown("**1. Reset Your Energy in Minutes**  \nFeel off? Overwhelmed? Disconnected? Tap through 8 steps to realign with your truth.")
    st.markdown("**2. Anchor Into Presence**  \nEach prompt invites you into the now—calm, conscious, and grounded.")
    st.markdown("**3. Hold Space for Your Emotions**  \nInstead of escaping what you feel, this app teaches you how to witness it without judgment.")
    st.markdown("**4. Activate Your Inner Wisdom**  \nThe journey ends in clarity, not confusion. These prompts help awaken insights already inside you.")
    st.markdown("**5. Create a Ritual of Return**  \nMake this your daily check-in. A tap becomes your sacred pause—morning, mid-storm, or just before sleep.")
    st.markdown("**6. Accessible. Private. Deeply Yours.**  \nNo advice. No noise. No distractions. Just you, your truth, and a quiet return to alignment.")

    st.markdown("---")
    st.markdown("> *The shift you’ve been seeking isn’t outside you. It’s within.*  \n**Tap in. Align. Begin again.**")
