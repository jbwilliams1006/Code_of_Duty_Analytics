import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime as dt
import plotly.express as px
from getData import getData

class VisualsGrief:

    def lineGraph():
        df1 = getData.GetDF1()
        df2 = getData.GetDF2()
        df3 = getData.GetDF3()
        df1 = df1.groupby(['date','grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['date','grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['date','grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df = pd.concat([df1,df2,df3])
        df.drop(df[df['grief'] == "Once"].index, inplace = True)
        df.drop(df[df['grief'] == "Yearly"].index, inplace = True)
        df.drop(df[df['grief'] == "Seldom"].index, inplace = True)
        df.drop(df[df['grief'] == "Never"].index, inplace =True)
                
        fig=(px.line(df,x=df["date"], y='count', color='grief', hover_data=['count'], labels='grief', color_discrete_sequence=px.colors.qualitative.G10))
        fig.update_layout(legend_title_text = "PTSD")
        
        fig.update_xaxes(title_text="Date Range Selector", showline = True)
        fig.update_yaxes(title_text="Count",showline = True)
        fig.update_xaxes(rangeslider_visible=True)
        fig.update_layout(title_text="High Risk Grief Reported in 2021-2023")  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(fig, use_container_width=True)
    
    def pieChart():
        df1 = getData.GetDF1()
        df2 = getData.GetDF2()
        df3 = getData.GetDF3()
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
                    y = 1.08,
                    yanchor = "middle",
                    showactive=True,
                    font = dict({"color":"black","size":18}),
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


    def barGraph():
        df1 = getData.GetDF1()
        df2 = getData.GetDF2()
        df3 = getData.GetDF3()
        df1 = df1.groupby(['grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['grief']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        fig = go.Figure()
        for Grief, group in df1.groupby('grief'):
            fig.add_trace(go.Bar(x=group['grief'], y=group["count"],name=Grief,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "Grief")
            fig.update_xaxes(title_text="Grief",categoryorder='array', categoryarray= ['Daily','Often','Weekly','Monthly','Seldom','Yearly','Never'])
            fig.update_yaxes(title_text="Count")

        for Grief, group in df2.groupby('grief'):
            fig.add_trace(go.Bar(x=group['grief'], y=group["count"],name=Grief,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "Grief")
            fig.update_xaxes(title_text="Grief",categoryorder='array', categoryarray= ['Daily','Often','Weekly','Monthly','Seldom','Yearly','Never'])
            fig.update_yaxes(title_text="Count")

        for Grief, group in df3.groupby('grief'):
            fig.add_trace(go.Bar(x=group['grief'], y=group["count"],name=Grief,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "Grief")
            fig.update_xaxes(title_text="Grief",categoryorder='array', categoryarray= ['Daily','Often','Weekly','Monthly','Seldom','Yearly','Never'])
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
                    font = dict({"color":"black","size":18}),
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
        VisualsGrief.lineGraph()
        VisualsGrief.pieChart()
            

if __name__=='__main__':
    st.title("grief Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()