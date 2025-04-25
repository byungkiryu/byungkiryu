# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:29:43 2025

@author: cta4r
"""



import streamlit as st
import pandas as pd
import numpy as np




def show_link():
    df_link = pd.read_excel( "./tabs/ZDATA__link_for_DBSW.xlsx" , sheet_name="read")
    
    
    contenttype_list = df_link.contenttype.unique().tolist()
    
    for contenttype in contenttype_list:
        # contenttype = 'DB'
        show_link_each(df_link, contenttype)
    

def show_link_each(df_link, contenttype):
    
    df = df_link[ df_link.contenttype == contenttype ]
    st.header(":blue[{}]".format(contenttype) )

    for index, row in df.iterrows():
        
        # contenttype = row.type
        name = row['name'] 
        content = row.content 
        link = row.link
        
        
    #     st.header(":blue[Professional Experience]")
        
        st.subheader("{}".format(name) )  
        st.write("""
                 Content: {}       
                 Link:  {}   
                 """.format(content,link)
                 )
    #     st.write("*Korea Electrotechnology Research Institute (KERI)* | 2013.12.–Present")
    #     st.write("""
    #     - Have conducted advanced research on :red[**thermoelectric materials & devices**].  
    #     - Have conducted large-scale interface modelling for :red[**alloys & interfaces**].
    #     - Have investigated intrinsic, extrinsic, and complexes :red[**defects in thermoelectric materials**].
    #     - Have investigated :red[**thermoelectric metastable structure**].
    #     - Have investigated :red[**thermoelectric instability & device physics**] in thermoelectric modules.
    #     - Developed :red[**thermoelectcric algebraic framework**] within const-Seebeck approx.
    #     - Proposed :red[**three thermoelectric degrees of freedom**] for thermoelectric conversion efficiency.
    #     - Developed thermoelectric device simulator :red[***pykeri 2019***].  
    #     - Have supervised postdoctoral researchers and led thermoelectric design projects.
    # #     """)
        
        
    #     if (itemType == 'journalArticle') :
    #         printtemp = ":blue[[{}] **{}**]  \n:red[*{}*]  **{}** ({}).   \n Authors: {}   \n https://doi.org/{}".format(
    #                                                                    paperindex,
    #                                                                    title, pub, volume, year,
    #                                                                    author, doi)
    #     elif (itemType == 'thesis'):
    #         printtemp = ":blue[[{}] **{}**]  \n:red[*KAIST, Ph.D. Thesis*] ({}).   \n Authors: {}".format(
    #                                                                    paperindex,
    #                                                                    title, year,
    #                                                                    author)  
    #     else:
    #         printtemp = ":blue[[{}] **{}**]   \n:red[Type: {}] ({}).   \n Authors: {}   \n https://doi.org/{}".format(
    #                                                                    paperindex,
    #                                                                    title, itemType, year,
    #                                                                    author, doi)
    #     print(printtemp)
    #     st.markdown(printtemp)
        
    # # df_publications = df_publications[ df_publications['Item Type'] == 'journalArticle']
    
    # # df_pubs.sort_values(by="Date")
    
    
    # # df_publications.drop(["id","status"],axis=1,inplace=True)
    # st.dataframe(df_team)
    
    

if __name__=="__main__":
    df_link = pd.rea_excel( "./tab/ZDATA__link_for_DBSW.xlsx" , sheet_name="read")
    print( "this is DB SW linker ")
    print(df_link)
