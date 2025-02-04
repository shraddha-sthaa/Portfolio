import streamlit as st

# Page Configuration
st.set_page_config(page_title='Contact', page_icon="🕸️")

# Function to add local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Contact Form Section
st.header("📫 Get in Touch")

contact_form = """
<form action="https://formsubmit.co/feaa3c03ce9b3f1f99b0663d16747021" method="POST">
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
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn">
    </a>
    <a href="https://github.com/mallikarjun25/" target="_blank">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub">
    </a>
    <a href="https://www.instagram.com/mallikarjun_aitha/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" alt="Instagram">
    </a>
</div>
""", unsafe_allow_html=True)
