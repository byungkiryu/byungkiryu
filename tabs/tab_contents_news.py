# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:29:43 2025

@author: cta4r
"""


import os
import streamlit as st
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(HERE, "ZDATA__news.xlsx")




def show_recentnews():
    
    df_news_all = pd.read_excel(EXCEL_PATH, sheet_name="news_all")
    df_news_recent = df_news_all[ df_news_all["recentnews"] == 1]
    
    
    df_news_recent = df_news_recent.head(4)
    
    
    
    
    # status_list = ['current','alumni','visitors']
    # status_list = df_team.status.unique().tolist()
    
    # for status in status_list:
    #     df_sub_team = df_team[ df_team.status == status]
    #     show_sub_team(df_sub_team,status)
    st.header("📰 Research News")
    df = df_news_recent
    for _, row in df.sort_values("date", ascending=False).iterrows():
        
        news_title         = row['title']
        news_date          = row['date'].strftime('%Y-%b-%d')
        news_description   = row['description']
        news_link          = row['link']
        
        st.subheader(":blue[{}]".format(news_title ) )
        # st.markdown(":red[({})]".format(news_date ) )
        
        # if pd.notna(news_link):
        #     news_contents = news_description + "\n     [🔗 Related Link]({})".format(news_link)
        # else:
        #     news_contents = news_description
        
        st.markdown(":grey[({})] {}".format(news_date,news_description) )
        if pd.notna(news_link):
            st.markdown("[🔗 Related Link]({})".format(news_link) )
        st.markdown("---")
    



    

if __name__=="__main__":
    df_news_all = pd.read_excel(EXCEL_PATH, sheet_name="news_all")
    cols = ['recentnews',  'title', 'date']
    df_news__brief = df_news_all[ cols ]
    print(df_news__brief)
