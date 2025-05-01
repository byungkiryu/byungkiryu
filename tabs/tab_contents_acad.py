# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:29:43 2025

@author: cta4r
"""


import os
import streamlit as st
import pandas as pd
# import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(HERE, "ZDATA__presentations.xlsx")


def show_presentations_by_years():
    
    st.header("🎓 Research Presentations")
    
    df_presentations = pd.read_excel(EXCEL_PATH, sheet_name="read")    
    
    df_presentations['Date'] = pd.to_datetime( df_presentations['Date'])
    # latest_date = df_publications['Date'].max().strftime("%Y-%m-%d")
    # st.markdown(":grey[*publications as of {}, including journal articles, proceedings, data, thesis*]".format(latest_date))  
    
    years_list = df_presentations['Publication Year'].unique()
    
    for year in years_list:
    # year = 2022
        show_presentations_years(df_presentations, year)
    pass
    


def show_presentations_years(df_presentations, year):

    
    df_pubs = df_presentations
    df_pubs =     df_pubs[ df_pubs['Publication Year'] == year]
    num_pubs = len(df_presentations)
    num_pubs_year = len(df_pubs)
    
    # printtemp = "{}   ({} pubs)".format(
    #                                     year,
    #                                     num_pubs_year
    #                                     )
    st.subheader(year)
    st.text("({} presentations)".format(num_pubs_year))

    for index, row in df_pubs.iterrows():
        paperindex = num_pubs-index
        itemType = row['Item Type']
        
        year = row['Publication Year']
        author = row.Author
        title = row.Title
        date = row.Date.strftime("%Y-%m-%d")
        place = row.Place
        presentationtype = row['Type']
        meetingname = row['Meeting Name']


        printtemp="hello"
        if (itemType == 'presentation') :
            printtemp = ":blue[[{}] **{}**]  \n:red[*{}*],  **{}**, on {} ({}).   \n Authors: {}  \nPresentation Type: {} ".format(
                                                                       paperindex,
                                                                       title,
                                                                       meetingname,
                                                                       place,
                                                                       date,
                                                                       year,
                                                                       author     ,                                                                  
                                                                       presentationtype,)

            
        # print(printtemp)
        st.markdown(printtemp)
    
    return df_pubs



# def show_presentations(df_presentations):
#     # df_publications = pd.read_excel("./tabs/ZDATA__presentations.xlsx", sheet_name="read")
#     # st.header(":blue[Byungki Ryu, Dr.]")
#     # cols = ['Publication','Title']
    
#     df_presentations['Date'] = pd.to_datetime( df_presentations['Date'])
#     latest_date = df_presentations['Date'].max().strftime("%Y-%m-%d")
#     st.markdown(":grey[*publications as of {}, including journal articles, proceedings, data, thesis*]".format(latest_date))  
    
#     cols = ['Key', 'Item Type', 'Publication Year', 'Author', 'Title',
#            'Publication Title', 
#            'Date', 
#            'Place','Meeting Name',
#            'Type', 
#            ]
    
#     df_pubs = df_presentations[ cols ]
#     # df_pubs = df_publications
#     num_pubs = len(df_pubs)
        

#     for index, row in df_pubs.iterrows():
#         paperindex = num_pubs-index
#         itemType = row['Item Type']
        
#         year = row['Publication Year']
#         author = row.Author
#         title = row.Title
#         date = row.Date.strftime("%Y-%m-%d")
#         place = row.Place
#         presentationtype = row['Type']
#         meetingname = row['Meeting Name']


#         printtemp="hello"
#         if (itemType == 'presentation') :
#             printtemp = ":blue[[{}] **{}**]  \n:red[*{}*],  **{}**, on {} ({}).   \n Authors: {}  \nPresentation Type: {} ".format(
#                                                                        paperindex,
#                                                                        title,
#                                                                        meetingname,
#                                                                        place,
#                                                                        date,
#                                                                        year,
#                                                                        author     ,                                                                  
#                                                                        presentationtype,)

            
#         print(printtemp)
#         st.markdown(printtemp)
        

    
#     return df_pubs

if __name__=="__main__":
    df_presentations = pd.read_excel("./ZDATA__presentations.xlsx", sheet_name="read")
    df_pubs = show_presentations(df_presentations)
    print( df_pubs.columns)
