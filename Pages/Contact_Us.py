import streamlit as st
from send_email import send_email

st.header("Conact Me!")


with st.form(key="contact_form"):
    user_email = st.text_input("Your Email")
    user_message = st.text_area("Your Message")
    message = f"""\
Subject: New email from {user_email}
    
{user_message}
From: {user_email}
"""
    submit_button = st.form_submit_button()
    if submit_button:
        send_email(message)
        st.info("Email has been sent Successfully.")
