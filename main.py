import streamlit as st
from docxtpl import DocxTemplate

st.write("# Resume Builder")

st.write("Your particulars!")

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
    "projects": []
}

user_name = st.text_input('Enter your full name: ', placeholder=" Full Name")
user_email = st.text_input('Enter your email: ', placeholder=" Email")
user_nationality = st.text_input('Enter your nationality: ', placeholder=" Nationality")
user_phone = st.text_input('Enter your phone number: ', placeholder=" Phone Number")
user_github = st.text_input('Enter your github link, otherwise put N.A.', placeholder=" Github Link")
user_career_obj = st.text_area('Describe your career objectives: ', placeholder=" Career Objectives")

contact["name"] = user_name
contact["email"] = user_email
contact["nationality"] = user_nationality
contact["phone"] = user_phone
contact["github"] = user_github
contact["career_objective"] = user_career_obj

#End of getting user particulars

# print('Moving to your Skillsets')

# for each_basic_skill in range(2):
#     each_basic_skill=input("Enter the list of skills you learnt from Basics & Networking: ")
#     contact["basic_skills"].append(each_basic_skill)


# for each_soc_skill in range(2):
#     each_soc_skill=input("Enter the list of skills you learnt from SOC: ")
#     contact["soc_skills"].append(each_soc_skill)


# for each_pt_skill in range(2):
#     each_pt_skill=input("Enter the list of skills you learnt from PT: ")
#     contact["pt_skills"].append(each_pt_skill)


# for each_other_skill in range(2):
#     each_other_skill=input("Enter the list of skills from other areas: ")
#     contact["other_skills"].append(each_other_skill)


# #End of getting the skills input

# print('Moving on to the projects section. Please provide details of your projects starting from the most recent one')

# n=int(input("How many projects information would you like to key in?: "))

# all_projects=[]

# for number_of_projects in range(n):
#     each_proj={}
#     proj_title=input("Please provide the title of the project: ")
#     proj_date=input("Please provide the Start date of the project: ")
#     proj_content=input("Please provide the content of the project: ")
#     contact["pt_skills"].append(proj_title)
#     each_proj["date"] = proj_date
#     each_proj["content"] = proj_content
#     all_projects.append(each_proj)

# contact["projects"]=all_projects

# #print(contact)

# doc = DocxTemplate("template-cv.docx")
# doc.render(contact)
# doc.save("test-template.docx")
