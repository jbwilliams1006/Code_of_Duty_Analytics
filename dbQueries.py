import json
from google.oauth2 import service_account
import streamlit as st
from google.cloud import firestore
from pprint import pprint

########################### GET ACCESS TO THE DATA BASE ###############################
@st.cache_resource
def access_db():
    #secure database access
    key_dict = json.loads(st.secrets["textkey"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds, project="care-of-duty-analytics")
    return db


#------------------------------------------------------------------------------
#
#   Description:
#       Get's a dictionary count of the different 'choices' for the different occasional
#       things inside the database
#
#   Params:
#       type - str : the type of 'occasional query' 
#                    example: (stress,grief,anxiety,ptsd,depression,alcohol_substance_use)
#
#   Returns: 
#       dictionary - dictionary containting the counts for the different occasions
#
#   Example of call:
#       counts = occasional_query_count('stress')
#       
#      < output > counts['daily'] -> 115
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


#------------------------------------------------------------------------------
#
#   Decription: 
#       Return's a list of of the patients seen, on a certain date, in a dictionary.
#
#   Params:
#       date - str : needs to be in the format (YYYY-MM-DD)
#
#   Returns:
#       data_list - list(dic) : all the people with data on that day
def get_date_query(date):

    db = access_db()

    data_ref = db.collection('data').where('date', '==', date).stream()

    data_list = []

    for data in data_ref:
        data_list.append(data.to_dict())

    return data_list



#------------------------------------------------------------------------------
#
#   Decription: 
#       Return's a list of of the patients seen in a certain date range
#       in a dictionary.
#
#   Params:
#       start - str : needs to be in the format (YYYY-MM-DD)
#       end   - str : needs to be in the format (YYYY-MM-DD)
#
#   Returns:
#       data_list - list(dic) : all the people with data in that date range
def date_range_query(start, end):
    
    db = access_db()

    data_ref = db.collection('data').where('date', '>=', start).where('date', '<=', end).stream()

    data_list = []

    for data in data_ref:
        data_list.append(data.to_dict())
    
    return data_list
