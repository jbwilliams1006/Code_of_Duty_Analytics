import streamlit as st
import pandas as pd
import datetime as dt
import plotly.express as px
import plotly.graph_objects as go
# anger_course,alcohol_course,stress_course,SA_course,DV_course
class VisCourses:
       
    @st.cache_data
    def load_data1(nrows):
        data1 = pd.read_csv('Data/MockData/MOCK_DATA.csv',nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df1 = pd.DataFrame(data1)
        # df1.info()
        df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d')
        df1['Month'] = pd.to_datetime(df1['date']).dt.month
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
    
    def angerLine():
        df1 = VisCourses.load_data1(1000)
        df2 = VisCourses.load_data2(1000)
        df3 = VisCourses.load_data3(1000)
        df1.drop(df1[df1['anger_course'] == False].index, inplace=True)
        df1 = df1.groupby(['date','anger_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2.drop(df2[df2['anger_course'] == False].index, inplace=True)
        df2 = df2.groupby(['date','anger_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3.drop(df3[df3['anger_course'] == False].index, inplace=True)
        df3 = df3.groupby(['date','anger_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()

        fig = go.Figure()

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df1.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "anger_course")
        fig.update_xaxes(title_text="anger_course")
        fig.update_yaxes(title_text="Count")

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "anger_course")
        fig.update_xaxes(title_text="anger_course")
        fig.update_yaxes(title_text="Count")

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "Anger Management")
        fig.update_xaxes(title_text="Anger Management")
        fig.update_yaxes(title_text="Count")

        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    showactive=True,
                    font = dict({"color":"black", "size":14}),
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                {"title": "Anger Management Courses Completed in 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Anger Management Courses Completed in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                {"title": "Anger Management Courses Completed in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Anger Management Courses Completed in 2023"}]),
                    ]),
                )
            ])
        fig.update_layout(title_text="Anger Management Courses Completed in 2021-2023",showlegend =False)  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        
        st.plotly_chart(fig)
    
    def angerBar():
        data2 = VisCourses.load_data2(1000)
        data2.sort_values(by = 'Month')
        data = data2.drop(data2[data2['anger_course'] == False].index, inplace=True)
        data = data2.groupby(['Month','anger_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        # print(data)
        plot = px.bar(data, x='Month',  y='count', color='anger_course', hover_data=['count'], labels='anger_course',title = 'Anger Management Courses in 2022')
        plot.update_traces(texttemplate="%{y}")
        plot.update_layout(showlegend = False)
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    
    def alcLine():
        df1 = VisCourses.load_data1(1000)
        df2 = VisCourses.load_data2(1000)
        df3 = VisCourses.load_data3(1000)
        df1.drop(df1[df1['alcohol_course'] == False].index, inplace=True)
        df1 = df1.groupby(['date','alcohol_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2.drop(df2[df2['alcohol_course'] == False].index, inplace=True)
        df2 = df2.groupby(['date','alcohol_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3.drop(df3[df3['alcohol_course'] == False].index, inplace=True)
        df3 = df3.groupby(['date','alcohol_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()

        fig = go.Figure()

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df1.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "alcohol_course")
        fig.update_xaxes(title_text="alcohol_course")
        fig.update_yaxes(title_text="Count")

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "alcohol_course")
        fig.update_xaxes(title_text="alcohol_course")
        fig.update_yaxes(title_text="Count")

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "Alcohol Awareness")
        fig.update_xaxes(title_text="Alcohol Awareness")
        fig.update_yaxes(title_text="Count")

        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    showactive=True,
                    font = dict({"color":"black", "size":14}),
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                {"title": "Alcohol Awareness Courses Completed in 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Alcohol Awareness Courses Completed in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                {"title": "Alcohol Awareness Courses Completed in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Alcohol Awareness Courses Completed in 2023"}]),
                    ]),
                )
            ])
        fig.update_layout(title_text="Alcohol Awareness Courses Completed in 2021-2023",showlegend =False)  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        
        st.plotly_chart(fig, use_container_width=True)
    
    
    def alcBar():
        data2 = VisCourses.load_data2(1000)
        data2.sort_values(by = 'Month')
        data = data2.drop(data2[data2['alcohol_course'] == False].index, inplace=True)
        data = data2.groupby(['Month','alcohol_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        # print(data)
        plot = px.bar(data, x='Month',  y='count', color='alcohol_course', hover_data=['count'], labels='alcohol_course',title = 'Alcohol Management Courses in 2022')
        plot.update_traces(texttemplate="%{y}")
        plot.update_layout(showlegend = False)
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    
    def stressLine():
        df1 = VisCourses.load_data1(1000)
        df2 = VisCourses.load_data2(1000)
        df3 = VisCourses.load_data3(1000)
        df1.drop(df1[df1['stress_course'] == False].index, inplace=True)
        df1 = df1.groupby(['date','stress_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2.drop(df2[df2['stress_course'] == False].index, inplace=True)
        df2 = df2.groupby(['date','stress_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3.drop(df3[df3['stress_course'] == False].index, inplace=True)
        df3 = df3.groupby(['date','stress_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()

        fig = go.Figure()

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df1.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "stress_course")
        fig.update_xaxes(title_text="stress_course")
        fig.update_yaxes(title_text="Count")

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "stress_course")
        fig.update_xaxes(title_text="stress_course")
        fig.update_yaxes(title_text="Count")

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "Stress Management")
        fig.update_xaxes(title_text="Stress Management")
        fig.update_yaxes(title_text="Count")

        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    showactive=True,
                    font = dict({"color":"black", "size":14}),
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                {"title": "Stress Management Courses Completed in 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Stress Management Courses Completed in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                {"title": "Stress Management Courses Completed in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Stress Management Courses Completed in 2023"}]),
                    ]),
                )
            ])
        fig.update_layout(title_text="Stress Management Courses Completed in 2021-2023",showlegend =False)  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        
        st.plotly_chart(fig, use_container_width=True)
    
    
    def stressBar():
        data2 = VisCourses.load_data2(1000)
        data2.sort_values(by = 'Month')
        data = data2.drop(data2[data2['stress_course'] == False].index, inplace=True)
        data = data2.groupby(['Month','stress_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        # print(data)
        plot = px.bar(data, x='Month',  y='count', color='stress_course', hover_data=['count'], labels='stress_course',title = 'Stress Management Courses in 2022')
        plot.update_traces(texttemplate="%{y}")
        plot.update_layout(showlegend = False)
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    
    
    def SALine():
        df1 = VisCourses.load_data1(1000)
        df2 = VisCourses.load_data2(1000)
        df3 = VisCourses.load_data3(1000)
        df1.drop(df1[df1['SA_course'] == False].index, inplace=True)
        df1 = df1.groupby(['date','SA_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2.drop(df2[df2['SA_course'] == False].index, inplace=True)
        df2 = df2.groupby(['date','SA_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3.drop(df3[df3['SA_course'] == False].index, inplace=True)
        df3 = df3.groupby(['date','SA_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()

        fig = go.Figure()

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df1.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "SA_course")
        fig.update_xaxes(title_text="SA_course")
        fig.update_yaxes(title_text="Count")

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "SA_course")
        fig.update_xaxes(title_text="SA_course")
        fig.update_yaxes(title_text="Count")

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "Sexual Assault Prevention")
        fig.update_xaxes(title_text="Sexual Assault Prevention")
        fig.update_yaxes(title_text="Count")

        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    showactive=True,
                    font = dict({"color":"black", "size":14}),
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                {"title": "Sexual Assault Prevention Courses Completed in 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Sexual Assault Prevention Courses Completed in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                {"title": "Sexual Assault Prevention Courses Completed in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Sexual Assault Prevention Courses Completed in 2023"}]),
                    ]),
                )
            ])
        fig.update_layout(title_text="Sexual Assault Prevention Courses Completed in 2021-2023",showlegend =False)  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        st.plotly_chart(fig, use_container_width=True)
    
    def SABar():
        data2 = VisCourses.load_data2(1000)
        data2.sort_values(by = 'Month')
        data = data2.drop(data2[data2['SA_course'] == False].index, inplace=True)
        data = data2.groupby(['Month','SA_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        # print(data)
        plot = px.bar(data, x='Month',  y='count', color='SA_course', hover_data=['count'], labels='SA_course',title = 'Sexual Assault Prevenetion Courses in 2022')
        plot.update_traces(texttemplate="%{y}")
        plot.update_layout(showlegend = False)
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)
    
    def DVLine():
        df1 = VisCourses.load_data1(1000)
        df2 = VisCourses.load_data2(1000)
        df3 = VisCourses.load_data3(1000)
        df1.drop(df1[df1['DV_course'] == False].index, inplace=True)
        df1 = df1.groupby(['date','DV_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df2.drop(df2[df2['DV_course'] == False].index, inplace=True)
        df2 = df2.groupby(['date','DV_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        df3.drop(df3[df3['DV_course'] == False].index, inplace=True)
        df3 = df3.groupby(['date','DV_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()

        fig = go.Figure()

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df1.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "DV_course")
        fig.update_xaxes(title_text="DV_course")
        fig.update_yaxes(title_text="Count")

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "DV_course")
        fig.update_xaxes(title_text="DV_course")
        fig.update_yaxes(title_text="Count")

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=True))
        fig.update_layout(legend_title_text = "Domestic Violence Prevention")
        fig.update_xaxes(title_text="Domestic Violence  Prevention")
        fig.update_yaxes(title_text="Count")

        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    showactive=True,
                    font = dict({"color":"black", "size":14}),
                    buttons=list([
                        dict(label="2021-2023",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                {"title": "Domestic Violence Prevention Courses Completed in 2021-2023"}]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                {"title": "Domestic Violence Prevention Courses Completed in 2021"}]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                {"title": "Domestic Violence Prevention Courses Completed in 2022"}]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                {"title": "Domestic Violence Prevention Courses Completed in 2023"}]),
                    ]),
                )
            ])
        fig.update_layout(title_text="Domestic Violence Prevention Courses Completed in 2021-2023",showlegend =False)  
        fig.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        st.plotly_chart(fig)
    
    def DVBar():
        data2 = VisCourses.load_data2(1000)
        data2.sort_values(by = 'Month')
        data = data2.drop(data2[data2['DV_course'] == False].index, inplace=True)
        data = data2.groupby(['Month','DV_course']).apply(len).reindex(fill_value=0).to_frame('count').reset_index()
        # print(data)
        plot = px.bar(data, x='Month',  y='count', color='DV_course', hover_data=['count'], labels='DV_course',title = 'Domestic Violence Prevention Courses in 2022')
        plot.update_traces(texttemplate="%{y}")
        plot.update_layout(showlegend = False)
        plot.update_layout({'plot_bgcolor': 'rgba(0,0,0,0)','paper_bgcolor': 'rgba(0,0,0,0)'})
        return st.plotly_chart(plot, use_container_width=True)

    
def getGraphs():
        VisCourses.DVLine()
        VisCourses.DVBar()
        VisCourses.SALine()
        VisCourses.SABar()
        VisCourses.angerLine()
        VisCourses.angerBar()
        VisCourses.alcLine()
        VisCourses.alcBar()
        VisCourses.stressLine()
        VisCourses.stressBar()
        
      
            

if __name__=='__main__':
    st.title("Counseling Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()