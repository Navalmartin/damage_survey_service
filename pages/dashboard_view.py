import streamlit as st
from menu import menu_with_redirect


def dashboard_view():
    
    username = "Alex" #st.session_state['username']

    st.subheader(f"Hello {username}")
    st.write("---------------------")


    clicked = st.button("Create New Damage Survey")

    if clicked:
        st.switch_page("pages/damage_survey_form_view.py")


menu_with_redirect()
dashboard_view()