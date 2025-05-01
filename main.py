# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:29:43 2025

@author: cta4r
"""



import streamlit as st

import tabs.tab_contents_people as tab_contents_people
import tabs.tab_contents_res    as tab_contents_res
import tabs.tab_contents_pubs   as tab_contents_pubs
import tabs.tab_contents_acad   as tab_contents_acad
import tabs.tab_contents_news   as tab_contents_news
import tabs.tab_contents_BR     as tab_contents_BR
import tabs.tab_contents_DBSW   as tab_contents_DBSW



st.set_page_config(
    page_title="BR",
    page_icon="./images/B.png",  # 또는 URL/이미지 경로 사용 가능
    layout="centered"
)


col1, col2 = st.columns([1,5])
with col1:
    st.image("./images/B.png", width=100)
with col2:
    st.title("Byungki Ryu (BR)")
st.subheader(":blue[T]hermo-:blue[E]lectric :blue[S]cience (:blue[TES]) Group at KERI")


tab_res, tab_people, tab_pubs,   tab_acad, tab_news,   tab_about, tab_dbswhw = st.tabs([
                                                    "RESEARCH", 
                                                    "PEOPLE",        ##tab2
                                                    "PUBLICATIONS",  ## tab_pubs
                                                    "PRESENTATIONS",      ## tab_acad
                                                    "NEWS",  
                                                    "About",           ##tab7
                                                    "Data / SW / HW"      ##tab8
                                                    ])



with tab_res:
    tab_contents_res.show_vision()
    tab_contents_res.show_research_interest()
    
with tab_people:
    tab_contents_people.show_team()     

with tab_pubs:
    tab_contents_pubs.show_publications_by_years()

with tab_acad:
    tab_contents_acad.show_presentations_by_years()

with tab_news:
    tab_contents_news.show_recentnews()
    
with tab_about:
    tab_contents_BR.show_BRCV()
    
with tab_dbswhw:
    tab_contents_DBSW.show_link()

st.write("")
st.write("---")
st.caption("© 2025 Byungki Ryu. All rights reserved.")    
