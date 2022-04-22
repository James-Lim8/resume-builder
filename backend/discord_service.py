import streamlit as st
import requests

def notify_members(id, name, email):
    webhook_url = st.secrets["DISCORD_WEBHOOK_URL"]
    notification = f"""
-----------------------------------------------
Hey guys, someone just used the resume builder! 

Here is some info about the user:

- Submission number: {id}
- Name: {name}
- Email: {email}
-----------------------------------------------
    """
    data = {"content": notification}
    requests.post(webhook_url, json=data)