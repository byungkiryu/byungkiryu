# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:29:43 2025

@author: cta4r
"""



import streamlit as st



def show_vision():
    st.header(":blue[Vision and Direction]")
    st.markdown("""
                We aim to understand fundamentals of  
                -- :red[thermelectric phenomena] from materials to energy-conversion application,  
                -- :red[thermolectric as numbers] via ab-initio, data, machine learning, and evaluation. 
                
                We aim to apply thermoelectric conversion to    
                -- :red[power generation, cooling and thermal management],   
                -- :red[thermal-information technology]
                
                We aim to develop   
                -- :red[high-efficiency thermoelectric materials] beyond ZT,  
                -- :red[thermoelectric power generator] modules and systems.  
                
                """)


def show_research_interest():

    st.header(":blue[Research Interest]")
    st.subheader("1. Thermoelectrics")
    st.markdown("""
                :red[thermelectric device and applications]   
                Thermoelectric material interface design based on solute chemical potentials.(\*)   
                Thermoelectric efficiency and invariance over temperature and geometry transformation.(\*)   
                Thermoelectric metrology for device and module power characteristics.   
                Chip hot spot and thermoelectric active cooling.  
                Thermoelectric life-time modelling.                   
                
                
                :red[thermelectric phenomena and transport]   
                First-principles Boltzmann transport calculations for electron and phonon.  
                Diffusion and Kim's Law.  
                Temperature quantization.   
                
                
                :red[thermelectric data and machine learning]   
                teMatDb: an ultra-high quality TE material property database and self-consistent ZT filter.(\*) [DB link](https://tematdbv114.streamlit.app/)                      
                LaNN: an artificial neural network model predicting thermoelectric property curves.   
                Online e.g. 
                [BiTe](https://jaywan-chung.github.io/ml-tep-BiTe/),
                [PbTe](https://jaywan-chung.github.io/ml-tep-PbTe/),
                [Cu alloys](https://jaywan-chung.github.io/ml-copper-poongsan/)   
                
                
                :red[thermelectric materials design]   
                Ag-induced chemical stacking faults and metastable BiSbTe thermoelectric alloys.(\*)   
                Lattice similarity for PGEC-like materials.(*)   
                Reference BiTe thermoelectric alloys: compositions, legs, TGMs.   
                Origin of incommensurate structure for higher-manganese silidies (HMSs).
                Order-disorder and high-power factor Bi-Te-Se thermoelectric alloys.   
                Fermi-surface anisotropy and material texture.  
                
                
                :red[thermelectric simulation and circuit]      
                Thermoelectric simulator. pykeri2019, [TES](https://tes.keri.re.kr/)   
                Finite-element method analsis for thermoelectric generator module (TGM).   
                Thermoelectric circuit.    
                
                
                :red[defect-rich thermoelectric materials]                 
                Defect-impurity clustering in thermoelectric materials.       
                
                
                
                """)

    st.subheader("2. Materials, Interfaces, and Alloys Design")
    st.markdown("""
                Modelling method for incommensurate structures.(\*)   
                Alloy single and clustered solute database. [DB link](https://byungkiryu-alloydesigndb-demo-v0-33-main-v0-33-u86ejf.streamlit.app/)      
                Graph MLP for solute/interface in Cu alloys.   
                Tilt and twisted grain boundaries (GBs) in Cu-Ni-Si-Mn alloys.   
                Orientation-independent interface energies.   
                
                
                """)

    # st.header(":blue[Research Interest]")
    # st.subheader("TE efficiency theory")
    # st.subheader("Nanoscale transport")
    # st.subheader("Metastable TE materials")
    # st.subheader("Defect clusters")
    # st.subheader("Alloys, interfaces, and machine learning potentials")
    # st.subheader("Device simulator")
    # st.subheader("Device physics & thermoelectric instability")
    # st.subheader("TE segmented legs")   
    # st.subheader("TE module fabrication")   
    # st.subheader("Power modules & generators")
    # st.subheader("Thermoelectric data")
    # st.subheader("Machine learning model for property curves")
    
    
    printtemp = ""
    return printtemp

if __name__=="__main__":
    
    
    printtemp = show_research_interest()
    print( printtemp )
