#For authentication
import pickle
from pathlib import Path
import altair as alt

import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import numpy as np
import plost
from PIL import Image
from google.cloud import firestore
# import firebase_admin
from firebase_admin import credentials
import json
from google.oauth2 import service_account
from page_navigation import nav_page
from VisualsPTSD import VisualsPTSD
from VisualsAlc import VisualsAlc
from VisualsDep import VisualsDep
from VisualsStress import VisualsStress


#secure database access
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="care-of-duty-analytics")

## reference to the users collection ID
users_ref = db.collection("credentials").document("usernames")
users = users_ref.get()


# """

#              _______                                     _     _    _                   
#     _  _    |_   __ \                                   / |_  / |_ (_)                  
#   _| || |_    | |__) |,--.   .--./) .---.   .--.  .---.`| |-'`| |-'__   _ .--.   .--./) 
#  |_| || |_|   |  ___/`'_\ : / /'`\;/ /__\\ ( (`\]/ /__\\| |   | | [  | [ `.-. | / /'`\; 
#  |_| || |_|  _| |_   // | |,\ \._//| \__.,  `'.'.| \__.,| |,  | |, | |  | | | | \ \._// 
#    |_||_|   |_____|  \'-;__/.',__`  '.__.' [\__) )'.__.'\__/  \__/[___][___||__].',__`  
#                            ( ( __))                                            ( ( __)) 

# """
st.set_page_config(initial_sidebar_state="collapsed",layout="wide")



# """
 
#   _____  _____                           _               _   __                      _    _                 _    _                   
#  |_   _||_   _|                         / \             / |_[  |                    / |_ (_)               / |_ (_)                  
#    | |    | | .--.  .---.  _ .--.      / _ \    __   _ `| |-'| |--.  .---.  _ .--. `| |-'__   .---.  ,--. `| |-'__   .--.   _ .--.   
#    | '    ' |( (`\]/ /__\\[ `/'`\]    / ___ \  [  | | | | |  | .-. |/ /__\\[ `.-. | | | [  | / /'`\]`'_\ : | | [  |/ .'`\ \[ `.-. |  
#     \ \__/ /  `'.'.| \__., | |      _/ /   \ \_ | \_/ |,| |, | | | || \__., | | | | | |, | | | \__. // | |,| |, | || \__. | | | | |  
#      `.__.'  [\__) )'.__.'[___]    |____| |____|'.__.'_/\__/[___]|__]'.__.'[___||__]\__/[___]'.___.'\'-;__/\__/[___]'.__.' [___||__] 
                                                                                                                                     
 
# """

# DATA BASE CREDS

# Creation of credentials dictionary from database
creds = {"usernames":users.to_dict()}


# creds = {"usernames":{}}

# # get data from database into lists
# usernames = [user.id for user in users_ref.stream()]
# passwords = [user.to_dict()['hash_password'] for user in users_ref.stream()]
# names = [user.to_dict()['name'] for user in users_ref.stream()]

# # turn lists into database
# for username, password, name in zip(usernames, passwords, names):
#     user_dict = {"name":name,"password":password}
#     creds["usernames"].update({username:user_dict})

# print(creds)

#Creation of authentication object
authenticator = stauth.Authenticate(creds,
       "analytics_dashboard", "abcdef", cookie_expiry_days = 1)

#Returns the specified variables from streamlits' built in login authenticator form
name, authentication_status, username = authenticator.login("Login", "main")
# authenticator.register_user("main")


if authentication_status == False:
    st.error("Username/password  is incorrect")
    if st.button('Sign Up'):
        nav_page("Sign_Up")
        #Hides sidebar on Login Page
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
    
if authentication_status == None:
    st.warning("Please enter your username and password")
    if st.button('Sign Up'):
        nav_page("Sign_Up")
        #Hides sidebar on Login Page
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

if authentication_status:
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    # """
    
    #              ______           _          
    #     _  _    |_   _ `.        / |_        
    #   _| || |_    | | `. \ ,--. `| |-',--.   
    #  |_| || |_|   | |  | |`'_\ : | | `'_\ :  
    #  |_| || |_|  _| |_.' /// | |,| |,// | |, 
    #    |_||_|   |______.' \'-;__/\__/\'-;__/ 
                                            
    
    # """
    MentalData = np.random.randn(10, 1)
    PhysicalData = np.random.randn(10, 1)
    SpiritualData = np.random.randn(10, 1)
    CrimeData = np.random.randn(10, 1)
    heatmap = pd.read_csv('Data/weather.csv', parse_dates=['date'])
    stocks = pd.read_csv('Data/stocks.csv')




    # """
    
    #    ______    _        __        ______                   
    #  .' ____ \  (_)      |  ]      |_   _ \                  
    #  | (___ \_| __   .--.| | .---.   | |_) |  ,--.   _ .--.  
    #   _.____`. [  |/ /'`\' |/ /__\\  |  __'. `'_\ : [ `/'`\] 
    #  | \____) | | || \__/  || \__., _| |__) |// | |, | |     
    #   \______.'[___]'.__.;__]'.__.'|_______/ \'-;__/[___]    
                                                            
    
    # """

    st.sidebar.success("Select a page above.")
    #Logout button
    authenticator.logout("Logout", "sidebar")




    # """
    
    #              _______                              _       
    #     _  _    |_   __ \                            / \      
    #   _| || |_    | |__) |   .--.   _   _   __      / _ \     
    #  |_| || |_|   |  __ /  / .'`\ \[ \ [ \ [  ]    / ___ \    
    #  |_| || |_|  _| |  \ \_| \__. | \ \/\ \/ /   _/ /   \ \_  
    #    |_||_|   |____| |___|'.__.'   \__/\__/   |____| |____| 
                                                            
    
    # """
    a1, a2 = st.columns([1,3])
    # a1, a2,a3,a4= st.columns([3,1,1,1])
    a1.image('https://raw.githubusercontent.com/jbwilliams1006/Code_of_Duty_Analytics/e94586754e72914891ca847d313eab72defc092c/Icons/screenshot.png')
    a1.caption(f"Welcome {creds['usernames'][username]['fname']}")
    a1.text(f'Patients are seeing a 52.6% increase in mental health')
    a2.header(f'Week Overview')
    a3,a4,a5 = a2.columns(3
                    )
    with a3:
        st.metric(f"Patient Return", "72 out of 93", "+72%")
    with a4:
        st.metric(f"Patient Graduation", "27, last week 30", "-3%")
    with a5:
        st.metric(f"Costs", "850.97", "+92.4", "inverse")





    # """
    
    #              _______                         ______    
    #     _  _    |_   __ \                       |_   _ \   
    #   _| || |_    | |__) |   .--.   _   _   __    | |_) |  
    #  |_| || |_|   |  __ /  / .'`\ \[ \ [ \ [  ]   |  __'.  
    #  |_| || |_|  _| |  \ \_| \__. | \ \/\ \/ /   _| |__) | 
    #    |_||_|   |____| |___|'.__.'   \__/\__/   |_______/  
                                                        
    
    # """
    # b1, b2, b3, b4 = st.columns([2,2,2,2])
    b1, b2, b3, b4 = st.columns(4)
    with b1:
        st.image(Image.open('Icons/mind.png'))
        st.subheader("Mental Health",)
        st.line_chart(MentalData)
    with b2:
        st.image(Image.open('Icons/muscle.png'))
        st.subheader("Physical Health")
        st.line_chart(PhysicalData)
    with b3:
        st.image(Image.open('Icons/spiritual.png'))
        st.subheader("Spiritual Health")
        st.line_chart(SpiritualData)
    with b4:
        st.image(Image.open('Icons/crime.png'))
        st.subheader("Crime")
        st.line_chart(CrimeData)


    # """
    
    #              _______                           ______  
    #     _  _    |_   __ \                        .' ___  | 
    #   _| || |_    | |__) |   .--.   _   _   __  / .'   \_| 
    #  |_| || |_|   |  __ /  / .'`\ \[ \ [ \ [  ] | |        
    #  |_| || |_|  _| |  \ \_| \__. | \ \/\ \/ /  \ `.___.'\ 
    #    |_||_|   |____| |___|'.__.'   \__/\__/    `.____ .' 
                                                        
    
    # """

    # Row C
    c1, c2 = st.columns((7,3))
    with c1:
        st.markdown('### LineGraph')
        VisualsAlc.lineGraph()
        # plost.time_hist(
        # data=heatmap,
        # date='date',
        # x_unit='week',
        # y_unit='day',
        # color='temp_max',
        # aggregate='median',
        # legend=None)
    with c2:
        st.markdown('### Pie chart')
        VisualsPTSD.pieChart()
        # plost.donut_chart(
        #     data=stocks,
        #     theta='q2',
        #     color='company')