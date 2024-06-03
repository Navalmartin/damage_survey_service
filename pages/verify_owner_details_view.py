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
st.subheader("Verify the following owner details")


    
# get the current owner data from session
owner_data = st.session_state['user_data_session']['owner_data']
owner_name = owner_data['owner_name']
owner_surname = owner_data['owner_surname']
owner_email = owner_data['owner_email']


st.write(f'Owner email (required): {owner_email}')
st.write(f'Owner surname (required): {owner_surname}')
st.write(f'Owner name (required): {owner_name}')
        
yes_owner_verify = st.button(label='Verify')
print(f'yes_owner_verify {yes_owner_verify}')
if yes_owner_verify:
    st.switch_page("pages/owner_exists_success_view.py")
# else:
#     st.write(f'Owner with email {owner_email} was not found.')