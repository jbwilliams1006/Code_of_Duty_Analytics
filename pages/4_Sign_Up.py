import json
import streamlit as st
# import streamlit_authenticator as stauth
from google.oauth2 import service_account
from google.cloud import firestore
from page_navigation import nav_page
from register_user import *
import base64

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
@st.cache_data()
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
def build_markup_for_logo(
    png_file,
    background_position="50% 10%",
    margin_top="0%",
    image_width="60%",
    image_height="",
):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (
        binary_string,
        background_position,
        margin_top,
        image_width,
        image_height,
    )

def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )

add_logo("Icons/fullName_logo.png")
########################### GET ACCESS TO THE DATA BASE ###############################

#secure database access
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="care-of-duty-analytics")

## reference to the users collection ID
users_ref = db.collection("credentials").document("usernames")
users = users_ref.get()

# #Creation of credentials dictionary
creds = {"usernames": users.to_dict()}

# reference to preauthorized emails 
pre_auth_ref = db.collection("preauthorized").document("emails")
pre_auth = pre_auth_ref.get()

# Creation of preauthorized emails
auth_emails = {"emails": pre_auth.to_dict()}
print(auth_emails)

# ## reference to the users collection ID
# users_ref = db.collection("users")
# preauth_users_ref = db.collection("preauthorized").document("emails")
# preauth_users = preauth_users_ref.get()
# preauth_user_emails = preauth_users.to_dict()["email"]

# # #Creation of credentials dictionary
# creds = {"usernames":{}}

# # get data from database into lists
# usernames = [user.id for user in users_ref.stream()]
# passwords = [user.to_dict()['hash_password'] for user in users_ref.stream()]
# names = [user.to_dict()['name'] for user in users_ref.stream()]

# # turn lists into database
# for username, password, name in zip(usernames, passwords, names):
#     user_dict = {"name":name,"password":password}
#     creds["usernames"].update({username:user_dict})

# #Creation of authentication object
# authenticator = stauth.Authenticate(creds,
#        "analytics_dashboard", "abcdef", cookie_expiry_days = 1, preauthorized=auth_emails)

#######################################################################################

try:
    if register_user('Register user', preauthorization=True, credentials=creds, preauthorized=auth_emails):
        st.success('User registered successfully')
        db.collection("credentials").document("usernames").set(
            creds['usernames'], merge = True
        )
        db.collection("preauthorized").document("emails").set(
            auth_emails['emails']
        )
except Exception as e:
    st.error(e)

if st.button("Back"):
    nav_page("") 
    
