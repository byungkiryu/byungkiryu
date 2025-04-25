# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:29:43 2025

@author: cta4r
"""



import streamlit as st
import pandas as pd


def show_team():
    
    # st.header(":blue[Byungki Ryu, Dr.]")
    df_team = pd.read_excel("./tabs/ZDATA__tes_at_keri_team.xlsx", sheet_name="people")
    df_team.drop(["id","status"],axis=1,inplace=True)
    st.dataframe(df_team)