import streamlit as st
import pandas as pd
import datetime as dt

class getData():
    @st.cache_data
    def load_data1(nrows):
        df = pd.read_csv('Data/MockData/MOCK_DATA.csv',nrows=nrows, parse_dates=['date'])
        df['date'] = pd.to_datetime(df['date'].dt.strftime('%B %Y'))
        return df
    
    @st.cache_data
    def load_data2(nrows):
        df = pd.read_csv('Data/MockData/MOCK_DATA2.csv', nrows=nrows,parse_dates=['date'])
        df['date'] = pd.to_datetime(df['date'].dt.strftime('%B %Y'))
        return df
    @st.cache_data
    def load_data3(nrows):
        df = pd.read_csv('Data/MockData/MOCK_DATA3.csv', nrows=nrows, parse_dates=['date'])
        df['date'] = pd.to_datetime(df['date'].dt.strftime('%b %Y'))
        return df
    
    def GetDF1():
        df1 = getData.load_data1(1000)
        return df1
    
    def GetDF2():
        df2 = getData.load_data2(1000)
        return df2
    
    def GetDF3():
        df3 = getData.load_data3(1000)
        return df3