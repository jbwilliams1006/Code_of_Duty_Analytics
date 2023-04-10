import streamlit as st
from PIL import Image
import streamlit_authenticator as stauth
from Dashboard import authenticator



st.set_page_config(layout="wide")

# Chanegs the font size using custom css
st.markdown("""
<style>
.big-font {
    font-size:90px !important;
    font-family: "Source Sans Pro", sans-serif;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.subheader(":green[Experience More]")
img = Image.open('Icons/mentalhealth.jpeg')
# Multiply each value in the tuple by the multiplier
new_img_size = tuple([value * 3 for value in img.size])
img = img.resize((img.size))
a1, a2 = st.columns([2,1])
a1.markdown('<p class="big-font">The Best mental health classes in Wichita Falls, Period.</p>',unsafe_allow_html=True)
a2.image(img, use_column_width=True)
b1,b2 = st.columns([2,1])
b1.text("Take control of your mind and elevate your well-being! Join these mental health classes and learn powerful strategies to \nimprove your patients’ mental health. With expert guidance, interactive activities, and a supportive community, they’ll be\non their way to a happier and healthier life. Sign up now!")

    # """
    
    #    ______    _        __        ______                   
    #  .' ____ \  (_)      |  ]      |_   _ \                  
    #  | (___ \_| __   .--.| | .---.   | |_) |  ,--.   _ .--.  
    #   _.____`. [  |/ /'`\' |/ /__\\  |  __'. `'_\ : [ `/'`\] 
    #  | \____) | | || \__/  || \__., _| |__) |// | |, | |     
    #   \______.'[___]'.__.;__]'.__.'|_______/ \'-;__/[___]    
                                                            
    
    # ""
logo = Image.open('Icons/fullName_logo.png')
st.sidebar.image(logo, use_column_width =True)
st.sidebar.success("Select a page above.")
#Logout button
authenticator.logout("Logout", "sidebar")
