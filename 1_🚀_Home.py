import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Mallikarjun Aitha - Data Scientist",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar content
with st.sidebar:
    # Display profile picture
    #st.image('assets/img/profile-pic.png', width=150)  
    #st.title("Mallikarjun Aitha")
    
    # GitHub Icon, hyperlink
    st.markdown(
        '''
        <div style="display: flex; align-items: center;">
            <a href="https://github.com/mallikarjun25" target="_blank">
                <img src="https://www.svgrepo.com/show/369327/github.svg" width="24" height="24" style="margin-right: 10px;"/>
            </a>
            <a href="https://www.linkedin.com/in/mallikarjun-aitha/" target="_blank">
                <img src="https://www.svgrepo.com/show/452047/linkedin-1.svg" width="24" height="24"/>
            </a>
        </div>
        ''', unsafe_allow_html=True
    )

with st.container():
    col1, col2 = st.columns((2, 1), gap="medium")
    with col1:
        st.title("Hey there! 👋 I'm a Data Spider 🕷️")
        st.markdown("""
            **I'm Mallikarjun Aitha**, a passionate Data Scientist on a mission to transform raw data into powerful insights 
            that drive real-world impact! With a Master’s in Data Science from the University of New Haven and hands-on 
            expertise in Machine Learning, Spatial Data Science, and Advanced Analytics, I specialize in uncovering patterns, 
            optimizing decisions, and building predictive solutions that make a difference.
            """)
        
        st.markdown("""
            My journey spans working as a Software Engineer and Data Analyst Intern at American Express and a non-profit 
            organization, where I leveraged analytics to refine strategies, enhance offerings, and create data-driven solutions. 
            Whether it’s developing machine learning models, exploring spatial data with GIS, or automating workflows, 
            I thrive on solving complex challenges and delivering actionable intelligence.
            """)

        st.markdown("""
            But beyond the world of data, I’m a curious explorer with a love for traveling, cricket, and photography. 
            I believe that the best insights come from a mix of technical expertise, creativity, and storytelling—transforming 
            data into experiences that truly matter.
            """)

        st.markdown("""
            _In the world of data, with great algorithms comes great responsibility — but don’t worry, I’ve got your back! 🕷️✨_
            """)

        # Add the download button
        with open("assets/Mallikarjun_Aitha_Resume.pdf", "rb") as file:
            st.download_button(
                label="Download my resume",
                data=file,
                file_name="Mallikarjun_Aitha_Resume.pdf",
                mime="application/pdf"
            )

    with col2:
        st.markdown('<div class="profile-img">', unsafe_allow_html=True)
        st.image('./assets/img/profile-pic.png', width=200)
        st.markdown('</div>', unsafe_allow_html=True)