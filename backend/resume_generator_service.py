from docxtpl import DocxTemplate

def generate_resume(contact):
    doc = DocxTemplate("template-cv.docx")
    doc.render(contact)
    doc.save(f"{contact['name']}.docx")