import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Joshua Williams", "Noah Orta"]
usernames = ["joshw", "norta"]
passwords = ["abc123", "123abc"]

#Hashes using bcrypt which is considered a very secure hashing algorithm
hashed_passwords = stauth.Hasher(passwords).generate()

#dumps passwords into file
file_path = Path(__file__).parent/ "hashed_pw.pk1"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
