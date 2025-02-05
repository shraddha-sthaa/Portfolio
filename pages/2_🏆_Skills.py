import streamlit as st
from sidebar import add_sidebar_message

# Set page configuration
st.set_page_config(
    page_title="Mallikarjun - Skills",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add the sidebar footer
add_sidebar_message()

st.markdown("## Skills")

# Programming
st.markdown("### Programming:")
st.markdown("""
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#) 
[![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)](#) 
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](#) 
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](#) 
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](#) 
[![Java](https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=java&logoColor=white)](#)<br>  
[![VS Code](https://img.shields.io/badge/Visual_Studio_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](#) 
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](#) 
[![Notebook](https://img.shields.io/badge/Notebook-FF9800?style=for-the-badge)](#)  
""", unsafe_allow_html=True)

# AI/ML Frameworks
st.markdown("### AI/ML Frameworks:")
st.markdown("""
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](#) 
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](#) 
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](#) 
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](#) 
[![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)](#)  
""", unsafe_allow_html=True)

# Databases
st.markdown("### Databases:")
st.markdown("""
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](#) 
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](#) 
[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](#)  
""", unsafe_allow_html=True)

# Visualization
st.markdown("### Visualization:")
st.markdown("""
[![Matplotlib](https://img.shields.io/badge/Matplotlib-0088CC?style=for-the-badge)](#) 
[![Seaborn](https://img.shields.io/badge/Seaborn-003262?style=for-the-badge)](#) 
[![Plotly](https://img.shields.io/badge/Plotly-1F77B4?style=for-the-badge&logo=plotly&logoColor=white)](#) 
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](#) 
[![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)](#) 
[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black)](#)  
""", unsafe_allow_html=True)

# Cloud Services
st.markdown("### Cloud Services:")
st.markdown("""
[![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)](#) 
[![GCP](https://img.shields.io/badge/GCP-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](#)  
""", unsafe_allow_html=True)

# GIS
st.markdown("### Geographic Information System (GIS):")
st.markdown("""
[![ESRI](https://img.shields.io/badge/ESRI-0076D6?style=for-the-badge)](#) 
[![ArcGIS](https://img.shields.io/badge/ArcGIS-1E4D2B?style=for-the-badge)](#)  
""", unsafe_allow_html=True)
