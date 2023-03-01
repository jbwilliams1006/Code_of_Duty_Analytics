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
MentalData = np.random.randn(10, 1)
PhysicalData = np.random.randn(10, 1)
SpiritualData = np.random.randn(10, 1)
CrimeData = np.random.randn(10, 1)
# seattle_weather = pd.read_csv('weather.csv', parse_dates=['date'])
# stocks = pd.read_csv('stocks.csv')


# Row A
a1, a2 = st.columns([1,3])
# a1, a2,a3,a4= st.columns([3,1,1,1])
a1.image(Image.open('screenshot.png'))
a1.caption(f"Welcome Joshua")
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
b1, b2, b3, b4 = st.columns([2,2,2,2])
with b1:
    # st.image(Image.open('mind.png'))
    st.subheader("Mental Health",)
    st.line_chart(MentalData)
with b2:
    st.subheader("Physical Health")
    st.line_chart(PhysicalData)
with b3:
    st.subheader("Spiritual Health")
    st.line_chart(SpiritualData)
with b4:
    st.subheader("Crime")
    st.line_chart(CrimeData)


