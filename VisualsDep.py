import streamlit as st
import pandas as pd
import datetime as dt
import plotly.express as px
import plotly.graph_objects as go

class VisualsDep:
       
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
        df3['Week'] = pd.to_datetime(df3['date']).dt.isocalendar().week
        return df3

    def lineGraph():
        df1 = VisualsDep.load_data1(1000)
        df2 = VisualsDep.load_data2(1000)
        df3 = VisualsDep.load_data3(1000)
        df1 = df1.groupby(['date','Depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['date','Depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['date','Depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        fig = go.Figure()

        for Depression in df1['Depression'].unique():
            yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
            for val in df1.values:
                if val[1] == Depression:
                    yStuff[val[0].month - 1] += val[2]
                    
            fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=Depression))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")


        for Depression in df2['Depression'].unique():
            yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
            for val in df2.values:
                if val[1] == Depression:
                    yStuff[val[0].month - 1] += val[2]
                    
            fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=Depression))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")

        for Depression in df3['Depression'].unique():
            yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
            for val in df3.values:
                if val[1] == Depression:
                    yStuff[val[0].month - 1] += val[2]
                    
            fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=Depression))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")

            
        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                {"title": "Frequency of Depression Reported 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Frequency of Depression Reported in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False, True,False]},
                                {"title": "Frequency of Depression Reported in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Frequency of Depression Reported in 2023"}]),
                    ]),
                )
            ])
        fig.update_layout(title_text="Depression Reports")  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        st.plotly_chart(fig, use_container_width=True)
    
    def pieChart():
        data1 = VisualsDep.load_data1(1000)
        depression_data = data1.groupby(['depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        plot = px.pie(depression_data, values='count', names='depression', hover_data='count', labels = 'depression', title = 'Frequency of Depression Reported in 2021')
        plot.update_traces(textposition='inside', textinfo='label + percent')
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    
    def Scatter():
        data2 = VisualsDep.load_data2(1000)
        data2.sort_values(by = 'Month')
        depression_data = data2.groupby(['Month','depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        #print(depression_data)
        plot = px.scatter(depression_data, 'Month',  'count', color='depression', size = 'count', hover_data=['count'],title = 'Frequency of Depression Reported per Month in 2022',render_mode = "auto")
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)

    def barGraph():
        df1 = VisualsDep.load_data1(1000)
        df2 = VisualsDep.load_data2(1000)
        df3 = VisualsDep.load_data3(1000)
        df1 = df1.groupby(['Depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['Depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['Depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        fig = go.Figure()
        for Depression, group in df1.groupby("Depression"):
            fig.add_trace(go.Bar(x=group["Depression"], y=group["count"], name=Depression))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")

        for Depression, group in df2.groupby("Depression"):
            fig.add_trace(go.Bar(x=group["Depression"], y=group["count"], name=Depression))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")
            
        for Depression, group in df3.groupby("Depression"):
            fig.add_trace(go.Bar(x=group["Depression"], y=group["count"], name=Depression))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")
            
        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                {"title": "Frequency of Depression Reported 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [ True, False, False]},
                                {"title": "Frequency of Depression Reported in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False, True,False]},
                                {"title": "Frequency of Depression Reported in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Frequency of Depression Reported in 2023"}]),
                    ]),
                )
            ])
        fig.update_layout(title_text="Depression Reports")  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})   
        return st.plotly_chart(fig, use_container_width=True)
    
def getGraphs():
        VisualsDep.barGraph()
        VisualsDep.Scatter()
        VisualsDep.lineGraph()
        VisualsDep.pieChart()
            

if __name__=='__main__':
    st.title("Depression Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()