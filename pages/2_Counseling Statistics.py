import streamlit as st
import streamlit_authenticator as stauth
from Dashboard import authenticator
from VisCounsel import VisCounsel
from PIL import Image
import base64


st.set_page_config(layout="wide")
# Chanegs the font size using custom css
st.markdown("""
<style>
.big-font {
    font-size:100px !important;
    font-family: "Source Sans Pro", sans-serif;
    font-weight: bold;
}
.css-1a32fsj.e19lei0e0 {
    display: flex;
    background-color: #eeeeee;
    padding: 1% 1% 1% 1%;
    border-radius: 30px;
}
}
</style>
""", unsafe_allow_html=True)
st.subheader(":green[SAFB Counseling Statistics]")
st.text("Personnel seeking counseling services at Shepard Air Force Base.")

VisCounsel.spritualLine()
VisCounsel.relationLine()
VisCounsel.griefLine()




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
