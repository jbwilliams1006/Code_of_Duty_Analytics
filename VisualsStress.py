import streamlit as st
import pandas as pd
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.io as pio

class VisualsStress:
       
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
        # df2.info()
        df2['date'] = pd.to_datetime(df2['date'], format='YYYY-mm-dd')
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
        # df3.info()
        df3['date'] = pd.to_datetime(df3['date'], format='%Y-%m-%d')
        df3['Month'] = pd.to_datetime(df3['date']).dt.month
        # ({1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'})
        # group by year
        df3['Week'] = pd.to_datetime(df3['date']).dt.isocalendar().week
        return df3

    def lineGraph():
        data3 = VisualsStress.load_data3(1000)
        data3.sort_values(by = 'Month')
        # data3['Month'] = dict({1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'})
        stress_data = data3.drop(data3[data3['stress'] == "Never"].index, inplace = True)
        # stress_data = data3.drop(data3[data3['stress'] == "Once"].index, inplace = True,)
        stress_data = data3.drop(data3[data3['stress'] == "Yearly"].index, inplace = True)
        stress_data = data3.drop(data3[data3['stress'] == "Seldom"].index, inplace = True)
        stress_data = data3.groupby(['Month','stress']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        # print(stress_data)
        plot = px.line(stress_data, x='Month',  y='count', color='stress', hover_data=['count'], labels='stress',title = 'High Risk Alchol Use Reported per Month in 2023')
        plot.update_traces(texttemplate="%{y}")
        
        plot.update_layout({'width' : 740, 'height' :320,'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot)
    
    def pieChart():
        data1 = VisualsStress.load_data1(1000)
        stress_data = data1.drop(data1[data1['stress'] == "Never"].index, inplace = True)
        stress_data = data1.drop(data1[data1['stress'] == "Yearly"].index, inplace = True)
        stress_data = data1.groupby(['stress']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        plot = px.pie(stress_data, values='count', names='stress', hover_data='count', labels = 'stress', title = 'Frequency of stress Reported in 2021')
        plot.update_traces(textposition='inside', textinfo='label + percent')
        plot.update_layout({ 'width' : 320, 'height' :400,'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot)
    def Scatter():
        data2 = VisualsStress.load_data2(1000)
        data2.sort_values(by = 'Month')
        stress_data = data2.drop(data2[data2['stress'] == "Never"].index, inplace = True)
        stress_data = data2.drop(data2[data2['stress'] == "Yearly"].index, inplace = True)
        stress_data = data2.drop(data2[data2['stress'] == "Once"].index, inplace = True)
        stress_data = data2.groupby(['Month','stress']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        #print(stress_data)
        plot = px.scatter(stress_data, 'Month',  'count', color='stress', size = 'count', hover_data=['count'],title = 'Frequency of stress Reported per Month in 2022',render_mode = "auto")
        
        # plot.update_traces(textposition='top center')
        return st.plotly_chart(plot)

    def barGraph():
        data1 = VisualsStress.load_data1(1000)
        stress_data = data1.drop(data1[data1['stress'] == "Never"].index, inplace = True)
        stress_data = data1.groupby(['stress']).apply(len).to_frame('count').reset_index()
        plot = px.bar(stress_data, x = 'stress', y = 'count', color  = 'stress', labels='stress',title = 'Frequency of stress Reported in 2021',text_auto=True)
        plot.update_coloraxes(showscale=True)
        return st.plotly_chart(plot)
    
def getGraphs():
        VisualsStress.barGraph()
        VisualsStress.Scatter()
        VisualsStress.lineGraph()
        VisualsStress.pieChart()
            

if __name__=='__main__':
    st.title("Stress Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()