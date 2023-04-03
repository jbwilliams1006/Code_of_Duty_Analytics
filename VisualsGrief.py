import streamlit as st
import pandas as pd
import datetime as dt
import plotly.express as px
import plotly.io as pio

class VisualsGrief:
       
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
        data3 = VisualsGrief.load_data3(1000)
        data3.sort_values(by = 'Month')
        # data3['Month'] = dict({1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'})
        # grief_data = data3.drop(data3[data3['grief'] == "Never"].index, inplace = True)
        grief_data = data3.groupby(['Month','grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        # print(grief_data)
        plot = px.line(grief_data, x='Month',  y='count', color='grief', hover_data=['count'], labels='grief',title = 'High Risk Alchol Use Reported per Month in 2023')
        plot.update_traces(texttemplate="%{y}")
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    
    def pieChart():
        data1 = VisualsGrief.load_data1(1000)
        # grief_data = data1.drop(data1[data1['grief'] == "Never"].index, inplace = True)
        # grief_data = data1.drop(data1[data1['grief'] == "Yearly"].index, inplace = True)
        grief_data = data1.groupby(['grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        plot = px.pie(grief_data, values='count', names='grief', hover_data='count', labels = 'grief', title = 'Frequency of grief Reported in 2021')
        plot.update_traces(textposition='inside', textinfo='label + percent')
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    def Scatter():
        data2 = VisualsGrief.load_data2(1000)
        data2.sort_values(by = 'Month')
        # grief_data = data2.drop(data2[data2['grief'] == "Never"].index, inplace = True)
        # grief_data = data2.drop(data2[data2['grief'] == "Yearly"].index, inplace = True)
        # grief_data = data2.drop(data2[data2['grief'] == "Once"].index, inplace = True)
        grief_data = data2.groupby(['Month','grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        #print(grief_data)
        plot = px.scatter(grief_data, 'Month',  'count', color='grief', size = 'count', hover_data=['count'],title = 'Frequency of grief Reported per Month in 2022',render_mode = "auto")
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)

    def barGraph():
        data1 = VisualsGrief.load_data1(1000)
        # grief_data = data1.drop(data1[data1['grief'] == "Never"].index, inplace = True)
        grief_data = data1.groupby(['grief']).apply(len).to_frame('count').reset_index()
        plot = px.bar(grief_data, x = 'grief', y = 'count', color  = 'grief', labels='grief',title = 'Frequency of grief Reported in 2021',text_auto=True)
        plot.update_coloraxes(showscale=True)
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    
def getGraphs():
        VisualsGrief.barGraph()
        VisualsGrief.Scatter()
        VisualsGrief.lineGraph()
        VisualsGrief.pieChart()
            

# if __name__=='__main__':
#     st.title("Grief Reports")
#     data_load_state = st.text('Loading data...')
#     getGraphs()