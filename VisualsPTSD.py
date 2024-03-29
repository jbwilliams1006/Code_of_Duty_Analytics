import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime as dt
import plotly.express as px
from getData import getData

class VisualsPTSD:

    def lineGraph():
        df1 = getData.GetDF1()
        df2 = getData.GetDF2()
        df3 = getData.GetDF3()
        df1 = df1.groupby(['date','PTSD']).apply(len).reindex().to_frame('count').reset_index()
        df2 = df2.groupby(['date','PTSD']).apply(len).reindex().to_frame('count').reset_index()
        df3 = df3.groupby(['date','PTSD']).apply(len).reindex().to_frame('count').reset_index()
        df = pd.concat([df1,df2,df3])
        df.drop(df[df['PTSD'] == "Once"].index, inplace = True)
        df.drop(df[df['PTSD'] == "Yearly"].index, inplace = True)
        df.drop(df[df['PTSD'] == "Seldom"].index, inplace = True)
        df.drop(df[df['PTSD'] == "Never"].index, inplace =True)
                
        fig=(px.line(df,x=df["date"], y='count', color='PTSD', hover_data=['count'], labels='PTSD', color_discrete_sequence=px.colors.qualitative.G10))
        fig.update_layout(legend_title_text = "PTSD")
        
        fig.update_xaxes(title_text="Date Range Selector", showline = True)
        fig.update_yaxes(title_text="Count", showline =True)
        fig.update_xaxes(rangeslider_visible=True)
        fig.update_layout(title_text="High Risk PTSD Reported in 2021-2023")  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(fig, use_container_width=True)
    
    def pieChart():
        df1 = getData.GetDF1()
        df2 = getData.GetDF2()
        df3 = getData.GetDF3()
        df1 = df1.groupby(['PTSD']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['PTSD']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['PTSD']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()

        fig = go.Figure()

        for PTSD in df1:
            fig.add_trace(go.Pie(labels=df1['PTSD'],values = df1['count'], name = PTSD))
            fig.update_layout(legend_title_text = "PTSD")
            fig.update_xaxes(title_text="PTSD")
            fig.update_yaxes(title_text="Count")

        for PTSD in df2:
            fig.add_trace(go.Pie(labels=df2['PTSD'], values = df2['count'],name=PTSD))
            fig.update_layout(legend_title_text = "PTSD")
            fig.update_xaxes(title_text="PTSD")
            fig.update_yaxes(title_text="Count")
            
        for PTSD in df3:
            fig.add_trace(go.Pie(labels=df3["PTSD"],values = df3['count'], name=PTSD))
            fig.update_layout(legend_title_text = "PTSD")
            fig.update_xaxes(title_text="PTSD")
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
                                {"title": "Frequency of PTSD Reported 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Frequency of PTSD Reported in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False, True,False]},
                                {"title": "Frequency of PTSD Reported in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Frequency of PTSD Reported in 2023"}]),
                    ]),
                )
            ])
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(title_text="Frequency of PTSD Reported 2021-2023")
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})    
        st.plotly_chart(fig, use_container_width = True)
        
   


    def barGraph():
        df1 = getData.GetDF1()
        df2 = getData.GetDF2()
        df3 = getData.GetDF3()
        df1 = df1.groupby(['PTSD']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['PTSD']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['PTSD']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        fig = go.Figure()
        for PTSD, group in df1.groupby("PTSD"):
            fig.add_trace(go.Bar(x=group["PTSD"], y=group["count"], name=f"2021 - {PTSD}", text=group['count'], textposition='auto',textfont=dict(family ='Arial Black',size=14)))
        for PTSD, group in df2.groupby("PTSD"):
            fig.add_trace(go.Bar(x=group["PTSD"], y=group["count"], name=f"2022 - {PTSD}", text=group['count'], textposition='auto',textfont=dict(family ='Arial Black',size=14)))
        for PTSD, group in df3.groupby("PTSD"):
            fig.add_trace(go.Bar(x=group["PTSD"], y=group["count"], name=f"2023 - {PTSD}", text=group['count'], textposition='auto',textfont=dict(family ='Arial Black',size=14)))

        # create dropdown menu to toggle through years
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
                            args=[{"visible": [True] * len(df1) + [True] * len(df2) + [True] * len(df3)},
                                # {"title": "Frequency of PTSD Reported in 2021-2023"}
                                ]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True] * len(df1) + [False] * len(df2) + [False] * len(df3)},
                                # {"title": "Frequency of PTSD Reported in 2021"}
                                ]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False] * len(df1) + [True] * len(df2) + [False] * len(df3)},
                                # {"title": "Frequency of PTSD Reported in 2022"}
                                ]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False] * len(df1) + [False] * len(df2) + [True] * len(df3)},
                                # {"title": "Frequency of PTSD Reported in 2023"}
                                ])
                    ]),
                )
            ]
        )
        # update layout of the chart
        fig.update_layout(barmode='group',
        xaxis={'categoryorder':'array', 'categoryarray': ['Daily', 'Often', 'Weekly', 'Monthly', 'Seldom', 'Yearly', 'Never']},
        title={
            'text': "Frequency of Reported PTSD at SAFB",
            'font': {'size': 20}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        hoverlabel=dict(font=dict(size=16, color = "black")))
        fig.update_yaxes(showline=True,title_font=dict(size=16, color = "black"), tickfont=dict(size=16, color = "black"))
        fig.update_xaxes(showline=True,title_text ="Air Force PTSD Survey Data", title_font=dict(size=20, color = "black"), tickfont=dict(size=16, color = "black"))
        return st.plotly_chart(fig, use_container_width=True)
    
def getGraphs():
        VisualsPTSD.barGraph()
        VisualsPTSD.lineGraph()
        VisualsPTSD.pieChart()
            

if __name__=='__main__':
    st.title("PTSD Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()