import streamlit as st
import requests
import json
from loguru import logger
from menu import menu_with_redirect
from config import (MIR_API_URL, 
                    MIR_API_VERSION)

menu_with_redirect()


st.header("mir damage survey service")
st.write("----------")
st.subheader("Owner details")
st.write("Does the vessel owner have an account with  mir?")
st.write("----------")
yes_button = st.button(label="Yes")

st.write("----------")
no_button = st.button(label="No")

if no_button:
    st.switch_page("pages/create_new_owner_form_view.py")

if yes_button:
    st.switch_page("pages/search_existing_owner_view.py")
    
    