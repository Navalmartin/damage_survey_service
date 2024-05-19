"""Entry point for the mir damage surevy app
"""
import requests
import streamlit as st
import json
from loguru import logger
from menu import menu
from config import (MIR_API_URL, 
                    MIR_API_VERSION)



def _handle_login_credentials(email: str, password: str) -> bool:
    print(f"email {email}")
    print(f"password {password}")
    return True
    # if email == "alex@naval.com":
    #     return True
    # return False
    


def login_view():
    with st.form("damage_survey_login_form"):
        st.header("Welcom to mir damage survey service")
        st.write("Use your credentials to login and use the service")
        st.write("----------")
        email = st.text_input(label="email (required)")
        password = st.text_input(label="password (required)", type="password")

        

        # _handle_login_credentials(email=email, password=password)

        # try to login the user
        submitted = st.form_submit_button("Login", 
                                          on_click=_handle_login_credentials,
                                          kwargs={'email': email, 'password': password })
        
    if submitted:
        valid_credentials = _handle_login_credentials(email=email, password=password)

        # login with mir 
        if valid_credentials:

            URL = MIR_API_URL + "/" + MIR_API_VERSION + "/surveyors/login"
            data={'username': email, 'password': password}

            # login_response = requests.post(url=URL, 
            #                                data=data)

            #login_response = login_response.json()

            login_response = {}
            login_response['access_token'] = '123'
            login_response['refresh_token'] = '123'
            login_response['token_type'] = 'Bearer'
            
            #if login_response.status_code == 200:

            

            user_data_session = {
                    'email': email,
                    'access_token': login_response['access_token'],
                    'refresh_token': login_response['refresh_token'],
                    'token_type': login_response['token_type']
            }

            print(login_response)
            st.session_state['user_data_session'] = user_data_session
            st.switch_page("pages/damage_survey_form_view.py")
            #else:
                #logger.error(f"Error occured whilst trying to log user with email {email}")
        else:
            logger.error(f"Error occured whilst trying to log user with email {email}")
            st.rerun()

    menu()
       
 

login_view()
