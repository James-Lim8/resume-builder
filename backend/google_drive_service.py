from datetime import datetime
import pytz
import streamlit as st
from googleapiclient.discovery import build 
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account 

def create_services():
    scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"]
    credentials = service_account.Credentials.from_service_account_info(st.secrets["google_drive_service_account"], scopes=scopes)

    spreadsheet_service = build("sheets", "v4", credentials=credentials)
    drive_service = build("drive", "v3", credentials=credentials)

    return spreadsheet_service, drive_service


def get_current_id(spreadsheet_service):
    spreadsheet_id = st.secrets["SPREADSHEET_ID"]

    # Get current id
    rows = spreadsheet_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range="Streamlit Helper!A2"
    ).execute().get("values", [])
    current_id = rows[0][0]

    # Increment id by 1
    current_id = int(current_id) + 1
    body = {
        'values': [[current_id]]
    }

    spreadsheet_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, 
        range="Streamlit Helper!A2",
        valueInputOption="RAW",
        body=body
    ).execute()

    return current_id


def append_to_spreadsheets(spreadsheet_service, current_id, contact, email_for_marketing):
    spreadsheet_id = st.secrets["SPREADSHEET_ID"]
    timestamp = datetime.strftime(datetime.now(pytz.timezone('Asia/Singapore')), "%Y-%m-%d %H:%M:%S")

    # Append to Personal Particulars
    range = "Personal Particulars!A:G"

    data = [[
        timestamp,
        current_id,
        contact["name"],
        email_for_marketing,
        contact["email"],
        contact["nationality"],
        contact["phone"],
        contact["github"],
        contact["career_objective"]
    ]]
    body = {
        "values": data
    }

    spreadsheet_service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range,
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()

    # Append to Skills
    range = "Skills!A:C"

    data = []
    for basic_skill in contact["basic_skills"]:
        data.append([current_id, basic_skill, "Basics & Networking"])

    for basic_skill in contact["soc_skills"]:
        data.append([current_id, basic_skill, "SOC Analyst"])

    for basic_skill in contact["pt_skills"]:
        data.append([current_id, basic_skill, "Penetration Testing"])

    for basic_skill in contact["other_skills"]:
        data.append([current_id, basic_skill, "Other Skills"])

    body = {
        "values": data
    }

    spreadsheet_service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range,
        valueInputOption="RAW",
        body=body
    ).execute()

    # Append to Projects
    range = "Projects!A:D"

    data = []
    for project in contact["projects"]:
        data.append([
            current_id,
            project["title"],
            project["date"],
            project["content"]
        ])

    body = {
        "values": data
    }

    spreadsheet_service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range,
        valueInputOption="RAW",
        body=body
    ).execute()

    # Append to Professional Experiences
    range = "Professional Experiences!A:D"

    data = []
    for experience in contact["experiences"]:
        data.append([
            current_id,
            experience["title"],
            experience["period"],
            experience["content"]
        ])
        
    body = {
        "values": data
    }

    spreadsheet_service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range,
        valueInputOption="RAW",
        body=body
    ).execute()

    # Append to Education
    range = "Education!A:C"

    data = []
    for education in contact["educations"]:
        data.append([
            current_id,
            education["title"],
            education["period"]
        ])
        
    body = {
        "values": data
    }

    spreadsheet_service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range,
        valueInputOption="RAW",
        body=body
    ).execute()

    # Append to Certifications
    range = "Certifications!A:C"

    data = []
    for certification in contact["certifications"]:
        data.append([
            current_id,
            certification["title"],
            certification["date"]
        ])
        
    body = {
        "values": data
    }

    spreadsheet_service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range,
        valueInputOption="RAW",
        body=body
    ).execute()

    # Append to Additional Information
    range = "Additional Information!A:C"

    data = []
    for info in contact["additional_infos"]:
        data.append([
            current_id,
            info["title"],
            info["date"],
            info["content"]
        ])
        
    body = {
        "values": data
    }

    spreadsheet_service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range,
        valueInputOption="RAW",
        body=body
    ).execute()

def save_resume(drive_service, path_to_resume, current_id, name):
    folder_id = st.secrets["FOLDER_ID"]
    file_metadata = {
        "name": f"{current_id} - {name}.docx",
        "parents": [folder_id]
    }
    media = MediaFileUpload(path_to_resume, mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    drive_service.files().create(body=file_metadata, media_body=media, fields="id").execute()