import streamlit as st
from docxtpl import DocxTemplate

st.write("# Resume Builder")

st.write("Fill in each of the section to the best of your ability. You can use the example as a guide and copy the point-form.")
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
    user_career_obj = st.text_area('Describe your career objectives: ', placeholder="Write in Paragraphs about what the employer should know about you, why you want to enter cybersecurity.")

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
    st.info("""Photoshop, SPSS, msfconsole etc..
    
If nothing, leave blank.
    
    Note: You can key in multiple lines of skill 
    
    before doing <Ctrl+Enter> to submit the input""")
    first, second, third, fourth = st.columns(4)

    basic_skills = first.text_area(label="Enter the skills you learnt from Basics & Networking: ", placeholder=" wireshark")
    soc_skills = second.text_area("Enter the skills you learnt from SOC: ", placeholder=" ELK")
    pt_skills = third.text_area("Enter the list of skills you learnt from PT: ", placeholder=" msfconsole")
    other_skills = fourth.text_area("Enter the list of skills you learnt from other sources: ", placeholder="photoshop / SPSS/ accounting etc.")

    contact["basic_skills"].extend(basic_skills.strip().split("\n"))
    contact["soc_skills"].extend(soc_skills.strip().split("\n"))
    contact["pt_skills"].extend(pt_skills.strip().split("\n"))
    contact["other_skills"].extend(other_skills.strip().split("\n"))

#[*]--------------------------------------------------------------------------------------------[*]

#PROJECTS
with st.expander("Project Information"):
    st.info("""(Example)

Network Research (This is the title)

•   Using Wireshark to profile network traffic and analyse packets 

(This is the content/ details of the project)
""")
    proj_n=st.number_input("How many projects information would you like to key in?: ",min_value=0,max_value=20)

    all_projects=[]

    for project_number in range(int(proj_n)):
        each_proj={}
        st.write(f"Project #{project_number+1}")
        proj_title=st.text_input("Please provide the title of the project: ", key=project_number, placeholder="Project Title")
        proj_end_date=st.text_input("Please provide the completion date of the project in (MMM YYYY): ", key=project_number, placeholder="Jul 2022")
        proj_content=st.text_area("Please provide the content of the project: ", key=project_number, placeholder="•   Detail 1")
        each_proj["title"] = proj_title
        each_proj["date"] = proj_end_date
        each_proj["content"] = proj_content
        all_projects.append(each_proj)

    contact["projects"]=all_projects

#[*]--------------------------------------------------------------------------------------------[*]

#EXPERIENCES
with st.expander("Professional Experiences"):
    st.info("""(Example)

Executive, Company ABC

•	Top Sales in Company ABC in 3 months

•	Head a project that had xyz achievement
""")
    exp_n=st.number_input("How many experiences information would you like to key in?: ",min_value=0,max_value=20)

    all_exps=[]

    for experience_number in range(int(exp_n)):
        each_exp={}
        st.write(f"Experience #{experience_number+1}")
        exp_title=st.text_input("Please provide the job title,followed by company name: ", key=experience_number, placeholder="Position Title, Company Name")
        exp_period=st.text_input("Please provide the Start - End date of the project in (MMM YYYY - MMM YYYY): ", key=experience_number, placeholder="Apr 2022 - Dec 2022")
        exp_content=st.text_area("Please provide the content of the work experience: ", key=experience_number, placeholder="Achievement and Skill Details")
        each_exp["title"] = exp_title
        each_exp["period"] = exp_period
        each_exp["content"] = exp_content
        all_exps.append(each_exp)

    contact["experiences"]=all_exps

#[*]--------------------------------------------------------------------------------------------[*]

#EDUCATIONS
with st.expander("Education"):
    st.info("""(Example)
    
    Diploma, Institute of Education
""")
    edu_n=st.number_input("How many Education information would you like to key in?: ",min_value=0,max_value=20)

    all_edu=[]

    for number_of_edu in range(int(edu_n)):
        each_edu={}
        edu_title=st.text_input("Please provide the name of the education, name of the Institute: ", key=number_of_edu, placeholder="Name of Education, Name of the Institute/School")
        edu_period=st.text_input("Please provide the duration of the education in (MMM YYYY - MMM YYYY): ", key=number_of_edu, placeholder="Apr 2022 - Dec 2022")
        #proj_content=st.text_area("Please provide the content of the project: ", key=number_of_edu, placeholder="Project Details")
        each_edu["title"] = edu_title
        each_edu["period"] = edu_period
        #each_proj["content"] = proj_content
        all_edu.append(each_edu)

    contact["educations"]=all_edu

#[*]--------------------------------------------------------------------------------------------[*]

#CERTIFICATIONS
with st.expander("Professional Certifications/ Association"):
    st.info(""" (Example)

Advanced Certificate in Learning and Performance (ACLP), Institute for Adult Learning
""")
    n=st.number_input("How many Certificates Information would you like to key in?: ",min_value=0,max_value=20)

    all_certificates=[]

    for number_of_certs in range(int(n)):
        each_cert={}
        cert_title=st.text_input("Please provide the title of the cert, and the issuing organisation: ", key=number_of_certs, placeholder="Certificate Title, Issuing Organisation")
        cert_obtained_date=st.text_input("Please provide the date conferred (MMM YYYY): ", key=number_of_certs, placeholder="Jan 2022")
        #proj_content=st.text_area("Please provide the content of the project: ", key=number_of_certs, placeholder="Project Details")
        each_cert["title"] = cert_title
        each_cert["date"] = cert_obtained_date
        #each_proj["content"] = proj_content
        all_certificates.append(each_cert)

    contact["certifications"]=all_certificates

#[*]--------------------------------------------------------------------------------------------[*]

#ADDITIONAL INFORMATION
with st.expander("Additional Information"):
    st.info("""(Example)

Awards

•	Scholarship ABC

•   Top Sales Award 


Inventions / Publications

•	Journal / Book Title
""")
    n=st.number_input("How many Additional information would you like to key in?: ",min_value=0,max_value=20)

    all_infos=[]

    for number_of_infos in range(int(n)):
        each_info={}
        info_title=st.text_input("Please provide the Category of the Information: ", key=number_of_infos, placeholder="")
        info_date=st.text_input("Please provide the date in (MMM YYYY): ", key=number_of_infos, placeholder="Jan 2021")
        info_content=st.text_area("Please provide the content of the project: ", key=number_of_infos, placeholder="•   Top Sales Award")
        each_info["title"] = info_title
        each_info["date"] = info_date
        each_info["content"] = info_content
        all_infos.append(each_info)

    contact["projects"]=all_projects


#TRANSFERING INFO TO TEMPLATE

# DEBUG
#st.write(contact)

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

#[*]--------------------------------------------------------------------------------------------[*]


#[*]--------------------------------------------------------------------------------------------[*]