import streamlit as st
import pandas as pd
import datetime as dt
import plotly.express as px
import plotly.graph_objects as go

class VisualsGrief:

    @st.cache_data
    def load_data1(nrows):
        data1 = pd.read_csv('Data/MockData/MOCK_DATA.csv',nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df1 = pd.DataFrame(data1)
        df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d')
        df1['Month'] = pd.to_datetime(df1['date']).dt.month
        return df1
    
    @st.cache_data
    def load_data2(nrows):
        data2 = pd.read_csv('Data/MockData/MOCK_DATA2.csv', nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df2 = pd.DataFrame(data2)
        df2['date'] = pd.to_datetime(df2['date'], format='YYYY-mm-dd')
        df2['Month'] = pd.to_datetime(df2['date']).dt.month
        return df2
    
    @st.cache_data
    def load_data3(nrows):
        data3 = pd.read_csv('Data/MockData/MOCK_DATA3.csv', nrows=nrows, parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df3 = pd.DataFrame(data3)
        df3['date'] = pd.to_datetime(df3['date'], format='%Y-%m-%d')
        df3['Month'] = pd.to_datetime(df3['date']).dt.month
        return df3

    def lineGraph():
        df1 = VisualsGrief.load_data1(1000)
        df2 = VisualsGrief.load_data2(1000)
        df3 = VisualsGrief.load_data3(1000)
        df1 = df1.groupby(['date','grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['date','grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['date','grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        fig = go.Figure()

        for grief in df1['grief'].unique():
            yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
            for val in df1.values:
                if val[1] == grief:
                    yStuff[val[0].month - 1] += val[2]
                    
            fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=grief))
            fig.update_layout(legend_title_text = "Grief")
            fig.update_xaxes(title_text="Grief")
            fig.update_yaxes(title_text="Count")


        for grief in df2['grief'].unique():
            yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
            for val in df2.values:
                if val[1] == grief:
                    yStuff[val[0].month - 1] += val[2]
                    
            fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=grief))
            fig.update_layout(legend_title_text = "Grief")
            fig.update_xaxes(title_text="=Grief")
            fig.update_yaxes(title_text="Count")

        for grief in df3['grief'].unique():
            yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
            for val in df3.values:
                if val[1] == grief:
                    yStuff[val[0].month - 1] += val[2]
                    
            fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=grief))
            fig.update_layout(legend_title_text = "Grief")
            fig.update_xaxes(title_text="Grief")
            fig.update_yaxes(title_text="Count")

            
        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    showactive=True,
                    font = dict({"color":"black","size":16}),
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                {"title": "Frequency of Grief Reported 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Frequency of Grief Reported in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False, True,False]},
                                {"title": "Frequency of Grief Reported in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Frequency of Grief Reported in 2023"}]),
                    ]),
                )
            ])
        fig.update_layout(title_text="Grief Reports")  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        st.plotly_chart(fig)
    
    def pieChart():
        df1 = VisualsGrief.load_data1(1000)
        df2 = VisualsGrief.load_data2(1000)
        df3 = VisualsGrief.load_data3(1000)
        df1 = df1.groupby(['grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()

        fig = go.Figure()

        for Grief in df1:
            fig.add_trace(go.Pie(labels=df1['grief'],values = df1['count'], name = Grief))
            fig.update_layout(legend_title_text = "Grief")
            fig.update_xaxes(title_text="Grief")
            fig.update_yaxes(title_text="Count")

        for Grief in df2:
            fig.add_trace(go.Pie(labels=df2['grief'], values = df2['count'],name=Grief))
            fig.update_layout(legend_title_text = "Grief")
            fig.update_xaxes(title_text="Grief")
            fig.update_yaxes(title_text="Count")
            
        for Grief in df3:
            fig.add_trace(go.Pie(labels=df3['grief'],values = df3['count'], name=Grief))
            fig.update_layout(legend_title_text = "Grief")
            fig.update_xaxes(title_text="Grief")
            fig.update_yaxes(title_text="Count")
            
        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    x = .5,
                    xanchor = "center",
                    y = 1,
                    yanchor = "middle",
                    showactive=True,
                    font = dict({"color":"black","size":16}),
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                {"title": "Frequency of Grief Reported 2021-2023"},
                                {"titleposition" : "top center"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Frequency of Grief Reported in 2021"},
                                {"titleposition" : "top center"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False, True,False]},
                                {"title": "Frequency of Grief Reported in 2022"},
                                {"titleposition" : "top center"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Frequency of Grief Reported in 2023"},
                                {"titleposition" : "top center"}]),
                    ]),
                )
            ])
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(title_text="Frequency of Grief Reported 2021-2023")
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})    

        st.plotly_chart(fig, use_container_width = True)
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
        df1 = VisualsGrief.load_data1(1000)
        df2 = VisualsGrief.load_data2(1000)
        df3 = VisualsGrief.load_data3(1000)
        df1 = df1.groupby(['grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        fig = go.Figure()
        for Grief, group in df1.groupby('grief'):
            fig.add_trace(go.Bar(x=group['grief'], y=group["count"],name=Grief,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "Grief")
            fig.update_xaxes(title_text="Grief")
            fig.update_yaxes(title_text="Count")

        for Grief, group in df2.groupby('grief'):
            fig.add_trace(go.Bar(x=group['grief'], y=group["count"],name=Grief,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "Grief")
            fig.update_xaxes(title_text="Grief")
            fig.update_yaxes(title_text="Count")

        for Grief, group in df3.groupby('grief'):
            fig.add_trace(go.Bar(x=group['grief'], y=group["count"],name=Grief,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "Grief")
            fig.update_xaxes(title_text="Grief")
            fig.update_yaxes(title_text="Count")

            
        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    showactive=True,
                    font = dict({"color":"black","size":16}),
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                {"title": "Frequency of Grief Reported 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [ True, False, False]},
                                {"title": "Frequency of Grief Reported in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False, True,False]},
                                {"title": "Frequency of Grief Reported in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Frequency of Grief Reported in 2023"}]),
                    ]),
                )
            ])

        fig.update_layout(title_text="Frequency of Grief Reported 2021-2023")  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})   
        st.plotly_chart(fig, use_container_width=True)

def getGraphs():
        VisualsGrief.barGraph()
        VisualsGrief.Scatter()
        VisualsGrief.lineGraph()
        VisualsGrief.pieChart()
            

if __name__=='__main__':
    st.title("grief Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()