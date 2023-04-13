import streamlit as st
import streamlit_authenticator as stauth
from Dashboard import authenticator
from VisCourses import VisCourses
from PIL import Image

import logo

# st.set_page_config(layout="wide")
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
</style>
""", unsafe_allow_html=True)
st.subheader(":green[SAFB Support Services Statistics]")
st.text("Personnel completing additional support classes offered at Shepard Air Force Base.")

VisCourses.DVLine()
VisCourses.SALine()
VisCourses.alcLine()
VisCourses.angerLine()
VisCourses.stressLine()

 # logo above sidebar menu options
logo.add_logo("Icons/fullName_logo.png")
