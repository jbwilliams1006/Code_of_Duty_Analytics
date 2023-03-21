import jwt
import bcrypt
import streamlit as st
from datetime import datetime, timedelta
import extra_streamlit_components as stx

from hasher import Hasher

def register_credentials(username: str, name: str, fname: str, lname: str, password: str, email: str, militaryID: str, 
                            preauthorization: bool, credentials: dict, preauthorized: list):
        """
        Adds to credentials dictionary the new user's information.
        Parameters
        ----------
        username: str
            The username of the new user.
        name: str
            The name of the new user.
        password: str
            The password of the new user.
        email: str
            The email of the new user.
        preauthorization: bool
            The preauthorization requirement, True: user must be preauthorized to register, 
            False: any user can register.
        """
        credentials['usernames'][username] = {'name': name, 'fname': fname, 'lname': lname, 'militaryid': militaryID,
            'password': Hasher([password]).generate()[0], 'email': email}
        if preauthorization:
            preauthorized['emails']['email'].remove(email)

        return credentials, preauthorized


class RegisterError(Exception):
    """
    Exceptions raised for the register user widget.
    Attributes
    ----------
    message: str
        The custom error message to display.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


def register_user(form_name: str, location: str='main', preauthorization=True, credentials: list=[], preauthorized: list=[]) -> bool:
        """
        Creates a sign-up widget.
        Parameters
        ----------
        form_name: str
            The rendered name of the password reset form.
        location: str
            The location of the sign-up form i.e. main or sidebar.
        preauthorization: bool
            The preauthorization requirement, True: user must be preauthorized to register, 
            False: any user can register.
        Returns
        -------
        bool
            The status of registering the new user, True: user registered successfully.
        """
        if preauthorization:
            if not preauthorized:
                raise ValueError("preauthorization argument must not be None")
        if location not in ['main', 'sidebar']:
            raise ValueError("Location must be one of 'main' or 'sidebar'")
        if location == 'main':
            register_user_form = st.form('Register user')
        elif location == 'sidebar':
            register_user_form = st.sidebar.form('Register user')

        register_user_form.subheader(form_name)
        new_email = register_user_form.text_input('Email')
        new_username = register_user_form.text_input('Username').lower()
        new_fname = register_user_form.text_input('First Name')
        new_lname = register_user_form.text_input('Last Name')
        new_militaryID = register_user_form.text_input('Military ID')
        new_password = register_user_form.text_input('Password', type='password')
        new_password_repeat = register_user_form.text_input('Repeat password', type='password')
        new_name = new_fname + " " + new_lname
        

        if register_user_form.form_submit_button('Register'):
            if len(new_email) and len(new_username) and len(new_fname) and len(new_lname) and len(new_militaryID) and len(new_password) > 0:
                if new_username not in credentials['usernames']:
                    if new_password == new_password_repeat:
                        if preauthorization:
                            if new_email in preauthorized['emails']['email']:
                                credentials, preauthorized = register_credentials(new_username, new_name, new_fname, new_lname, new_password, 
                                                                                  new_email, new_militaryID, preauthorization, credentials, preauthorized)
                                return True
                            else:
                                raise RegisterError('User not preauthorized to register')
                        else:
                            credentials, preauthorized = register_credentials(new_username, new_name, new_fname, new_lname, new_password, 
                                                                                  new_email, new_militaryID, preauthorization, credentials, preauthorized)
                            return True
                    else:
                        raise RegisterError('Passwords do not match')
                else:
                    raise RegisterError('Username already taken')
            else:
                raise RegisterError('Please enter an email, username, first name, last name, military ID and password')

