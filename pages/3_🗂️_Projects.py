import streamlit as st
from PIL import Image
from sidebar import add_sidebar_message
from sidebar import add_sidebar_message

# Set page configuration
st.set_page_config(page_title='Shraddha - Projects', layout="wide", page_icon="❄")

# Add the sidebar footer
add_sidebar_message()

# Add the sidebar footer
add_sidebar_message()

# Page title
st.title('Projects')

# Project: InceptFace
with st.container():
  col9, col10 = st.columns((1, 2))
  with col9:
    st.image(Image.open('./assets/img/DeepLearning.png'))  # Project image
  with col10:
    st.subheader("InceptFace")
    st.write("""
This project implements a facial recognition system using InceptionResNetV1 and a custom dataset, with MTCNN for face detection and a robust preprocessing pipeline. The model is trained with Adam optimizer and Cross Entropy Loss for multi-class classification.""")
    st.markdown('`facenet-PyTorch`, `InceptionResNetV1`, `Python`, `Deep Learning`, `Facial Recognition`, `Multi-class Classification`')
    st.markdown('[GitHub](https://github.com/shraddha-sthaa/Deep-Learning-Project.git)')
st.write('---')

# Project: Trading Strategy Planner
with st.container():
  col1, col2 = st.columns((1, 2))
  with col1:
    st.image(Image.open('./assets/img/DSDE.png'))  # Project image
  with col2:
    st.subheader("Trading Strategy Planner")
    st.write("""
    Developed an automated data processing pipeline for ABC Hedge Fund, utilizing Yahoo Finance API over million records from S&P 1000 and S&P 500 indices. Leveraged AWS Glue, Lambda, SQS Queue, and S3 storage for efficient data processing. Conducted feature engineering and integrated with Redshift database for advanced analytics and ML model training
    """)
    st.markdown('`Amazon Web Services (AWS)`, `Apache Spark`, `Apache Kafka`, `Data Analysis`, `Python`, `Microsoft Power BI`, `Machine Learning`, `pandas`, `ETL`')
    st.markdown('[GitHub](https://github.com/mallikarjun25/Data-Engineering-for-Smart-City-Monitoring)')

st.write('---')

# Project: Quora Question Pair Similarity
with st.container():
  col1, col2 = st.columns((1, 2))
  with col1:
    st.image(Image.open('./assets/img/DL.png'))  # Project image
  with col2:
    st.subheader("Quora Question Pair Similarity")
    st.write("""
    Enhanced question similarity detection accuracy on Quora by 5.18% through feature engineering in a Machine Learning project, fostering improved user experience and knowledge-sharing efficiency.
    """)
    st.markdown('`Machine Learning`, `Data Analysis`, `Exploratory Data Analysis`, `Python`, `Artificial Intelligence (AI)`, `Data Visualization`, `pandas`, `Git`')
    st.markdown('[GitHub](https://github.com/mallikarjun25/Quora-Question-Pair-Similarity)')

st.write('---')

# Project: Himalayan Climbing Trends Analysis
with st.container():
  col3, col4 = st.columns((1, 2))
  with col3:
    st.image(Image.open('./assets/img/PBI.png'))  # Project image
  with col4:
    st.subheader("Himalayan Climbing Trends Analysis")
    st.write("""
    Power BI dashboard analyzing Himalayan climbing trends, based on 3,854 summit attempts, highlighting Everest's popularity, autumn as the peak climbing season, and 185 summit-related deaths.
    """)
    st.markdown('`Python`, `Data Analysis`, `Data Visualization`, `Git`, `Exploratory Data Analysis`, `SQL`')
    st.markdown('[GitHub](https://github.com/mallikarjun25/Himalayan-Climbing-Trends-Analysis)')

st.write('---')

# Project: Tic-Tac-Toe with Multiple Agents
with st.container():
  col5, col6 = st.columns((1, 2))
  with col5:
    st.image(Image.open('./assets/img/AI.png'))  # Project image
  with col6:
    st.subheader("Tic-Tac-Toe with Multiple Agents")
    st.write("""
    A project on designing a Tic-Tac-Toe game with Q-Learning, Min-Max algorithm, and Alpha-Beta pruning agents for diverse gameplay strategies.
    """)
    st.markdown('`Python`, `Data Analysis`, `Artificial Intelligence (AI)`, `Data Visualization`, `Web Development`, `pandas`, `Git`, `Exploratory Data Analysis`, `User Experience (UX)`')
    st.markdown('[GitHub](https://github.com/mallikarjun25/Multiple-Tic-Tac-Toe-Agents)')

st.write('---')

# Project: Water Quality Prediction
with st.container():
  col7, col8 = st.columns((1, 2))
  with col7:
    st.image(Image.open('./assets/img/DS.png'))  # Project image
  with col8:
    st.subheader("Water Quality Prediction")
    st.write("""
    Using machine learning to predict water potability by analyzing quality indicators from 3276 water bodies, encouraging proactive water quality management for global access to clean drinking water. Demonstrated results using FLASK.
    """)
    st.markdown('`Putty`, `Python`, `Data Analysis`, `Data Visualization`, `Machine Learning`, `Flask`, `HTML`, `Web Development`, `pandas`, `Git`, `Exploratory Data Analysis`, `Data Modeling`, `User Experience (UX)`')
    st.markdown('[GitHub](https://github.com/mallikarjun25/Water-Quality-Prediction)')

st.write('---')

# Project: Serenity
with st.container():
  col9, col10 = st.columns((1, 2))
  with col9:
    st.image(Image.open('./assets/img/AEM.png'))  # Project image
  with col10:
    st.subheader("Serenity")
    st.write("""
    Dynamic international travel and tourism website built with Adobe Experience Manager (AEM), showcasing location-based travel destinations and tour options.
    """)
    st.markdown('`Adobe Experience Manager (AEM)`, `Maven`, `Postman API`, `HTL`, `HTML`, `PostgreSQL`, `Web Development`, `REST APIs`, `OSGi`, `Git`, `React.js`, `User Experience (UX)`')
    st.markdown('[GitHub](https://github.com/mallikarjun25/Geeks-Holiday-Planners)')