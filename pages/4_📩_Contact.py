import streamlit as st
from sidebar import add_sidebar_message

# Page Configuration
st.set_page_config(page_title='Mallikarjun - Contact', layout="wide", page_icon="🕸️")

# Add the sidebar footer
add_sidebar_message()

# Function to add local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Contact Form Section
st.header("📫 Get in touch with me")

contact_form = """
<form action="https://formsubmit.co/mallikarjunaitha@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Social Media Icons (Without Text Labels)
st.markdown("""
<div class="social-icons">
    <a href="https://www.linkedin.com/in/mallikarjun-aitha/" target="_blank">
        <img src="https://www.svgrepo.com/show/447138/linkedin-fill.svg" alt="LinkedIn">
    </a>
    <a href="https://github.com/mallikarjun25/" target="_blank">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub">
    </a>
    <a href="https://www.instagram.com/mallikarjun_aitha/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" alt="Instagram">
    </a>
</div>
""", unsafe_allow_html=True)
