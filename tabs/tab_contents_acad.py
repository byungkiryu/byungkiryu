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
    
    years_list = df_presentations['Publication Year'].unique()
    
    for year in years_list:
        row = show_presentations_years(df_presentations, year)
    
    return row



def show_presentations_years(df_presentations, year):

    
    df = df_presentations
    df =     df[ df['Publication Year'] == year]
    num_pubs = len(df_presentations)
    num_pubs_year = len(df)
    
    # printtemp = "{}   ({} pubs)".format(
    #                                     year,
    #                                     num_pubs_year
    #                                     )
    st.subheader(year)
    st.text("({} presentations)".format(num_pubs_year))

    for index, row in df.iterrows():
        paperindex = num_pubs-index
        itemType = row['Item Type']
        
        year = row['Publication Year']
        author = row.Author
        title = row.Title
        date = row.Date.strftime("%Y-%b-%d")
        place = row.Place
        presentationtype = row['Type']
        meetingname = row['Meeting Name']

        if (presentationtype == "Invited" and row.Author[0:6] == 'Ryu, B'):
            presentationtype = ":green[Invited Talk]"
        elif (presentationtype == "Invited" and row.Author[0:6] != 'Ryu, B'):
            presentationtype = "Invited Talk, Co-author"


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
    
    return row




if __name__=="__main__":
    
    row = show_presentations_by_years()
    print( row )
