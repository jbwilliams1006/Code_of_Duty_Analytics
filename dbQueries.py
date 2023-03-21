import json
from google.oauth2 import service_account
import streamlit as st
from google.cloud import firestore

########################### GET ACCESS TO THE DATA BASE ###############################
@st.cache_resource
def access_db():
    #secure database access
    key_dict = json.loads(st.secrets["textkey"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds, project="care-of-duty-analytics")
    return db



#   Description:
#       Get's a dictionary count of the different 'choices' for the different occasional
#       things inside the database
#   Params:
#       type - str : the type of 'occasional query' 
#                    ex (stress,grief,anxiety,ptsd,depression,alcohol_substance_use)
@st.cache_resource
def occasional_query_count(type):

    # make sure the string is lowercase
    type = type.lower()

    # get access to database
    db = access_db()
    choices = ['Daily', 'Weekly', 'Monthly', 'Seldom', 'Often', 'Never', 'Yearly', 'Once']

    counts = {}

    # counts up all the occurances in the database for each choice
    for choice in choices:
        anxiety_ref = db.collection('data').where(type, '==', choice).stream()
        count = 0
        for _ in anxiety_ref:
            count += 1
        counts[choice] = count

    # returns the counts of the difference an
    return counts



