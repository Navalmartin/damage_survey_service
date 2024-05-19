"""Hnadles the various options for the menu
"""
import streamlit as st


def authenticated_menu():
    #st.sidebar.page_link("pages/dashboard_view.py", label="Me")
    st.sidebar.page_link("pages/logout_view.py", label="Logout")
    

def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("damage_survey_app.py", label="Log in")


def menu():
    if "user_data_session" not in st.session_state or st.session_state.user_data_session is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "user_data_session" not in st.session_state or st.session_state.user_data_session is None:
        st.switch_page("damage_survey_app.py")
    menu()