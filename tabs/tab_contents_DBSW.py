# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:29:43 2025

@author: cta4r
"""


import os
import streamlit as st
import pandas as pd
import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(HERE, "ZDATA__link_for_DBSW.xlsx")

def show_link():
    df_link = pd.read_excel( EXCEL_PATH , sheet_name="read")
    contenttype_list = df_link.contenttype.unique().tolist()
    
    for contenttype in contenttype_list:
        # contenttype = 'DB'
        show_link_each(df_link, contenttype)
    

def show_link_each(df_link, contenttype):
    
    df = df_link[ df_link.contenttype == contenttype ]
    st.header("{}".format(contenttype) )

    for index, row in df.iterrows():
        
        # contenttype = row.type
        name = row['name'] 
        content = row.content 
        link = row.link
        
        
        
        st.subheader(":blue[{}]".format(name) )  
        st.write("""
                 Content: {}       
                 Link:  {}   
                 """.format(content,link)
                 )

    

if __name__=="__main__":
    df_link = pd.rea_excel( "./tab/ZDATA__link_for_DBSW.xlsx" , sheet_name="read")
    print( "this is DB SW linker ")
    print(df_link)
