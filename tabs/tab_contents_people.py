# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:29:43 2025

@author: cta4r
"""


import os
import streamlit as st
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(HERE, "ZDATA__people.xlsx")

def show_team_old():    
    # st.header(":blue[Byungki Ryu, Dr.]")
    df_team = pd.read_excel(EXCEL_PATH, sheet_name="people")
    df_team.drop(["id","status"],axis=1,inplace=True)
    st.dataframe(df_team)


def show_team():
    
    df_team = pd.read_excel(EXCEL_PATH, sheet_name="people")
        
    # status_list = ['current','alumni','visitors']
    # status_list = df_team.status.unique().tolist()
    
    # for status in status_list:
    #     df_sub_team = df_team[ df_team.status == status]
    #     show_sub_team(df_sub_team,status)
    
    status = "Members"
    df_sub_team = df_team[ df_team.status == status]
    show_Members(df_sub_team,status)

    status = "Alumni"
    df_sub_team = df_team[ df_team.status == status]
    show_Alumni(df_sub_team,status)    

    status = "Visitors"
    df_sub_team = df_team[ df_team.status == status]
    show_Visitors(df_sub_team,status) 
    

def show_Members(df_sub_team,status):    
    # st.header("{}".format(status))
    for index, rho_person_info in df_sub_team.iterrows():
        # show_person(rho_person_info)
        # print(rho_person_info)
        rho = rho_person_info
       
        name   = rho['name']
        title  = rho['title']
        brief  = rho['brief']   
        
        st.subheader(":blue[{} ({})]".format(name,title))
        
        if pd.notna(brief) and str(brief).strip():
                st.markdown(f"{brief}")
    return rho_person_info


def show_Alumni(df_sub_team,status):    
    st.header("{}".format(status))
    for index, rho_person_info in df_sub_team.iterrows():
        # show_person(rho_person_info)
        # print(rho_person_info)
        rho = rho_person_info
       
        name   = rho['name']
        title  = rho['title']
        brief  = rho['brief']   
        where_now = rho['where_now']
        period = rho['period']
          
        
        st.subheader(":blue[{} ({})]".format(name,title))
        
        if pd.notna(brief) and str(brief).strip():
                st.markdown(f"{brief}")
                st.markdown(f"Current affiliation: {where_now}")
                st.markdown(f"Period: {period}")
    return rho_person_info


def show_Visitors(df_sub_team,status):    
    st.header("{} (long stay)".format(status))
    for index, rho_person_info in df_sub_team.iterrows():
        # show_person(rho_person_info)
        # print(rho_person_info)
        rho = rho_person_info
       
        name   = rho['name']
        title  = rho['title']
        brief  = rho['brief']   
        where_now = rho['where_now']
        period = rho['period']
        
        st.subheader(":blue[{} ({})]".format(name,title))
        
        if pd.notna(brief) and str(brief).strip():
                st.markdown(f"{brief}")
                st.markdown(f"Affiliation: {where_now}")
                st.markdown(f"Stay: {period}")
    return rho_person_info

    

if __name__=="__main__":
    df_team = pd.read_excel(EXCEL_PATH, sheet_name="people")
    print(df_team)
