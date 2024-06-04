import streamlit as st
import requests
import json
#import bson
from loguru import logger
from menu import menu_with_redirect
from config import (MIR_API_URL, 
                    MIR_API_VERSION)

menu_with_redirect()

with st.form("get_owner_email_form"):
        owner_email: str = st.text_input(label="Owner email (required)")
        yes_owner_submitted = st.form_submit_button("Search")

        print(f'yes_owner_submitted {yes_owner_submitted}')

if yes_owner_submitted:
    print(f'yes_owner_submitted {yes_owner_submitted}')
            # we need to make sure that the email
            # exists
    URL = MIR_API_URL + "/" + MIR_API_VERSION + "/admin/search-for-owner"

    owner_query_form = {"email": owner_email, "collections": ["owners"]}
    access_token: str = st.session_state['user_data_session']['access_token']
    header_data = {'Authorization': f'Bearer {access_token}',
                        'is-user': 'surveyor',
                        'Content-Type': 'application/json'}
            
            # query_response = requests.post(url=URL, 
            #                                headers=header_data,
            #                                data=json.dumps(owner_query_form))

    from collections import namedtuple
    QueryResponse = namedtuple(typename='QueryResponse', field_names=['status_code'])
    query_response = QueryResponse(status_code=200)

    print(query_response)
            
    if query_response.status_code == 200:

        # query_response = query_response.json()
        # owner_email = query_response['owner_email']
        # owner_name = query_response['owner_name']
        # owner_surname = query_response['owner_surname']

        owner_name = 'some_name'
        owner_surname = 'some_surname'
        owner_email = 'some_email'
        st.session_state['user_data_session']['owner_data'] = {'owner_email': owner_email,
                                                               'owner_name': owner_name,
                                                               'owner_surname': owner_surname,
                                                               'owner_idx': '123456'}
        st.switch_page("pages/verify_owner_details_view.py")

        # owner_name = 'some_name'
        # owner_surname = 'some_surname'
        # owner_email = 'some_email'

        # st.write(f'The owner with email {owner_email} was found in the database')
        # st.write(f'Verify the following')

        # st.write(f'Owner email (required): {owner_email}')
        # st.write(f'Owner surname (required): {owner_surname}')
        # st.write(f'Owner name (required): {owner_name}')
        
        # yes_owner_verify = st.button(label='Verify')
        # print(f'yes_owner_verify {yes_owner_verify}')
        # if yes_owner_verify:
        #     st.switch_page("pages/owner_exists_success_view.py")
    else:
        st.write(f'Owner with email {owner_email} was not found.')