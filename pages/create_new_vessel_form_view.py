import streamlit as st
from menu import menu_with_redirect


menu_with_redirect()

st.header("mir damage survey service")
st.write("----------")
st.subheader("Create a new vessel")
st.write("Use the form below to register a new vessel with mir")

with st.form("create_new_vessel_form"):
        vessel_name: str = st.text_input(label="Vessel name (required)")
        vessel_mmsi: str = st.text_input(label="Vessel mmsi (optional)")
        vessel_hin: str = st.text_input(label="Vessel hin (optional)")
        create_button = st.form_submit_button("Create")

if create_button:
        
         st.switch_page("pages/success_create_vessel_view.py")
