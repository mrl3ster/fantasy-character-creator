import streamlit as st

st.set_page_config(page_title="Streamlit Test", page_icon="✨")

st.title("✨ Streamlit Is Working!")

st.write("If you can see this page, your Streamlit app is set up correctly.")

name = st.text_input("What is your name?")

if name:
    st.success(f"Hello, {name}! 🎉")
