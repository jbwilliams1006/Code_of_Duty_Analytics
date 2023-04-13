#For authentication
import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth
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
from VisualsGrief import VisualsGrief
from VisualsAnx import VisualsAnx
from VisCounsel import VisCounsel
from VisCourses import VisCourses
import base64
from dbQueries import *

#secure database access
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="care-of-duty-analytics")



# reference to the users collection ID
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
pageIcon = Image.open("Icons/CODA_logo.png")
st.set_page_config(page_title = "Care of Duty Analytics",page_icon=pageIcon, initial_sidebar_state="collapsed",layout="wide")


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
    # MentalData = np.random.randn(10, 1)
    # PhysicalData = np.random.randn(10, 1)
    # SpiritualData = np.random.randn(10, 1)
    # CrimeData = np.random.randn(10, 1)
    # heatmap = pd.read_csv('Data/weather.csv', parse_dates=['date'])
    # stocks = pd.read_csv('Data/stocks.csv')




    # """
    
    #    ______    _        __        ______                   
    #  .' ____ \  (_)      |  ]      |_   _ \                  
    #  | (___ \_| __   .--.| | .---.   | |_) |  ,--.   _ .--.  
    #   _.____`. [  |/ /'`\' |/ /__\\  |  __'. `'_\ : [ `/'`\] 
    #  | \____) | | || \__/  || \__., _| |__) |// | |, | |     
    #   \______.'[___]'.__.;__]'.__.'|_______/ \'-;__/[___]    
                                                            
    
    # ""
   # logo above sidebar menu options
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
    # logo = Image.open('Icons/fullName_logo.png')
    # st.sidebar.image(logo, use_column_width=True)
    st.sidebar.success("Select a page above.")
    # Logout button
    authenticator.logout("Logout", "sidebar")




    # """
    
    #              _______                              _       
    #     _  _    |_   __ \                            / \      
    #   _| || |_    | |__) |   .--.   _   _   __      / _ \     
    #  |_| || |_|   |  __ /  / .'`\ \[ \ [ \ [  ]    / ___ \    
    #  |_| || |_|  _| |  \ \_| \__. | \ \/\ \/ /   _/ /   \ \_  
    #    |_||_|   |____| |___|'.__.'   \__/\__/   |____| |____| 
                                                            
    
    # """
  
    img = Image.open('Icons/screenshot1.png')
    a1, a2 = st.columns([1,3],gap = "small")
    # a1, a2,a3,a4= st.columns([3,1,1,1])
    a1.image(img, use_column_width=True)
    a1.header(f"Welcome {creds['usernames'][username]['fname']}")
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
    b1, b2, b3, b4 = st.columns(4, gap = "small")
    with b1:
        # st.image(Image.open('Icons/mind.png'))
        VisCourses.stressLine()
        # st.subheader("Mental Health",)
        # st.line_chart(MentalData)
    with b2:
        # st.image(Image.open('Icons/muscle.png'))
        VisCourses.angerLine()
        # st.subheader("Physical Health")
        # st.line_chart(PhysicalData)
    with b3:
        # st.image(Image.open('Icons/spiritual.png'))
        # st.subheader("Spiritual Health")
        VisCounsel.spritualLine()
       
    with b4:
        # st.image(Image.open('Icons/crime.png'))
        # st.subheader("Crime")
        VisualsAlc.offenseLine()
        # st.line_chart(CrimeData)
        


    # """
    
    #              _______                           ______  
    #     _  _    |_   __ \                        .' ___  | 
    #   _| || |_    | |__) |   .--.   _   _   __  / .'   \_| 
    #  |_| || |_|   |  __ /  / .'`\ \[ \ [ \ [  ] | |        
    #  |_| || |_|  _| |  \ \_| \__. | \ \/\ \/ /  \ `.___.'\ 
    #    |_||_|   |____| |___|'.__.'   \__/\__/    `.____ .' 
                                                        
    
    # """

 
    c1, c2 = st.columns([7,3], gap = "small")
    with c1:
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
        # st.markdown('### Stress Reports')
        VisualsDep.pieChart()
        # plost.donut_chart(
        #     data=stocks,
        #     theta='q2',
        #     color='company')
        
          # """
    
    #              _______                           ______  
    #     _  _    |_   __ \                        .' ___  | 
    #   _| || |_    | |__) |   .--.   _   _   __  / .'   \_| 
    #  |_| || |_|   |  __ /  / .'`\ \[ \ [ \ [  ] | |        
    #  |_| || |_|  _| |  \ \_| \__. | \ \/\ \/ /  \ `.___.'\ D
    #    |_||_|   |____| |___|'.__.'   \__/\__/    `.____ .' 
                                                        
    
    # """

    # Row D
    d1, d2 = st.columns([3,7], gap = "small")
    with d1:
        # st.markdown('### LineGraph')
        VisualsAnx.pieChart()
      
    with d2:
        # st.markdown('### ')
        VisualsPTSD.barGraph()
       