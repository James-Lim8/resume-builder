import streamlit as st
from docxtpl import DocxTemplate

st.write("# Resume Builder")

st.write("Your particulars!")
#DEFINE THE DICTIONARY
contact = {
    "name": "",
    "email": "",
    "nationality": "",
    "phone": 0,
    "github": "",
    "career_objective": "",
    "basic_skills": [],
    "soc_skills": [],
    "pt_skills": [],
    "other_skills": [],
    "projects": [],
    "experiences": [],
    "educations": [],
    "certifications": [],
    "additional_infos": []
}

with st.expander("Personal Particulars"):
    #PERSONAL PARTICULARS
    user_name = st.text_input('Enter your full name: ', placeholder=" Full Name")
    user_email = st.text_input('Enter your email: ', placeholder=" Email")
    user_nationality = st.text_input('Enter your nationality: ', placeholder=" Nationality")
    user_phone = st.text_input('Enter your phone number: ', placeholder=" Phone Number")
    user_github = st.text_input('Enter your github link, otherwise put N.A.', placeholder=" Github Link")
    user_career_obj = st.text_area('Describe your career objectives: ', placeholder=" Career Objectives")

    #ADDING TO RESPECTIVE DICTIONARY KEYS
    contact["name"] = user_name
    contact["email"] = user_email
    contact["nationality"] = user_nationality
    contact["phone"] = user_phone
    contact["github"] = user_github
    contact["career_objective"] = user_career_obj

#[*]--------------------------------------------------------------------------------------------[*]

#SKILLS
with st.expander("Skills"):
    st.info("HELLO WORLD")
    first, second, third, fourth = st.columns(4)

    basic_skills = first.text_area(label="Enter the list of skills you learnt from Basics & Networking: ", placeholder=" Linux commands")
    soc_skills = second.text_area("Enter the list of skills you learnt from SOC: ", placeholder=" ELK")
    pt_skills = third.text_area("Enter the list of skills you learnt from PT: ", placeholder=" msfconsole")
    other_skills = fourth.text_area("Enter the list of skills you learnt from other sources: ", placeholder="photoshop / SPSS/ accounting etc.")

    contact["basic_skills"].extend(basic_skills.strip().split("\n"))
    contact["soc_skills"].extend(soc_skills.strip().split("\n"))
    contact["pt_skills"].extend(pt_skills.strip().split("\n"))
    contact["other_skills"].extend(other_skills.strip().split("\n"))

#[*]--------------------------------------------------------------------------------------------[*]

#PROJECTS
with st.expander("Project Information"):
    st.info("HELLO WORLD")
    proj_n=st.number_input("How many projects information would you like to key in?: ",min_value=0,max_value=20)

    all_projects=[]

    for project_number in range(int(proj_n)):
        each_proj={}
        st.write(f"Project #{project_number+1}")
        proj_title=st.text_input("Please provide the title of the project: ", key=project_number, placeholder="Project Title")
        proj_start_date=st.text_input("Please provide the Start date of the project in (MM/YYYY): ", key=project_number, placeholder="Start Date")
        proj_content=st.text_area("Please provide the content of the project: ", key=project_number, placeholder="Project Details")
        each_proj["title"] = proj_title
        each_proj["date"] = proj_start_date
        each_proj["content"] = proj_content
        all_projects.append(each_proj)

    contact["projects"]=all_projects

#[*]--------------------------------------------------------------------------------------------[*]

#EXPERIENCES
with st.expander("Experiences"):
    st.info("HELLO WORLD")
    exp_n=st.number_input("How many experiences information would you like to key in?: ",min_value=0,max_value=20)

    all_exps=[]

    for experience_number in range(int(exp_n)):
        each_exp={}
        st.write(f"Experience #{experience_number+1}")
        exp_title=st.text_input("Please provide the job title ,followed by company name: ", key=experience_number, placeholder="Project Title")
        exp_start_date=st.text_input("Please provide the Start - end date of the project in (month year - month year): ", key=experience_number, placeholder="Start Date")
        exp_content=st.text_area("Please provide the content of the work experience: ", key=experience_number, placeholder="Project Details")
        each_exp["title"] = exp_title
        each_exp["date"] = exp_start_date
        each_exp["content"] = exp_content
        all_exps.append(each_exp)

    contact["experiences"]=all_exps

#[*]--------------------------------------------------------------------------------------------[*]

#TRANSFERING INFO TO TEMPLATE

# DEBUG
st.write(contact)

# DOWNLOAD RESUME
checked = st.checkbox("I agree that the information is contributed by me and is true")

generated_button_disabled = True

if checked:
    generated_button_disabled = False

if st.button("Generate Resume", disabled=generated_button_disabled):
    doc = DocxTemplate("template-cv.docx")
    doc.render(contact)
    doc.save(f"{user_name}.docx")

    with open(f"{user_name}.docx", "rb") as docx_file:
        st.success("Resume generated successfully!")
        st.download_button("Download Resume", data=docx_file, file_name=f"{user_name}_resume.docx")