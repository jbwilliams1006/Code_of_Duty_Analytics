import json
import streamlit as st
import streamlit_authenticator as stauth
from google.oauth2 import service_account
from google.cloud import firestore
from page_navigation import nav_page


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

st.title("Sign Up")

########################### GET ACCESS TO THE DATA BASE ###############################

#secure database access
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="care-of-duty-analytics")

## reference to the users collection ID
users_ref = db.collection("users")
preauth_users_ref = db.collection("preauthorized").document("emails")
preauth_users = preauth_users_ref.get()

preauth_user_emails = preauth_users.to_dict()["email"]



# #Creation of credentials dictionary
creds = {"usernames":{}}


# get data from database into lists
usernames = [user.id for user in users_ref.stream()]
passwords = [user.to_dict()['hash_password'] for user in users_ref.stream()]
names = [user.to_dict()['name'] for user in users_ref.stream()]

# turn lists into database
for username, password, name in zip(usernames, passwords, names):
    user_dict = {"name":name,"password":password}
    creds["usernames"].update({username:user_dict})


#Creation of authentication object
authenticator = stauth.Authenticate(creds,
       "analytics_dashboard", "abcdef", cookie_expiry_days = 1, preauthorized=preauth_user_emails)

#######################################################################################

try:
    if authenticator.register_user('Register user', preauthorization=False):
        st.success('User registered successfully')
        db.collection("credentials").document("usernames").set(
            creds['usernames']
        )
except Exception as e:
    st.error(e)

if st.button("Back"):
    nav_page("") 