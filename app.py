import streamlit as st

st.title("LIFE-OS-AI 🚀")
st.subheader("Your Personal AI Assistant")

name = st.text_input("Enter your name")
task = st.text_input("What is your goal today?")

if st.button("Create My Plan"):
    if name and task:
        st.success(f"Welcome, {name}!")
        st.write("Your goal:", task)
    else:
        st.warning("Please enter your name and goal.")
