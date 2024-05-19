from typing import Any, List
import streamlit as st
import requests
import json
from loguru import logger
from result import Err, Ok, Result

from menu import menu_with_redirect
from config import (SI_ITEMS, 
                    MIR_API_URL, 
                    MIR_API_VERSION)

@st.cache_resource
def init_mongo_db_connection():
    pass


menu_with_redirect()

survey_items = {}

for item in SI_ITEMS:
        si_data = SI_ITEMS[item]

        si_type = item
        si_description = si_data[0]
        si_checkpoints = si_data[1]

        checkpoints = []

        for chp in si_checkpoints:
            checkpoints.append([chp['chpt_id'], chp['checkpoint_type'], chp['description']])

        survey_items[(si_description, si_type)] = checkpoints


def _check_form_validity(*, owner_name:str, owner_surname: str, owner_email: str,
                         vessel_type: str, vessel_hull_material_type: str,
                         propulsion_type: str, vessel_mmsi: str,
                         survey_items_submitted: dict[str, List]) -> Result[str, str]:
    
    # import pdb
    # pdb.set_trace()

    if owner_name is None or owner_name == "":
        return Err("Owner name is missing")
    
    if owner_surname is None or owner_surname == "":
        return Err("Owner owner_surname is missing")

    if owner_email is None or owner_email == "":
        return Err("Owner owner_email is missing") 
    
    checkpoints = []
    for item in survey_items_submitted:
        checkpoints.extend(survey_items_submitted[item])
    
    if len(checkpoints) == 0:
        return Err("Cannot create a damage survey with empty checkpoints")

    return Ok({"owner_surname": owner_surname, 
               "owner_name": owner_name, 
               "owner_email": owner_email, 
               "vessel_type": vessel_type,
               "vessel_hull_material_type": vessel_hull_material_type, 
               "vessel_propulsion_type": propulsion_type, "vessel_mmsi": vessel_mmsi,
               "survey_items": survey_items_submitted}) 


survey_items_submitted = {}
checkpoint_description_to_type_map = {}
with st.form("create_damage_survey_form"):
    st.header("Create new damage survey")
    st.write("----------")
    owner_name:str = st.text_input(label="Owner name (required)")
    owner_surname: str = st.text_input(label="Owner surname (required)")
    owner_email: str = st.text_input(label="Owner email (required)")
    vessel_type: str = st.selectbox("Vessel type", ["Select", "Monohull", "RIB", "Trimaran", "Catamaran"])
    vessel_hull_material_type: str = st.selectbox("Vessel hull material type", ["Select", "Monohull", "RIB", "Trimaran", "Catamaran"])
    propulsion_type: str = st.selectbox("Propulsion type", ["Select", "Monohull", "RIB", "Trimaran", "Catamaran"])
    vessel_mmsi: str = st.text_input(label="Vessel mmsi (required)")

    st.write("Select checkpoints to be included in the survey")
    for si in survey_items:
        st.subheader(f"{si[0]} | Checkpoints")
        survey_items_submitted[si[1]] = []
        

        checkpoints = survey_items[si]
        items = []
        for chpt in checkpoints:
            description = f"{chpt[0]} | {chpt[2]}"
            items.append(description)
            checkpoint_description_to_type_map[description] = chpt[1]
           

        si_checkpoints_selected = st.multiselect(label=si[1], options=items, label_visibility='hidden')
        survey_items_submitted[si[1]] = si_checkpoints_selected
        st.write("----------")

    st.subheader("Instructions")
    st.text_area(label="Instructions", label_visibility="hidden",
                 placeholder="Instructions you may want to pass over the vessel owner")

    submitted = st.form_submit_button("Create")


if submitted:

    owner_email="a.giavaras@gmail.com"
    owner_name="Alex"
    owner_surname="Giavaras"
    result = _check_form_validity(owner_surname=owner_surname,
                                  owner_email=owner_email, 
                                  owner_name=owner_name,
                                  vessel_type=vessel_type,
                                  vessel_hull_material_type=vessel_hull_material_type,
                                  propulsion_type=propulsion_type,
                                  vessel_mmsi=vessel_mmsi,
                                  survey_items_submitted=survey_items_submitted)

    if isinstance(result, Ok):


        si_items = result.ok_value['survey_items']

        si_to_post = {}
        for si in si_items:
            checkpoints = si_items[si]

            checkpoints_to_post = []

            for chpt in checkpoints:
                checkpoints_to_post.append(checkpoint_description_to_type_map[chpt])

            if len(checkpoints_to_post) != 0:
                si_to_post[si] =  checkpoints_to_post
            

        URL = MIR_API_URL + "/" + MIR_API_VERSION + "/" + "surveys/damage-survey/new"

        form_data = result.ok_value
        form_data['survey_items'] = si_to_post

        access_token: str = st.session_state['user_data_session']['access_token']
        header_data = {'Authorization': f'Bearer {access_token}',
                       'is-user': 'surveyor',
                       'Content-Type': 'application/json'}
        

        print(form_data)

        response = requests.post(url=URL, 
                                 headers=header_data,
                                 data=json.dumps(form_data))
        
        if response.status_code == 201:
            st.switch_page("pages/success_view.py")
        else:
            logger.error("Could not create damage survey")
    else:
        logger.error(f"Error occurred {result.err_value}")




