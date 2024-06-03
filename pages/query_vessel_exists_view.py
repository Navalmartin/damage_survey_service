import streamlit as st
from menu import menu_with_redirect

st.header("mir damage survey service")
st.write("----------")
st.subheader("Vessel details")


st.write("The vessel you want to survey is it registered with  mir?")
st.write("----------")
st.write("If yes you will need to supply at least the vessel name as it is registered with mir")
yes_button = st.button(label="Yes")
st.write("----------")
no_button = st.button(label="No")


if no_button:
   st.switch_page("pages/create_new_vessel_form_view.py")

if yes_button:

    # the vessel exists we should verify the data
    st.switch_page("pages/search_existing_vessel_view.py")


    # with st.form("get_vessel_details_form"):
    #     vessel_name: str = st.text_input(label="Vessel name (required)")
    #     yes_owner_submitted = st.form_submit_button("Create")


    # if yes_owner_submitted:
    #     # we need to make sure that the email
    #     # exists
    #     URL = MIR_API_URL + "/" + MIR_API_VERSION + "/admin/search-for-owner"

    #     owner_query_form = {"email": owner_email, "collections": ["owners"]}
    #     access_token: str = st.session_state['user_data_session']['access_token']
    #     header_data = {'Authorization': f'Bearer {access_token}',
    #                    'is-user': 'surveyor',
    #                    'Content-Type': 'application/json'}
    #     query_response = requests.post(url=URL, 
    #                                    headers=header_data,
    #                                    data=json.dumps(owner_query_form))
        
    #     if query_response.status_code == 200:
    #         # the owner exists let's register a vessel
    #         st.switch_page("pages/owner_exists_success_view.py")

