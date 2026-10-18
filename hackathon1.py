import streamlit as st

st.set_page_config(
    page_title="LIFE-OS-AI",
    page_icon="🚀"
)

st.title("🚀 LIFE-OS-AI")
st.subheader("Your Personal AI Life Assistant")

st.write(
    "Plan your day, manage tasks and improve productivity."
)

name = st.text_input("Enter your name")

task = st.text_input("What do you want to accomplish today?")

if st.button("Create My Plan"):
    if name and task:
        st.success(f"Welcome, {name}!")
        st.write("Your goal for today:")
        st.info(task)
    else:
        st.warning("Please enter your name and goal.")
