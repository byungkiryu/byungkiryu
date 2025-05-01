# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:29:43 2025

@author: cta4r
"""



import streamlit as st
import pandas as pd
import tabs.tab2_contents as tab2_contents
import tabs.tab_contents_res  as tab_contents_res
import tabs.tab_contents_pubs as tab_contents_pubs
import tabs.tab_contents_acad as tab_contents_acad
import tabs.tab_contents_BR as tab_contents_BR
import tabs.tab_contents_DBSW as tab_contents_DBSW
# from tabs.tab7_contents import show_tab7

st.set_page_config(page_title="TES@KERI")


st.title("Byungki Ryu (Scientist at KERI)")
st.subheader(":red[T]hermo-:red[E]lectric :red[S]cience Group")


tab_res, tab_team, tab_pubs,   tab_acad, tab5, tab6,   tab_BR, tab_DBSW = st.tabs([
                                                    "RESEARCH", 
                                                    "People",        ##tab2
                                                    "Publications",  ## tab_pubs
                                                    "Academic",      ## tab_acad
                                                    "Visitors",
                                                    "NEWS",  
                                                    "cvBR",           ##tab7
                                                    "Data-SW-HW"      ##tab8
                                                    ])         


with tab_res:
    tab_contents_res.show_vision()
    tab_contents_res.show_research_interest()
    
with tab_team:
    tab2_contents.show_team()

with tab_pubs:
    tab_contents_pubs.show_publications_by_years()

with tab_acad:
    tab_contents_acad.show_presentations_by_years()

with tab_BR:
    tab_contents_BR.show_BRCV()
    
with tab_DBSW:
    tab_contents_DBSW.show_link()
    
# with tab3:  
#     st.subheader(":red[Select TE Mat. DB]")
#     # show_tab3(st)