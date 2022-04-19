from components import layout
from components import inputs

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

# Show header
layout.header()

# User Inputs
contact = inputs.personal_particulars_component(contact)
contact = inputs.skills_component(contact)
contact = inputs.projects_component(contact)
contact = inputs.experiences_component(contact)
contact = inputs.educations_component(contact)
contact = inputs.certifications_component(contact)
contact = inputs.additional_information_component(contact)

# Generate Resume
layout.download_resume_component(contact)