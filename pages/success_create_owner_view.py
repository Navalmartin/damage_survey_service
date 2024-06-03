import streamlit as st
from menu import menu_with_redirect


menu_with_redirect()

st.header("mir damage survey service")
st.write("----------")

st.write(f"Successfully created new owner and send email")
next = st.button("Register vessel")

if next:
    st.switch_page("pages/create_new_vessel_form_view.py")