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

number_of_basic_skills=st.number_input('How many Basics & Networking skills would you like to input? (Up to 20)',min_value=0,max_value=20)
for each_basic_skill in range(int(number_of_basic_skills)):
    each_basic_skill = st.text_input(label="Enter the list of skills you learnt from Basics & Networking: ", key=each_basic_skill, placeholder=" Linux commands")
    contact["basic_skills"].append(each_basic_skill)

number_of_soc_skills=st.number_input('How many SOC skills would you like to input? (Up to 20)',min_value=0,max_value=20)
for each_soc_skill in range(int(number_of_soc_skills)):
    each_soc_skill = st.text_input("Enter the list of skills you learnt from SOC: ", key=each_soc_skill, placeholder=" ELK")
    contact["soc_skills"].append(each_soc_skill)

number_of_pt_skills=st.number_input('How many Pen-Test skills would you like to input? (Up to 20)',min_value=0,max_value=20)
for each_pt_skill in range(int(number_of_pt_skills)):
    each_pt_skill=st.text_input("Enter the list of skills you learnt from PT: ", key=each_pt_skill, placeholder=" msfconsole")
    contact["pt_skills"].append(each_pt_skill)

number_of_other_skills=st.number_input('How many Other skills would you like to input? (Up to 20)',min_value=0,max_value=20)
for each_other_skill in range(int(number_of_other_skills)):
    each_other_skill=st.text_input("Enter the list of skills from other areas: ", key=each_other_skill,placeholder=" photoshop / SPSS/ accounting etc.")
    contact["other_skills"].append(each_other_skill)

#[*]--------------------------------------------------------------------------------------------[*]

#PROJECTS
proj_n=st.number_input("How many projects information would you like to key in?: ",min_value=0,max_value=20)

all_projects=[]

for number_of_projects in range(proj_n):
    each_proj={}
    proj_title=st.text_input("Please provide the title of the project: ", key=number_of_projects, placeholder="Project Title")
    proj_start_date=st.text_input("Please provide the Start date of the project in (MM/YYYY): ", key=number_of_projects, placeholder="Start Date")
    proj_content=st.text_area("Please provide the content of the project: ", key=number_of_projects, placeholder="Project Details")
    each_proj["title"] = proj_title
    each_proj["date"] = proj_start_date
    each_proj["content"] = proj_content
    all_projects.append(each_proj)

contact["projects"]=all_projects

#[*]--------------------------------------------------------------------------------------------[*]

#EXPERIENCES
exp_n=st.number_input("How many experiences information would you like to key in?: ",min_value=0,max_value=20)

all_exps=[]

for number_of_exps in range(exp_n):
    each_exp={}
    exp_title=st.text_input("Please provide the job title ,followed by company name: ", key=number_of_exps, placeholder="Project Title")
    exp_start_date=st.text_input("Please provide the Start - end date of the project in (month year - month year): ", key=number_of_exps, placeholder="Start Date")
    exp_content=st.text_area("Please provide the content of the work experience: ", key=number_of_exps, placeholder="Project Details")
    each_exp["title"] = exp_title
    each_exp["date"] = exp_start_date
    each_exp["content"] = exp_content
    all_exps.append(each_exp)

contact["experiences"]=all_exps

#[*]--------------------------------------------------------------------------------------------[*]

#TRANSFERING INFO TO TEMPLATE

#doc = DocxTemplate("template-cv.docx")
#doc.render(contact)
#doc.save("test-template.docx")
st.checkbox("I agree that the information is contributed by me and is true")
#st.download_button("Download your resume", file_name=contact["name"]'_resume')
