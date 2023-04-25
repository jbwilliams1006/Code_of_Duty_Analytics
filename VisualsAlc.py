import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime as dt
import plotly.express as px
from getData import getData

class VisualsAlc:

    def lineGraph():
        df1 = getData.GetDF1()
        df2 = getData.GetDF2()
        df3 = getData.GetDF3()
        df1 = df1.groupby(['date','alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['date','alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['date','alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df = pd.concat([df1,df2,df3])
        df.drop(df[df['alcohol_use'] == "Once"].index, inplace = True)
        df.drop(df[df['alcohol_use'] == "Yearly"].index, inplace = True)
        df.drop(df[df['alcohol_use'] == "Seldom"].index, inplace = True)
        df.drop(df[df['alcohol_use'] == "Never"].index, inplace =True)
                
        fig=(px.line(df,x=df["date"], y='count', color='alcohol_use', hover_data=['count'], labels=dict(alcohol_use =""), color_discrete_sequence=px.colors.qualitative.G10))
        
        fig.update_layout(
    xaxis={
        'title': {
            'text': 'Date Range Selector',
            'font': {'size': 20, 'color': 'black'},
        },
        'showline': True,
        'title_font': {'size': 20, 'color': 'black'},
        'tickfont': {'size': 14, 'color': 'black'},
    }
)
        
        fig.update_layout(
        xaxis=dict(
        rangeselector=dict(
            font = dict({"color":"black","size":16}),
            x = 1,
            xanchor = "right",
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
        fig.add_annotation(
            x=0.5,
            y=-0.3,
            xref="paper",
            yref="paper",
            showarrow=False,
            text="Air Force Alcohol Use Survey Data",
            font=dict(size=20, color = "black"),
        )
        fig.update_yaxes(title_text="Count",showline =True, title_font=dict(size=16, color = "black"), tickfont=dict(size=16, color = "black"))
        fig.update_layout(title={
            'text': "High Risk Alcohol Use Reported at SAFB",
            'font': {'size': 20}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        hoverlabel=dict(font=dict(size=16, color = "black")))
  
        st.plotly_chart(fig, use_container_width=True)
        
 
    def pieChart():
        df1 = getData.GetDF1()
        df2 = getData.GetDF2()
        df3 = getData.GetDF3()
        df1 = df1.groupby(['alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        
        fig = go.Figure()
    
        for Alcohol in df1:
            fig.add_trace(go.Pie(labels=df1['alcohol_use'],values = df1['count'], name = Alcohol))
            fig.update_layout(legend_title_text = "Alcohol Use")
            fig.update_xaxes(title_text="Alcohol Use")
            fig.update_yaxes(title_text="Count")

        for Alcohol in df2:
            fig.add_trace(go.Pie(labels=df2['alcohol_use'], values = df2['count'],name=Alcohol ))
            fig.update_layout(legend_title_text = "Alcohol Use")
            fig.update_xaxes(title_text="Alcohol Use")
            fig.update_yaxes(title_text="Count")
            
        for Alcohol in df3:
            fig.add_trace(go.Pie(labels=df3['alcohol_use'],values = df3['count'], name=Alcohol))
            fig.update_layout(legend_title_text = "Alcohol Use")
            fig.update_xaxes(title_text="Alcohol Use")
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
                                {"title": "Frequency of Alcohol Use Reported 2021-2023"},
                                {"titleposition" : "top center"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Frequency of Alcohol Use Reported in 2021"},
                                {"titleposition" : "top center"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False, True,False]},
                                {"title": "Frequency of Alcohol Use Reported in 2022"},
                                {"titleposition" : "top center"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Frequency of Alcohol Use Reported in 2023"},
                                {"titleposition" : "top center"}]),
                    ]),
                )
            ])
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(title_text="Frequency of Alcohol Use Reported 2021-2023")
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})    
        return st.plotly_chart(fig, use_container_width = True)
        

    def barGraph():
        df1 = getData.GetDF1()
        df2 = getData.GetDF2()
        df3 = getData.GetDF3()
        df1 = df1.groupby(['alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        fig = go.Figure()
        for Alcohol, group in df1.groupby("alcohol_use"):
            fig.add_trace(go.Bar(x=group["alcohol_use"], y=group["count"], name=Alcohol))
            fig.update_layout(legend_title_text = "Alcohol")
            fig.update_xaxes(title_text="Alcohol",categoryorder='array', categoryarray= ['Daily','Often','Weekly','Monthly','Seldom','Yearly','Never'])
            fig.update_yaxes(title_text="Count")

        for Alcohol, group in df2.groupby("alcohol_use"):
            fig.add_trace(go.Bar(x=group["alcohol_use"], y=group["count"], name=Alcohol))
            fig.update_layout(legend_title_text = "Alcohol")
            fig.update_xaxes(title_text="Alcohol",categoryorder='array', categoryarray= ['Daily','Often','Weekly','Monthly','Seldom','Yearly','Never'])
            fig.update_yaxes(title_text="Count")
            
        for Alcohol, group in df3.groupby("alcohol_use"):
            fig.add_trace(go.Bar(x=group["alcohol_use"], y=group["count"], name=Alcohol))
            fig.update_layout(legend_title_text = "Alcohol")
            fig.update_xaxes(title_text="Alcohol",categoryorder='array', categoryarray= ['Daily','Often','Weekly','Monthly','Seldom','Yearly','Never'])
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
                                {"title": "Frequency of Alcohol Use Reported 2021-2023"},
                                ]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [ True, False, False]},
                                # {"title": "Frequency of Alcohol Use Reported in 2021"}
                                ]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False, True,False]},
                                # {"title": "Frequency of Alcohol Use Reported in 2022"}
                                ]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                # {"title": "Frequency of Alcohol Use Reported in 2023"}
                                ]),
                    ]),
                )
            ])
        fig.update_layout(title_text="Frequency of Alcohol Use Reported 2021-2023")  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})   
        return st.plotly_chart(fig, use_container_width=True)
    

    def offenseLine():
        df1 = getData.GetDF1()
        df2 = getData.GetDF2()
        df3 = getData.GetDF3()
        df1.drop(df1[df1['alcohol_offense'] == False].index, inplace=True)
        df1 = df1.groupby(['date','alcohol_offense']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2.drop(df2[df2['alcohol_offense'] == False].index, inplace=True)
        df2 = df2.groupby(['date','alcohol_offense']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3.drop(df3[df3['alcohol_offense'] == False].index, inplace=True)
        df3 = df3.groupby(['date','alcohol_offense']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()

        fig = go.Figure()

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df1.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name="2021", 
                        hoverinfo='x + y', hovertemplate='<b>%{x} 2021</b><br>Count: %{y}<extra></extra>', 
                         textfont=dict(size=16)))
        # fig.update_layout(legend ="2021")
        

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name="2022", 
                        hoverinfo='x + y', hovertemplate='<b>%{x} 2022</b><br>Count: %{y}<extra></extra>', 
                         textfont=dict(size=16)))
        # fig.update_layout(legend = "2022")
     

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff,name="2023", 
                        hoverinfo='x + y', hovertemplate='<b>%{x} 2023</b><br>Count: %{y}<extra></extra>', 
                         textfont=dict(size=16)))
        # fig.update_layout(legend ="2023")
       

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
                                # {"title": "Alcohol Related Offenses in 2021-2023"}
                                ]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                # {"title": "Alcohol Related Offenses in 2021"}
                                ]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                # {"title": "Alcohol Related Offenses in 2022"}
                                ]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                # {"title": "Alcohol Related Offenses in 2023"}
                                ]),
                    ]),
                )
            ])
       
        fig.update_xaxes(title_text="No. of Alcohol Offenses at SAFB ", showline = True, title_font=dict(size=16 , color = "black"), tickfont=dict(size=13,color = "black"))
        fig.update_yaxes(showline =True, tickfont=dict(size=16, color = "black"))
        fig.update_layout(title={
            'text': "Alcohol Related Offenses",
            'font': {'size': 20}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",showlegend = False,
        hoverlabel=dict(font=dict(size=16, color = "black")))
        st.plotly_chart(fig,use_container_width=True)
    

def getGraphs():
        VisualsAlc.barGraph()
        VisualsAlc.lineGraph()
        VisualsAlc.pieChart()
        VisualsAlc.offenseLine()
            

if __name__=='__main__':
    st.title("Alcohol Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()