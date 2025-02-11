import streamlit as st
from PIL import Image
from sidebar import add_sidebar_message

# Set page configuration (title, icon, layout, sidebar state)
st.set_page_config(
    page_title="Shraddha Shrstha - Data Analyst",
    page_icon="🕸️",
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
            "Without data, you're just another person with an opinion." We've all heard this, and honestly, it's kind of true. 
            In today's world, data isn't just powerful—it’s a game-changer. It can shape narratives, drive decisions, and sometimes 
            even cause chaos. That’s why I find it so fascinating.
            """)
        
        # Background and expertise
        st.markdown("""
            My journey into data started with a simple conversation during my undergrad with the CEO of ING Skills Academy, and 
            ever since, I’ve been hooked. Now, as an MS Data Science student at the University of New Haven, I thrive on 
            turning raw data into meaningful insights through machine learning and AI. Because let’s be real—with great algorithms 
            comes great responsibility! And let’s not forget—without proper data cleaning, all you have is garbage in, garbage out.
            """)

        # Current job
        st.markdown("""
            Currently, I work as a Graduate Assistant, where I don’t just analyze data—I make it work smarter. I ensure seamless data integration between the Common App and internal systems, 
            manage live student data in Slate with precision, and collaborate with the marketing team to uncover trends that drive better enrollment strategies. Basically, if there’s a way to 
            optimize something with data, I’m on it.
            """)
        
        # Relevant experience
        st.markdown("""
            Previously, as a Data Analyst intern at Downtown Evening Soup Kitchen, I built real-time Power BI dashboards to track donations and monitored homeless populations to optimize resource distribution. 
                    It was data with impact—helping the team make smarter, more efficient decisions to support those in need.
                    """)

        # Closing statement
        st.markdown("""
            From predicting enrollment trends to fine-tuning donation strategies, my goal is simple: turn numbers into narratives and data into decisions. Because at the end of the day, data might not lie, but it sure loves a good storyteller! 
            """)

        # Resume download button
        with open("assets/Mallikarjun_Aitha_Resume.pdf", "rb") as file:
            st.download_button(
                label="Download my resume",
                data=file,
                file_name="Shraddha_Shrestha_CV.pdf",
                mime="application/pdf"
            )
