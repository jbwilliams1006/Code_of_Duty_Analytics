#Hey
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Data


# Row A
a1, a2 = st.columns([1,2])
a1.image(Image.open('screenshot.png'))
a2.header(f'Week Overview')
a2.metric(f"Patient Return", "72 out of 93", "+72%")
a2.metric(f"Patient Graduation", "27, last week 30", "-3%")
a2.metric(f"Costs", "850.97", "+92.4", "inverse")

# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperature", "70 °F", "1.2 °F")
b2.metric("Wind", "9 mph", "-8%")
b3.metric("Humidity", "86%", "4%")
b4.metric("Humidity", "86%", "4%")
