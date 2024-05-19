import streamlit as st

st.session_state.pop("user_data_session")
st.switch_page("damage_survey_app.py")