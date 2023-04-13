import json
import streamlit as st
# import streamlit_authenticator as stauth
from google.oauth2 import service_account
from google.cloud import firestore
from page_navigation import nav_page
from register_user import *

import logo

## to hide the sidebar
st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

 # logo above sidebar menu options
logo.add_logo("Icons/fullName_logo.png")
