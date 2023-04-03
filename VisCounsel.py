import streamlit as st
import pandas as pd
import datetime as dt
import plotly.express as px
import plotly.io as pio
# relation_counseling,grief_counseling,spiritual_counseling

class VisCounsel:
       
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

    def spritualLine():
        data2 = VisCounsel.load_data2(1000)
        data2.sort_values(by = 'Month')
        data = data2.drop(data2[data2['spiritual_counseling'] == False].index, inplace=True)
        data = data2.groupby(['Month','spiritual_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        # print(data)
        plot = px.line(data, x='Month',  y='count', color='spiritual_counseling', hover_data=['count'], labels='spiritual_counseling',title = 'Spiritual Counseling in 2022')
        plot.update_traces(texttemplate="%{y}")
        plot.update_layout(showlegend = False)
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    
    def relationLine():
        data2 = VisCounsel.load_data2(1000)
        data2.sort_values(by = 'Month')
        data = data2.drop(data2[data2['relation_counseling'] == False].index, inplace=True)
        data = data2.groupby(['Month','relation_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        # print(data)
        plot = px.line(data, x='Month',  y='count', color='relation_counseling', hover_data=['count'], labels='relation_counseling',title = 'Relationship Counseling in 2022')
        plot.update_traces(texttemplate="%{y}")
        plot.update_layout(showlegend = False)
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    
    def griefLine():
        data2 = VisCounsel.load_data2(1000)
        data2.sort_values(by = 'Month')
        data = data2.drop(data2[data2['grief_counseling'] == False].index, inplace=True)
        data = data2.groupby(['Month','grief_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        # print(data)
        plot = px.line(data, x='Month',  y='count', color='grief_counseling', hover_data=['count'], labels='grief_counseling',title = 'Grief Counseling in 2022')
        plot.update_traces(texttemplate="%{y}")
        plot.update_layout(showlegend = False)
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    
    def griefBar():
        data2 = VisCounsel.load_data2(1000)
        data2.sort_values(by = 'Month')
        data = data2.drop(data2[data2['grief_counseling'] == False].index, inplace=True)
        data = data2.groupby(['Month','grief_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        # print(data)
        plot = px.bar(data, x='Month',  y='count', color='grief_counseling', hover_data=['count'], labels='grief_counseling',title = 'Grief Counseling in 2022')
        plot.update_traces(texttemplate="%{y}")
        plot.update_layout(showlegend = False)
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    
def getGraphs():
        VisCounsel.spritualLine()
        VisCounsel.relationLine()
        VisCounsel.griefLine()
        VisCounsel.griefBar()
      
            

if __name__=='__main__':
    st.title("Counseling Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()