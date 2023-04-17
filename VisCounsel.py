import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime as dt
# relation_counseling,grief_counseling,spiritual_counseling

class VisCounsel:
       
    @st.cache_data(ttl = dt.timedelta(hours=1))
    def load_data1(nrows):
        df1 = pd.read_csv('Data/MockData/MOCK_DATA.csv',nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df1 = pd.DataFrame(df1)
        # df1.info()
        df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d')
        return df1
    
    @st.cache_data(ttl = dt.timedelta(hours=1))
    def load_data2(nrows):
        df2 = pd.read_csv('Data/MockData/MOCK_DATA2.csv', nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df2 = pd.DataFrame(df2)
        # df2.info()
        df2['date'] = pd.to_datetime(df2['date'], format='YYYY-mm-dd')
        return df2
    
    @st.cache_data(ttl = dt.timedelta(hours=1))
    def load_data3(nrows):
        df3 = pd.read_csv('Data/MockData/MOCK_DATA3.csv', nrows=nrows, parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df3 = pd.DataFrame(df3)
        # df3.info()
        df3['date'] = pd.to_datetime(df3['date'], format='%Y-%m-%d')
        return df3

    def spritualLine():
        df1 = VisCounsel.load_data1(1000)
        df2 = VisCounsel.load_data2(1000)
        df3 = VisCounsel.load_data3(1000)
        df1.drop(df1[df1['spiritual_counseling'] == False].index, inplace=True)
        df1 = df1.groupby(['date','spiritual_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2.drop(df2[df2['spiritual_counseling'] == False].index, inplace=True)
        df2 = df2.groupby(['date','spiritual_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3.drop(df3[df3['spiritual_counseling'] == False].index, inplace=True)
        df3 = df3.groupby(['date','spiritual_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()

        fig = go.Figure()

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df1.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff,name="2021", 
                        hoverinfo='x + y', hovertemplate='<b>%{x} 2021</b><br>Count: %{y}<extra></extra>', 
                         textfont=dict(size=16)))
       

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name="2022", 
                        hoverinfo='x + y', hovertemplate='<b>%{x} 2022</b><br>Count: %{y}<extra></extra>', 
                         textfont=dict(size=16)))
       

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name="2023", 
                        hoverinfo='x + y', hovertemplate='<b>%{x} 2023</b><br>Count: %{y}<extra></extra>', 
                         textfont=dict(size=16)))
        

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
                                # {"title": "Spiritual Counseling in 2021-2023"}
                                ]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                # {"title": "Spiritual Counseling in 2021"}
                                ]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                # {"title": "Spiritual Counseling in 2022"}
                                ]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                # {"title": "Spiritual Counseling in 2023"}
                                ]),
                    ]),
                )
            ])
        fig.update_xaxes(title_text="No. of Airmen in Spiritual Counseling", showline = True, title_font=dict(size=16 , color = "black"), tickfont=dict(size=13,color = "black"))
        fig.update_yaxes(showline =True, tickfont=dict(size=16, color = "black"))
        fig.update_layout(title={
            'text': "Spiritual Counseling",
            'font': {'size': 20}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",showlegend = False,
        hoverlabel=dict(font=dict(size=16, color = "black")))
        st.plotly_chart(fig,use_container_width=True)
    
    def relationLine():
        df1 = VisCounsel.load_data1(1000)
        df2 = VisCounsel.load_data2(1000)
        df3 = VisCounsel.load_data3(1000)
        df1.drop(df1[df1['relation_counseling'] == False].index, inplace=True)
        df1 = df1.groupby(['date','relation_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2.drop(df2[df2['relation_counseling'] == False].index, inplace=True)
        df2 = df2.groupby(['date','relation_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3.drop(df3[df3['relation_counseling'] == False].index, inplace=True)
        df3 = df3.groupby(['date','relation_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()

        fig = go.Figure()

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df1.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name="2021", 
                        hoverinfo='x + y', hovertemplate='<b>%{x} 2021</b><br>Count: %{y}<extra></extra>', 
                         textfont=dict(size=16)))
        

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name="2022", 
                        hoverinfo='x + y', hovertemplate='<b>%{x} 2022</b><br>Count: %{y}<extra></extra>', 
                         textfont=dict(size=16)))
        

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name="2023", 
                        hoverinfo='x + y', hovertemplate='<b>%{x} 2023</b><br>Count: %{y}<extra></extra>', 
                         textfont=dict(size=16)))
        
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
                                # {"title": "Relationship Counseling in 2021-2023"}
                                ]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                # {"title": "Relationship Counseling in 2021"}
                                ]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                # {"title": "Relationship Counseling in 2022"}
                                ]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                # {"title": "Relationship Counseling in 2023"}
                                ]),
                    ]),
                )
            ])
        fig.update_xaxes(title_text="No. of Airmen in Relationship Counseling", showline = True, title_font=dict(size=16 , color = "black"), tickfont=dict(size=13,color = "black"))
        fig.update_yaxes(showline =True, tickfont=dict(size=16, color = "black"))
        fig.update_layout(title={
            'text': "Relationship Counseling ",
            'font': {'size': 20}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",showlegend = False,
        hoverlabel=dict(font=dict(size=16, color = "black")))
        st.plotly_chart(fig,use_container_width=True)
        
      
    
    def griefLine():
        df1 = VisCounsel.load_data1(1000)
        df2 = VisCounsel.load_data2(1000)
        df3 = VisCounsel.load_data3(1000)
        df1.drop(df1[df1['grief_counseling'] == False].index, inplace=True)
        df1 = df1.groupby(['date','grief_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2.drop(df2[df2['grief_counseling'] == False].index, inplace=True)
        df2 = df2.groupby(['date','grief_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3.drop(df3[df3['grief_counseling'] == False].index, inplace=True)
        df3 = df3.groupby(['date','grief_counseling']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()

        fig = go.Figure()

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df1.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name="2021", 
                        hoverinfo='x + y', hovertemplate='<b>%{x} 2021</b><br>Count: %{y}<extra></extra>', 
                         textfont=dict(size=16)))
        

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff,name="2022", 
                        hoverinfo='x + y', hovertemplate='<b>%{x} 2022</b><br>Count: %{y}<extra></extra>', 
                         textfont=dict(size=16)))
        

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff,name="2023", 
                        hoverinfo='x + y', hovertemplate='<b>%{x} 2023</b><br>Count: %{y}<extra></extra>', 
                         textfont=dict(size=16)))
        

        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    x = .5,
                    xanchor = "center",
                    y = 1.08,
                    yanchor = "middle",
                    showactive=True,
                    font = dict({"color":"black", "size":18}),
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                # {"title": "Grief Counseling in 2021-2023"}
                                ]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                # {"title": "Grief Counseling in 2021"}
                                ]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                # {"title": "Grief Counseling in 2022"}
                                ]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                # {"title": "Grief Counseling in 2023"}
                                ]),
                    ]),
                )
            ])
        fig.update_xaxes(title_text="No. of Airmen in Grief Counseling", showline = True, title_font=dict(size=16 , color = "black"), tickfont=dict(size=13,color = "black"))
        fig.update_yaxes(showline =True, tickfont=dict(size=16, color = "black"))
        fig.update_layout(title={
            'text': "Grief Counseling ",
            'font': {'size': 20}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",showlegend = False,
        hoverlabel=dict(font=dict(size=16, color = "black")))
        st.plotly_chart(fig,use_container_width=True)
      
    

    
def getGraphs():
        VisCounsel.spritualLine()
        VisCounsel.relationLine()
        VisCounsel.griefLine()
            

if __name__=='__main__':
    st.title("Counseling Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()