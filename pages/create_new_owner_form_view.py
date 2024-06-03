import streamlit as st
import requests
import json
from loguru import logger
from menu import menu_with_redirect

menu_with_redirect()

st.header("mir damage survey service")
st.write("----------")

st.subheader("Register a new owner with mir")
st.write("Use the form below to register a new vessel owner")

with st.form("create_new_owner_form"):
        owner_name: str = st.text_input(label="Owner name (required)")
        owner_surname: str = st.text_input(label="Owner surname (required)")
        owner_email: str = st.text_input(label="Owner email (required)")
        create_button = st.form_submit_button("Register")

if create_button:
    # validate the search form

    # query the REST API

    # if response is ok redirect to
    # register vessel form as the vessel should not
    # be in mir
    st.switch_page("pages/success_create_owner_view.py")