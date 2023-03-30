import streamlit as st
import pandas as pd
import csv
import datetime as dt
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
@st.cache_data
def load_data1(nrows):
    data1 = pd.read_csv('Data/MockData/MOCK_DATA.csv',nrows=nrows,parse_dates=['date'])
   
    # df = set up the data in pandas Data Frame format
    df1 = pd.DataFrame(data1)
    # df1.info()
    df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d')
    df1['Month'] = pd.to_datetime(df1['date']).dt.month
    # group by year
    df1['Year'] = pd.to_datetime(df1['date']).dt.year
    df1['Week'] = pd.to_datetime(df1['date']).dt.isocalendar().week
    return df1
@st.cache_data
def load_data2(nrows):
    data2 = pd.read_csv('Data/MockData/MOCK_DATA2.csv', nrows=nrows,parse_dates=['date'])
    # df = set up the data in pandas Data Frame format
    df2 = pd.DataFrame(data2)
    df2.info()
    df2['date'] = pd.to_datetime(df2['date'], format='%Y-%m-%d')
    df2['Month'] = pd.to_datetime(df2['date']).dt.month
    # group by year
    df2['Year'] = pd.to_datetime(df2['date']).dt.year
    df2['Week'] = pd.to_datetime(df2['date']).dt.isocalendar().week
    return df2
@st.cache_data
def load_data3(nrows):
    data3 = pd.read_csv('Data/MockData/MOCK_DATA3.csv', nrows=nrows, parse_dates=['date'])
    # df = set up the data in pandas Data Frame format
    df3 = pd.DataFrame(data3)
    df3.info()
    df3['date'] = pd.to_datetime(df3['date'], format='%Y-%m-%d')
    df3['Month'] = pd.to_datetime(df3['date']).dt.month
    # group by year
    df3['Year'] = pd.to_datetime(df3['date']).dt.year
    df3['Week'] = pd.to_datetime(df3['date']).dt.isocalendar().week
    return df3
# change the path to the location of your file
# read in the csv file and set to data
# data = pd.read_csv('/Users/lesliecook/Desktop/CODA/mockdata/MOCK_DATA.csv')


data_load_state = st.text('Loading data...')
data1 = load_data1(100)
data2 = load_data2(100)
data3 = load_data3(100)

def lineGraph2021():
    data1.sort_values(by = 'Week')
    stress_data = data1.groupby(['Week','stress']).apply(len).reindex(fill_value=0).to_frame('count')
    print(stress_data)
    mylabels = ['Daily', 'Monthly', 'Never', 'Often', 'Once', 'Seldom', 'Weekly', 'Yearly'] 
    mylabels.append(mylabels)
    print(mylabels)
    stress_data = stress_data.unstack()
    fig, ax = plt.subplots(figsize=(12,6))
    plt.plot(stress_data, marker='o', markersize=4, linewidth=2 )
    ax.set_ylim(0,12)
    ax.set_xlim(1, 12)
    plt.xlabel("Weekss in 2021")
    plt.ylabel("stress frequency")
    plt.title("Stress frequency reported per Month in 2022")
    plt.legend(labels = mylabels, bbox_to_anchor=(.85, 1.0), loc='upper left')
    
    return st.write(fig)

lineGraph2021()


def lineGraph2022():
    data2.sort_values(by = 'Month')
    PTSD_data = data2.groupby(['Month','PTSD']).apply(len).reindex(fill_value=0).to_frame('count')
    print(PTSD_data)
    mylabels = ['Daily', 'Monthly', 'Never', 'Often', 'Once', 'Seldom', 'Weekly', 'Yearly']  
    print(mylabels)
    PTSD_data = PTSD_data.unstack()
    fig, ax = plt.subplots(figsize=(12,6))
    plt.plot(PTSD_data, marker='o', markersize=4, linewidth=2 )
    ax.set_ylim(0,12)
    ax.set_xlim(1, 12)
    plt.xlabel("Months in 2022")
    plt.ylabel("PTSD frequency")
    plt.title("PTSD frequency reported per Month in 2022")
    plt.legend(labels = mylabels, bbox_to_anchor=(.85, 1.0), loc='upper left')
    
    return st.write(fig)

lineGraph2022()

def lineGraph2023():
    data2.sort_values(by = 'Month')
    alcohol_data = data2.groupby(['Month','alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count')
    print(alcohol_data)
    mylabels = ['Daily', 'Monthly', 'Never', 'Often', 'Once', 'Seldom', 'Weekly', 'Yearly']  ##Declare and build an array of labels
    mylabels.append(mylabels)
    print(mylabels)
    alcohol_data = alcohol_data.unstack()
    fig, ax = plt.subplots(figsize=(12,6))
    plt.plot(alcohol_data, marker='o', markersize=4, linewidth=2 )
    ax.set_ylim(0,12)
    ax.set_xlim(1, 12)
    plt.xlabel("Months in 2023")
    plt.ylabel("alcohol_use frequency")
    plt.title("Acohol Use frequency reported per Month in 2023")
    plt.legend(labels = mylabels, bbox_to_anchor=(.85, 1.0), loc='upper left')
    
    return st.write(fig)

lineGraph2023()

    

