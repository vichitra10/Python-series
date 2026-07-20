## Basic Streamlit App ()
import streamlit as st
st.title('Welcome to Streamlit')
userinput = st.text_input('Enter Your Name')
if st.button('Greet Me'):
    st.write(f"Hello, {userinput}")