# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:29:43 2025

@author: cta4r
"""


import os
import streamlit as st
import pandas as pd
import pydeck as pdk



HERE = os.path.dirname(os.path.abspath(__file__))
PATH_MAP_collabo = os.path.join(HERE, "ZDATA_map_collaborations.xlsx")
PATH_iMAP = os.path.join(HERE, "ZDATA_map_I_have_been.xlsx")


def show_where_I_have_been():
    st.subheader(":blue[Steps on]")
    df_imap = pd.read_excel(PATH_iMAP, sheet_name="read")
    df_imap.dropna(subset=["latitude","longitude"],inplace=True) 
    st.map(df_imap)
    

# def show_map():
#     st.header(":blue[ThermoElectric Science Group (TES) at KERI]")
#     # st.write("ThermoElectric Science Group at KERI, Korea")
#     df_map = pd.read_excel(EXCEL_PATH, sheet_name="read")
#     df_map_keri = df_map[0:1]
#     st.map(df_map_keri, zoom=12)
#     st.map(df_map)


def show_map_and_collaboration(seemap=False,seedf=True):
    st.subheader(":blue[TES at KERI] & :red[world-wide friends]")
    
    # (1) 점 데이터: 친구들 위치 점 표시
    df_map = pd.read_excel(PATH_MAP_collabo, sheet_name="read")
    df_map = df_map.where(pd.notnull(df_map), None)
    
    # (2) 현재 위치 (KERI 본원 위치로 예시)
    lat = 35.190
    lon = 128.718
    
    # (3) View 설정 (줌인할 위치)
    view_state = pdk.ViewState(
        latitude=  lat,
        longitude= lon,
        zoom=12,
        pitch=0
    )
    
    # (4) 전국 점들 레이어 (빨간 점)
    layer_all = pdk.Layer(
        "ScatterplotLayer",
        data=df_map[1:],
        get_position='[longitude, latitude]',
        get_radius='radius',
        radius_min_pixels=5,
        get_fill_color=[255, 0, 0, 80],
        pickable=True
    )  
    
    # (5) 현재 위치 레이어 (노란 큰 점)
    layer_current = pdk.Layer(
        "ScatterplotLayer",
        data=df_map[0:1],
        get_position='[longitude, latitude]',
        get_radius='radius',
        radius_min_pixels=5,
        get_fill_color=[0, 0, 255, 100],  # 파란색 강조
        pickable=True
    )
    
    # (6) 지도 렌더링
    if (seemap==True):
        st.pydeck_chart(pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=view_state,
            layers=[layer_all,  layer_current]
        ))
    if (seedf==True):
        with st.expander("See world-wide friends:", expanded=True):   
            st.dataframe(df_map)
        
        
if __name__=="__main__":
    df_maps = pd.read_excel( PATH_MAP_collabo , sheet_name="read")
    # print( "this is DB SW linker ")
    print(df_maps)
