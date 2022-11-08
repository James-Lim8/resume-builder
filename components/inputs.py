import streamlit as st

# PERSONAL PARTICULARS
def personal_particulars_component(contact):
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

    return contact

# SKILLS
def skills_component(contact):
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

    if basic_skills.strip() != "":
        contact["basic_skills"].extend(basic_skills.strip().split("\n"))
    if soc_skills.strip() != "":
        contact["soc_skills"].extend(soc_skills.strip().split("\n"))
    if pt_skills.strip() != "":
        contact["pt_skills"].extend(pt_skills.strip().split("\n"))
    if other_skills.strip() != "":
        contact["other_skills"].extend(other_skills.strip().split("\n"))

    return contact

#[*]--------------------------------------------------------------------------------------------[*]


#PROJECTS
def projects_component(contact):
    all_projects=[]

    with st.expander("Project Information"):
        st.info("""(Example)
    Network Research (This is the title)
    •   Using Wireshark to profile network traffic and analyse packets 
    (This is the content/ details of the project)
    """)
        proj_n=st.number_input("How many projects information would you like to key in?: ",min_value=0,max_value=20)

        widget_id = (id for id in range(1, 100_00))
        for project_number in range(int(proj_n)):
            each_proj={}
            
            st.write(f"Project #{project_number+1}")
            proj_title=st.text_input("Please provide the title of the project: ", key=next(widget_id), placeholder="Project Title")
            proj_end_date=st.text_input("Please provide the completion date of the project in (MMM YYYY): ", key=next(widget_id), placeholder="Jul 2022")
            proj_content=st.text_area("Please provide the content of the project: ", key=next(widget_id), placeholder="•   Detail 1")

            each_proj["title"] = proj_title
            each_proj["date"] = proj_end_date
            each_proj["content"] = proj_content
            all_projects.append(each_proj)
            

    contact["projects"]=all_projects

    return contact

#[*]--------------------------------------------------------------------------------------------[*]

#EXPERIENCES
def experiences_component(contact):
    all_exps=[]

    with st.expander("Professional Experiences"):
        st.info("""(Example)
    Executive, Company ABC
    •	Top Sales in Company ABC in 3 months
    •	Head a project that had xyz achievement
    •	Quantify your Work Experience
    """)
        exp_n=st.number_input("How many experiences information would you like to key in?: ",min_value=0,max_value=20)

        widget_id_1 = (id for id in range(1, 100_00))
        for experience_number in range(int(exp_n)):
            each_exp={}
           
            st.write(f"Experience #{experience_number+1}")
            exp_title=st.text_input("Please provide the job title,followed by company name: ", key=next(widget_id_1), placeholder="Position Title, Company Name")
            exp_period=st.text_input("Please provide the Start - End date of the project in (MMM YYYY - MMM YYYY): ", key=next(widget_id_1), placeholder="Apr 2022 - Dec 2022")
            exp_content=st.text_area("Please provide the content of the work experience: ", key=next(widget_id_!), placeholder="Achievement and Skill Details")
            each_exp["title"] = exp_title
            each_exp["period"] = exp_period
            each_exp["content"] = exp_content
            all_exps.append(each_exp)
           

    contact["experiences"]=all_exps

    return contact

#[*]--------------------------------------------------------------------------------------------[*]

#EDUCATIONS
def educations_component(contact):
    all_edu=[]
    with st.expander("Education"):
        st.info("""(Example)
        
        Diploma, Institute of Education
    """)
        edu_n=st.number_input("How many Education information would you like to key in?: ",min_value=0,max_value=20)

        widget_id_2 = (id for id in range(1, 100_00))
        for number_of_edu in range(int(edu_n)):
            each_edu={}

            edu_title=st.text_input("Please provide the name of the education, name of the Institute: ", key=next(widget_id_2), placeholder="Name of Education, Name of the Institute/School")
            edu_period=st.text_input("Please provide the duration of the education in (MMM YYYY - MMM YYYY): ", key=next(widget_id_2), placeholder="Apr 2022 - Dec 2022")
            
            each_edu["title"] = edu_title
            each_edu["period"] = edu_period
            
            all_edu.append(each_edu)


    contact["educations"]=all_edu

    return contact

#[*]--------------------------------------------------------------------------------------------[*]

#CERTIFICATIONS
def certifications_component(contact):
    all_certificates=[]

    with st.expander("Professional Certifications/ Association"):
        st.info(""" (Example)
    Advanced Certificate in Learning and Performance (ACLP), Institute for Adult Learning
    """)
        n=st.number_input("How many Certificates Information would you like to key in?: ",min_value=0,max_value=20)

        widget_id_3 = (id for id in range(1, 100_00))
        for number_of_certs in range(int(n)):
            each_cert={}

            cert_title=st.text_input("Please provide the title of the cert, and the issuing organisation: ", key=next(widget_id_3) , placeholder="Certificate Title, Issuing Organisation")
            cert_obtained_date=st.text_input("Please provide the date conferred (MMM YYYY): ", key=next(widget_id_3), placeholder="Jan 2022")
            
            each_cert["title"] = cert_title
            each_cert["date"] = cert_obtained_date
            
            all_certificates.append(each_cert)


    contact["certifications"]=all_certificates

    return contact

#[*]--------------------------------------------------------------------------------------------[*]

#ADDITIONAL INFORMATION
def additional_information_component(contact):
    all_infos=[]

    with st.expander("Additional Information"):
        st.info("""(Example)
    Awards
    •	Scholarship ABC
    •   Top Sales Award 
    Inventions / Publications
    •	Journal / Book Title
    """)
        n=st.number_input("How many Additional information would you like to key in?: ",min_value=0,max_value=20)

        widget_id_4 = (id for id in range(1, 100_00))
        for number_of_infos in range(int(n)):
            each_info={}

            info_title=st.text_input("Please provide the Category of the Information: ", key=next(widget_id_4), placeholder="")
            info_date=st.text_input("Please provide the date in (MMM YYYY): ", key=next(widget_id_4), placeholder="Jan 2021")
            info_content=st.text_area("Please provide the content of the project: ", key=next(widget_id_4), placeholder="•   Top Sales Award")
            each_info["title"] = info_title
            each_info["date"] = info_date
            each_info["content"] = info_content
            all_infos.append(each_info)


    contact["additional_infos"]=all_infos

    return contact
