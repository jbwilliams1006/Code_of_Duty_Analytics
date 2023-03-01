#Hey
import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image


# Page setting
st.set_page_config(layout="wide")

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
seattle_weather = pd.read_csv('weather.csv', parse_dates=['date'])
stocks = pd.read_csv('stocks.csv')


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
 
#              _______                         ______    
#     _  _    |_   __ \                       |_   _ \   
#   _| || |_    | |__) |   .--.   _   _   __    | |_) |  
#  |_| || |_|   |  __ /  / .'`\ \[ \ [ \ [  ]   |  __'.  
#  |_| || |_|  _| |  \ \_| \__. | \ \/\ \/ /   _| |__) | 
#    |_||_|   |____| |___|'.__.'   \__/\__/   |_______/  
                                                       
 
# """
b1, b2, b3, b4 = st.columns([2,2,2,2])
with b1:
    st.image(Image.open('mind.png'))
    st.subheader("Mental Health",)
    st.line_chart(MentalData)
with b2:
    st.image(Image.open('muscle.png'))
    st.subheader("Physical Health")
    st.line_chart(PhysicalData)
with b3:
    st.image(Image.open('spiritual.png'))
    st.subheader("Spiritual Health")
    st.line_chart(SpiritualData)
with b4:
    st.image(Image.open('crime.png'))
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
    st.markdown('### Heatmap')
    plost.time_hist(
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color='temp_max',
    aggregate='median',
    legend=None)
with c2:
    st.markdown('### Bar chart')
    plost.donut_chart(
        data=stocks,
        theta='q2',
        color='company')