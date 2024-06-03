import streamlit as st
from menu import menu_with_redirect


menu_with_redirect()

st.header("mir damage survey service")
st.write("----------")

st.write(f"Successfully created vessel")
next = st.button("Create damage survey")

if next:
    st.switch_page("pages/damage_survey_form_view.py")