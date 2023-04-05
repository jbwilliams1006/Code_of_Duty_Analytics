import streamlit as st
import pandas as pd
import datetime as dt
import plotly.express as px
import plotly.graph_objects as go

class VisualsAlc:
       
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
        df1 = VisualsAlc.load_data1(1000)
        df2 = VisualsAlc.load_data2(1000)
        df3 = VisualsAlc.load_data3(1000)
        df1 = df1.groupby(['date','alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['date','alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['date','alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        fig = go.Figure()

        for alcohol_use in df1['alcohol_use'].unique():
            yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
            for val in df1.values:
                if val[1] == alcohol_use:
                    yStuff[val[0].month - 1] += val[2]
                    
            fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=alcohol_use))
            fig.update_layout(legend_title_text = "alcohol_use")
            fig.update_xaxes(title_text="alcohol_use")
            fig.update_yaxes(title_text="Count")


        for alcohol_use in df2['alcohol_use'].unique():
            yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
            for val in df2.values:
                if val[1] == alcohol_use:
                    yStuff[val[0].month - 1] += val[2]
                    
            fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=alcohol_use))
            fig.update_layout(legend_title_text = "alcohol_use")
            fig.update_xaxes(title_text="alcohol_use")
            fig.update_yaxes(title_text="Count")

        for alcohol_use in df3['alcohol_use'].unique():
            yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
            for val in df3.values:
                if val[1] == alcohol_use:
                    yStuff[val[0].month - 1] += val[2]
                    
            fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=alcohol_use))
            fig.update_layout(legend_title_text = "alcohol_use")
            fig.update_xaxes(title_text="alcohol_use")
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
                                {"title": "Frequency of Alcohol Use Reported 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Frequency of Alcohol Use Reported in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False, True,False]},
                                {"title": "Frequency of Alcohol Use Reported in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Frequency of Alcohol Use Reported in 2023"}]),
                    ]),
                )
            ])
        fig.update_layout(title_text="Alcohol Use Reports")  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        st.plotly_chart(fig, use_container_width=True)
    
    def pieChart():
        data1 = VisualsAlc.load_data1(1000)
        # alcohol_use_data = data1.drop(data1[data1['alcohol_use'] == "Never"].index, inplace = True)
        # alcohol_use_data = data1.drop(data1[data1['alcohol_use'] == "Yearly"].index, inplace = True)
        alcohol_use_data = data1.groupby(['alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        plot = px.pie(alcohol_use_data, values='count', names='alcohol_use', hover_data='count', labels = 'alcohol_use', title = 'Frequency of Alcohol Use Reported in 2021')
        plot.update_traces(textposition='inside', textinfo='label + percent')
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    def Scatter():
        data2 = VisualsAlc.load_data2(1000)
        data2.sort_values(by = 'Month')
        # alcohol_use_data = data2.drop(data2[data2['alcohol_use'] == "Never"].index, inplace = True)
        # alcohol_use_data = data2.drop(data2[data2['alcohol_use'] == "Yearly"].index, inplace = True)
        # alcohol_use_data = data2.drop(data2[data2['alcohol_use'] == "Once"].index, inplace = True)
        
        alcohol_use_data = data2.groupby(['Month','alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        # print(alcohol_use_data)
        #print(alcohol_use_data)
        plot = px.scatter(alcohol_use_data, 'Month',  'count', color='alcohol_use', size = 'count', hover_data=['count'],title = 'Frequency of Alcohol Use Reported per Month in 2022',render_mode = "auto")
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        # plot.update_traces(textposition='top center')
        return st.plotly_chart(plot, use_container_width=True)

    def barGraph():
        df1 = VisualsAlc.load_data1(1000)
        df2 = VisualsAlc.load_data2(1000)
        df3 = VisualsAlc.load_data3(1000)
        df1 = df1.groupby(['alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2 = df2.groupby(['alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3 = df3.groupby(['alcohol_use']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        fig = go.Figure()
        for Alcohol, group in df1.groupby("alcohol_use"):
            fig.add_trace(go.Bar(x=group["alcohol_use"], y=group["count"], name=Alcohol))
            fig.update_layout(legend_title_text = "Alcohol")
            fig.update_xaxes(title_text="Alcohol")
            fig.update_yaxes(title_text="Count")

        for Alcohol, group in df2.groupby("alcohol_use"):
            fig.add_trace(go.Bar(x=group["alcohol_use"], y=group["count"], name=Alcohol))
            fig.update_layout(legend_title_text = "Alcohol")
            fig.update_xaxes(title_text="Alcohol")
            fig.update_yaxes(title_text="Count")
            
        for Alcohol, group in df3.groupby("alcohol_use"):
            fig.add_trace(go.Bar(x=group["alcohol_use"], y=group["count"], name=Alcohol))
            fig.update_layout(legend_title_text = "Alcohol")
            fig.update_xaxes(title_text="Alcohol")
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
                                {"title": "Frequency of Alcohol Use Reported 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [ True, False, False]},
                                {"title": "Frequency of Alcohol Use Reported in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False, True,False]},
                                {"title": "Frequency of Alcohol Use Reported in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Frequency of Alcohol Use Reported in 2023"}]),
                    ]),
                )
            ])
        fig.update_layout(title_text="Alcohol Use Reports")  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})   
        return st.plotly_chart(fig, use_container_width=True)
    
    def offenseLine():
        df1 = VisualsAlc.load_data1(1000)
        df2 = VisualsAlc.load_data2(1000)
        df3 = VisualsAlc.load_data3(1000)
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
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "Alcohol Related Offenses")
        fig.update_xaxes(title_text="Alcohol Related Offenses")
        fig.update_yaxes(title_text="Count")

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "Alcohol Related Offenses")
        fig.update_xaxes(title_text="Alcohol Related Offenses")
        fig.update_yaxes(title_text="Count")

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "Alcohol Related Offenses")
        fig.update_xaxes(title_text="Alcohol Related Offenses")
        fig.update_yaxes(title_text="Count")

        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    x = .5,
                    xanchor = "center",
                    y = 1.05,
                    yanchor = "middle",
                    showactive=True,
                    font = dict({"color":"black", "size":14}),
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                {"title": "Alcohol Related Offenses in 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Alcohol Related Offenses in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                {"title": "Alcohol Related Offenses in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Alcohol Related Offenses in 2023"}]),
                    ]),
                )
            ])
        fig.update_layout(title_text="Alcohol Related Offenses in 2021-2023",showlegend =False)  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        st.plotly_chart(fig,use_container_width=True)
    

def getGraphs():
        VisualsAlc.barGraph()
        VisualsAlc.Scatter()
        VisualsAlc.lineGraph()
        VisualsAlc.pieChart()
        VisualsAlc.offenseLine()
            

if __name__=='__main__':
    st.title("Alcohol Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()