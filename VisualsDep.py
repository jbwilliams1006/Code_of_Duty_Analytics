import streamlit as st
import pandas as pd
import datetime as dt
import plotly.express as px
import plotly.graph_objects as go

class VisualsDep:
       
    @st.cache_data(experimental_allow_widgets=True)
    def load_data1(nrows):
        df1 = pd.read_csv('Data/MockData/MOCK_DATA.csv',nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df1 = pd.DataFrame(df1)
        df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d')
        return df1
    
    @st.cache_data(experimental_allow_widgets=True)
    def load_data2(nrows):
        df2 = pd.read_csv('Data/MockData/MOCK_DATA2.csv', nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df2 = pd.DataFrame(df2)
        df2['date'] = pd.to_datetime(df2['date'], format='YYYY-mm-dd')
        return df2
    
    @st.cache_data(experimental_allow_widgets=True)
    def load_data3(nrows):
        df3 = pd.read_csv('Data/MockData/MOCK_DATA3.csv', nrows=nrows, parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df3 = pd.DataFrame(df3)
        df3['date'] = pd.to_datetime(df3['date'], format='%Y-%m-%d')
        return df3

    def lineGraph():
        df1 = VisualsDep.load_data1(1000)
        df2 = VisualsDep.load_data2(1000)
        df3 = VisualsDep.load_data3(1000)
        df1 = df1.groupby(['date','depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['date','depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['date','depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        fig = go.Figure()

        for depression in df1['depression'].unique():
            yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
            for val in df1.values:
                if val[1] == depression:
                    yStuff[val[0].month - 1] += val[2]
                    
            fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=depression))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")


        for depression in df2['depression'].unique():
            yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
            for val in df2.values:
                if val[1] == depression:
                    yStuff[val[0].month - 1] += val[2]
                    
            fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=depression))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")

        for depression in df3['depression'].unique():
            yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
            for val in df3.values:
                if val[1] == depression:
                    yStuff[val[0].month - 1] += val[2]
                    
            fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=depression))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")

            
        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    x = .5,
                    xanchor = "center",
                    y = 1.08,
                    yanchor = "middle",
                    showactive=True,
                    font = dict({"color":"black","size":16}),
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
        fig.update_layout(title_text="depression Reports")  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        st.plotly_chart(fig, use_container_width=True)
    
    def pieChart():
        df1 = VisualsDep.load_data1(1000)
        df2 = VisualsDep.load_data2(1000)
        df3 = VisualsDep.load_data3(1000)
        df1 = df1.groupby(['depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()

        fig = go.Figure()

        for Depression in df1:
            fig.add_trace(go.Pie(labels=df1['depression'],values = df1['count'], name = Depression))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")

        for Depression in df2:
            fig.add_trace(go.Pie(labels=df2['depression'], values = df2['count'],name=Depression))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")
            
        for Depression in df3:
            fig.add_trace(go.Pie(labels=df3['depression'],values = df3['count'], name=Depression))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")
            
        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    x = .5,
                    xanchor = "center",
                    y = 1.08,
                    yanchor = "middle",
                    showactive=True,
                    font = dict({"color":"black","size":16}),
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                {"title": "Frequency of Depression Reported 2021-2023"},
                                {"titleposition" : "top center"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Frequency of Depression Reported in 2021"},
                                {"titleposition" : "top center"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False, True,False]},
                                {"title": "Frequency of Depression Reported in 2022"},
                                {"titleposition" : "top center"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Frequency of Depression Reported in 2023"},
                                {"titleposition" : "top center"}]),
                    ]),
                )
            ])
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(title_text="Frequency of Depression Reported 2021-2023")
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})    

        st.plotly_chart(fig, use_container_width = True)
    

    def barGraph():
        df1 = VisualsDep.load_data1(1000)
        df2 = VisualsDep.load_data2(1000)
        df3 = VisualsDep.load_data3(1000)
        df1 = df1.groupby(['depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        fig = go.Figure()
        for Depression, group in df1.groupby('depression'):
            fig.add_trace(go.Bar(x=group['depression'], y=group["count"],name=Depression,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")

        for Depression, group in df2.groupby('depression'):
            fig.add_trace(go.Bar(x=group['depression'], y=group["count"],name=Depression,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")

        for Depression, group in df3.groupby('depression'):
            fig.add_trace(go.Bar(x=group['depression'], y=group["count"],name=Depression,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression")
            fig.update_yaxes(title_text="Count")

            
        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    x = .5,
                    xanchor = "center",
                    y = 1.08,
                    yanchor = "middle",
                    showactive=True,
                    font = dict({"color":"black","size":16}),
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

        fig.update_layout(title_text="Frequency of Depression Reported 2021-2023")  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})   
        st.plotly_chart(fig, use_container_width=True)
    
def getGraphs():
        VisualsDep.barGraph()
        VisualsDep.lineGraph()
        VisualsDep.pieChart()
            

if __name__=='__main__':
    st.title("depression Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()