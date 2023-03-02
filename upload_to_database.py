# for practicing database stuff

import streamlit_authenticator as stauth
import json
import streamlit as st
from google.oauth2 import service_account
from google.cloud import firestore

# names = ["Joshua Williams", "Noah Orta"]
# usernames = ["joshw", "norta"]
# passwords = ["abc123", "def456"]
# hash_passwords = stauth.Hasher(passwords).generate()

#secure database access
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="care-of-duty-analytics")

# for (name, username, hash_password) in zip(names, usernames, hash_passwords):
#     doc_ref = db.collection("users").document(username)
#     doc_ref.set({
#         "hash_password": hash_password,
#         "name": name
#     })

users_ref = db.collection("users")

# users_data = users_ref.get()

creds = {"usernames":{}}

usernames = [user.id for user in users_ref.stream()]
passwords = [user.to_dict()['hash_password'] for user in users_ref.stream()]
names = [user.to_dict()['name'] for user in users_ref.stream()]

for username, password, name in zip(usernames, passwords, names):
    user_dict = {"name":name,"password":password}
    creds["usernames"].update({username:user_dict})

creds['usernames'] = {key.lower(): value for key, value in creds['usernames'].items()}


print(creds)

# authenticator = stauth.Authenticate(creds, 
#                     "analytics_dashboard", "abcdef", cookie_expiry_days=0)


