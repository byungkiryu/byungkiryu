# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:29:43 2025

@author: cta4r
"""



import streamlit as st



def show_BRCV():
    
    st.header("About Byungki Ryu")
    
    # Header
    # st.title(":blue[Curriculum  Vitae]")
    st.title(":blue[CV]")
    st.header(":blue[Byungki Ryu (류병기)]")
    st.markdown("""
    **Principal Researcher**  
    Energy Conversion Research Center  
    Electrical Materials Division  
    Korea Electrotechnology Research Institute (KERI)  
    Changwon-si, 51543, South Korea  
    Email: byungkiryu@keri.re.kr | Phone: +82-55-280-1657 | [LinkedIn](https://linkedin.com/in/byungki-ryu-9896a222)
    """)
    
    st.markdown("""
    **Professor**  
    Electric Energy and Materials Engineering (KERI School)   
    University of Science and Technology (UST)
    Changwon-si, 51543, South Korea 
    """)
    
    st.markdown("---")
    
    # Professional Summary
    st.header(":blue[Professional Summary]")
    st.write("""
    Innovative transdiciplinary researcher over **thermoelectrics**, **device physics**, and **materials design**.    
    Expert in 1st-principles calculations, thermoelectric device efficiency, defects and interfaces in solids.  
    Published 90+ peer-reviewed papers.
    """)
    
    st.markdown("---")
    
    # Education
    st.header(":blue[Education]")
    st.markdown("""
    - **Ph.D. in Physics**  
      Korea Advanced Institute of Science and Technology (KAIST) | 2005.3-2011.2  
      *Thesis*: First-principles study of the atomic and electronic structures of semiconductor/insulator interfaces and transparent amorphous oxide semiconductors
    
    
    - **B.S. in Physics and Mathematics** (Double Major)  
      KAIST | 2000.3-2005.2
    """)
    
    st.markdown("---")
    
    # Professional Experience
    st.header(":blue[Professional Experience]")
    
    st.subheader("Principal Researcher")  
    st.write("*Korea Electrotechnology Research Institute (KERI)* | 2013.12.–Present")
    st.write("""
    - Have conducted advanced research on :red[**thermoelectric materials & devices**].  
    - Have conducted large-scale interface modelling for :red[**alloys & interfaces**].
    - Have investigated intrinsic, extrinsic, and complexes :red[**defects in thermoelectric materials**].
    - Have investigated :red[**thermoelectric metastable structure**].
    - Have investigated :red[**thermoelectric instability & device physics**] in thermoelectric modules.
    - Developed :red[**thermoelectcric algebraic framework**] within const-Seebeck approx.
    - Proposed :red[**three thermoelectric degrees of freedom**] for thermoelectric conversion efficiency.
    - Developed thermoelectric device simulator :red[***pykeri 2019***] (core developer: Dr. Jaywan Chung).  
    - Have developed machine learning model representation for thermoelectric property curves :red[***LaNN***] (core developer: Dr. Jaywan Chung).  
    - Have supervised postdoctoral researchers and led thermoelectric design projects.
    """)
    
    st.subheader("Research Staff Member")  
    st.write("*Samsung Advanced Institute of Technology (SAIT), South Korea* | 2011.3.–2013.12.")
    st.write("""
    - Materials design for thermoelectrics, H2/CO2 membranes, phosphor for LEDs, transparent electrodes
    """)
    
    st.markdown("---")
    
    # Publications
    st.header("Publications (Selected)")
    
    st.markdown("""
    1. **"Best thermoelectric efficiency of ever-explored materials"**  
       *iScience*, 2023.   
       [DOI] https://doi.org/10.1016/j.isci.2023.106494
    
    2. **"Thermoelectric degrees of freedom determining thermoelectric efficiency"**  
       *iScience*, 2021.   
       [DOI] https://doi.org/10.1016/j.isci.2021.102934
    
    3. **"High-Performance Thermoelectric Devices Made Faster: Interface Design from First Principles Calculations"**  
       *Advanced Physics Research*, 2024.  
       [DOI] https://doi.org/10.1002/apxr.202300077
    
    For a full list of publications, visit [Google Scholar](https://scholar.google.com/citations?user=fldxgiEAAAAJ).
    """)
    
    st.markdown("---")
    
    # Awards and Honors
    st.header("Awards and Honors")
    st.markdown("""
    - **한국물리학회 논문상** | 2022.10.  
    - **한국계산과학공학회 우수논문상** | 2022.9.   
    - **한국전기연구원 표창장 최우수상(개인)** | 2022.6.
    - **한국과학기술이사회 이사장 포상 표창장** | 2020.10.
    - **Appl. Phys. Lett. Featured Article** | 2020.5.13.
    - **제27회 한국과학기술단체총연합회 과학기술우수논문상** | 2017.7.7.
    - **KERI 대상 우수상(팀)** | 2017.1.2.
    - **한국물리학회 가을추계 우수발표상** | 2016.10.22.
    - **한국세라믹학회 우수논문상** | 2016.7.25.
    - **삼성논문상 금상** | 2012.11.
    - **4th BK21 Young Physicists Workshop 우수논문상** | 2011.1.
    - **Phys. Rev. B Kaleidoscope of June** | 2007.6. 
    """)
    
    st.markdown("---")
    
    # Skills
    st.header("Skills")
    st.markdown("""
    - **Technical Expertise**: Thermoelectric transport, DFT simulations, numerical modeling  
    - **Software**: VASP, Python, Excel, COMSOL Multiphysics, m3gnet, SevenNet  
    - **Languages**: Korean (native), English (professional working proficiency)
    """)
    
    # st.markdown("---")
    # st.markdown("# :blue[Curriculum Vitae (CV)]")
    # st.markdown("## :blue[Dr. Byungki Ryu]")
    # st.markdown("### :blue[Principal Researher ]")
    # st.markdown("Principal Researher")
    # st.markdown("Energy Conversion Research Center")
    # st.markdown("Electrical Materials Division")

    # st.header("Curriculum Vitae (CV)")
    
    # # 레벨 1
    # st.header("Personal Information")
    
    # # 레벨 2
    # st.subheader("Name")
    # st.write("Byungki Ryu")
    
    # # 레벨 3
    # st.markdown("### Contact Information")
    # st.write("Email: example@example.com")
    # st.write("Phone: +82-10-1234-5678")
    
    # # 레벨 4
    # st.markdown("#### Address")
    # st.write("123 Science Street, Research City, Korea")
    
    # 다른 섹션도 동일한 방식으로 작성 가능
# with tab3:  
#     st.subheader(":red[Select TE Mat. DB]")
#     # show_tab3(st)