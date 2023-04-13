import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime as dt
import plotly.express as px

class VisualsDep:
       
    @st.cache_data(ttl = dt.timedelta(hours=1))
    def load_data1(nrows):
        df1 = pd.read_csv('Data/MockData/MOCK_DATA.csv',nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df1 = pd.DataFrame(df1)
        df1['date'] = pd.to_datetime(df1['date'].dt.strftime('%B %Y'))
        return df1
    
    @st.cache_data(ttl = dt.timedelta(hours=1))
    def load_data2(nrows):
        df2 = pd.read_csv('Data/MockData/MOCK_DATA2.csv', nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df2 = pd.DataFrame(df2)
        df2['date'] = pd.to_datetime(df2['date'].dt.strftime('%B %Y'))
        return df2
    
    @st.cache_data(ttl = dt.timedelta(hours=1))
    def load_data3(nrows):
        df3 = pd.read_csv('Data/MockData/MOCK_DATA3.csv', nrows=nrows, parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df3 = pd.DataFrame(df3)
        df3['date'] = pd.to_datetime(df3['date'].dt.strftime('%B %Y'))
        return df3

    def lineGraph():
        df1 = VisualsDep.load_data1(1000)
        df2 = VisualsDep.load_data2(1000)
        df3 = VisualsDep.load_data3(1000)
        df1 = df1.groupby(['date','depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['date','depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['date','depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df = pd.concat([df1,df2,df3])
        df.drop(df[df['depression'] == "Once"].index, inplace = True)
        df.drop(df[df['depression'] == "Yearly"].index, inplace = True)
        df.drop(df[df['depression'] == "Seldom"].index, inplace = True)
        df.drop(df[df['depression'] == "Never"].index, inplace =True)
                
        fig=(px.line(df,x=df["date"], y='count', color='depression', hover_data=['count'], labels='depression', color_discrete_sequence=px.colors.qualitative.G10))
        fig.update_layout(legend_title_text = "PTSD")
        
        fig.update_xaxes(title_text="Date Range Selector", showline = True)
        fig.update_yaxes(title_text="Count",showline = True)
        fig.update_xaxes(rangeslider_visible=True)
        fig.update_layout(title_text="High Risk Depression Reported in 2021-2023")  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(fig, use_container_width=True)
    
    def pieChart():
        df1 = VisualsDep.load_data1(1000)
        df2 = VisualsDep.load_data2(1000)
        df3 = VisualsDep.load_data3(1000)
        df1 = df1.groupby(['depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['depression']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df_merge1 = pd.merge(df1, df2, on='depression', how='outer', suffixes=('_df1', '_df2'))
        df_merge2 = pd.merge(df_merge1, df3, on='depression', how='outer')
        df_merged = df_merge2.fillna(0)
        df_merged['count'] = df_merge2['count_df1'] + df_merge2['count_df2'] + df_merge2['count']
        df_merged = df_merged[['depression', 'count']]
        # print(df_merged)
        # create pie chart with all data visible
        fig = go.Figure()
        fig.add_trace(go.Pie(labels=df_merged['depression'], values=df_merged['count'], name="2021-2023", textinfo='label+percent', visible = True,
                        hoverinfo='label+value', hovertemplate='<b>%{label}</b><br>Count: %{value}<extra></extra>', 
                         textfont=dict(size=16)))
        # create pie chart with all data visible
        
        fig.add_trace(go.Pie(labels=df1['depression'], values=df1['count'], name="2021", textinfo='label+percent', visible = False,
                            hoverinfo='label+value', hovertemplate='<b>%{label}</b><br>Count: %{value}<extra></extra>', 
                             textfont=dict(size=16)))
        fig.add_trace(go.Pie(labels=df2['depression'], values=df2['count'], name="2022", textinfo='label+percent', visible = False,
                            hoverinfo='label+value', hovertemplate='<b>%{label}</b><br>Count: %{value}<extra></extra>', 
                             textfont=dict(size=16)))
        fig.add_trace(go.Pie(labels=df3['depression'], values=df3['count'], name="2023", textinfo='label+percent', visible = False,
                            hoverinfo='label+value', hovertemplate='<b>%{label}</b><br>Count: %{value}<extra></extra>', 
                             textfont=dict(size=16)))

        # create dropdown menu to toggle through years
        fig.update_layout(
            updatemenus=[
                dict(
                    x = .5,
                    xanchor = "center",
                    y = 1.08,
                    yanchor = "middle",
                    
                    font = dict({"color":"black","size":18}),
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, False, False, False] + [False] * (len(df_merged)-1) },
                            # {"title": "Frequency of Depression Reported in 2021-2023"}
                            ]),
                    dict(label="2021",
                        method="update",
                        args=[{"visible": [False, True, False, False] + [False] * (len(df_merged)-1) },
                            # {"title": "Frequency of Depression Reported in 2021"}
                            ]),
                    dict(label="2022",
                        method="update",
                        args=[{"visible": [False, False, True, False] + [False] * (len(df_merged)-1) },
                                # {"title": "Frequency of Depression Reported in 2022"}
                                ]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False, False, False, True] + [False] * (len(df_merged)-1)},
                                # {"title": "Frequency of Depression Reported in 2023"}
                                ]),
                       
                        ]),
                    showactive=True,
                    active =0,
                )
            ]
        )
        fig.update_layout(title={
            'text': "Frequency of Depression Reported in 2021-2023",
            'font': {'size': 20}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",
        hoverlabel=dict(font=dict(size=16, color = "black")))
        fig.update_traces(hoverinfo='label+value', textfont=dict(family = "Arial Black", size=14))
        st.plotly_chart(fig, use_container_width=True)

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
            fig.update_xaxes(title_text="Depression",categoryorder='array', categoryarray= ['Daily','Often','Weekly','Monthly','Seldom','Yearly','Never'])
            fig.update_yaxes(title_text="Count")

        for Depression, group in df2.groupby('depression'):
            fig.add_trace(go.Bar(x=group['depression'], y=group["count"],name=Depression,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression",categoryorder='array', categoryarray= ['Daily','Often','Weekly','Monthly','Seldom','Yearly','Never'])
            fig.update_yaxes(title_text="Count")

        for Depression, group in df3.groupby('depression'):
            fig.add_trace(go.Bar(x=group['depression'], y=group["count"],name=Depression,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "Depression")
            fig.update_xaxes(title_text="Depression",categoryorder='array', categoryarray= ['Daily','Often','Weekly','Monthly','Seldom','Yearly','Never'])
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
    st.title("Depression Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()