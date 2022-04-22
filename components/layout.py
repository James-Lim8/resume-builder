import re
import streamlit as st
from backend import resume_generator_service

# HEADER
def header():
    st.write("# Resume Builder")
    st.write("Fill in each of the section to the best of your ability. You can use the example as a guide and copy the point-form.")

#[*]--------------------------------------------------------------------------------------------[*]

# DOWNLOAD RESUME
def download_resume_component(contact):
    generated_button_disabled = True

    email = st.text_input("Please enter your email address")
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_is_valid = re.fullmatch(regex,email)
    if not email == "" and not email_is_valid:
        st.error("Please enter a valid email address")

    checked = st.checkbox("I agree that the information is contributed by me and is true")

    if checked and email_is_valid:
        generated_button_disabled = False

    if st.button("Generate Resume", disabled=generated_button_disabled):
        resume_generator_service.generate_resume(contact)

        with open(f"{contact['name']}.docx", "rb") as docx_file:
            st.success("Resume generated successfully!")
            st.download_button("Download Resume", data=docx_file, file_name=f"{contact['name']}_resume.docx")
    
        return True, f"{contact['name']}.docx", email

    return False, None, None