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
EXCEL_PATH = os.path.join(HERE, "ZDATA__publications.xlsx")


# def print_df_pubs(df_pubs):
    
#     for index, row in df_pubs.iterrows():
#         year = row['Publication Year']
#         printtemp = "[{}] year={}".format(index+1,year)
        
#         st.markdown(printtemp)

def show_publications_by_years():
    
    st.header("📚 Publications – Articles, Theses & Data")
    
    df_publications = pd.read_excel(EXCEL_PATH, sheet_name="read")    
    
    df_publications['Date'] = pd.to_datetime( df_publications['Date'])
    latest_date = df_publications['Date'].max().strftime("%Y-%b-%d")
    st.markdown(":grey[*publications as of {}, including journal articles, proceedings, datasets, theses*]".format(latest_date))  
    
    years_list = df_publications['Publication Year'].unique()
    
    
    for year in years_list:
    # year = 2022
        show_publications_year(df_publications, year)
        if (year != years_list[-1]):
            st.markdown("---")
   
    return df_publications


def show_publications_year(df_publications, year):
    # df_publications = pd.read_excel("./tabs/ZDATA__publications.xlsx", sheet_name="read")

    
    

    
    cols = ['Item Type', 'Publication Year', 'Author', 'Title',
           'Publication Title', 
           'ISBN', 'ISSN', 'Date',
           'DOI', 'Url', 'Pages',
           'Num Pages', 'Issue', 'Volume', 'Number Of Volumes',
           'Journal Abbreviation', 'Short Title', 'Series', 'Series Number',
           'Series Text', 'Series Title', 'Publisher', 'Place', 'Language',
           'Rights', 'Type', 'Archive', 'Archive Location', 'Library Catalog',
           'main','CA','FA','valCA'
           ]
    
    df_pubs = df_publications[ cols ]
    df_pubs =     df_pubs[ df_pubs['Publication Year'] == year]
    num_pubs = len(df_publications)
    num_pubs_year = len(df_pubs)
    
    # printtemp = "{}   ({} pubs)".format(
    #                                     year,
    #                                     num_pubs_year
    #                                     )
    st.subheader(year)
    st.text("({} publications)".format(num_pubs_year))

    for index, row in df_pubs.iterrows():
        paperindex = num_pubs-index
        itemType = row['Item Type']
        year = row['Publication Year']
        pub = row['Publication Title']
        doi = row['DOI']
        date = row['Date'].strftime('%Y-%b-%d')
        volume = row['Volume']
        if (volume > 0):
            volume = int(volume)
        # elif (volume == 0)
        pages = row['Pages']
        
        author = row.Author
        title = row.Title
        # main  = row.main
        valCA = row.valCA
        valFA = row.FA

        if (valFA == 1):
            author = author + "  \n :grey[-- first authored work]"
        if (valCA == 1):
            author = author + "  \n :grey[-- corresponding-authored work]"
        elif (valCA >0):
            author = author + "  \n :grey[-- co-corresponding authored work]"


        author = author + "     \n :grey[-- Publihsed on {}]".format(date)
            
        if (itemType == 'journalArticle') :
            printtemp = ":blue[[{}]    **{}**]  \n:red[*{}*]  **{}**, {} ({}).   \n Authors: {}   \n https://doi.org/{}".format(
                                                                       paperindex,
                                                                       title, pub, volume, pages, year,
                                                                       author, doi)
        elif (itemType == 'thesis'):
            printtemp = ":blue[[{}]    **{}**]  \n:red[*KAIST, Ph.D. Thesis*] ({}).   \n Authors: {}".format(
                                                                       paperindex,
                                                                       title, year,
                                                                       author)  
        else:
            printtemp = ":blue[[{}]    **{}**]  \n:red[Type: {}] ({}).   \n Authors: {}   \n https://doi.org/{}".format(
                                                                       paperindex,
                                                                       title, itemType, year,
                                                                       author, doi)
        print(printtemp)
        st.markdown(printtemp)
        
    # df_publications = df_publications[ df_publications['Item Type'] == 'journalArticle']
    
    # df_pubs.sort_values(by="Date")
    
    
    # df_publications.drop(["id","status"],axis=1,inplace=True)
    # st.dataframe(df_team)
    
    return df_pubs



# def show_publications(df_publications):
#     # df_publications = pd.read_excel("./tabs/ZDATA__publications.xlsx", sheet_name="read")
#     # st.header(":blue[Byungki Ryu, Dr.]")
#     # cols = ['Publication','Title']
    
#     df_publications['Date'] = pd.to_datetime( df_publications['Date'])
#     latest_date = df_publications['Date'].max().strftime("%Y-%m-%d")
#     st.markdown(":grey[*publications as of {}, including journal articles, proceedings, data, thesis*]".format(latest_date))  
    
#     cols = ['Item Type', 'Publication Year', 'Author', 'Title',
#            'Publication Title', 
#            'ISBN', 'ISSN', 'Date',
#            'DOI', 'Url', 'Pages',
#            'Num Pages', 'Issue', 'Volume', 'Number Of Volumes',
#            'Journal Abbreviation', 'Short Title', 'Series', 'Series Number',
#            'Series Text', 'Series Title', 'Publisher', 'Place', 'Language',
#            'Rights', 'Type', 'Archive', 'Archive Location', 'Library Catalog',
#            ]
    
#     df_pubs = df_publications[ cols ]
#     num_pubs = len(df_pubs)
        

#     for index, row in df_pubs.iterrows():
#         paperindex = num_pubs-index
#         itemType = row['Item Type']
#         year = row['Publication Year']
#         pub = row['Publication Title']
#         doi = row['DOI']
#         volume = row['Volume']
#         if (volume > 0):
#             volume = int(volume)
#         # elif (volume == 0)
        
#         author = row.Author
#         title = row.Title
        
#         if (itemType == 'journalArticle') :
#             printtemp = ":blue[[{}] **{}**]  \n:red[*{}*]  **{}** ({}).   \n Authors: {}   \n https://doi.org/{}".format(
#                                                                        paperindex,
#                                                                        title, pub, volume, year,
#                                                                        author, doi)
#         elif (itemType == 'thesis'):
#             printtemp = ":blue[[{}] **{}**]  \n:red[*KAIST, Ph.D. Thesis*] ({}).   \n Authors: {}".format(
#                                                                        paperindex,
#                                                                        title, year,
#                                                                        author)  
#         else:
#             printtemp = ":blue[[{}] **{}**]   \n:red[Type: {}] ({}).   \n Authors: {}   \n https://doi.org/{}".format(
#                                                                        paperindex,
#                                                                        title, itemType, year,
#                                                                        author, doi)
#         print(printtemp)
#         st.markdown(printtemp)
        
#     # df_publications = df_publications[ df_publications['Item Type'] == 'journalArticle']
    
#     # df_pubs.sort_values(by="Date")
    
    
#     # df_publications.drop(["id","status"],axis=1,inplace=True)
#     # st.dataframe(df_team)
    
#     return df_pubs

if __name__=="__main__":
    # df_publications = pd.read_excel("./ZDATA__publications.xlsx", sheet_name="read")
    # df_publications = pd.read_excel(EXCEL_PATH, sheet_name="read")    
    df_publications = show_publications_by_years()
    print( df_publications.columns)
