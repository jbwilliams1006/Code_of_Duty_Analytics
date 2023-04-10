import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime as dt
import plotly.express as px

class VisualsPTSD:
       
    @st.cache_data(ttl = dt.timedelta(hours=1))
    def load_data1(nrows):
        df1 = pd.read_csv('Data/MockData/MOCK_DATA.csv',nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df1 = pd.DataFrame(df1)
        # df1.info()
        df1['date'] = pd.to_datetime(df1['date'].dt.strftime('%B %Y'))
      
        return df1
    
    @st.cache_data(ttl = dt.timedelta(hours=1))
    def load_data2(nrows):
        df2 = pd.read_csv('Data/MockData/MOCK_DATA2.csv', nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df2 = pd.DataFrame(df2)
        # df2.info()
        df2['date'] = pd.to_datetime(df2['date'].dt.strftime('%B %Y'))
        return df2
    
    @st.cache_data(ttl = dt.timedelta(hours=1))
    def load_data3(nrows):
        df3 = pd.read_csv('Data/MockData/MOCK_DATA3.csv', nrows=nrows, parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df3 = pd.DataFrame(df3)
        # df3.info()
        df3['date'] = pd.to_datetime(df3['date'].dt.strftime('%B %Y'))
        return df3

    def lineGraph():
        df1 = VisualsPTSD.load_data1(1000)
        df2 = VisualsPTSD.load_data2(1000)
        df3 = VisualsPTSD.load_data3(1000)
        df1 = df1.groupby(['date','PTSD']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['date','PTSD']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['date','PTSD']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
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
        df1 = VisualsPTSD.load_data1(1000)
        df2 = VisualsPTSD.load_data2(1000)
        df3 = VisualsPTSD.load_data3(1000)
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
                    font = dict({"color":"black","size":16}),
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
        df1 = VisualsPTSD.load_data1(1000)
        df2 = VisualsPTSD.load_data2(1000)
        df3 = VisualsPTSD.load_data3(1000)
        df1 = df1.groupby(['PTSD']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['PTSD']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['PTSD']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        fig = go.Figure()
        for PTSD, group in df1.groupby("PTSD"):
            fig.add_trace(go.Bar(x=group["PTSD"], y=group["count"], name=PTSD,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "PTSD")
            fig.update_xaxes(title_text="PTSD",categoryorder='array', categoryarray= ['Daily','Often','Weekly','Monthly','Seldom','Yearly','Never'])
            fig.update_yaxes(title_text="Count")

        for PTSD, group in df2.groupby("PTSD"):
            fig.add_trace(go.Bar(x=group["PTSD"], y=group["count"], name=PTSD,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "PTSD")
            fig.update_xaxes(title_text="PTSD",categoryorder='array', categoryarray= ['Daily','Often','Weekly','Monthly','Seldom','Yearly','Never'])
            fig.update_yaxes(title_text="Count")
            
        for PTSD, group in df3.groupby("PTSD"):
            fig.add_trace(go.Bar(x=group["PTSD"], y=group["count"], name=PTSD,textposition='outside', text = group['count']))
            fig.update_layout(legend_title_text = "PTSD")
            fig.update_xaxes(title_text="PTSD",categoryorder='array', categoryarray= ['Daily','Often','Weekly','Monthly','Seldom','Yearly','Never'])
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
        fig.update_layout(title_text="Frequency of PTSD Reported 2021-2023")
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})    
        return st.plotly_chart(fig, use_container_width=True)
    
def getGraphs():
        VisualsPTSD.barGraph()
        VisualsPTSD.lineGraph()
        VisualsPTSD.pieChart()
            

if __name__=='__main__':
    st.title("PTSD Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()