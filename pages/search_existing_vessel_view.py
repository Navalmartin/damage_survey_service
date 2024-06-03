import streamlit as st
from menu import menu_with_redirect

menu_with_redirect()

st.header("mir damage survey service")
st.write("----------")

st.write("Search for the vessel. Please provide either the vessel mmsi or vessel HIN as used within mir." 
         " If you don't know this check the checkbox 'Use owner id in search' .")

with st.form("search_vessel_form"):
        vessel_name: str = st.text_input(label="Vessel name (required)")
        vessel_mmsi: str = st.text_input(label="Vessel mmsi (optional)")
        vessel_hin: str = st.text_input(label="Vessel hin (optional)")
        user_owner_in_search: bool = st.checkbox(label="Use owner id in search",
                                                 value=False)

        search_button = st.form_submit_button("Search")

if search_button:
    # validate the search form

    # query the REST API

    # if response is ok redirect to
    # create survey
    st.switch_page("pages/damage_survey_form_view.py")