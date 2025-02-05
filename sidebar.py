import streamlit as st

def add_sidebar_message():
    # Add a static message to the sidebar
    st.sidebar.markdown(
        '<div style="position: fixed; bottom: 25px; width: 19%; text-align: center;">'
        'Made with coffee ☕ and magic ✨</div>',
        unsafe_allow_html=True
    )

# Add the sidebar message
add_sidebar_message()
