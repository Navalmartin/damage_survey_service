import streamlit as st
from menu import menu_with_redirect


menu_with_redirect()

st.header("mir damage survey service")
st.write("----------")

st.write(f"Survey successfully created")
clicked = st.button("Close service")

if clicked:
    st.switch_page("pages/logout_view.py")