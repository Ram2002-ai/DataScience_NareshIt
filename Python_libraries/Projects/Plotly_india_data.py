import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df=pd.read_csv(r"E:\data\data_set\india.csv")

st.dataframe(df)

list_of_states=list(df['State'].unique())
list_of_states.insert(0,'Overall India')

# sidebar
st.sidebar.title('India Data Visualization')

selected_state=st.sidebar.selectbox('Select a state',list_of_states)

primary=st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))

secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[:5]))

# graphs
plot=st.sidebar.button('Plot Graph')

if plot:

    st.subheader('Size represent primary parameter')
    st.subheader('Color represents secondary parameter')

    if selected_state=='Overall India':
        # plot for india

        fig=px.scatter_map(df,lat='Latitude',lon='Longitude',size=primary,color=secondary,zoom=4,size_max=35,
                             map_style="carto-darkmatter" ,width=1200,height=700,hover_name='District',center={"lat": 22.5, "lon": 79.0})
        
        st.plotly_chart(fig,use_container_width=True)

    else:
        # plot for state
        state_df=df[df['State']==selected_state]

        fig=px.scatter_map(state_df,lat='Latitude',lon='Longitude',size=primary,color=secondary,zoom=6,size_max=35,
                           map_style="carto-darkmatter",width=1200,height=700,hover_name='District')
        
        st.plotly_chart(fig,use_container_width=True)



  





state_df = df[df["State"] == selected_state]

if state_df.empty:
    if selected_state=='Overall India':
        # plot for india

        fig=px.density_map(df,lat='Latitude',lon='Longitude',z=primary,radius=25,zoom=4,
                             map_style="carto-darkmatter" ,width=1200,height=700,hover_name='District',center={"lat": 22.5, "lon": 79.0})
        
        st.plotly_chart(fig,use_container_width=True)

else:
    fig = px.density_map(
        state_df,
        lat="Latitude",
        lon="Longitude",
        z=primary,                # e.g. "Confirmed"
        radius=25,                # adjust for smoothing
        hover_name="District",
        map_style="carto-darkmatter",
        zoom=6,
        width=1200,
        height=700
    )

    st.plotly_chart(fig, use_container_width=True, key="india_overall_map")



state_df = df[df["State"] == selected_state]

if state_df.empty:
    
        fig=px.density_map(df,lat='Latitude',lon='Longitude',z=primary,radius=25,zoom=4,
                             map_style="carto-darkmatter" ,width=1200,height=700,hover_name='District',center={"lat": 22.5, "lon": 79.0})
        
        st.plotly_chart(fig,use_container_width=True,key='india')

else:
    fig = px.density_map(
        state_df,
        lat="Latitude",
        lon="Longitude",
        z=primary,                # e.g. "Confirmed"
        radius=25,                # adjust for smoothing
        hover_name="District",
        map_style="carto-darkmatter",
        zoom=6,
        width=1200,
        height=700
    )

    st.plotly_chart(fig, use_container_width=True)


