import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime as dt
# anger_course,alcohol_course,stress_course,SA_course,DV_course
class VisCourses:
       
    @st.cache_data(ttl = dt.timedelta(hours=1))
    def load_data1(nrows):
        data1 = pd.read_csv('Data/MockData/MOCK_DATA.csv',nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df1 = pd.DataFrame(data1)
        # df1.info()
        df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d')
        return df1
    
    @st.cache_data(ttl = dt.timedelta(hours=1))
    def load_data2(nrows):
        data2 = pd.read_csv('Data/MockData/MOCK_DATA2.csv', nrows=nrows,parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df2 = pd.DataFrame(data2)
        # df2.info()
        df2['date'] = pd.to_datetime(df2['date'], format='YYYY-mm-dd')
        return df2
    
    @st.cache_data(ttl = dt.timedelta(hours=1))
    def load_data3(nrows):
        data3 = pd.read_csv('Data/MockData/MOCK_DATA3.csv', nrows=nrows, parse_dates=['date'])
        # df = set up the data in pandas Data Frame format
        df3 = pd.DataFrame(data3)
        # df3.info()
        df3['date'] = pd.to_datetime(df3['date'], format='%Y-%m-%d')
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
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2021"))
        
        

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2022"))
        

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2023"))
       

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
                                # {"title": "Anger Management Courses Completed in 2021-2023"}
                                ]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                # {"title": "Anger Management Courses Completed in 2021"}
                                ]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                # {"title": "Anger Management Courses Completed in 2022"}
                                ]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                # {"title": "Anger Management Courses Completed in 2023"}
                                ]),
                    ]),
                )
            ])
        fig.update_xaxes(title_text="No. of Airmen in Anger Management", showline = True, title_font=dict(size=16 , color = "black"), tickfont=dict(size=13,color = "black"))
        fig.update_yaxes(showline =True, tickfont=dict(size=16, color = "black"))
        fig.update_layout(title={
            'text': "Anger Management",
            'font': {'size': 20}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",showlegend = False,
        hoverlabel=dict(font=dict(size=16, color = "black")))
        st.plotly_chart(fig, use_container_width=True)

    
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
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2021"))
        
        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2022"))

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2023"))

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
                                # {"title": "Alcohol Awareness Courses Completed in 2021-2023"}
                                ]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                # {"title": "Alcohol Awareness Courses Completed in 2021"}
                                ]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                # {"title": "Alcohol Awareness Courses Completed in 2022"}
                                ]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                # {"title": "Alcohol Awareness Courses Completed in 2023"}
                                ]),
                    ]),
                )
            ])
        fig.update_xaxes(title_text="No. of Airmen in Alcohol Awareness", showline = True, title_font=dict(size=16 , color = "black"), tickfont=dict(size=13,color = "black"))
        fig.update_yaxes(showline =True, tickfont=dict(size=16, color = "black"))
        fig.update_layout(title={
            'text': "Alcohol Awareness",
            'font': {'size': 20}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",showlegend = False,
        hoverlabel=dict(font=dict(size=16, color = "black")))
        st.plotly_chart(fig,use_container_width=True)

    
 
    
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
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2021"))
        

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2022"))
        

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2023"))
        
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
                                # {"title": "Stress Management Courses Completed in 2021-2023"}
                                ]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                # {"title": "Stress Management Courses Completed in 2021"}
                                ]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                # {"title": "Stress Management Courses Completed in 2022"}
                                ]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                # {"title": "Stress Management Courses Completed in 2023"}
                                ]),
                    ]),
                )
            ])
        fig.update_xaxes(title_text="No. of Airmen in Stess Management", showline = True, title_font=dict(size=16 , color = "black"), tickfont=dict(size=13,color = "black"))
        fig.update_yaxes(showline =True, tickfont=dict(size=16, color = "black"))
        fig.update_layout(title={
            'text': "Stress Management",
            'font': {'size': 20}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",showlegend = False,
        hoverlabel=dict(font=dict(size=16, color = "black")))
        st.plotly_chart(fig, use_container_width=True)
    
    
    
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
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2021"))
      
        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2022"))
      

        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2023"))
     
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
                                # {"title": "Sexual Assault Prevention Courses Completed in 2021-2023"}
                                ]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                # {"title": "Sexual Assault Prevention Courses Completed in 2021"}
                                ]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                # {"title": "Sexual Assault Prevention Courses Completed in 2022"}
                                ]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                # {"title": "Sexual Assault Prevention Courses Completed in 2023"}
                                ]),
                    ]),
                )
            ])
        fig.update_xaxes(title_text="No. of Airmen in Sexual Assault Prevention ", showline = True, title_font=dict(size=16 , color = "black"), tickfont=dict(size=13,color = "black"))
        fig.update_yaxes(showline =True, tickfont=dict(size=16, color = "black"))
        fig.update_layout(title={
            'text': "Sexual Assault Prevention",
            'font': {'size': 20}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",showlegend = False,
        hoverlabel=dict(font=dict(size=16, color = "black")))
        st.plotly_chart(fig,use_container_width=True)
       
    
    
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
                
        fig.add_trace(go.Scatter(x=df1["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2021"))
        
        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df2.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df2["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2022"))


        yStuff = [0,0,0,0,0,0,0,0,0,0,0,0]
        for val in df3.values:
            yStuff[val[0].month - 1] += val[2]
                
        fig.add_trace(go.Scatter(x=df3["date"].dt.month_name().unique(), y=yStuff, name=True,hovertext="2023"))
     

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
                                # {"title": "Domestic Violence Prevention Courses Completed in 2021-2023"}
                                ]),
                        dict(label="2021",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                # {"title": "Domestic Violence Prevention Courses Completed in 2021"}
                                ]),
                        dict(label="2022",
                            method="update",
                            args=[{"visible": [False,True,False]},
                                # {"title": "Domestic Violence Prevention Courses Completed in 2022"}
                                ]),
                        dict(label="2023",
                            method="update",
                            args=[{"visible": [False,False,True]},
                                # {"title": "Domestic Violence Prevention Courses Completed in 2023"}
                                ]),
                    ]),
                )
            ])
        fig.update_xaxes(title_text="No. of Airmen in Domestic Violence Prevention", showline = True, title_font=dict(size=16 , color = "black"), tickfont=dict(size=13,color = "black"))
        fig.update_yaxes(showline =True, tickfont=dict(size=16, color = "black"))
        fig.update_layout(title={
            'text': "Domestic Violence Prevention",
            'font': {'size': 20}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="rgba(0,0,0,0)",showlegend = False,
        hoverlabel=dict(font=dict(size=16, color = "black")))
        st.plotly_chart(fig,use_container_width=True)
     
    

    
def getGraphs():
        VisCourses.DVLine()
        VisCourses.SALine()
        VisCourses.angerLine()
        VisCourses.alcLine()
        VisCourses.stressLine()
  
        
      
            

if __name__=='__main__':
    st.title("Counseling Reports")
    data_load_state = st.text('Loading data...')
    getGraphs()