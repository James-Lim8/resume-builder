from components import layout
from components import inputs
from backend import google_drive_service, discord_service

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

# Generate and download Resume
generated = False
generated, path_to_resume, email = layout.download_resume_component(contact)

# Save info to Google Sheets
if generated:
    # Create connect to Google Drive
    spreadsheet_service, drive_service = google_drive_service.create_services()

    # Save user info to Google Sheets
    current_id = google_drive_service.get_current_id(spreadsheet_service)
    google_drive_service.append_to_spreadsheets(spreadsheet_service, current_id, contact, email)

    # Save resume to Google Drive
    google_drive_service.save_resume(drive_service, path_to_resume, current_id, contact["name"])

    # Send notification to Discord
    discord_service.notify_members(current_id, contact["name"], email)