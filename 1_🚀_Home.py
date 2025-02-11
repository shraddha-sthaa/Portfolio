import streamlit as st
from PIL import Image
from sidebar import add_sidebar_message

# Set page configuration (title, icon, layout, sidebar state)
st.set_page_config(
    page_title="Shraddha Shrstha - Data Analyst",
    page_icon="❄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add the sidebar footer
add_sidebar_message()

# Main content
with st.container():
    st.title("Hey there! I'm Shraddha.")  # Title
    st.markdown("")
    # Create two columns with a minimal gap
    col1, col2 = st.columns((1, 1.5), gap="small")
    
    with col1:
        # Display profile image
        st.markdown('<div class="profile-img">', unsafe_allow_html=True)
        st.image('./assets/img/profile.jpg', use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Personal introduction
        st.markdown("""
            **I'm Shraddha Shrestha**, your go-to Data Analyst, here to utilize the power of data to make a difference.
            """)
        
        st.markdown("""
            "Without data, you're just another person with an opinion." We've all heard this, and honestly, it's kind of true. 
            In today's world, data isn't just powerful—it’s a game-changer. It can shape narratives, drive decisions, and sometimes 
            even cause chaos. That’s why I find it so fascinating.
             """)
        # Background and expertise
        st.markdown("""
            My data journey began with a conversation during undergrad with the CEO, and I’ve been hooked ever since. Now, as an MS Data Science student at 
            the University of New Haven, I turn raw data into meaningful insights through machine learning and AI—because with great algorithms comes great responsibility! 
            And let’s be real, without proper data cleaning, it’s just garbage in, garbage out.
            """)

        # Current job
        st.markdown("""
            As a Graduate Assistant, I don’t just analyze data—I make it work smarter. I manage data integration, 
            oversee live student data in Slate, and collaborate with marketing to uncover trends that 
            enhance enrollment strategies. Previously, as a Data Analyst intern at Downtown Evening Soup Kitchen, I 
            built Power BI dashboards to track donations and optimized resource distribution for greater impact.
            """)
        

        # Closing statement
        st.markdown("""
            From predicting enrollment trends to fine-tuning donation strategies, I turn numbers into narratives and data into 
            decisions—because data might not lie, but it sure loves a good storyteller!
            """)

        # Resume download button
        with open("assets/Mallikarjun_Aitha_Resume.pdf", "rb") as file:
            st.download_button(
                label="Download my resume",
                data=file,
                file_name="Shraddha_Shrestha_CV.pdf",
                mime="application/pdf"
            )
