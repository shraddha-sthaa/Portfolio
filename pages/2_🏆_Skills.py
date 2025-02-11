import streamlit as st
from sidebar import add_sidebar_message

# Set page configuration
st.set_page_config(
    page_title="Shraddha - Skills",
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
[![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white)](#)  
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
""", unsafe_allow_html=True)

