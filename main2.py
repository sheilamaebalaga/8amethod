def a7_method():
    st.title("🌀 7A Method: Your Inner Shift")

    st.markdown("Welcome to your energetic reset. Take a breath and move through each step at your own pace.")

    awareness = st.text_input("1. **Awareness** — What are you feeling or noticing right now?")
    allowing = st.text_input("2. **Allowing** — Can you let that feeling exist without trying to fix it?")
    acknowledgement = st.text_input("3. **Acknowledgement** — What is the truth or root behind this feeling?")
    acceptance = st.text_input("4. **Acceptance** — Can you accept this part of your experience without judgment?")
    acting = st.text_input("5. **Acting** — What aligned action (or inaction) feels right to take?")
    activation = st.text_input("6. **Activation** — What truth or insight is waking up within you now?")
    alignment = st.text_input("7. **Alignment** — How do you want to carry this forward from this space?")

    if st.button("✨ Complete My 7A Shift"):
        st.markdown("## 🔓 You’ve Completed the 7A Method")
        st.success("You just created a shift in your field. Let this new alignment carry you forward. 🌿")

        st.markdown("### 🌀 Your Responses:")
        st.write("**Awareness:**", awareness)
        st.write("**Allowing:**", allowing)
        st.write("**Acknowledgement:**", acknowledgement)
        st.write("**Acceptance:**", acceptance)
        st.write("**Acting:**", acting)
        st.write("**Activation:**", activation)
        st.write("**Alignment:**", alignment)

a7_method()
