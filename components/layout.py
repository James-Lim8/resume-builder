import streamlit as st
from backend import resume_generator

def header():
    st.write("# Resume Builder")
    st.write("Fill in each of the section to the best of your ability. You can use the example as a guide and copy the point-form.")

#[*]--------------------------------------------------------------------------------------------[*]

# DOWNLOAD RESUME
def download_resume_component(contact):
    checked = st.checkbox("I agree that the information is contributed by me and is true")

    generated_button_disabled = True

    if checked:
        generated_button_disabled = False

    if st.button("Generate Resume", disabled=generated_button_disabled):
        resume_generator.generate_resume(contact)

        with open(f"{contact['name']}.docx", "rb") as docx_file:
            st.success("Resume generated successfully!")
            st.download_button("Download Resume", data=docx_file, file_name=f"{contact['name']}_resume.docx")