import streamlit as st
from menu import menu_with_redirect

menu_with_redirect()

st.header("mir damage survey service")
st.write("----------")

email: str = "some email"
st.subheader(f'Successfully found owner with email: {email}')

clicked = st.button('Register vessel')

if clicked:
    st.switch_page("pages/query_vessel_exists_view.py")