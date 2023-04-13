import streamlit as st
from PIL import Image
import streamlit_authenticator as stauth
from Dashboard import authenticator
import base64



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
# logo above dashboard header!
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
